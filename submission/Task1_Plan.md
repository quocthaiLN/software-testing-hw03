# HW03 — Kế hoạch thực hiện Task 1: GUI Checklist

Ngày lập: 2026-11-10. Trạng thái: kế hoạch, chưa thiết kế checklist cuối hoặc thực thi kiểm thử.

## 1. Mục tiêu và cơ sở

Thiết kế, phản biện và thực thi GUI checklist cho bốn feature đã chọn; báo lỗi có bằng chứng thật. Task 1 chiếm 30 điểm. Domain Testing và Boundary Value Analysis được dùng để chọn dữ liệu cho form và trạng thái giao diện; kết quả chính vẫn là GUI checklist, không thay bằng bộ API test hay bộ Domain Testing của HW02.

Nguồn: đề `../2026.HW03.GUI Usability_En.pdf`, §4–6 (trang 2–4), §9–12 (trang 6–7), §14–15 (trang 7–8); `../../policies.md`; đặc tả `../../eshop-sut/README.md`, FR-02/04/09/17 và FR-21–24; `../../eshop-sut/api_specification.md`. Các đường dẫn này tính từ thư mục `hw03/submission`; khi hoàn thiện báo cáo phải đưa nội dung cần thiết vào bộ nộp, không dùng liên kết thay bằng chứng.

## 2. Phạm vi

| Feature | Giao diện | Phạm vi kiểm tra | Giới hạn |
| --- | --- | --- | --- |
| A — FR-02 | Web Login, `/login` | Nhãn, email/password, bàn phím/focus, gửi form, thông báo đăng nhập sai/khóa, điều hướng sau thành công | Không kiểm thử chi tiết JWT hoặc lỗ hổng API trong checklist GUI |
| B — FR-09 | Khối mã giảm giá tại Web Checkout, `/checkout` | Nhập mã, phản hồi khi mã không hợp lệ/hết hạn/không đủ điều kiện; hiển thị giảm giá, tổng tiền và trạng thái khi sửa mã | Cart và tạo đơn chỉ là tiền điều kiện/thiết lập lượt dùng; không mở rộng thành kiểm thử toàn bộ thanh toán |
| C — FR-17 | Web Admin → tab Mã giảm giá; màn hình trọng tâm | Form tạo mã, danh sách, xóa, validation và phản hồi; các điều khiển dùng được bằng bàn phím | Đặc tả chỉ yêu cầu Thêm/Xem/Xóa; không tự thêm chức năng Sửa từ chữ “CRUD” |
| D — FR-04 Mobile | Expo Go → Hồ sơ cá nhân | Họ tên, điện thoại, địa chỉ, email chỉ đọc; bàn phím mobile, cuộn, lưu và phản hồi; đăng xuất | Không kiểm thử lịch sử/hủy đơn dù cùng màn hình |

## 3. Phân bổ checklist dự kiến

Đây là ngân sách thiết kế, không phải số mục đã tạo hoặc kết quả đã chạy. Mục tiêu 68 mục độc lập; sau rà soát phải còn ít nhất 41 mục có ý nghĩa, bao phủ đủ bốn IA. Không nhân số mục bằng cách đếm từng bộ dữ liệu hoặc từng trình duyệt thành một mục mới.

| Feature / mã dự kiến | IA-01: UI chung | IA-02: Form | IA-03: Điều hướng | IA-04: Phản hồi/trạng thái | Tổng |
| --- | ---: | ---: | ---: | ---: | ---: |
| A / GUI-A-001…016 | 4 | 6 | 2 | 4 | 16 |
| B / GUI-B-001…008 | 1 | 2 | 1 | 4 | 8 |
| C / GUI-C-001…028 | 6 | 12 | 4 | 6 | 28 |
| D / GUI-D-001…016 | 4 | 5 | 3 | 4 | 16 |
| Tổng | 15 | 25 | 10 | 18 | 68 |

Nhóm nội dung để phát triển thành từng mục:

