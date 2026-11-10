# HW03 Progress

Ngày cập nhật: 2026-11-10 (Asia/Ho_Chi_Minh). Phạm vi yêu cầu hiện tại: thực hiện Task 1; Login đã chạy 16 mục, còn 52 mục B/C/D chưa chạy.

| Requirement / step | Status | Outputs / verification evidence | Next action |
| --- | --- | --- | --- |
| Preparation 1 — Read requirements, policies and AI templates | done | Read all 9 pages of source PDF, existing `requirments.md`, root AGENTS/policies, SUT README/setup/API specification and AI templates. HW03 requires >40 GUI items, 7 real sessions + pilot, >=3 platforms, AI records and Git history. | Select screens/flow without overlap before test design. |
| Preparation 2 — Initialize HW03 Git repository | done | `git init hw03`; local identity already configured. No existing HW03 history was present; existing requirement files preserved. | Commit each completed step; configure actual GitHub remote for Issues later. |
| Preparation 3 — Start and verify local SUT | done | `tools/environment.py`, `ENVIRONMENT.md`, `environment/verification.json`; 5/5 real HTTP/login checks passed. In-app browser rendered 5 products and Admin login. Node v24.21.0/npm 11.19.0; dependencies verified. Original backend reset retained per user instruction. | Keep runner active; complete required platform matrix before Task 3. |
| Task 1 — GUI design/execution | in_progress | 68 retained initial items; Login 16 executed: 6 Passed / 10 Failed. 52 B/C/D Not run. Failed screenshots saved; student-authored bug reports still pending. | Continue Admin Coupons, Coupon Apply and real Mobile; finish student additions/bug reports. |
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

## Task 1 execution start — initial design, 2026-11-10

| Requirement / step | Status | Outputs / verification evidence | Next action |
| --- | --- | --- | --- |
| HW03-T1-01 — course guide intake | done | User supplied `../skills/gui-testing-guide/` as lecture synthesis. Read SKILL plus heuristics, widget checklists, strategies and Playwright references. Source hashes recorded in `environment/task1-design-sources.json`. Resolves the earlier missing-GUI-guide blocker; no invented slide numbers. | Student checks final draft against their course understanding. |
| HW03-T1-02 step 1 — preserve initial AI checklist | done | `submission/ai/task1_initial_checklist.md` and `.json`: generated at 2026-11-10T19:28:16+07:00 (artifact timestamp, not prompt timestamp). Verified 68 unique IDs, A/B/C/D=16/8/28/16, IA=15/25/10/18, all Not run, each has steps/expected/source/heuristic. `Task1_Intake.md` inventories 31 widgets with widget × heuristic mapping and phase order. H10 absence and oracle gaps exposed, not silently declared covered. | Preserve original output; student review before finalizing checklist. |
| HW03-T1-02 step 2 — Excel working draft | done | `submission/GUI_Checklist.xlsx`, authored with bundled Artifact Tool. Four sheets: Summary, Checklist, Execution, AI Review. Verified live status counts by changing one item to Failed then restoring Not run; exported cached totals 68 designed, 0 executed, 68 Not run; no formula errors. Checked saved XLSX sheet names, freeze panes and dropdowns; rendered and visually reviewed each sheet. All reviews Pending; no synthetic run IDs/times/actual results. | Student fills AI Review; preserve original AI Markdown/JSON; update working checklist only after real review. |
| HW03-T1-03 — student critique/additions | pending | `submission/Task1_AI_Review.md` is a blank review form with instructions; no student verdicts or independent additions invented. | Student records Keep/Revise/Remove and adds genuinely missing items with reasons. |
| HW03-T1-04 — readiness only | in_progress | `environment/task1-readiness.json`: 5/5 actual local readiness checks passed at 19:25:33+07:00 after localhost access was permitted. Login page opened/observed in in-app browser for intake. No GUI item marked Passed/Failed and no bug inference from source inspection. Existing SUT changes preserved. | Execute reviewed checklist; verify real mobile device and browser evidence. |
| HW03-AI — initial design provenance | in_progress | AI initial output retained, guide sources hashed; generation time distinguished from unavailable user-message timestamps. No AI Critique, student fixes/signatures or full audit claimed. | Export full transcript with real interaction timestamps and complete student audit/disclosure. |

