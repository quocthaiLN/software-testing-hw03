# Task 1 - Báo cáo thực thi GUI (bản đang hoàn thiện)

Mốc dữ liệu: các lượt chạy Web ngày 2026-11-10. Phạm vi thiết kế gồm bốn feature A/B/C/D. Task 1 chưa hoàn tất: Mobile đang được sinh viên kiểm thử thủ công; kết quả chưa được cung cấp. Báo cáo này tổng hợp hồ sơ thực thi, không thay bug report do sinh viên tự viết.


## 1. Thống kê hiện tại

| Feature | Thiết kế | Đã chạy | Passed | Failed | Not run |
| --- | --- | --- | --- | --- | --- |
| A / FR-02 - Web Login | 16 | 16 | 6 | 10 | 0 |
| B / FR-09 - Web Apply Coupon | 8 | 8 | 5 | 3 | 0 |
| C / FR-17 - Admin Coupons | 28 | 28 | 15 | 13 | 0 |
| D / FR-04 - Mobile Profile | 16 | 0 | 0 | 0 | 16 |
| Tổng | 68 | 52 | 26 | 26 | 16 |

52/68 mục đã thực thi (76,47%); 26/52 mục đã thực thi Passed (50%). Có 55 lượt chạy scenario thật do A003 và C006 được chạy lại; không nhân biến thể dữ liệu thành mục checklist mới. Một lần lỗi launcher trước UI bị loại khỏi số liệu sản phẩm. Số bug duy nhất chưa được xác định; 26 Failed không có nghĩa là 26 bug.

Blocked và Spec-gap chưa được gán cho mục Mobile nào vì chưa nhận kết quả. Các điểm oracle chưa rõ được nêu riêng ở mục 7. Không dùng smoke check, kết nối thiết bị hay nhập thử Unicode làm kết quả Mobile.


## 2. Phạm vi và cơ sở thiết kế

| Feature / màn hình | Nội dung trong phạm vi | Giới hạn |
| --- | --- | --- |
| A / Web /login | Nhãn, input, focus/bàn phím, login, phản hồi sai/khóa và phục hồi | Tài khoản thử riêng; không khóa tài khoản demo dùng chung |
| B / Web /checkout | Khối coupon, điều kiện C1-C5, công thức/biên, phản hồi và recovery | Cart là tiền điều kiện; không chốt đơn/thanh toán |
| C / Admin Coupons | Tạo, xem, xóa coupon; form, bảng, navigation và trạng thái | FR-17 chi tiết chỉ yêu cầu Thêm/Xem/Xóa; không tự thêm Sửa |
| D / Expo Go Profile | Email chỉ đọc, tên/điện thoại/địa chỉ, bàn phím/cuộn, lưu, đăng xuất | Đang chờ kiểm thử thủ công; không gồm lịch sử/hủy đơn |

Nguồn: đề HW03 §6 Task 1; EShop README v2.0 FR-02/04/09/17 và FR-21-24; API specification; bản tổng hợp bài giảng tại skills/gui-testing-guide do sinh viên chỉ định. Tiêu chí heuristic có H1-H10 để truy vết, không được tự gán thành yêu cầu nghiệp vụ. Domain/Boundary chọn input và trạng thái; GUI thật vẫn là đối tượng quan sát.

| IA | A | B | C | D | Tổng |
| --- | --- | --- | --- | --- | --- |
| IA-01 | 4 | 1 | 6 | 4 | 15 |
| IA-02 | 6 | 2 | 12 | 5 | 25 |
| IA-03 | 2 | 1 | 4 | 3 | 10 |
| IA-04 | 4 | 4 | 6 | 4 | 18 |

Bản AI đầu 68 mục được bảo toàn tại ai/task1_initial_checklist.md/.json/.pdf. Sinh viên trả lời Keep cho các mục hiện có; quyết định này không chứng minh đã tự bổ sung mục hoặc viết lý do phản biện. Phần đó còn thiếu trong Task1_AI_Review.md.


