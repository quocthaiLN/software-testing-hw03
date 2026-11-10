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
