# Task 1 — Feature brief, widgets và các phase

## Nguồn

Đặc tả EShop README v2.0, API specification, đề HW03 §6 Task 1; tài liệu bài giảng do sinh viên tổng hợp tại `skills/gui-testing-guide/SKILL.md` và bốn tệp references. Đã đọc tài liệu này ngày 2026-11-10 sau khi người dùng chỉ định. Không có số slide gốc để viện dẫn; dùng tên tài liệu/mục thực tế.

Đây là intake để thiết kế. Login đã được mở và quan sát bằng trình duyệt trong ứng dụng; các màn hình còn lại được kiểm kê từ source và đặc tả, còn cần đối chiếu trên UI thật. Kiểm kê source không phải evidence Pass/Fail. Không sửa mã SUT.

## Feature briefs

| Feature | Actor / mục tiêu | Tiền điều kiện | Luồng chính và phụ |
| --- | --- | --- | --- |
| A — Login | User vào tài khoản và hiểu trạng thái lỗi/khóa | Web hoạt động, user thử riêng, biết trạng thái khóa | Mở → nhập → validate → gửi → thành công; sai/khóa → sửa/chờ → thử lại; liên kết phụ tới đăng ký/quên mật khẩu |
| B — Apply Coupon | User nhận biết mã có áp dụng được và số tiền sau giảm | Giỏ đúng tổng, phiên/token/lượt dùng được kiểm soát | Mở checkout → nhập mã → áp dụng → phản hồi; mã sai/mạng lỗi → sửa/thử lại; sửa mã đã áp dụng |
| C — Admin Coupons | Admin tạo/xem/xóa mã thử | Admin đăng nhập, dữ liệu coupon cô lập | Vào tab → xem → nhập → validate → tạo → xem lại; xóa/hủy; lỗi → phục hồi |
| D — Mobile Profile | User cập nhật hồ sơ của chính mình | Điện thoại thật/Expo Go/LAN API, user đăng nhập | Mở hồ sơ → nhập/chọn → bàn phím/cuộn → lưu → xem lại; lỗi → sửa; đăng xuất |

Phân lớp theo `references/strategies.md`: low-level kiểm tra widget; application dùng domain/boundary; integration đối chiếu GUI với kết quả tải/lưu thật; compatibility dùng viewport/device. Không thêm performance/soak vào Task 1.

## Widget inventory

| Widget | Loại / vị trí | Quy tắc và trạng thái cần xem |
| --- | --- | --- |
| A-W01 | Heading / đầu form Login | Nội dung đúng tác vụ, h1 web |
| A-W02 | Textbox Email | Enabled, nhập/sửa/dán, required, email valid/invalid, focus |
| A-W03 | Password | Enabled, nhập/sửa/dán, required, che ký tự, focus |
| A-W04 | Submit | Click/Enter/focus, valid/invalid/locked/result |
| A-W05 | Links phụ | Quên mật khẩu/Đăng ký, click/Enter đúng đích |
| A-W06 | Error/feedback | Sai thông tin, khóa, hết khóa, vị trí lỗi, khôi phục |
| B-W01 | Textbox mã | Rỗng/whitespace, nhập, sửa, xóa; không tự giả định case-sensitive |
| B-W02 | Áp dụng | Enabled/disabled, pending, success/error, retry |
| B-W03 | Error/result/totals | C1–C5, percent/fixed, tiền tệ, stale state |
| B-W04 | Breadcrumb | Theo FR-23; widget theo yêu cầu, chưa khẳng định hiện có |
| C-W01 | Heading | Ngữ cảnh Coupons, tiếng Việt, h1 |
| C-W02 | Textbox code | Required, mới/trùng, whitespace, focus |
| C-W03 | Select type | percent/fixed, chọn/đóng bằng bàn phím, liên hệ đơn vị |
| C-W04 | Number discount_value | Required, -1/0/1, percent/fixed |
| C-W05 | Number min_order_amount | Required, -1/0/1 |
| C-W06 | Date picker expired_at | Required, valid/invalid/leap date |
| C-W07 | Number max_uses_per_user | Required, 0/1/2; số lẻ chưa có oracle rõ |
| C-W08 | Tạo mã | Click/Enter/focus, success/error/retry |
| C-W09 | Table | Hiển thị dữ liệu, format, refresh, empty/error, resize |
| C-W10 | Xóa / dialog nếu có | Đúng dòng, phòng xóa nhầm, cancel/ESC nếu có, lỗi/retry |
| C-W11 | Navigation tab | Vào/ra, highlight, keyboard, không tự thay đổi dữ liệu |
| C-W12 | Error/feedback | Tạo/xóa/network failure, vị trí, khả năng khôi phục |
| D-W01 | Native heading | Đúng ngữ cảnh/tiếng Việt, không kiểm tra thẻ HTML |
| D-W02 | Email readonly | Không sửa, nhận biết trạng thái |
| D-W03 | Name | Unicode, sửa/lưu, bàn phím/cuộn |
| D-W04 | Phone | Biên 9/10/11/12, đầu 0, ký tự sai, phone-pad |
| D-W05 | Address multiline | Unicode/nhiều dòng, sửa/lưu, không tràn |
| D-W06 | Cập nhật | Chạm, bàn phím không che, success/error/network/retry |
| D-W07 | Đăng xuất | Nhãn, chạm, session state |
| D-W08 | Profile navigation | Đến đúng hồ sơ của user |
| D-W09 | Feedback | Success/error/retry, vị trí lỗi theo FR-22 cần review native |