## 3. Môi trường và phương pháp thực thi

| Thành phần | Giá trị / giới hạn |
| --- | --- |
| Web GUI đã chạy | Linux; Microsoft Edge headless 155.0.4283.45; viewport 1280×800; C006 thêm 390×844 |
| Địa chỉ cục bộ | Web http://localhost:5173; Admin http://localhost:5174; API http://localhost:3000/api |
| SUT nền tại lúc chạy | 85af3ba875c88283615e22cb108f13e2fccaf0e9; giữ các thay đổi local có sẵn, không khẳng định đây là checkout sạch |
| Runner | Playwright; một worker; retries=0; Run ID mới mỗi lần; ảnh Failed và JSON quan sát thật |
| Mobile readiness | Android thật TECNO KJ7 / Android 14 / Expo Go đã mở Profile tài khoản test; chưa tính Passed/Failed |
| Task 3 | Edge headless và viewport hẹp chưa thỏa ma trận Chrome/Firefox/Expo Go; không tuyên bố đã hoàn tất đa nền tảng |

Trình tự thực thi: A → C → B; D chuyển sang sinh viên làm thủ công theo yêu cầu. Mỗi scenario có tiền điều kiện riêng; không dựa vào test trước. API/SQLite chỉ hỗ trợ fixture và đối chiếu; kết luận GUI dựa trên giao diện và request/response thật. Nếu assertion đầu hỏng, các assertion phía sau chưa chạy không được coi là đạt.

| Trường hợp | Thiết lập được công bố |
| --- | --- |
| A - khóa tài khoản | Đăng ký user demo riêng cho từng tình huống. Kiểm tra số lần sai và mốc hơn 30 giây bằng quan sát có timestamp; không thay logic khóa. |
| C - coupon thử | Code dùng prefix T1, ngoại trừ fixture whitespace được ghi rõ. C015 kiểm tra date input HTML, không chứng minh validation backend. |
| C027 - empty state | Fulfill GET coupons bằng danh sách rỗng có kiểm soát chỉ cho trang test; không xóa coupon dùng chung. |
| C028 - lỗi mạng | Abort GET coupons. Assertion phản hồi tải lỗi hỏng trước các nhánh recovery/tạo/xóa; các nhánh sau chưa được chứng minh. |
| B - tổng giỏ hàng | Seed sản phẩm thật đúng giá; Home → Add to cart → Cart → Checkout. Không sửa ô tổng tiền để giả lập biên. |
| B - điều kiện coupon | Coupon/user/lượt dùng riêng. Inactive đổi bằng SQLite parameterized theo đúng ID/code rồi API verify. Lượt dùng seed qua endpoint, không tuyên bố đã tạo đơn. |
| B - auth và mạng | JWT hết hạn thay riêng header request bằng public demo key; backend trả lời thật. Pending giữ response thật bằng gate; recovery abort transport rồi khôi phục. |


## 4. Lịch sử chạy và hiệu chỉnh

| Suite Run ID | Scenario | Passed | Failed | Bắt đầu (UTC) |
| --- | --- | --- | --- | --- |
| T1A_20261110_01 | 16 | 6 | 10 | 2026-11-10T12:40:54.651Z |
| T1A_20261110_02 | 1 | 0 | 1 | 2026-11-10T12:42:52.051Z |
| T1B_20261110_01 | 8 | 5 | 3 | 2026-11-10T13:11:40.610Z |
| T1C_20261110_02 | 28 | 16 | 12 | 2026-11-10T12:55:19.917Z |
| T1C_20261110_03 | 1 | 1 | 0 | 2026-11-10T12:57:02.149Z |
| T1C_20261110_04 | 1 | 0 | 1 | 2026-11-10T12:57:59.805Z |

