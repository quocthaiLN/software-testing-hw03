# Task 1 - Báo cáo thực thi GUI (bản đang hoàn thiện)

Mốc dữ liệu: các lượt chạy Web ngày 2026-11-10. Phạm vi thiết kế gồm bốn feature A/B/C/D. Task 1 chưa hoàn tất: Đã tích hợp kết quả Mobile do sinh viên cung cấp và 12 ảnh gốc; 3 tiêu chí còn Blocked và 1 Spec-gap. Báo cáo này tổng hợp hồ sơ thực thi, không thay bug report do sinh viên tự viết.


## 1. Thống kê hiện tại

| Feature | Thiết kế | Chốt P/F | Passed | Failed | Chờ B/S | Not run |
| --- | --- | --- | --- | --- | --- | --- |
| A / FR-02 - Web Login | 16 | 16 | 6 | 10 | 0 | 0 |
| B / FR-09 - Web Apply Coupon | 8 | 8 | 5 | 3 | 0 | 0 |
| C / FR-17 - Admin Coupons | 28 | 28 | 15 | 13 | 0 | 0 |
| D / FR-04 - Mobile Profile | 16 | 12 | 7 | 5 | 4 | 0 |
| Tổng | 68 | 64 | 33 | 31 | 4 | 0 |

64/68 mục đã chốt Passed/Failed; 33 Passed / 31 Failed / 3 Blocked / 1 Spec-gap / 0 Not run. Có 55 lượt scenario Web; 8 ca Mobile thủ công được ánh xạ vào 16 tiêu chí, không cộng 16 ánh xạ hoặc 12 ảnh thành số scenario runs.

Chờ B/S là tổng Blocked và Spec-gap; hai trạng thái vẫn tách riêng theo ID và Excel. Mọi tiêu chí Mobile đã có ghi nhận, nhưng ghi nhận một phần không đồng nghĩa hoàn tất kiểm tra. Số bug duy nhất chưa xác định; Failed không phải số bug đã khử trùng.


## 2. Phạm vi và cơ sở thiết kế

| Feature / màn hình | Nội dung trong phạm vi | Giới hạn |
| --- | --- | --- |
| A / Web /login | Nhãn, input, focus/bàn phím, login, phản hồi sai/khóa và phục hồi | Tài khoản thử riêng; không khóa tài khoản demo dùng chung |
| B / Web /checkout | Khối coupon, điều kiện C1-C5, công thức/biên, phản hồi và recovery | Cart là tiền điều kiện; không chốt đơn/thanh toán |
| C / Admin Coupons | Tạo, xem, xóa coupon; form, bảng, navigation và trạng thái | FR-17 chi tiết chỉ yêu cầu Thêm/Xem/Xóa; không tự thêm Sửa |
| D / Expo Go Profile | Email chỉ đọc, tên/điện thoại/địa chỉ, bàn phím/cuộn, lưu, đăng xuất | Kết quả thủ công một phần; không gồm lịch sử/hủy đơn |

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
| Mobile thủ công | Android thật / Expo Go theo ngữ cảnh phiên; ảnh gốc 1080×2436, tài khoản test@eshop.com. Model/OS từ bước setup trước không tự chứng minh metadata lần chạy này; timestamp đầy đủ và build chưa được cung cấp. |
| Task 3 | Edge headless và viewport hẹp chưa thỏa ma trận Chrome/Firefox/Expo Go; không tuyên bố đã hoàn tất đa nền tảng |

Trình tự thực thi: A → C → B; D chuyển sang sinh viên làm thủ công theo yêu cầu. Mỗi scenario Web có tiền điều kiện riêng; Mobile theo trình tự thủ công do sinh viên mô tả, có giới hạn bằng chứng ảnh tĩnh. API/SQLite chỉ hỗ trợ fixture và đối chiếu; kết luận GUI dựa trên giao diện và request/response thật. Nếu assertion đầu hỏng, các assertion phía sau chưa chạy không được coi là đạt.

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

Sinh viên xác nhận MOB-01/02/03 PASS; các trạng thái còn lại đối chiếu mô tả thao tác và ảnh thật. Bản phiếu vẫn là template trống; hồ sơ hiện tại nằm ở evidence/gui/mobile_execution.json. Ảnh 9 thay ảnh 6 cho số 1912345678; ảnh 8 lúc tắt mạng; ảnh 12 sau bật mạng; ảnh 11 sau Thoát và ảnh 10 sau đăng nhập lại.

