# Môi trường HW03

Đã chuẩn bị môi trường local ngày 2026-11-10. Đây là tài liệu vận hành, chưa phải báo cáo bài nộp. Bằng chứng kiểm tra máy: `environment/verification.json`.

## Chạy SUT

Từ thư mục workspace `homework`:

```bash
python3 hw03/tools/environment.py start
```

Giữ terminal mở. Dùng `Ctrl+C` để dừng các tiến trình do bộ chạy tạo. Bộ chạy kiểm tra cổng trước khi khởi động, không tự dừng ứng dụng khác. Log từng dịch vụ nằm trong `hw03/.runtime/{api,web,admin}.log`.

| Thành phần | URL | Tài khoản mẫu |
| --- | --- | --- |
| Web khách hàng | http://localhost:5173 | test@eshop.com / Test1234! |
| Web Admin | http://localhost:5174 | admin@eshop.com / Admin123! |
| API | http://localhost:3000/api/products | Không cần đăng nhập cho danh sách sản phẩm |

Backend gốc được chạy trực tiếp, không chỉnh mã SUT. Theo thiết kế của thầy, mỗi lần khởi động backend sẽ reset SQLite; giỏ hàng còn nằm trong bộ nhớ server. Khi mở buổi usability mới, ghi rõ dữ liệu ban đầu, trạng thái đăng nhập và localStorage của trình duyệt. Lưu minh chứng trước khi restart.

Không dùng `eshop-sut/run_servers.sh`: bản hiện tại dùng `killall node` và đường dẫn tuyệt đối `/backend`, `/frontend-web`, `/frontend-admin`. Bộ chạy HW03 dùng đường dẫn tính từ vị trí tệp và quản lý riêng từng tiến trình.

## Kiểm tra lại

Mở terminal thứ hai, từ workspace `homework`:

```bash
python3 hw03/tools/environment.py check --output hw03/environment/verification.json
```

Lệnh kiểm tra HTTP API, HTML Web/Admin, đăng nhập user/admin; ghi thời điểm thật theo giờ Việt Nam, OS, Node/npm, SUT commit, trạng thái sửa đổi và SHA-256 các lockfile. Token đăng nhập không được lưu trong kết quả. Exit code 0 nghĩa là 5 smoke checks thành công; không đồng nghĩa đã có đủ các trình duyệt hoặc hoàn thành GUI checklist.

Đã xác minh: 5/5 smoke checks thành công; trình duyệt trong ứng dụng hiển thị danh sách 5 sản phẩm và form đăng nhập Admin. Đây chỉ là kiểm tra khởi động, không được tính là thực thi Task 1/3.

## Dependency và công cụ

Đã có Node v24.21.0, npm 11.19.0, Python 3.14.4 và dependency của cả ba dịch vụ (`npm ls --depth=0` không báo thiếu). Không cần cài lại. Khi làm trên máy mới, dùng `npm ci` trong từng thư mục `eshop-sut/backend`, `frontend-web`, `frontend-admin`, rồi chạy bộ lệnh ở trên. Các lockfile hiện có là nguồn phiên bản; không nâng dependency trong quá trình đo.

Pandoc, Poppler và lệnh ZIP có trong PATH. Có launcher OBS nhưng chưa kiểm tra capture màn hình/microphone hoặc xuất video; cần quay thử và phát lại trước pilot. Chưa xuất PDF trong bước chuẩn bị; khi có báo cáo phải render và kiểm tra trực quan từng trang.

## Ma trận nền tảng cần hoàn thiện

| Môi trường | Hiện trạng | Điều kiện để dùng làm bằng chứng Task 3 |
| --- | --- | --- |
| Trình duyệt trong ứng dụng | Web/Admin mở được | Chỉ dùng hỗ trợ chuẩn bị; không thay cho nền tảng được đề chỉ định |
| Microsoft Edge | CLI báo phiên bản 155.0.4283.45 | Không tự tính thay Chrome theo đề |
| Chrome | Chưa tìm thấy binary | Chuẩn bị Chrome local hoặc cloud thật |
| Firefox | Launcher Snap báo chưa cài Firefox | Chuẩn bị Firefox hoạt động local hoặc cloud thật |
| Safari / Android Chrome / Expo Go trên điện thoại thật | Chưa kiểm tra | Có phiên cloud hoặc thiết bị thật; ghi rõ OS/browser/device |
| BrowserStack / LambdaTest | Chưa cấu hình tài khoản hoặc tunnel | Người học cung cấp trial của mình, mở local tunnel và xác minh URL localhost truy cập được |

Frontend gốc gọi API cố định tại `http://localhost:3000`. Vì vậy chỉ mở cổng Vite hoặc truy cập IP LAN từ điện thoại chưa đảm bảo API hoạt động. Với cloud, cần tunnel truy cập được cả cổng 3000 và 5173/5174 và kiểm tra Network trong phiên thật. Không tự đổi mã SUT để tạo kết quả. Nếu chọn Expo Go, đọc cấu hình hiện có của `frontend-mobile` và kiểm tra API LAN trước khi tính là nền tảng hợp lệ.

Task 3 cần chạy toàn bộ checklist Task 1 trên ít nhất 3 nền tảng. Responsive viewport/emulation trên một trình duyệt không phải 3 nền tảng thật. Ảnh cần thể hiện URL localhost, OS/browser/device, overlay email sinh viên; đáp ứng thêm yêu cầu MSSV và họ tên trong form. Chưa điền thông tin sinh viên vì chưa được xác nhận cho HW03.

## Nơi lưu công việc

- `submission/evidence/gui/`: ảnh lỗi GUI thật; tên gợi ý `GUI-001_platform_timestamp.png`.
- `submission/evidence/platforms/`: thông tin và ảnh phiên nền tảng thật.
- `submission/evidence/usability/`: bản ghi, quan sát, câu trả lời đã được đồng ý và xử lý riêng tư.
- `submission/ai/`: transcript, audit, disclosure, critique sau khi người học rà soát.
- `private/`: liên hệ chưa che, consent hoặc dữ liệu riêng tư; được Git ignore. Chỉ đưa bản phù hợp vào bài nộp sau khi rà soát.

Dùng OBS thêm nguồn Text chứa email sinh viên để overlay trong bản ghi/ảnh; kiểm tra một bản thử trước khi dùng. Không thay đổi nội dung màn hình hay tạo ảnh minh chứng giả.

## Git và bước tiếp theo

HW03 có Git repository local riêng. Chưa có remote GitHub; vì chưa có URL repository được xác nhận, chưa push hoặc tạo Issues. Khi có repository của bạn, đặt remote bằng `git -C hw03 remote add origin <URL-repository-HW03>`. Commit riêng từng bước và từng usability session thật. Khi chuẩn bị bài nộp, xuất lịch sử thực bằng `git -C hw03 log --graph --all --stat > hw03/submission/git-log.txt`.

Trước Task 1 cần bổ sung bài giảng, chốt màn hình/flow tránh trùng thành viên. Trước pilot cần xác nhận deadline Moodle, chuẩn bị consent, scale và ghi thử OBS; người tham gia phải là người thật ngoài lớp HW03. Chưa có checklist, kết quả GUI, người tham gia, bug, issue hoặc phân tích usability trong lần chuẩn bị này.