T1C_20261110_01 bị lỗi guard lúc worker nạp config, trước mọi thao tác UI; giữ log riêng và loại khỏi tổng 55. A003 được thu hẹp assertion nhãn hành động tiếng Việt rồi vẫn Failed. C006 có hai kết quả hình học hẹp trước đó được giữ trong history; sau visual QA, assertion vùng hiển thị ký tự được bổ sung và run 04 Failed. Chỉ kết quả cuối theo ID được tính vào summary.


## 5.A Kết quả theo mục - FR-02 - Web Login

Đây là trạng thái checklist, không phải danh sách bug đã khử trùng. Bước, input và kỳ vọng gốc nằm trong checklist AI và workbook; actual, assertion và ảnh nằm trong hồ sơ raw tương ứng.

| Item ID | Tiêu chí giữ lại | IA | Trạng thái |
| --- | --- | --- | --- |
| GUI-A-001 | Tiêu đề đúng tác vụ đăng nhập | IA-01 | Failed |
| GUI-A-002 | Một h1 mô tả trang | IA-01 | Failed |
| GUI-A-003 | Ngôn ngữ tiếng Việt | IA-01 | Failed |
| GUI-A-004 | Màu nút đăng nhập | IA-01 | Passed |
| GUI-A-005 | Input email đúng kiểu | IA-02 | Failed |
| GUI-A-006 | Che mật khẩu | IA-02 | Failed |
| GUI-A-007 | Nhãn trường bắt buộc | IA-02 | Failed |
| GUI-A-008 | Chặn submit thiếu dữ liệu | IA-02 | Passed |
| GUI-A-009 | Sửa và dán thông tin | IA-02 | Passed |
| GUI-A-010 | Thứ tự Tab theo bố cục | IA-02 | Failed |
| GUI-A-011 | Liên kết phụ đúng đích | IA-03 | Passed |
| GUI-A-012 | Đăng nhập đúng và điều hướng | IA-03 | Passed |
| GUI-A-013 | Thông báo đăng nhập sai an toàn | IA-04 | Passed |
| GUI-A-014 | Lỗi ở phía trên nút gửi | IA-04 | Failed |
| GUI-A-015 | Khóa sau ba lần sai | IA-04 | Failed |
| GUI-A-016 | Khôi phục sau hết khóa | IA-04 | Failed |


## 5.B Kết quả theo mục - FR-09 - Web Apply Coupon

Đây là trạng thái checklist, không phải danh sách bug đã khử trùng. Bước, input và kỳ vọng gốc nằm trong checklist AI và workbook; actual, assertion và ảnh nằm trong hồ sơ raw tương ứng.

| Item ID | Tiêu chí giữ lại | IA | Trạng thái |
| --- | --- | --- | --- |
| GUI-B-001 | Đơn vị và định dạng số tiền | IA-01 | Passed |
| GUI-B-002 | Không áp dụng mã rỗng | IA-02 | Passed |
| GUI-B-003 | Sửa mã làm mất hiệu lực kết quả cũ | IA-02 | Passed |
| GUI-B-004 | Breadcrumb tại checkout | IA-03 | Failed |
| GUI-B-005 | Hiển thị kết quả giảm giá hợp lệ | IA-04 | Failed |
| GUI-B-006 | Phản hồi điều kiện mã không đạt | IA-04 | Failed |
| GUI-B-007 | Trạng thái đang áp dụng | IA-04 | Passed |
| GUI-B-008 | Phục hồi sau mã sai hoặc lỗi mạng | IA-04 | Passed |


## 5.C Kết quả theo mục - FR-17 - Admin Coupons

Đây là trạng thái checklist, không phải danh sách bug đã khử trùng. Bước, input và kỳ vọng gốc nằm trong checklist AI và workbook; actual, assertion và ảnh nằm trong hồ sơ raw tương ứng.