| Item ID | Tiêu chí giữ lại | IA | Trạng thái |
| --- | --- | --- | --- |
| GUI-D-001 | Tiêu đề và nhãn tiếng Việt | IA-01 | Passed |
| GUI-D-002 | Màu cập nhật và đăng xuất | IA-01 | Passed |
| GUI-D-003 | Layout trên màn hình điện thoại | IA-01 | Passed |
| GUI-D-004 | Nhận biết email chỉ đọc | IA-01 | Passed |
| GUI-D-005 | Không sửa email qua GUI | IA-02 | Passed |
| GUI-D-006 | Tên tiếng Việt lưu nguyên vẹn | IA-02 | Blocked |
| GUI-D-007 | Biên độ dài số điện thoại | IA-02 | Failed |
| GUI-D-008 | Điện thoại sai miền và kiểu bàn phím | IA-02 | Failed |
| GUI-D-009 | Địa chỉ nhiều dòng | IA-02 | Blocked |
| GUI-D-010 | Đến hồ sơ từ điều hướng | IA-03 | Passed |
| GUI-D-011 | Bàn phím không chặn thao tác lưu | IA-03 | Passed |
| GUI-D-012 | Đăng xuất đúng nhãn và hiệu lực | IA-03 | Failed |
| GUI-D-013 | Phản hồi cập nhật thành công | IA-04 | Failed |
| GUI-D-014 | Sửa điện thoại sau lỗi | IA-04 | Failed |
| GUI-D-015 | Vị trí lỗi form mobile | IA-04 | Spec-gap |
| GUI-D-016 | Phục hồi cập nhật khi mất mạng | IA-04 | Blocked |


## 5.D.1 Ghi nhận Mobile theo ID gốc

Các dòng sau là bản chép/đối chiếu dữ liệu thực thi, không phải mô tả bug do AI soạn. Passed dựa trên xác nhận người thực hiện kết hợp ảnh; ảnh tĩnh không tự chứng minh mọi thao tác chạm, cuộn hay dán. Từng vector biên được người dùng xác nhận, ảnh alert là bằng chứng đại diện.

