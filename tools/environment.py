#!/usr/bin/env python3
"""Start the original EShop SUT and perform environment-only smoke checks."""
import argparse
import hashlib
import json
import platform
import shutil
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HW = Path(__file__).resolve().parents[1]
SUT = HW.parent / 'eshop-sut'
SERVICES = [('api', 3000, 'backend'), ('web', 5173, 'frontend-web'), ('admin', 5174, 'frontend-admin')]


def request(url, data=None):
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=5) as response:
        return response.status, response.read().decode()


def check():
    results = []
    for name, port, _ in SERVICES:
        route = '/api/products' if name == 'api' else '/'
        try:
            status, body = request(f'http://localhost:{port}{route}')
            valid = bool(json.loads(body)) if name == 'api' else '<div id="root">' in body
            assert status == 200 and valid, 'Unexpected response'
            results.append({'check': name, 'passed': True, 'http_status': status})
        except Exception as exc:
            results.append({'check': name, 'passed': False, 'error': str(exc)})
    for email, password, role in [('test@eshop.com', 'Test1234!', 'user'), ('admin@eshop.com', 'Admin123!', 'admin')]:
        try:
            status, body = request('http://localhost:3000/api/login', {'email': email, 'password': password})
            payload = json.loads(body)
            assert status == 200 and payload.get('token') and payload['user']['role'] == role
            results.append({'check': f'login:{role}', 'passed': True, 'http_status': status})
        except Exception as exc:
            results.append({'check': f'login:{role}', 'passed': False, 'error': str(exc)})
    return results


def snapshot():
    def version(*args):
        try:
            p = subprocess.run(args, capture_output=True, text=True, timeout=10)
            return {'exit_code': p.returncode, 'output': (p.stdout + p.stderr).strip()}
        except (OSError, subprocess.TimeoutExpired) as exc:
            return {'error': str(exc)}
    return {
        'observed_at': datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(),
        'purpose': 'Environment smoke checks only; not HW03 GUI/usability execution',
        'os': platform.platform(), 'python': platform.python_version(),
        'node': version('node', '--version'), 'npm': version('npm', '--version'),
        'sut_commit': version('git', '-C', str(SUT), 'rev-parse', 'HEAD'),
        'sut_status': version('git', '-C', str(SUT), 'status', '--short', '--untracked-files=no'),
        'lockfile_sha256': {folder: hashlib.sha256((SUT / folder / 'package-lock.json').read_bytes()).hexdigest() for _, _, folder in SERVICES},
        'browsers': {name: version(name, '--version') for name in ('google-chrome', 'firefox', 'microsoft-edge')},
        'checks': check(),
    }


def start():
    for binary in ('node', 'npm'):
        if not shutil.which(binary):
            raise RuntimeError(f'Missing {binary}')
    for _, port, folder in SERVICES:
        if not (SUT / folder / 'node_modules').is_dir():
            raise RuntimeError(f'Install dependencies first: cd {SUT / folder} && npm ci')
        with socket.socket() as sock:
            try:
                sock.bind(('127.0.0.1', port))
            except OSError as exc:
                raise RuntimeError(f'Port {port} unavailable; no existing process was stopped') from exc
    logs = HW / '.runtime'
    logs.mkdir(exist_ok=True)
    children, handles = [], []
    def stop(_signum, _frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGTERM, stop)
    print('Starting original SUT. Backend resets its database on EVERY startup.', flush=True)
    try:
        for name, port, folder in SERVICES:
            command = ['node', 'server.js'] if name == 'api' else ['node', 'node_modules/vite/bin/vite.js', '--host', '127.0.0.1', '--port', str(port), '--strictPort']
            handle = (logs / f'{name}.log').open('w')
            handles.append(handle)
            children.append(subprocess.Popen(command, cwd=SUT / folder, stdout=handle, stderr=subprocess.STDOUT))
        for _ in range(30):
            if any(child.poll() is not None for child in children):
                raise RuntimeError(f'Service exited. Inspect {logs}')
            try:
                if all(request(f'http://localhost:{port}' + ('/api/products' if name == 'api' else '/'))[0] == 200 for name, port, _ in SERVICES):
                    break
            except Exception:
                pass
            time.sleep(1)
        else:
            raise RuntimeError('Startup timed out; inspect .runtime/*.log')
        print('Ready: API http://localhost:3000 | Web http://localhost:5173 | Admin http://localhost:5174', flush=True)
        print('Keep this terminal open; Ctrl+C stops only these three services.', flush=True)
        while True:
            if any(child.poll() is not None for child in children):
                raise RuntimeError('Service exited; inspect .runtime/*.log')
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopping HW03 services.', flush=True)
    finally:
        for child in children:
            if child.poll() is None:
                child.terminate()
        for child in children:
            try:
                child.wait(timeout=5)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait()
        for handle in handles:
            handle.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('start', 'check'))
    parser.add_argument('--output', type=Path, help='Save actual environment observations as JSON')
    args = parser.parse_args()
    if args.action == 'start':
        start()
        return 0
    report = snapshot()
    output = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    print(output, end='')
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    return 0 if all(result['passed'] for result in report['checks']) else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (RuntimeError, OSError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
