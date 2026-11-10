# Task 1 - Phiếu ghi nhận Mobile thủ công

## Hướng dẫn

1. Bản rút gọn gồm 7 nhóm ca thao tác cho 13 tiêu chí Mobile active; D006/D009/D016 đã Removed. Dùng chung bước mở màn hình, nhập/lưu và quan sát để giảm thao tác lặp. Vẫn ghi kết quả theo ID gốc để đối chiếu Excel; không tính nhóm ca thành tiêu chí mới.
2. Phiếu trống cho Android thật / Expo Go; mọi kết quả vẫn Not run. Bản AI gốc giữ nguyên; Excel có 65 mục active đã kết luận và 3 dòng Removed để truy vết; Web giữ 26 Passed / 26 Failed.
3. Dùng các nhóm MOB-01…06 và MOB-08 (MOB-07 đã loại), đăng xuất cuối cùng. Dùng tài khoản thử; ghi môi trường và dữ liệu thực tế. Passed chỉ khi quan sát đủ kỳ vọng; Failed cần ảnh và thực tế. Các tiêu chí cùng ca có thể có kết quả khác nhau.
4. Nếu số hợp lệ bị từ chối, vẫn thử đủ bốn vector MOB-05. D006/D009/D016 đã loại, không cần chạy lại; không dùng kết quả đó để kết luận validation hoặc lưu bằng số hợp lệ FR-04 đạt. Phần chưa thể chạy ghi Blocked và ID phụ thuộc; oracle chưa rõ ghi Spec-gap.
5. Mỗi ghi nhận phải nêu ID gốc và vector; ảnh ví dụ GUI-D-007-phone10.png. Không tự suy kết quả mọi tiêu chí từ một lần lưu. Bug ID chỉ điền sau khi sinh viên tự viết báo cáo.
6. Đây là bản gộp do AI theo yêu cầu giảm số ca; không phải phần sinh viên tự bổ sung. Kết quả và bằng chứng để trống cho sinh viên điền sau.

## Môi trường / phiên chạy

- Người thực hiện: __________
- Ngày / giờ / múi giờ: __________
- Model / Android / Expo Go: __________
- Hướng màn hình / kích thước: __________
- SUT commit / thay đổi local: __________
- Tài khoản thử (không ghi mật khẩu/token): __________

## MOB-01 - Mở hồ sơ và kiểm tra giao diện

**Bước / input:** Sau đăng nhập, mở Hồ sơ. Kiểm tra đúng tài khoản, tiêu đề/nhãn tiếng Việt; quan sát màu Cập nhật và Đăng xuất.

**Kỳ vọng:** Đúng hồ sơ; nhãn nhất quán; Cập nhật xanh dương, hành động thoát đỏ. Chưa bấm đăng xuất.

**ID gốc:** GUI-D-001, GUI-D-002, GUI-D-010

**Nguồn / heuristic:** FR-21 language; H2; FR-21; FR-04; FR-20 / H2,H3,H4,H6

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
| Kết quả GUI-D-001 | Not run |
| Kết quả GUI-D-002 | Not run |
| Kết quả GUI-D-010 | Not run |

## MOB-02 - Bố cục và bàn phím

**Bước / input:** Trên điện thoại thật, cuộn toàn form; mở bàn phím ở tên, điện thoại và địa chỉ, cuộn rồi đóng bàn phím.

**Kỳ vọng:** Không chồng/cắt nội dung; tiếp cận được trường đang nhập và nút Cập nhật, không mắc kẹt bởi bàn phím.

**ID gốc:** GUI-D-003, GUI-D-011

**Nguồn / heuristic:** strategies Compatibility; H8; strategies Compatibility; H3/H7 / H3,H7,H8

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
| Kết quả GUI-D-003 | Not run |
| Kết quả GUI-D-011 | Not run |

## MOB-03 - Email chỉ đọc

**Bước / input:** Quan sát email; thử chạm, gõ và dán giá trị khác. Ghi email ban đầu; đối chiếu lại sau ca MOB-04.

**Kỳ vọng:** Nhận biết được email chỉ đọc; không sửa được qua GUI; email vẫn nguyên sau cập nhật các trường khác.

**ID gốc:** GUI-D-004, GUI-D-005

**Nguồn / heuristic:** FR-04; widget Text Boxes State; FR-04 / H4,H5,H6

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
| Kết quả GUI-D-004 | Not run |
| Kết quả GUI-D-005 | Not run |

## MOB-04 - Lưu hồ sơ và kiểm tra cô lập

**Bước / input:** D013: nhập bộ hồ sơ với điện thoại 0912345678, bấm Cập nhật và quan sát phản hồi; đối chiếu dữ liệu sau mở lại nếu lưu được.

**Kỳ vọng:** Có phản hồi thành công và dữ liệu được giữ khi mở lại. Không dùng số sai miền để kết luận lưu hợp lệ đạt. D006/D009 đã loại khỏi scope.

**ID gốc:** GUI-D-013

**Nguồn / heuristic:** FR-04; H1 / H1

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
| Kết quả GUI-D-013 | Not run |

## MOB-05 - Biên số điện thoại

**Bước / input:** Giữ các trường khác hợp lệ. Lần lượt nhập và lưu: 091234567 (9), 0912345678 (10), 09123456789 (11), 091234567890 (12 chữ số). Ghi riêng kết quả từng giá trị.

**Kỳ vọng:** 9 và 12 chữ số bị từ chối; 10 và 11 chữ số bắt đầu 0 được chấp nhận. Không bỏ hai biên hợp lệ khi gặp lỗi.

**ID gốc:** GUI-D-007

**Nguồn / heuristic:** FR-04 / H5,H9

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
| Kết quả GUI-D-007 | Not run |

## MOB-06 - Sai miền, thông báo lỗi và sửa lại

**Bước / input:** Kiểm tra bàn phím điện thoại; thử lưu 1912345678 và dán 09abc45678. Ghi nội dung/vị trí lỗi, sau đó sửa thành 0912345678 và lưu lại.

**Kỳ vọng:** Bàn phím thuận nhập số; cả hai dữ liệu sai miền bị từ chối; lỗi dễ hiểu, sửa và thử lại được. FR-22 yêu cầu lỗi trên nút submit; native Alert được đánh giá theo vị trí, FR-22 không bắt buộc inline.

**ID gốc:** GUI-D-008, GUI-D-014, GUI-D-015

**Nguồn / heuristic:** FR-04; widget Text Boxes Input type; H7; FR-04; H9; FR-22 / H5,H7,H9

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
| Kết quả GUI-D-008 | Not run |
| Kết quả GUI-D-014 | Not run |
| Kết quả GUI-D-015 | Not run |

## MOB-08 - Đăng xuất

**Bước / input:** Thực hiện cuối cùng: quan sát nhãn Đăng xuất, chạm nút rồi thử mở lại Hồ sơ.

**Kỳ vọng:** Nhãn là Đăng xuất; phiên đã thoát không còn xem hồ sơ riêng như đang đăng nhập; có đường tới đăng nhập.

**ID gốc:** GUI-D-012

**Nguồn / heuristic:** FR-23; FR-04 / H3,H4

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
| Kết quả GUI-D-012 | Not run |