| ID / trạng thái | Quan sát và giới hạn | Ảnh gốc |
| --- | --- | --- |
| GUI-D-001 / Passed | MOB-01: người dùng xác nhận PASS; ảnh hiển thị Hồ sơ của bạn và các nhãn tiếng Việt. | image-01.png |
| GUI-D-002 / Passed | MOB-01: người dùng xác nhận PASS; ảnh có Cập nhật xanh và Thoát đỏ. Nhãn đăng xuất được đánh giá riêng ở D012. | image-01.png |
| GUI-D-003 / Passed | MOB-02: người dùng xác nhận PASS; ảnh toàn form và ảnh khi bàn phím mở. Khả năng cuộn/đóng bàn phím theo xác nhận người thực hiện. | image-01.png, image-02.png |
| GUI-D-004 / Passed | MOB-03: người dùng xác nhận PASS; email có nhãn (Không đổi), nền khác trường sửa. | image-01.png, image-03.png |
| GUI-D-005 / Passed | MOB-03: người dùng xác nhận PASS; email test@eshop.com giữ nguyên trên các ảnh sau. Thao tác thử nhập/dán dựa vào xác nhận người dùng, ảnh tĩnh không tự chứng minh thao tác. | image-03.png, image-09.png, image-10.png |
| GUI-D-006 / Blocked | Đã nhập Nguyễn Văn Ánh; ảnh sau đăng nhập lại còn tên có dấu, nhưng lần lưu với số đúng 0912345678 báo lỗi. Chưa chứng minh lưu tên với bộ dữ liệu hợp lệ theo D006; lần lưu số 1912345678 thuộc dữ liệu sai miền. | image-04.png, image-06.png, image-10.png |
| GUI-D-007 / Failed | Theo người dùng, cả 091234567 / 0912345678 / 09123456789 / 091234567890 đều báo lỗi. 9/12 bị từ chối đúng kỳ vọng; 10/11 bắt đầu 0 cũng bị từ chối. Ảnh là thông báo đại diện, không phải ảnh riêng từng vector. | image-05.png |
| GUI-D-008 / Failed | Người dùng xác nhận 1912345678 cập nhật thành công, dùng ảnh 9 thay ảnh 6 dán nhầm; 09abc45678 báo lỗi ở ảnh 7. Bàn phím điện thoại chưa có ảnh riêng, không tự kết luận phần đó đạt. | image-07.png, image-09.png |
| GUI-D-009 / Blocked | Ảnh 6 có địa chỉ 12 Nguyễn Trãi Phường Bến Thành trên một dòng; ảnh sau đăng nhập lại để trống địa chỉ. Chưa có bằng chứng nhập/sửa nhiều dòng và lưu với điện thoại hợp lệ như D009 yêu cầu. | image-04.png, image-06.png, image-10.png |
| GUI-D-010 / Passed | Người dùng xác nhận MOB-01 PASS và ảnh 10 là mở Profile sau đăng nhập; email test@eshop.com hiển thị. | image-01.png, image-10.png |
| GUI-D-011 / Passed | MOB-02 được người dùng xác nhận PASS; ảnh bàn phím ở trường tên. Các trường khác và thao tác cuộn/đóng dựa vào xác nhận người dùng, không suy từ ảnh này. | image-02.png |
| GUI-D-012 / Failed | Ảnh nút ghi Thoát thay Đăng xuất. Người dùng xác nhận ảnh 11 sau bấm Thoát, ảnh 10 sau đăng nhập lại/mở Profile. Điều hướng ra đăng nhập được xác nhận; không có kiểm tra truy cập trái phép riêng. | image-01.png, image-11.png, image-10.png |
| GUI-D-013 / Failed | Người dùng báo lưu bộ hồ sơ hợp lệ thì báo lỗi điện thoại; ảnh 4 có native alert Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số. Ảnh 6 hiển thị 0912345678; không phải bằng chứng cập nhật thành công. | image-04.png, image-06.png |
| GUI-D-014 / Failed | Dữ liệu có chữ bị từ chối; số đúng 0912345678 vẫn báo lỗi theo người dùng. Cập nhật thành công với 1912345678 không thỏa nhánh sửa về số hợp lệ; chưa có video/thứ tự đầy đủ từng lần bấm. | image-04.png, image-06.png, image-07.png, image-09.png |
| GUI-D-015 / Spec-gap | Ảnh cho thấy native alert giữa màn hình, không phải lỗi inline trên nút Cập nhật. Giữ điểm review cách áp dụng FR-22 cho native; chưa tự chốt native Alert tương đương hoặc không tương đương oracle. | image-04.png, image-05.png, image-07.png |
| GUI-D-016 / Blocked | Người dùng xác nhận ảnh 8 có Lỗi cập nhật là lúc tắt mạng, ảnh 12 là cập nhật sau bật mạng; ảnh 9/10 có tên Nguyễn Văn Ánh và số 1912345678. Đã ghi nhận nhánh mất mạng và thao tác retry theo người thực hiện. D016 còn Blocked cho oracle dữ liệu hợp lệ vì retry dùng 1912345678 (sai miền); số đúng 0912345678 bị validation chặn. Ảnh sau retry không có phản hồi thành công riêng; không suy persistence backend chỉ từ ảnh form. | image-08.png, image-12.png |

Các ảnh được lưu nguyên byte và SHA-256 trong evidence/gui/T1D_MANUAL_01/manifest.json. Giữ cả ảnh người dùng dán nhầm để bảo toàn nguồn; không dùng ảnh 6 làm bằng chứng 1912345678 thành công. Hash xác nhận ảnh 2/3, 4/5/7 và 9/10/12 giống nguyên byte. Ngữ cảnh khác nhau do sinh viên xác nhận; không tính upload thành các frame/lần chạy độc lập.


## 6. Độ phủ widget × heuristic

Mỗi ô là số mục thiết kế / số mục đã chốt P/F liên kết widget và heuristic. Đây là truy vết thiết kế, không phải số assertion đạt hoặc chứng nhận mọi trạng thái đã được thử. Dấu - nghĩa là chưa có ánh xạ. H10 chưa có mục; sinh viên cần xác định tính áp dụng và bổ sung khi review.

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
| D-W01 | - | 1/1 | - | 1/1 | - | - | - | - | - | - |
| D-W02 | - | - | - | 1/1 | 1/1 | 1/1 | - | 1/1 | - | - |
| D-W03 | - | 1/0 | 1/1 | - | - | - | 1/1 | 1/1 | - | - |
| D-W04 | - | - | 1/1 | - | 2/2 | - | 2/2 | 1/1 | 2/2 | - |
| D-W05 | - | 1/0 | 1/1 | - | - | - | 2/1 | 1/1 | - | - |
| D-W06 | 2/1 | - | 1/1 | 1/1 | - | - | 1/1 | 1/1 | 3/1 | - |
| D-W07 | - | - | 1/1 | 2/2 | - | - | - | - | - | - |
| D-W08 | - | - | 1/1 | - | - | 1/1 | - | - | - | - |
| D-W09 | 2/1 | - | - | - | - | - | - | - | 3/1 | - |


