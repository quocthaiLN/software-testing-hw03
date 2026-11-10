# HW03 — Submission workspace

Trạng thái: đã bắt đầu thiết kế Task 1, chưa phải bài nộp hoàn chỉnh.

| Nội dung | Nơi dự kiến / trạng thái |
| --- | --- |
| Main report Markdown + PDF | Chưa tạo; GUI, usability, cross-platform và phụ lục AI |
| Excel GUI checklist + test summary | `GUI_Checklist.xlsx`: 68 mục được người dùng Keep; Login 16 đã chạy, 6 Passed / 10 Failed; 52 mục B/C/D Not run |
| Bug report + GitHub Issues | Chưa có; sinh viên tự viết mô tả theo AI Agreement |
| Usability | `evidence/usability/`; cần pilot + 7 phiên người thật, scale, notes, analysis |
| Cross-platform | `evidence/platforms/`; cần >=3 nền tảng hợp lệ và chạy checklist |
| GUI screenshots | `evidence/gui/T1A_20261110_01/` và `T1A_20261110_02/`: ảnh thật các mục Login Failed, raw JSON và error context; chưa có Bug ID do sinh viên viết |
| AI records | `ai/`; lưu prompt/output nguyên văn, audit/disclosure và critique 200–300 từ |
| Skills + demo video | Chưa tạo |
| Git log | Xuất lịch sử thật khi chuẩn bị nộp |
| Tự chấm và thống kê | Chưa tự chấm; chưa có kiểm thử homework nào được thực hiện |

Hướng dẫn môi trường ở `../ENVIRONMENT.md`; tiến độ ở `../PROGRESS.md`.
Không dùng các smoke checks môi trường làm số lượng checklist Passed.
Khi hoàn tất, bổ sung số màn hình/flow, checklist designed/executed/passed/failed, số bug, người tham gia và video; điền bảng tự chấm 30/40/20/10.

## Task 1 hiện tại

- `Task1_Plan.md`: phạm vi và kế hoạch bốn feature.
- `Task1_Intake.md`: feature briefs, 31 widgets, phase order, ma trận widget × heuristic và spec-gaps.
- `ai/task1_initial_checklist.md` / `.json` / `.pdf`: bản AI gốc 68 mục được giữ để so sánh; PDF 19 trang đã render/kiểm tra.
- `Task1_AI_Review.md` và sheet AI Review trong Excel: ghi nhận trả lời “Keep” cho bản đầu; lý do chi tiết/mục sinh viên tự thêm còn thiếu.
- Checklist thiết kế 68; thực thi 16 mục Login; Passed 6; Failed 10; Not run 52. Có 17 scenario runs vì A003 chạy lại một lần sau chỉnh assertion; không đếm lại thành mục mới hoặc bug mới.
- `evidence/gui/login_execution.json`: quan sát và lịch sử chạy thô, không phải bug report. Các mô tả bug và severity cần sinh viên tự viết theo AI Agreement.
- Bộ chạy và hướng dẫn tái lập ở `../tools/gui/README.md`. Edge headless không được tính thay Chrome/Firefox/Expo Go cho Task 3.

Nguồn hướng dẫn GUI là bản tổng hợp do sinh viên cung cấp tại `skills/gui-testing-guide/`; các tài liệu thiết kế khác ngoài bản checklist AI đầu còn chờ PDF. Mọi tài liệu được giữ trong bộ nộp cuối cần bản PDF theo policies, được render và kiểm tra trước đóng gói. Chưa có ZIP hoặc điểm tự chấm.
