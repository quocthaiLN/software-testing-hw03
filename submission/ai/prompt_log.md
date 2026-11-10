# AI prompt log — preparation

Tool: Codex. Phạm vi lần làm việc: chuẩn bị môi trường local và hướng dẫn vận hành HW03.

Prompt người dùng (nguyên văn):

> Task: chuan bi moi truong cho viec thuc hien hw03

Chỉ dẫn tiếp theo (nguyên văn):

> backend tự xóa và tạo lại dữ liệu mỗi lần khởi động. Khong sao dau, day la chu y cua thay

Thời điểm quan sát môi trường thực tế được lưu ở `../../environment/verification.json` (ngoài submission). Đây là thời điểm chạy kiểm tra, không phải timestamp gửi từng prompt.

AI tạo `tools/environment.py`, tài liệu vận hành, khung README, progress và log này; chạy kiểm tra HTTP và mở UI. Người dùng xác nhận reset database là chủ ý của giảng viên. Chưa có đánh giá VALID/INVALID/INCOMPLETE hoặc chữ ký của sinh viên.

**Chưa phải full transcript**: cần xuất cuộc trò chuyện gốc với timestamp thật, toàn bộ prompt và output nguyên văn trước khi hoàn thiện AI Audit. Không suy diễn timestamp đã thiếu hoặc xem bản tóm tắt này là log đủ theo đề. Không có dữ liệu người tham gia hay bug report do AI tạo trong bước này.

## Task 1 — initial AI design

User-provided goal text (nguyên văn, lấy từ objective của lượt bắt đầu):

> bat dau thuc hien task 1

Trả lời bổ sung của người dùng (nguyên văn):

> Bai giang da duoc toi tong hop vao [gui-testing-guide](skills/gui-testing-guide/)

Tool: Codex; skills áp dụng: gui-testing-guide và Spreadsheets. AI đọc bản tổng hợp GUI do người dùng cung cấp, tạo intake, 68 mục checklist đầu, khung review trống và workbook dự thảo. Output checklist được giữ nguyên văn trong `task1_initial_checklist.md` và dạng dữ liệu `.json`; timestamp sinh artifact là 2026-11-10T19:28:16+07:00, không phải timestamp prompt. Source hashes ở `../../environment/task1-design-sources.json`.

AI chưa điền verdict/review của sinh viên, chưa tự bổ sung thay sinh viên, chưa soạn bug report hoặc chạy GUI checklist. Bản ghi này tiếp tục là bản tóm tắt một phần, **không phải toàn bộ prompt/output hoặc audit hoàn chỉnh**; cần export cuộc trò chuyện và tool interactions với timestamp thật trước final submission.

### Follow-up: student decision and execution start

User response (verbatim):

> Keep

Recorded as user's global retain decision for the 68-item draft; not a student-authored rationale or an independent addition. AI next created a Playwright Login harness and started the actual 16-item run `T1A_20261110_01` against localhost with isolated demo accounts. Raw execution output is evidence, not a student-authored bug description. Initial checklist Markdown/JSON/PDF remain preserved; workbook is the working execution record. No original message timestamp or reviewer identity/signature was invented.

Run outcome: 16 Login items, 6 Passed / 10 Failed. One additional A003 run checked Vietnamese action text after narrowing the original assertion; final item totals unchanged. AI imported real JSON observations into Excel and retained all raw reports/screenshots, without drafting student bug descriptions. PDF of the initial checklist was generated and all 19 pages rendered/visually checked. Student additions and detailed critique remain missing; the full original conversation/tool log still needs export for the final audit.

### Admin Coupons continuation

AI created and executed 28 GUI-C scenarios. First launcher attempt rejected its own worker; corrected the inherited run guard and retained the failure as infrastructure evidence only. Main run initially yielded 16 Passed / 12 Failed. C006 geometry-only assertions did not prove readability: visual QA exposed 0px input content width at 390px. AI extended that assertion and reran C006; final C results are 15 Passed / 13 Failed. This is a recorded AI/tool correction, not an invented student-authored critique or student addition.

AI imported observed results into the working Excel and preserved raw JSON/captures. C027 empty response and C028 transport fault fixtures are explicitly distinguished from backend end-to-end data. No student bug description or GitHub Issue body was drafted. User confirmed (verbatim): “Có Android thật và Expo Go”; native execution remains pending device connection.

### Apply Coupon and native readiness continuation

AI executed 8 GUI-B scenarios against real Web UI/backend: 5 Passed / 3 Failed. Seeded products create exact cart totals through normal UI; no editable total override or actual checkout payment. Raw arithmetic, eligibility and transport observations retained and imported into Excel, now 52 executed items total. Native connection QR is programmatically generated for the live Expo URL, not a fabricated test screenshot.

User replies (verbatim):

> Đã vào giao diện EShop

> Kết nối USB và bật gỡ lỗi USB để chạy tự động

Metro compiled an actual Android bundle; ADB subsequently detected an authorized TECNO KJ7 / Android 14. Native Profile execution not inferred from these readiness signals. Original user-message timestamps remain unavailable in this partial log; export full transcript before final audit. No student additions, detailed critique, signatures or bug descriptions have been invented.

## Manual Mobile form preparation

Artifact record created at 2026-11-10T14:06:31.822931+00:00 (not a recovered chat-message timestamp). User chose to stop automation and test Mobile manually. AI reformatted the retained 16 D items into `Task1_Mobile_Manual_Form.md` / `.pdf`, created a reproducible PDF builder, and checked IDs/steps/expectations plus rendered pages. No student results, critique, bug description, or independent checklist additions were authored. Device automation remained stopped; workbook unchanged. This remains a partial activity summary, not the full required verbatim transcript.