31 widget được kiểm kê, gồm widget mong đợi từ yêu cầu ngay cả khi chưa có trên UI. Không coi kiểm kê này là chứng nhận đã bao phủ mọi biến thể. Độ phủ widget × heuristic do checklist truy vết; các lỗ hổng coverage còn lại phải được sinh viên rà soát/bổ sung.

## Trình tự thực thi dự kiến

1. A: Open → Input → Validate → Submit → Result → Recover/Navigate. Reset lockout bằng tài khoản thử riêng, ghi thời điểm thật; không đổi logic SUT.
2. C: Open/Navigate → Input → Validate → Submit → Result → Recover. Dùng prefix coupon riêng; không xóa coupon mặc định để tạo empty state.
3. B: dùng fixture tạo ở C, Open → Input → Submit → Result → Recover/Navigate. Mỗi biến thể chỉ làm sai một C1–C5; tiền đề không đạt thì ghi Blocked và chỉ rõ mục phụ thuộc.
4. D: Open/Navigate → Input/keyboard → Validate → Submit → Result → Recover → Logout. Không thay native profile bằng web profile.

Các test độc lập phải tự chuẩn bị trạng thái; thứ tự trên là tổ chức phiên, không cho phép test dựa vào kết quả run trước mà không nêu tiền điều kiện.

## Giả định / Spec-gap cần sinh viên review

- Không có quy tắc làm tròn tiền khi percent tạo số thập phân. GUI-B-005 có biến thể 300001; phép tính theo công thức là 30000.1 / 270000.9 nhưng quyết định format/làm tròn phải ghi căn cứ trước kết luận lỗi hiển thị.
- FR-17 chưa quy định lượt phải là số nguyên, percent ≤100 hay ngày tạo phải ở tương lai. Không đặt các giới hạn này làm kỳ vọng bắt buộc.
- Quy tắc FR-22 lỗi phía trên submit khi native app dùng alert cần đối chiếu cách áp dụng trong bài giảng/đặc tả. Không tự coi alert là tương đương hoặc tự gọi là lỗi trước review.
- Loading, ngăn gửi lặp, xác nhận/hoàn tác xóa coupon và giữ ý nghĩa đơn vị là heuristic có nguồn H1/H3/H5/H6; không gán lại thành FR-17.
- Ví dụ trong guide có chỗ không phải quy tắc nền tảng chung (double-click chọn một từ không mặc nhiên phải chọn cả input). Chỉ áp dụng ý nghĩa phù hợp; bảng không bắt buộc sort nếu SUT không nêu.

## Đối chiếu nguồn hiện tại

Môi trường smoke check lúc 2026-11-10T19:25:33+07:00: HTTP API/Web/Admin và login user/admin đều đạt 5/5; chỉ là readiness. Bản ghi máy ở `../environment/task1-readiness.json`. Trình duyệt hỗ trợ intake là in-app browser; không tính vào Chrome/Firefox/Expo Go cho Task 3. Các sửa đổi có sẵn trong SUT được giữ nguyên.

Đề yêu cầu sinh viên tự review/bổ sung sau bản AI gốc; `Task1_AI_Review.md` và sheet AI Review còn chờ sinh viên. Checklist Excel là working draft. Chưa có kết quả thực thi GUI hoặc bug report trong bước thiết kế.

## Ma trận truy vết widget × heuristic của bản AI đầu

Ô liệt kê Item ID; dấu — nghĩa là chưa có mục ánh xạ, không phải không áp dụng hoặc đã đạt. H10 chưa có mục ở bản AI đầu. Sinh viên xác định tính áp dụng và bổ sung sau review.