| Item ID | Tiêu chí giữ lại | IA | Trạng thái |
| --- | --- | --- | --- |
| GUI-C-001 | Nội dung tiếng Việt đúng ngữ cảnh | IA-01 | Passed |
| GUI-C-002 | Một h1 trên trang Admin | IA-01 | Failed |
| GUI-C-003 | Màu tạo và xóa | IA-01 | Failed |
| GUI-C-004 | Đơn vị theo loại coupon | IA-01 | Passed |
| GUI-C-005 | Cột danh sách đọc được | IA-01 | Passed |
| GUI-C-006 | Bố cục khi resize | IA-01 | Failed |
| GUI-C-007 | Nhãn trường bắt buộc luôn rõ | IA-02 | Failed |
| GUI-C-008 | Mã rỗng và whitespace | IA-02 | Failed |
| GUI-C-009 | Mã duy nhất | IA-02 | Passed |
| GUI-C-010 | Hai lựa chọn loại mã | IA-02 | Passed |
| GUI-C-011 | Biên giá trị giảm | IA-02 | Failed |
| GUI-C-012 | Biên ngưỡng đơn | IA-02 | Failed |
| GUI-C-013 | Biên số lượt mỗi người | IA-02 | Passed |
| GUI-C-014 | Không bỏ trống trường bắt buộc | IA-02 | Failed |
| GUI-C-015 | Ngày hợp lệ và ngày không tồn tại | IA-02 | Passed |
| GUI-C-016 | Nhãn giá trị đổi theo loại | IA-02 | Passed |
| GUI-C-017 | Thứ tự Tab trong form | IA-02 | Passed |
| GUI-C-018 | Gửi form bằng Enter | IA-02 | Passed |
| GUI-C-019 | Đến đúng tab Coupons | IA-03 | Passed |
| GUI-C-020 | Highlight tab hiện tại | IA-03 | Passed |
| GUI-C-021 | Điều hướng tab bằng bàn phím | IA-03 | Failed |
| GUI-C-022 | Rời form không tự lưu/xóa | IA-03 | Passed |
| GUI-C-023 | Tạo thành công cập nhật danh sách | IA-04 | Passed |
| GUI-C-024 | Lỗi tạo rõ và đúng vị trí | IA-04 | Failed |
| GUI-C-025 | Phòng xóa nhầm và hủy được | IA-04 | Failed |
| GUI-C-026 | Xóa đúng mã và làm mới danh sách | IA-04 | Passed |
| GUI-C-027 | Trạng thái danh sách rỗng | IA-04 | Failed |
| GUI-C-028 | Lỗi mạng không thành công giả | IA-04 | Failed |


## 5.D Kết quả theo mục - FR-04 - Mobile Profile

Chưa nhận kết quả thủ công. Phiếu Task1_Mobile_Manual_Form.md/.pdf được chuẩn bị để ghi môi trường, input, actual và ảnh. Không suy diễn kết quả từ source hoặc readiness.

| Item ID | Tiêu chí giữ lại | IA | Trạng thái |
| --- | --- | --- | --- |
| GUI-D-001 | Tiêu đề và nhãn tiếng Việt | IA-01 | Not run |
| GUI-D-002 | Màu cập nhật và đăng xuất | IA-01 | Not run |
| GUI-D-003 | Layout trên màn hình điện thoại | IA-01 | Not run |
| GUI-D-004 | Nhận biết email chỉ đọc | IA-01 | Not run |
| GUI-D-005 | Không sửa email qua GUI | IA-02 | Not run |
| GUI-D-006 | Tên tiếng Việt lưu nguyên vẹn | IA-02 | Not run |
| GUI-D-007 | Biên độ dài số điện thoại | IA-02 | Not run |
| GUI-D-008 | Điện thoại sai miền và kiểu bàn phím | IA-02 | Not run |
| GUI-D-009 | Địa chỉ nhiều dòng | IA-02 | Not run |
| GUI-D-010 | Đến hồ sơ từ điều hướng | IA-03 | Not run |
| GUI-D-011 | Bàn phím không chặn thao tác lưu | IA-03 | Not run |
| GUI-D-012 | Đăng xuất đúng nhãn và hiệu lực | IA-03 | Not run |
| GUI-D-013 | Phản hồi cập nhật thành công | IA-04 | Not run |
| GUI-D-014 | Sửa điện thoại sau lỗi | IA-04 | Not run |
| GUI-D-015 | Vị trí lỗi form mobile | IA-04 | Not run |
| GUI-D-016 | Phục hồi cập nhật khi mất mạng | IA-04 | Not run |