## 7. Oracle và giới hạn cần review

FR-09 chưa nêu cách làm tròn tiền lẻ. Không dùng riêng khác biệt format số lẻ để khẳng định lỗi. Kết luận B005 không phụ thuộc việc chọn rounding policy; dữ liệu gốc giữ các vector và số tiền thật.

FR-17 chưa yêu cầu percent ≤100, lượt là số nguyên hoặc ngày tạo luôn ở tương lai. Không thêm các oracle này để tăng số lỗi.

D015: FR-22 yêu cầu lỗi trên submit; cách áp dụng cho native Alert vẫn cần sinh viên review. Ảnh 4/5/7 cho thấy native Alert; D015 được giữ Spec-gap chờ quyết định oracle.

Các tiêu chí loading, ngăn gửi lặp, xác nhận/hoàn tác xóa là heuristic đã có nguồn. Không gọi chúng là điều kiện nghiệp vụ FR-17.

Các scenario có nhiều biến thể không chứng minh mọi nhánh nếu dừng sớm; raw log và mã test là căn cứ xác định phần thực sự đã chạy.


## 8. Hồ sơ bằng chứng và công việc còn lại

| Hồ sơ trong bộ nộp | Vai trò |
| --- | --- |
| GUI_Checklist.xlsx | Working checklist, Execution, Summary và AI Review; 68 trạng thái từ hồ sơ Web và Mobile khớp workbook ở checkpoint này. |
| evidence/gui/login_execution.json | 16 latest / 17 history; mỗi Failed latest trỏ tới ảnh thật. |
| evidence/gui/admin_execution.json | 28 latest / 30 history; giữ kết quả superseded và launcher bị loại. |
| evidence/gui/apply_execution.json | 8 latest / 8 history; giữ từng vector, fixture và request/response. |
| evidence/gui/T1A_*, T1B_*, T1C_* | Playwright JSON, screenshot và attachment gốc; 26 Web Failed có ảnh local. |
| evidence/gui/mobile_execution.json; T1D_MANUAL_01/ | 16 tiêu chí ánh xạ, 12 ảnh gốc và hash; 5 Mobile Failed có ảnh, một số ảnh đại diện nhiều vector theo lời người thực hiện. |
| Task1_AI_Review.md; ai/prompt_log.md | Keep đã ghi nhận; review độc lập/audit/transcript đầy đủ còn thiếu. Prompt log hiện là bản tóm tắt PARTIAL. |

D006/D009 còn Blocked ở lưu hợp lệ và nhiều dòng; D016 đã có ảnh sau bật mạng nhưng dùng số sai miền 1912345678, còn Blocked cho oracle dữ liệu hợp lệ. D015 còn Spec-gap. Không suy persistence backend từ ảnh form; không tự sửa SUT để bỏ qua validation.

Sinh viên tự review, sửa/bổ sung mục AI bỏ sót và ghi lý do. Không coi gợi ý hoặc phiếu AI tạo là đóng góp độc lập của sinh viên.

Sinh viên tự viết bug report Markdown, severity và GitHub Issues kèm ảnh; khử trùng trước thống kê bug. Repository HW03 hiện chưa có remote, issue URL/Bug ID chưa có. Báo cáo này không soạn mô tả bug.

Hoàn thiện transcript gốc, audit/disclosure/critique và thông tin sinh viên thật. Báo cáo hiện tại do AI tổng hợp dữ liệu thực thi; chưa phải bản sinh viên ký xác nhận.

Hoàn thiện main report và PDF các tài liệu cần giữ, xuất Git log thật khi đóng gói. Task 2, Task 3 và tự chấm/ZIP chưa hoàn thành và không thuộc kết quả Task 1 ở checkpoint này.