| Widget | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-W01 | — | GUI-A-001 | — | GUI-A-001, GUI-A-002 | — | — | — | — | — | — |
| A-W02 | — | GUI-A-003 | — | GUI-A-003, GUI-A-010 | GUI-A-005, GUI-A-008 | GUI-A-007 | GUI-A-009, GUI-A-010 | — | GUI-A-008 | — |
| A-W03 | — | GUI-A-003 | — | GUI-A-003, GUI-A-010 | GUI-A-006, GUI-A-008 | GUI-A-007 | GUI-A-009, GUI-A-010 | — | GUI-A-008 | — |
| A-W04 | GUI-A-012, GUI-A-015, GUI-A-016 | GUI-A-003 | — | GUI-A-003, GUI-A-004, GUI-A-010 | GUI-A-008 | — | GUI-A-010, GUI-A-012 | — | GUI-A-008, GUI-A-015, GUI-A-016 | — |
| A-W05 | — | GUI-A-003 | GUI-A-011 | GUI-A-003, GUI-A-010 | — | — | GUI-A-010, GUI-A-011 | — | — | — |
| A-W06 | GUI-A-015, GUI-A-016 | — | — | — | — | — | — | — | GUI-A-013, GUI-A-014, GUI-A-015, GUI-A-016 | — |
| B-W01 | GUI-B-003, GUI-B-008 | — | — | — | GUI-B-002, GUI-B-003 | — | — | — | GUI-B-008 | — |
| B-W02 | GUI-B-005, GUI-B-006, GUI-B-007, GUI-B-008 | — | — | — | GUI-B-002, GUI-B-007 | — | — | — | GUI-B-006, GUI-B-008 | — |
| B-W03 | GUI-B-003, GUI-B-005, GUI-B-006, GUI-B-008 | GUI-B-001 | — | GUI-B-001 | GUI-B-003 | — | — | — | GUI-B-006, GUI-B-008 | — |
| B-W04 | — | — | GUI-B-004 | — | — | GUI-B-004 | — | — | — | — |
| C-W01 | — | GUI-C-001 | — | GUI-C-001, GUI-C-002 | — | — | — | — | — | — |
| C-W02 | — | — | GUI-C-022 | GUI-C-017 | GUI-C-008, GUI-C-009, GUI-C-022 | GUI-C-007 | GUI-C-017 | GUI-C-006 | GUI-C-008, GUI-C-009 | — |
| C-W03 | — | GUI-C-016 | — | GUI-C-010, GUI-C-017 | — | GUI-C-007, GUI-C-016 | GUI-C-010, GUI-C-017 | GUI-C-006 | — | — |
| C-W04 | — | GUI-C-016 | — | GUI-C-017 | GUI-C-011, GUI-C-014 | GUI-C-007, GUI-C-016 | GUI-C-017 | GUI-C-006 | GUI-C-011, GUI-C-014 | — |
| C-W05 | — | — | — | GUI-C-017 | GUI-C-012, GUI-C-014 | GUI-C-007 | GUI-C-017 | GUI-C-006 | GUI-C-012, GUI-C-014 | — |
| C-W06 | — | — | — | GUI-C-017 | GUI-C-014, GUI-C-015 | GUI-C-007 | GUI-C-017 | GUI-C-006 | GUI-C-014 | — |
| C-W07 | — | — | — | GUI-C-017 | GUI-C-013, GUI-C-014 | GUI-C-007 | GUI-C-017 | GUI-C-006 | GUI-C-013, GUI-C-014 | — |
| C-W08 | GUI-C-023, GUI-C-028 | — | — | GUI-C-003 | GUI-C-003 | — | GUI-C-018 | GUI-C-006 | GUI-C-024, GUI-C-028 | — |
| C-W09 | GUI-C-023, GUI-C-026, GUI-C-027, GUI-C-028 | GUI-C-004, GUI-C-005 | GUI-C-022 | GUI-C-004 | GUI-C-022 | GUI-C-005, GUI-C-027 | — | GUI-C-006 | GUI-C-028 | — |
| C-W10 | GUI-C-026, GUI-C-028 | — | GUI-C-025 | GUI-C-003 | GUI-C-003, GUI-C-025 | — | — | — | GUI-C-028 | — |
| C-W11 | GUI-C-020 | — | GUI-C-019, GUI-C-022 | GUI-C-020, GUI-C-021 | GUI-C-022 | GUI-C-019 | GUI-C-021 | — | — | — |
| C-W12 | GUI-C-028 | — | — | — | — | — | — | — | GUI-C-024, GUI-C-028 | — |
| D-W01 | — | GUI-D-001 | — | GUI-D-001 | — | — | — | — | — | — |
| D-W02 | — | — | — | GUI-D-004 | GUI-D-005 | GUI-D-004 | — | GUI-D-003 | — | — |
| D-W03 | — | GUI-D-006 | GUI-D-011 | — | — | — | GUI-D-011 | GUI-D-003 | — | — |
| D-W04 | — | — | GUI-D-011 | — | GUI-D-007, GUI-D-008 | — | GUI-D-008, GUI-D-011 | GUI-D-003 | GUI-D-007, GUI-D-014 | — |
| D-W05 | — | GUI-D-009 | GUI-D-011 | — | — | — | GUI-D-009, GUI-D-011 | GUI-D-003 | — | — |
| D-W06 | GUI-D-013, GUI-D-016 | — | GUI-D-011 | GUI-D-002 | — | — | GUI-D-011 | GUI-D-003 | GUI-D-014, GUI-D-015, GUI-D-016 | — |
| D-W07 | — | — | GUI-D-012 | GUI-D-002, GUI-D-012 | — | — | — | — | — | — |
| D-W08 | — | — | GUI-D-010 | — | — | GUI-D-010 | — | — | — | — |
| D-W09 | GUI-D-013, GUI-D-016 | — | — | — | — | — | — | — | GUI-D-014, GUI-D-015, GUI-D-016 | — |