- IA-01: tiếng Việt, tiêu đề đúng ngữ cảnh, màu hành động, đơn vị tiền, nhãn dễ đọc và bố cục không che nội dung. Yêu cầu một `h1` áp dụng cho web; không áp thẻ HTML lên React Native.
- IA-02: nhãn trường và dấu bắt buộc theo đặc tả, loại input, che mật khẩu, email không sửa được, thứ tự focus, dữ liệu hợp lệ/không hợp lệ và vị trí thông báo lỗi phía trên submit. Không tự coi tên/địa chỉ bắt buộc khi FR-04 chưa quy định.
- IA-03: đến được màn hình đích, trang/tab hiện tại được nhận biết, chuyển màn hình/quay lại, nhãn “Đăng xuất”, thao tác bằng bàn phím trên web và thao tác chạm trên mobile.
- IA-04: phân biệt thành công/thất bại, trạng thái dữ liệu sau lưu/xóa, lỗi có thể phục hồi, trạng thái rỗng và phản hồi khi mạng lỗi. Các tiêu chí ngoài đặc tả, ví dụ trạng thái đang gửi hay xác nhận xóa coupon, phải ghi là nguyên tắc GUI được sinh viên đối chiếu bài giảng, không gán thành yêu cầu nghiệp vụ FR-17.

Không đưa RTL/dark mode vào chỉ để tăng số lượng. Chỉ thêm nếu có hỗ trợ hoặc có tiêu chí phù hợp được xác lập. Accessibility/focus/nhãn là hướng cần sinh viên tự rà; gợi ý trong kế hoạch này vẫn là đóng góp của AI.

## 4. Dữ liệu Domain + Boundary và oracle

Mỗi mục GUI có thể có nhiều biến thể dữ liệu; lưu kết quả từng biến thể để không che lỗi bằng một kết quả tổng hợp. Nếu một biến thể thất bại thì mục tương ứng Failed; sau sửa phải giữ lịch sử trước đó.

| Feature | Dữ liệu/trạng thái cần chuẩn bị | Kết quả mong đợi có căn cứ |
| --- | --- | --- |
| A | Email hợp lệ, sai định dạng, trống; mật khẩu trống/sai/đúng | Email dùng HTML5 email validation; mật khẩu che ký tự; lỗi không tiết lộ chi tiết nhạy cảm; thành công chuyển trạng thái đăng nhập |
| A | Tài khoản riêng, sai liên tiếp lần 1/2/3/4; thử đúng khi đang khóa, trước/sau mốc 30 giây | Từ lần sai thứ 3 khóa 30 giây. Ghi timestamp request/response; không khẳng định chính xác mốc thời gian chỉ bằng thao tác bấm tay. Kiểm tra bộ đếm đúng +1 thuộc kiểm tra chức năng hỗ trợ, không thay bằng quan sát GUI |
| B | Mã tồn tại/không tồn tại/không hoạt động; `EXPIRED`; phiên đăng nhập hợp lệ/không hợp lệ | FR-09 yêu cầu cả C1–C5; GUI phải hiển thị kết quả áp dụng hoặc lỗi tương ứng, không tiếp tục trình bày giảm giá cũ như hợp lệ |
| B | `SAVE10`: 299999, 300000, 300001 ₫; số lượt `m-1`, `m`, `m+1` với `m=max_uses_per_user` | Đủ ngưỡng khi tổng ≥300000; chỉ hợp lệ khi số lượt <m. Tổng 300000 giảm 30000, còn 270000 ₫ nếu thỏa các điều kiện khác |
| B | `BIGBUY`: tổng 500000 ₫; sửa mã sau áp dụng | Giảm cố định 50000, còn 450000 ₫ nếu đủ điều kiện. Ghi rõ quy tắc cập nhật/reset trạng thái là tiêu chí UI cần kiểm tra |
| C | Mã mới và trùng; percent/fixed; `discount_value`: -1, 0, 1; `min_order_amount`: -1, 0, 1; `max_uses_per_user`: 0, 1, 2; bỏ trống các trường bắt buộc | FR-17: code duy nhất, type thuộc hai lựa chọn, giá trị giảm >0, ngưỡng ≥0, lượt ≥1 và các trường đều bắt buộc |
| C | Ngày hợp lệ, trống, không hợp lệ nếu UI cho nhập; chuyển loại percent/fixed, tạo/xem/xóa mã thử riêng | Giá trị hiển thị đúng loại và đơn vị; danh sách phản ánh thao tác thật. Không tự đặt giới hạn percent ≤100, code tối đa N ký tự hoặc cấm tạo mã quá hạn vì đặc tả chưa nêu |
| D | SĐT bắt đầu 0, độ dài 9/10/11/12; ví dụ `091234567`, `0912345678`, `09123456789`, `091234567890`; không bắt đầu 0, chứa chữ | 10–11 chữ số bắt đầu 0 hợp lệ theo FR-04; các biến thể còn lại bị từ chối với phản hồi có thể hiểu |
| D | Tên tiếng Việt, địa chỉ nhiều dòng; mở bàn phím, cuộn tới Cập nhật, lưu rồi mở lại; thử sửa email qua UI | Dữ liệu hợp lệ được giữ sau lưu; email chỉ đọc; trường/nút vẫn thao tác được khi bàn phím mở. Không tự đặt giới hạn độ dài tên/địa chỉ |