## 6. Độ phủ widget × heuristic

Mỗi ô là số mục thiết kế / số mục đã chạy liên kết widget và heuristic. Đây là truy vết thiết kế, không phải số assertion đạt hoặc chứng nhận mọi trạng thái đã được thử. Dấu - nghĩa là chưa có ánh xạ. H10 chưa có mục; sinh viên cần xác định tính áp dụng và bổ sung khi review.

| Widget | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-W01 | - | 1/1 | - | 2/2 | - | - | - | - | - | - |
| A-W02 | - | 1/1 | - | 2/2 | 2/2 | 1/1 | 2/2 | - | 1/1 | - |
| A-W03 | - | 1/1 | - | 2/2 | 2/2 | 1/1 | 2/2 | - | 1/1 | - |
| A-W04 | 3/3 | 1/1 | - | 3/3 | 1/1 | - | 2/2 | - | 3/3 | - |
| A-W05 | - | 1/1 | 1/1 | 2/2 | - | - | 2/2 | - | - | - |
| A-W06 | 2/2 | - | - | - | - | - | - | - | 4/4 | - |
| B-W01 | 2/2 | - | - | - | 2/2 | - | - | - | 1/1 | - |
| B-W02 | 4/4 | - | - | - | 2/2 | - | - | - | 2/2 | - |
| B-W03 | 4/4 | 1/1 | - | 1/1 | 1/1 | - | - | - | 2/2 | - |
| B-W04 | - | - | 1/1 | - | - | 1/1 | - | - | - | - |
| C-W01 | - | 1/1 | - | 2/2 | - | - | - | - | - | - |
| C-W02 | - | - | 1/1 | 1/1 | 3/3 | 1/1 | 1/1 | 1/1 | 2/2 | - |
| C-W03 | - | 1/1 | - | 2/2 | - | 2/2 | 2/2 | 1/1 | - | - |
| C-W04 | - | 1/1 | - | 1/1 | 2/2 | 2/2 | 1/1 | 1/1 | 2/2 | - |
| C-W05 | - | - | - | 1/1 | 2/2 | 1/1 | 1/1 | 1/1 | 2/2 | - |
| C-W06 | - | - | - | 1/1 | 2/2 | 1/1 | 1/1 | 1/1 | 1/1 | - |
| C-W07 | - | - | - | 1/1 | 2/2 | 1/1 | 1/1 | 1/1 | 2/2 | - |
| C-W08 | 2/2 | - | - | 1/1 | 1/1 | - | 1/1 | 1/1 | 2/2 | - |
| C-W09 | 4/4 | 2/2 | 1/1 | 1/1 | 1/1 | 2/2 | - | 1/1 | 1/1 | - |
| C-W10 | 2/2 | - | 1/1 | 1/1 | 2/2 | - | - | - | 1/1 | - |
| C-W11 | 1/1 | - | 2/2 | 2/2 | 1/1 | 1/1 | 1/1 | - | - | - |
| C-W12 | 1/1 | - | - | - | - | - | - | - | 2/2 | - |
| D-W01 | - | 1/0 | - | 1/0 | - | - | - | - | - | - |
| D-W02 | - | - | - | 1/0 | 1/0 | 1/0 | - | 1/0 | - | - |
| D-W03 | - | 1/0 | 1/0 | - | - | - | 1/0 | 1/0 | - | - |
| D-W04 | - | - | 1/0 | - | 2/0 | - | 2/0 | 1/0 | 2/0 | - |
| D-W05 | - | 1/0 | 1/0 | - | - | - | 2/0 | 1/0 | - | - |
| D-W06 | 2/0 | - | 1/0 | 1/0 | - | - | 1/0 | 1/0 | 3/0 | - |
| D-W07 | - | - | 1/0 | 2/0 | - | - | - | - | - | - |
| D-W08 | - | - | 1/0 | - | - | 1/0 | - | - | - | - |
| D-W09 | 2/0 | - | - | - | - | - | - | - | 3/0 | - |