Task 1 remains in progress: real GUI runs, Failed screenshots, student-authored bug descriptions/GitHub Issues, final report/PDF and student review are not complete. Earlier planning records above describe historical state, not new execution results.

Git evidence: initial design/source step committed as `ff0d501`; workbook export is a separate completed requirement step. Working tree checks use `git diff --check`. User input requested for actual student review/additions under assignment §6; this is a content requirement, not an extra permission request. No goal completion is claimed.

| HW03-DOC / HW03-T1-02 step 3 — printable initial draft | done | `submission/ai/task1_initial_checklist.pdf`, 19 pages, 86,745 bytes. Produced from preserved Markdown/JSON with `tools/export_task1_initial_pdf.py`. Text checks confirmed every ID/title/step/expected/source/heuristic/status for all 68 items; rendered all 19 pages and visually reviewed them. No clipping, missing glyphs or split checklist cards observed. Initial Markdown/JSON unchanged. | Use PDF for student review; keep final execution report separate. |

## Task 1 — student Keep and Login execution

| Requirement / step | Status | Outputs / verification evidence | Next action |
| --- | --- | --- | --- |
| HW03-T1-03 — Keep decision | in_progress | User answered “Keep” to review request, interpreted as retaining all 68 initial items. Recorded verbatim in `Task1_AI_Review.md`. No detailed reasoning, reviewer signature, original message timestamp or student additions invented. | Complete independent student additions/reasons later; execute retained items now. |
| HW03-T1-04 step A1 — reproducible Login harness | done | `tools/gui/`: Playwright config, LoginPage, fixtures, demo data and 16 ID-mapped tests. Bundled runtime, Edge headless 1280×800, one worker, no retries; failed-only screenshots and raw observations. Temporary per-test users avoid locking shared accounts. JavaScript syntax/runtime import checked. Existing SUT untouched. | Inspect actual run, classify harness failures separately from product observations and update workbook. |
| HW03-T1-04 step A2 — Login run | done | `T1A_20261110_01`: 16 scenarios, 6 Passed / 10 Failed, 0 skipped. `T1A_20261110_02`: one focused rerun of GUI-A-003 after correcting the language assertion to check button text; still Failed (received Sign In). Final unique items: 16 executed, 6 Passed / 10 Failed. Raw observations in `submission/evidence/gui/login_execution.json`; original Playwright reports, all 11 Failed-run screenshots and error contexts retained. Visually inspected original captures; no infrastructure/locator failures found among the 10 final Failed results. | Student deduplicates/writes bug descriptions and severity; continue feature C. |
| HW03-T1-04 step A3 — execution workbook | done | Working Excel updated from observed results: 68 designed, 16 executed, 6 Passed, 10 Failed, 52 Not run; 17 scenario runs including the superseded A003 run. Each Failed entry has Notes and local screenshot reference. Raw JSON retained instead of clipping long logs into cells. Import/edit/export verified preserved formulas, validations and freeze panes; rendered affected views and checked layout. Keep decisions=68 is not a claim that independent student additions are done. | Preserve history and add later feature results without overwriting existing runs. |

Execution environment: Edge headless (Chromium engine 155.0.4283.45), Linux, 1280×800, local Web/API. SUT HEAD verified `85af3ba875c88283615e22cb108f13e2fccaf0e9`; existing SUT edits were retained, no application code changed. Raw run timestamps use UTC; run 01 started 2026-11-10 19:40:54 Asia/Ho_Chi_Minh and took approximately 71 seconds. This is not Task 3 cross-platform coverage.

Numerical observations from raw attachments: correct-login HTTP statuses after 1/2/3 wrong attempts were 200/403/403 on separate users; lock-duration check still returned 403 after 31,179 ms. These are execution facts, not a bug report drafted for the student. Ten Failed checklist items are not asserted to be ten distinct bugs.

Harness guard was added to refuse reuse of an existing evidence Run ID; verified the CLI refuses `T1A_20261110_01` before starting a browser. Public demo credentials only; browser observations do not store JWT tokens. Office lockfiles and local runtime symlink are excluded from staging; any existing live workbook lockfile is preserved.
