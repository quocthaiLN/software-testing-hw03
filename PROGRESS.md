# HW03 Progress

Ngày cập nhật: 2026-11-10 (Asia/Ho_Chi_Minh). Phạm vi yêu cầu hiện tại: chuẩn bị môi trường.

| Requirement / step | Status | Outputs / verification evidence | Next action |
| --- | --- | --- | --- |
| Preparation 1 — Read requirements, policies and AI templates | done | Read all 9 pages of source PDF, existing `requirments.md`, root AGENTS/policies, SUT README/setup/API specification and AI templates. HW03 requires >40 GUI items, 7 real sessions + pilot, >=3 platforms, AI records and Git history. | Select screens/flow without overlap before test design. |
| Preparation 2 — Initialize HW03 Git repository | done | `git init hw03`; local identity already configured. No existing HW03 history was present; existing requirement files preserved. | Commit each completed step; configure actual GitHub remote for Issues later. |
| Preparation 3 — Start and verify local SUT | done | `tools/environment.py`, `ENVIRONMENT.md`, `environment/verification.json`; 5/5 real HTTP/login checks passed. In-app browser rendered 5 products and Admin login. Node v24.21.0/npm 11.19.0; dependencies verified. Original backend reset retained per user instruction. | Keep runner active; complete required platform matrix before Task 3. |
| Task 1 — GUI design/execution | pending | No checklist execution or bug reports produced. | Review course lectures and agree scope. |
| Task 2 — Usability study | pending | No participants, consent, pilot or session data collected. | Recruit real participants outside this class; prepare instruments. |
| Task 3 — Cross-platform setup and execution | blocked | Chrome not found; Firefox Snap launcher cannot run. Edge installed; in-app browser can open SUT. Neither is claimed as the required Chrome/Firefox/Safari-or-Android matrix. | Obtain BrowserStack/LambdaTest trial or qualifying real devices; verify localhost tunnel before execution. |
| Final submission | pending | No final reports/PDFs/XLSX, self-assessment, Git log export or ZIP produced. | Complete testing and evidence before final packaging. |

| Preparation 4 — Organize evidence and AI records | done | Created submission README, evidence folders and explicitly partial AI preparation log. `.gitignore` excludes runtime/private data. | Export full original transcript before final AI Audit; verify OBS capture before pilot. |
