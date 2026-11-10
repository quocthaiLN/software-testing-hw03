# HW03 — Requirement checklist

Nguồn chuẩn: `2026.HW03.GUI Usability_En.pdf` (9 trang), `../policies.md`, `../AGENTS.md` và AI Templates. Trích xuất lần đầu ngày 2026-11-10 từ file checklist trước đó trống. Bảng này xác định nghĩa vụ; trạng thái và bằng chứng thực hiện ở `PROGRESS.md`. Tên file chưa tồn tại dưới đây là đầu ra dự kiến. Chưa đánh dấu hoàn thành Task 1 chỉ vì đã có kế hoạch.

| ID | Nguồn | Scope | Bước / đầu ra | Acceptance criteria và evidence |
| --- | --- | --- | --- | --- |
| HW03-SCOPE | §5, tr.3–4; policies Collaboration | Bắt buộc | Chọn màn hình/flow, ghi scope trong main report | Scope cụ thể, đủ phức tạp và hạn chế trùng tính năng. Đề gốc không cho trùng màn hình chính; người dùng xác nhận ngày 2026-11-10 giảng viên/TA cập nhật cho phép trùng màn hình. Áp dụng cập nhật này khi lập kế hoạch; không cần đưa trao đổi phân công vào báo cáo |
| HW03-T1-01 | §6 Task 1, tr.4 | Bắt buộc | Đọc bài giảng GUI trước thiết kế | Ghi bài giảng/phiên bản đã đối chiếu; người dùng cung cấp bản tổng hợp `../skills/gui-testing-guide/`, đã đọc SKILL và bốn references ngày 2026-11-10; hash nguồn ở `environment/task1-design-sources.json` |
| HW03-T1-02 | §6 Task 1, tr.4; §14 tr.8 | Bắt buộc | AI tạo bản đầu; thiết kế checklist; xuất Excel + summary | >40 mục riêng biệt, đủ IA-01–04; lưu bản AI gốc, mỗi mục có tiêu chí và màn hình; `submission/GUI_Checklist.xlsx` |
| HW03-T1-03 | §6 Task 1, tr.4 | Bắt buộc | Sinh viên phản biện, sửa và tự thêm mục AI bỏ sót | Có review và giải thích vì sao AI bỏ sót từng mục thêm; `submission/Task1_AI_Review.md` |
| HW03-T1-04 | §6 Task 1, tr.4 | Bắt buộc | Chạy từng mục; ghi Passed/Failed, Notes, ảnh Failed | Có environment/input/expected/actual/evidence; mọi Failed có lý do và screenshot thật; không lấy smoke checks làm kết quả |
| HW03-T1-05 | §6 Task 1, tr.4; AI-01 §11 | Bắt buộc khi phát hiện bug | Sinh viên viết bug report Markdown và GitHub Issues | Mọi bug phát hiện ghi cả hai nơi, issue có screenshot; lưu ảnh local; không để AI soạn mô tả bug |
| HW03-T2-01 | §5–6, tr.3–5 | Bắt buộc | Đọc bài giảng usability; chọn một flow, mục tiêu, scenario và instruments | Scenario hướng mục tiêu; SUS/UEQ-S hoặc thang có lý giải; câu hỏi clarity/error recovery/speed/trust |
| HW03-T2-02 | §6 tr.5; §11 tr.7 | Bắt buộc | Tuyển 7 người thật ngoài lớp; chạy pilot, chỉnh instruments | Danh sách tên/liên hệ có thể xác minh, che 4 số giữa; evidence pilot và chỉnh sửa, không bịa participant |
| HW03-T2-03 | §6 tr.5 | Bắt buộc | 7 phiên, một người/phiên, think aloud, quan sát trung lập | Notes có cấu trúc, screen recordings; audio có consent, trợ giúp chỉ khi bế tắc; §14 nói recordings “where available”, cần ghi rõ thiếu gì/lý do |
| HW03-T2-04 | §6 tr.5 | Bắt buộc | Chấm scale, nhóm pain points, xếp severity, ghi bug | Dữ liệu gốc 7 người, tính toán kiểm tra được; phân biệt isolated/systemic; bug thật ở Markdown/Issues kèm ảnh |
| HW03-T3 | §6 tr.5–6; §11 tr.7 | Bắt buộc | Chạy Task 1 trên ≥3 nền tảng | Chrome + Firefox + Safari/Android Chrome; Expo Go điện thoại thật có thể thay một nền tảng. Trial cloud ưu tiên mạnh; phương án thay theo đề. Ảnh browser/OS/device và localhost, overlay email sinh viên, MSSV/họ tên trong form; kết quả checklist theo nền tảng |
| HW03-SKILL | §7 tr.6; §15 tr.8 | Khuyến khích; rubric 10 điểm | Skill tái sử dụng và video demo YouTube | Nộp skill và demo end-to-end một màn hình/flow; không đồng nhất với điều kiện tối thiểu Task 1 |
| HW03-AI | §2,9–10 tr.1–2,6–7; policies; AI-01/02/03 | Bắt buộc | Transcript, audit appendix, disclosure và critique | Mỗi tương tác có tool/time/prompt/output thật; audit theo template, verdict/lý do/fix; critique 200–300 từ; disclosure đúng đóng góp, biểu mẫu sinh viên ký; không tự tạo chữ ký hoặc timestamp thiếu |
| HW03-GIT | §12 tr.7; AGENTS workflow 6 | Bắt buộc | Commit riêng mỗi bước, mỗi usability session; xuất log text | Lịch sử thật, thông điệp rõ; `git log --graph --all --stat`; xác minh repo/remote phục vụ GitHub Issues |
| HW03-DOC | §14 tr.7–8; policies Format | Bắt buộc | Main report, bug report/evidence, AI critique/audit, Excel, session/platform evidence | Main report và AI critique/audit có Markdown + PDF; Markdown/text khác có PDF theo policies. Render và kiểm tra trực quan PDF; bộ nộp tự chứa nội dung, link không thay evidence |
| HW03-FINAL | §14–15 tr.7–8; §17 tr.9; policies | Khi chuẩn bị nộp | README self-assessment + test summary, Git logs, ZIP | Tổng số screens/flows/items designed/executed/passed/failed/bugs/participants/demo; rubric 30/40/20/10; tên `<StudentID>_HW03_AI_GUIUsability_<grade 000–100>.zip`; xác nhận thông tin chưa biết; Moodle deadline, ≤20 file, ≤20 MB/file, không thiếu tài liệu bắt buộc |