## 7. Oracle và giới hạn cần review

FR-09 chưa nêu cách làm tròn tiền lẻ. Không dùng riêng khác biệt format số lẻ để khẳng định lỗi. Kết luận B005 không phụ thuộc việc chọn rounding policy; dữ liệu gốc giữ các vector và số tiền thật.

FR-17 chưa yêu cầu percent ≤100, lượt là số nguyên hoặc ngày tạo luôn ở tương lai. Không thêm các oracle này để tăng số lỗi.

D015: FR-22 yêu cầu lỗi trên submit; cách áp dụng cho native Alert vẫn cần sinh viên review. Chưa có kết quả thực thi D015.

Các tiêu chí loading, ngăn gửi lặp, xác nhận/hoàn tác xóa là heuristic đã có nguồn. Không gọi chúng là điều kiện nghiệp vụ FR-17.

Các scenario có nhiều biến thể không chứng minh mọi nhánh nếu dừng sớm; raw log và mã test là căn cứ xác định phần thực sự đã chạy.


## 8. Hồ sơ bằng chứng và công việc còn lại

| Hồ sơ trong bộ nộp | Vai trò |
| --- | --- |
| GUI_Checklist.xlsx | Working checklist, Execution, Summary và AI Review; 52 trạng thái raw khớp workbook ở checkpoint này. |
| evidence/gui/login_execution.json | 16 latest / 17 history; mỗi Failed latest trỏ tới ảnh thật. |
| evidence/gui/admin_execution.json | 28 latest / 30 history; giữ kết quả superseded và launcher bị loại. |
| evidence/gui/apply_execution.json | 8 latest / 8 history; giữ từng vector, fixture và request/response. |
| evidence/gui/T1A_*, T1B_*, T1C_* | Playwright JSON, screenshot và attachment gốc. Tất cả 26 Failed latest có file ảnh local tồn tại. |
| Task1_AI_Review.md; ai/prompt_log.md | Keep đã ghi nhận; review độc lập/audit/transcript đầy đủ còn thiếu. Prompt log hiện là bản tóm tắt PARTIAL. |

Cần kết quả và ảnh Mobile thủ công cho GUI-D-001…016; sau đó mới cập nhật workbook/báo cáo. Giữ trạng thái chưa chạy cho đến khi có bằng chứng.

Sinh viên tự review, sửa/bổ sung mục AI bỏ sót và ghi lý do. Không coi gợi ý hoặc phiếu AI tạo là đóng góp độc lập của sinh viên.

Sinh viên tự viết bug report Markdown, severity và GitHub Issues kèm ảnh; khử trùng trước thống kê bug. Repository HW03 hiện chưa có remote, issue URL/Bug ID chưa có. Báo cáo này không soạn mô tả bug.

Hoàn thiện transcript gốc, audit/disclosure/critique và thông tin sinh viên thật. Báo cáo hiện tại do AI tổng hợp dữ liệu thực thi; chưa phải bản sinh viên ký xác nhận.

Hoàn thiện main report và PDF các tài liệu cần giữ, xuất Git log thật khi đóng gói. Task 2, Task 3 và tự chấm/ZIP chưa hoàn thành và không thuộc kết quả Task 1 ở checkpoint này.