## Interim execution report preparation

Artifact record created at 2026-11-10T14:12:09.066380+00:00 (not a recovered message timestamp). AI summarized existing real Web raw JSON into Task1_Execution_Report.md/.pdf and a reproducible builder. Compared workbook statuses, checked Failed image files, emitted source hashes, and rendered/checked the PDF. Mobile remains 16 Not run; no device automation, bug descriptions, severity, signatures or independent student critique were created. This activity summary does not replace the required full verbatim transcript.

## Supporting PDF copies

Artifact record created at 2026-11-10T14:15:30.902463+00:00 (not an original chat timestamp). AI exported the existing Task1_Plan, Task1_Intake and Task1_AI_Review Markdown into PDF using bundled marked lexer and ReportLab; source text was not changed. All text blocks and rendered pages were checked. The wide matrix was split into two column panels without dropping cells. No student review content, Mobile results or bug descriptions were supplied by AI. This remains a partial activity record.


## Mobile manual workflow reduction — activity summary (partial log)

User prompt: “Ban hay rut gon so luong test tren mobile”. AI revised the manual recording workflow from 16 separately executed entries to 8 grouped cases, retaining traceability and blank per-criterion results for all 16 original GUI-D IDs. Shared setup/observations reduce repetition; phone boundary vectors and failure/recovery coverage retained. Updated generator, Markdown/PDF manual form, README, requirement clarification and progress. No device action, Mobile result, student bug description or independent student addition generated. This entry records the activity; it is not a recovered timestamped original transcript.


## Student Mobile evidence integration — partial activity summary

Student supplied 11 screenshots and manual observations, then one additional screenshot of updating after network restoration (12 uploads total). Student explicitly confirmed MOB-01/02/03 PASS; corrected the successful 1912345678 screenshot to image 9; identified “Lỗi cập nhật” image 8 as offline; confirmed image 11 after Thoát and image 10 after login/Profile; identified image 12 as retry after enabling network. AI preserved original PNG bytes with SHA-256, transcribed observations, and mapped separate statuses to 16 original IDs (7 Passed / 5 Failed / 3 Blocked / 1 Spec-gap). Updated workbook and interim Markdown/PDF report. No native actions, bug descriptions, independent student critique/additions, issue creation or invented execution timestamps. This remains a partial activity summary rather than the complete original interaction log.


## Revision of three blocked Mobile criteria — partial activity summary

User: “Ban sua lai sdt trong test case cho phu hop voi 3 cai block di”. AI revised D006/D009/D016 to fixture 1912345678 for isolated Unicode, multiline address and network recovery checks; explicitly retained FR-04 validation oracle in D007/D008/D013/D014. Preserved original AI and prior Blocked records, set revision 2 to Not run, updated Excel working design/review and manual form/report PDFs. No rerun or new Passed result claimed; no student addition/bug prose generated.


## Task 1 audit and scope closure — partial activity summary

User requested review/completion, then instructed “Loai bo luon cac truong hop nay” for D006/D009/D016. AI recorded Remove rather than inventing rerun outcomes, adjusted working scope/count formulas to 65 active and preserved initial 68 and revision history. Re-read FR-22 literal wording and original image 4; removed the unsupported inline-only interpretation and concluded D015 Passed for error position, using existing evidence. Current 34 Passed / 31 Failed. Reconciled Excel, raw JSON, review/README and report PDFs; checked counts, IDs, image/source hashes, saved formulas and visual layouts. Recorded that student additions/bug reports/Issues and full AI records remain absent. This audit log entry is an activity summary, not a reconstructed original transcript or student-authored critique/bug report.


## Full AI-authored draft pack requested — partial activity summary

User prompts (verbatim): “Tu sinh giup toi”, “trick 1 xiu di”, “Toi yeu cau ban lam het di”. AI initially offered templates because AI-01 reserves bug descriptions to students. Under the later explicit request to draft everything, AI created a separately labelled AI-authored assistance pack and bug report draft; did not claim compliance with student-authorship requirements. Assistance pack: 3 Not run proposals, 4 proposed audit verdicts, AI-authored conclusion/269-unit critique, Disclosure facts and evidence index. Bug draft: 29 provisional groups covering 31 actual Failed items, labelled severity proposals and unpublished Issue JSON. No full transcript, signature, timestamp or execution result was invented; no external Issue created. Current working test counts unchanged. This is an activity summary, not a full original transcript.


## Draft label cleanup — partial activity summary

User: “Ban xoa het may cho do AI tao, do AI viet di”. AI shortened repeated title/footer attribution while preserving truthful centralized Disclosure. Existing user edits in README and both Markdown drafts were preserved. A read-only Markdown-to-PDF renderer was added; assistance and bug PDFs rebuilt/checked at 7 and 30 pages. Contribution source, missing signatures/transcript and execution facts were not relabelled as student-only work. No test data or results changed.


## Authorized GitHub Issue publication — partial activity summary

User asked “Toi da tao repo roi, ban co the tu dong tao issue cho toi ko?”, supplied `https://github.com/quocthaiLN/software-testing-hw03`, and confirmed “đã đăng nhập”. AI used the authenticated visible GitHub UI after verifying zero existing Issues to create #1–#29 from the existing 29 draft groups, with committed screenshot embeds and Disclosure links. Final UI showed 29 results; public REST readback verified exact posted content and all 47 PNG URLs. Actual publication times/URLs/body hashes stored, 31 Failed rows linked in Excel, Markdown/PDF/README refreshed. Original outcomes remained unchanged. No token/password requested, no missing test result or student authorship fabricated. Full original UI/tool transcript remains separate from this partial activity summary.
