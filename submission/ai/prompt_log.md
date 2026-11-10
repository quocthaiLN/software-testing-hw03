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