Ngày hết hạn FR-09 có điều kiện nghiêm ngặt `now < expired_at`; muốn kiểm tra đúng biên phải ghi timezone và cách diễn giải ngày của SUT, không tự suy ra “hết cuối ngày”. Dữ liệu lượt dùng và khóa phải được thiết lập có thể tái lập. Nếu không tạo được tổng giỏ hàng đúng biên bằng UI, ghi phương pháp seed/API hỗ trợ và trạng thái dữ liệu; kết quả GUI vẫn phải quan sát trên ứng dụng thật.

## 5. Các bước thực hiện và điều kiện hoàn thành

Thời gian dự kiến 5–6 giờ cho Task 1, chưa tính chờ môi trường, phản biện của sinh viên và thời gian Task 2/3. Đây là ước lượng làm việc, không phải yêu cầu của đề.

| Bước / yêu cầu | Việc làm | Đầu ra dự kiến | Điều kiện chuyển bước | Ước lượng |
| --- | --- | --- | --- | --- |
| 1 / HW03-SCOPE, HW03-T1-01 | Đọc bài giảng GUI; chốt nguồn oracle và tiêu chí ngoài đặc tả; xác minh mobile truy cập backend | Scope và nguồn được ghi trong báo cáo | Có bài giảng hoặc ghi rõ đang thiếu; không gán quy tắc tự suy ra thành FR | 30 phút |
| 2 / HW03-T1-02 | AI tạo checklist đầu theo từng feature và IA; lưu nguyên văn prompt/output trước khi chỉnh | `ai/task1_initial_checklist.md`, `ai/` transcript thật | Có bản AI gốc, ≥41 mục dự kiến và không lặp | 45 phút |
| 3 / HW03-T1-03 | Sinh viên kiểm tra từng mục, loại/gộp/sửa và tự bổ sung mục AI bỏ sót; giải thích vì sao bỏ sót | `Task1_AI_Review.md`; checklist được duyệt | Mỗi mục thêm có lý do; phân biệt AI gợi ý với đóng góp độc lập của sinh viên | 45 phút |
| 4 / HW03-T1-02, HW03-T1-04 | Chuyển bản duyệt sang Excel, chuẩn bị tài khoản/coupon/dữ liệu và sổ chạy; thử một mục mỗi feature | `GUI_Checklist.xlsx`, execution log | Dữ liệu tái lập được; trường kết quả chưa chạy không điền Passed | 30 phút |
| 5 / HW03-T1-04 | Chạy A → C → B → D; C chuẩn bị coupon riêng trước B; lưu bằng chứng trước khi reset | Excel, execution log, `evidence/gui/` | Mỗi biến thể có actual result; mỗi Failed có Notes và ảnh | 90–120 phút |
| 6 / HW03-T1-05 | Sinh viên tự viết bug report, khử trùng bug, tạo GitHub Issues kèm ảnh; đối chiếu bug ↔ checklist | `BugReport.md`, issue thật và ảnh local | Mọi bug phát hiện được ghi cả hai nơi; không bịa issue URL | 45 phút |
| 7 / HW03-DOC, HW03-AI, HW03-GIT | Viết phần Task 1 trong main report, tổng hợp số liệu, audit; xuất PDF và kiểm tra từng trang; commit | `MainReport.md/.pdf`, hồ sơ AI, Git history | Số liệu khớp dữ liệu gốc, đủ bằng chứng; không tuyên bố hoàn tất HW03 chỉ vì Task 1 xong | 30 phút |

Commit riêng từng bước đã hoàn tất, ví dụ `HW03 HW03-T1-02 step 1: preserve initial AI GUI checklist`, `HW03 HW03-T1-03 step 1: record student review and additions`, `HW03 HW03-T1-04 step A: execute login GUI checks`. Chỉ commit sau khi có kết quả thật, kèm cập nhật PROGRESS.

## 6. Cấu trúc dữ liệu và bằng chứng

Workbook dự kiến có bốn sheet:

1. `Checklist`: ID, Feature/Screen, IA, nguồn/tiêu chí, tiền điều kiện, thao tác kiểm tra, expected result, nguồn AI/student/revised, lý do bổ sung.
2. `Execution`: Run ID, Item ID, biến thể/input, ngày giờ, SUT revision, OS/browser/device/version/viewport, actual result, status, Notes, ảnh, Bug ID/Issue URL.
3. `AI Review`: mục gốc, quyết định giữ/sửa/loại/thêm, giải thích, nguồn đối chiếu, người review.
4. `Summary`: số mục thiết kế duy nhất; số mục đã chạy; số lượt chạy; Passed/Failed/chưa chạy; bug duy nhất; phân bố feature và IA.

Trong quá trình chạy được phép ghi `Not run` hoặc `Blocked` để phản ánh đúng thực tế; đây không phải Passed. Trước khi tuyên bố Task 1 hoàn thành, mọi mục trong scope phải được chạy và kết luận Passed/Failed. Không đổi một mục bắt buộc không chạy được thành N/A để né blocker.

Một ảnh Failed dùng tên `T1_<ItemID>_<RunID>_<platform>.png`; có thể dùng cùng ảnh cho nhiều mục nếu thấy rõ từng lỗi. Ảnh phải là capture thật, đối chiếu được màn hình và dữ liệu. Task 1 chỉ yêu cầu ảnh Failed; bằng chứng nền tảng cho Task 3 là nghĩa vụ riêng. Lưu ảnh local trong ZIP, không chỉ để link GitHub.

Sổ chạy phải nêu environment, input, expected, actual và đường dẫn bằng chứng. Tổng bug không bằng tổng Failed: một bug có thể làm nhiều mục thất bại. Tách số mục checklist duy nhất khỏi số lượt chạy nhiều biến thể/nền tảng.

## 7. Môi trường, phụ thuộc và điểm chưa sẵn sàng

- Web/Admin/API: dùng bộ chạy trong `../ENVIRONMENT.md`; trạng thái môi trường trước đây không thay kết quả kiểm thử mới.
- Backend reset dữ liệu mỗi lần khởi động: lưu evidence trước restart; seed lại dữ liệu thử và ghi rõ trạng thái ban đầu. Không đổi hành vi reset gốc.
- Mobile dùng Expo Go trên thiết bị thật; hiện `frontend-mobile/App.js` đặt API tại `192.168.1.9:3000`. Xác minh IP LAN, cùng Wi-Fi và khả năng truy cập backend; nếu cần cấu hình phải ghi thay đổi môi trường, không sửa logic lỗi của SUT. Chưa xác minh thiết bị/Expo nên phần D chưa sẵn sàng chạy.
- Chưa tìm thấy bài giảng GUI trong workspace; cần sinh viên cung cấp/đối chiếu trước thiết kế chính thức theo đề §6.
- Repository HW03 hợp lệ, hiện chưa có remote. Cần GitHub repository/remote thật để hoàn thành Issues; local Markdown không thay yêu cầu GitHub Issues.
- Chọn trình duyệt thật cho lượt chạy Task 1. Task 3 sẽ chạy lại checklist trên ít nhất ba nền tảng theo đề; không mặc định một màn hình native chạy được trên mọi browser. Ghi ma trận áp dụng web/native và mọi giới hạn coverage. Không coi ảnh mobile giả lập viewport là bằng chứng Expo Go thật.

## 8. Điều kiện nghiệm thu Task 1

- Checklist cuối ≥41 mục riêng biệt, đủ IA-01–04, có nguồn và tiêu chí quan sát được.
- Có bản AI gốc, review thật và những mục sinh viên tự bổ sung kèm giải thích; không dùng kế hoạch AI này làm bằng chứng tự review.
- Đã chạy mọi mục trong scope; Failed có Notes và ảnh; số liệu báo cáo/Excel thống nhất.
- Mọi bug được sinh viên tự viết trong Markdown và GitHub Issues kèm screenshot, theo AI Agreement mục 11. Kế hoạch không chứa bug report hoặc kết quả giả định.
- Có báo cáo Markdown/PDF, Excel và summary; PDF cuối được render và kiểm tra trực quan.
- Lưu transcript/audit/disclosure thật và commit từng bước; chuẩn bị xuất `git log --graph --all --stat` khi đóng gói.

Kế hoạch hiện tại chưa tạo Excel, PDF, bug report, GitHub Issue hay kết quả Passed/Failed. PDF của tài liệu được đưa vào bộ nộp sẽ được tạo và kiểm tra khi hoàn thiện báo cáo; chưa đóng gói ZIP trong bước lập kế hoạch.
