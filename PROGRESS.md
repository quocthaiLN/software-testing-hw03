# HW03 Progress

Ngày cập nhật: 2026-11-10 (Asia/Ho_Chi_Minh). Phạm vi yêu cầu hiện tại: lập kế hoạch Task 1, chưa thực thi.

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

## Task 1 planning — 2026-11-10

| Requirement / step | Status | Outputs / verification evidence | Next action |
| --- | --- | --- | --- |
| HW03-SCOPE / HW03-T1-01 — source reconciliation | done | Read full original PDF (9 pages), policies, SUT requirements/API/setup, existing progress and AI templates. Populated previously empty `requirements_list.md` with stable IDs, sources, deliverables and acceptance criteria. User confirms instructor/TA allows shared screens; work allocation discussion omitted from report plan per user request. | Obtain course GUI lectures before actual checklist design; reading lecture requirement itself remains pending. |
| HW03-T1-02 — planning step | done | `submission/Task1_Plan.md`: A=16, B=8, C=28, D=16 planned items, total 68; IA allocation 15/25/10/18. Includes GUI scope, domain/boundary data, ordered steps, workbook schema, evidence rules and completion gates. Counts are design targets only. Checked totals and source-based limits. | AI initial checklist → independent student review/additions → Excel → real execution. |
| HW03-T1-01 — course lecture review | blocked | GUI lecture slides not found in workspace. No invented lecture citations. | Student supplies/consults course lecture and records references. |
| HW03-T1-04 — Mobile readiness | pending | Source inspection: Expo app API fixed at `192.168.1.9:3000/api`; no real device connectivity verified this turn. | Verify phone/Expo Go/LAN backend before Feature D. |
| HW03-T1-05 / HW03-GIT — GitHub Issues readiness | blocked | HW03 local repository valid; `git -C hw03 remote -v` returned empty. | Configure actual GitHub repository/remote before issue logging. |
| HW03-AI — planning disclosure | in_progress | Planning/checklist extraction are AI-assisted. This entry is a summary, not verbatim transcript or completed audit. | Export original prompts/outputs with actual timestamps; student reviews verdicts, writes critique/disclosure. |

No SUT changes, GUI test runs, new bugs, screenshots, participants, Excel/PDF outputs or ZIP were produced in this planning step. Planning Markdown will receive its PDF copy when preparing the report/submission; PDF export/visual QA remain pending.
