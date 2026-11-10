# HW03 — Submission workspace

Trạng thái: đã bắt đầu thiết kế Task 1, chưa phải bài nộp hoàn chỉnh.

| Nội dung | Nơi dự kiến / trạng thái |
| --- | --- |
| Main report Markdown + PDF | Chưa có bản toàn bài; `Task1_Execution_Report.md/.pdf` là phần GUI đang hoàn thiện, 52 mục Web có kết quả và 16 Mobile Not run |
| Excel GUI checklist + test summary | `GUI_Checklist.xlsx`: 68 mục được người dùng Keep; Web A/B/C 52 đã chạy, 26 Passed / 26 Failed; Mobile D 16 Not run |
| Bug report + GitHub Issues | Chưa có; sinh viên tự viết mô tả theo AI Agreement |
| Usability | `evidence/usability/`; cần pilot + 7 phiên người thật, scale, notes, analysis |
| Cross-platform | `evidence/platforms/`; cần >=3 nền tảng hợp lệ và chạy checklist |
| GUI screenshots | `evidence/gui/T1A_*/`, `T1B_*/`, `T1C_*/`: ảnh thật các mục Web Failed, raw JSON và error context; chưa có Bug ID do sinh viên viết |
| AI records | `ai/`; lưu prompt/output nguyên văn, audit/disclosure và critique 200–300 từ |
| Skills + demo video | Chưa tạo |
| Git log | Xuất lịch sử thật khi chuẩn bị nộp |
| Tự chấm và thống kê | Chưa tự chấm; Task 1 Web A/B/C đã thực thi 52 mục, Mobile D chờ kiểm thử thủ công |

Hướng dẫn môi trường ở `../ENVIRONMENT.md`; tiến độ ở `../PROGRESS.md`.
Không dùng các smoke checks môi trường làm số lượng checklist Passed.
Khi hoàn tất, bổ sung số màn hình/flow, checklist designed/executed/passed/failed, số bug, người tham gia và video; điền bảng tự chấm 30/40/20/10.

## Task 1 hiện tại

- `Task1_Plan.md` / `.pdf`: phạm vi và kế hoạch bốn feature; trạng thái thiết kế lịch sử, không thay kết quả thực thi hiện tại.
- `Task1_Execution_Report.md` / `.pdf`: báo cáo Task 1 đang hoàn thiện, tổng hợp 52 kết quả Web thật, lịch sử chạy/fixture và ma trận widget × heuristic; 16 Mobile vẫn Not run. Checkpoint nguồn có SHA-256 tại `evidence/gui/task1_report_checkpoint.json`.
- `Task1_Mobile_Manual_Form.md` / `.pdf`: phiếu trống rút gọn còn 8 ca thao tác (MOB-01…08), ánh xạ đủ 16 tiêu chí GUI-D gốc; dùng chung bước kiểm tra để giảm lặp, chưa chứa kết quả. PDF 5 trang. Thống kê Excel vẫn theo 16 tiêu chí gốc, không cộng thêm 8 ca.
- `Task1_Intake.md` / `.pdf`: feature briefs, 31 widgets, phase order, ma trận widget × heuristic và spec-gaps; PDF chia ma trận H1–H5 / H6–H10 để đọc rõ.
- `ai/task1_initial_checklist.md` / `.json` / `.pdf`: bản AI gốc 68 mục được giữ để so sánh; PDF 19 trang đã render/kiểm tra.
- `Task1_AI_Review.md` / `.pdf` và sheet AI Review trong Excel: ghi nhận trả lời “Keep” cho bản đầu; lý do chi tiết/mục sinh viên tự thêm còn thiếu.
- Checklist thiết kế 68; thực thi 52 mục A/B/C; Passed 26; Failed 26; Not run 16 (Mobile D). Có 55 GUI scenario runs; các lần chạy lại không thành mục hoặc bug mới. Lỗi launcher C01 được giữ riêng, không tính là kết quả sản phẩm.
- `evidence/gui/login_execution.json`: quan sát và lịch sử chạy thô, không phải bug report. Các mô tả bug và severity cần sinh viên tự viết theo AI Agreement.
- `evidence/gui/admin_execution.json`: 28 mục Admin, kết quả cuối 15 Passed / 13 Failed. C006 chuyển từ kết quả hình học ban đầu sang Failed sau QA và đo vùng hiển thị input. C027 dùng phản hồi rỗng có kiểm soát; C028 dùng fault injection, được ghi rõ trong dữ liệu gốc.
- `evidence/gui/apply_execution.json`: 8 mục Apply Coupon, 5 Passed / 3 Failed; giỏ hàng được tạo bằng sản phẩm thật và UI, không sửa trực tiếp tổng tiền. Fixture JWT hết hạn, giữ response chờ và ngắt mạng được ghi rõ; không có đơn hàng/thanh toán được tạo trong phần B.
- Bộ chạy và hướng dẫn tái lập ở `../tools/gui/README.md`. Edge headless không được tính thay Chrome/Firefox/Expo Go cho Task 3.

Nguồn hướng dẫn GUI là bản tổng hợp do sinh viên cung cấp tại `skills/gui-testing-guide/`; kế hoạch, intake và phiếu AI Review đã có PDF, được đối chiếu nội dung và render/kiểm tra. Hồ sơ AI và tài liệu cuối vẫn cần được hoàn thiện và xuất bản PDF tương ứng. Mọi tài liệu được giữ trong bộ nộp cuối cần bản PDF theo policies, được render và kiểm tra trước đóng gói. Chưa có ZIP hoặc điểm tự chấm.