## Phạm vi kế hoạch hiện tại

Bắt đầu thực hiện Task 1 cho FR-02, FR-09, FR-17 và FR-04 Mobile theo `submission/Task1_Plan.md`. Đã tạo bản AI đầu 68 mục và intake; checklist cuối còn chờ review/bổ sung của sinh viên. Task 2/3 và final được liệt kê để tránh bỏ nghĩa vụ toàn bài, chưa triển khai trong yêu cầu hiện tại.

## Điểm cần đối chiếu khi triển khai

- Bản tổng hợp bài giảng GUI đã được người dùng chỉ định tại `../skills/gui-testing-guide/`; dùng tên mục và hash thật, không viện dẫn giả số slide. Bài giảng usability và AI Usage Guideline đầy đủ vẫn chưa được cung cấp.
- FR-17 ghi CRUD nhưng chi tiết chỉ Thêm/Xem/Xóa. Theo chi tiết, không tự bắt buộc Sửa.
- Không tự bổ sung giới hạn discount percent ≤100 hoặc độ dài tên/code khi đặc tả không nêu.
- Quy định ảnh Task 3 khác ảnh Failed Task 1; phải đáp ứng cả khi dùng chung bằng chứng.

## Điều chỉnh cách thực hiện Mobile

Theo yêu cầu người dùng rút gọn số test Mobile: phiếu thủ công hiện dùng 8 ca MOB-01…08, gộp đủ 16 tiêu chí GUI-D gốc để giảm các thao tác mở/nhập/lưu lặp lại. Đây là 8 ca thực hiện, không phải giảm số tiêu chí thiết kế xuống 8: bản AI ban đầu, Excel và số liệu 68 designed / 52 executed / 16 Not run vẫn giữ nguyên. Khi có kết quả, cập nhật riêng từng ID gốc theo quan sát; không suy một kết quả chung cho cả nhóm. HW03-T1-04 vẫn chờ dữ liệu thật.

Cập nhật sau nhận kết quả thủ công: 12 ảnh gốc và lời xác nhận được ánh xạ vào 16 ID GUI-D tại `submission/evidence/gui/mobile_execution.json`; Mobile 7 Passed / 5 Failed / 3 Blocked / 1 Spec-gap. Tổng 68 tiêu chí: 33 Passed / 31 Failed / 3 Blocked / 1 Spec-gap. Bản AI gốc và phiếu template giữ nguyên; Excel/báo cáo đã tích hợp actual. Phần còn chờ là lưu hợp lệ, multiline, recovery đúng miền và oracle FR-22; kết quả ghi nhận không tự thỏa mọi acceptance criterion của HW03-T1-04.
