# Task 1 - Phiếu ghi nhận Mobile thủ công

## Hướng dẫn

1. Phiếu trống để ghi nhận kiểm thử thủ công trên Android thật / Expo Go. Không phải báo cáo kết quả. Tất cả 16 mục giữ trạng thái Not run cho đến khi có thao tác và quan sát thật.
2. Dùng tài khoản thử của bạn. Ghi model, Android, Expo Go, hướng màn hình, thời gian và phiên bản SUT. Không dùng tài khoản hoặc thông tin cá nhân của người khác.
3. Trước mỗi mục, đọc bước và kỳ vọng; ghi lại dữ liệu đầu vào thực sự sử dụng. Passed cần quan sát đủ toàn bộ kỳ vọng; Failed cần kết quả thực tế và ảnh. Chưa làm thì giữ Not run. Nếu bước trước chặn, ghi Blocked và ID phụ thuộc; nếu thiếu oracle, ghi Spec-gap để review.
4. Nếu số điện thoại hợp lệ bị từ chối, vẫn thử đầy đủ bốn vector D007. Không đổi sang số sai đặc tả để gọi các mục lưu thành công là Passed. Các mục phụ thuộc lưu có thể bị chặn; ghi rõ phần nào đã thực hiện.
5. Với D015, ghi nguyên văn thông báo và cách xuất hiện (inline/native alert). Checklist ban đầu yêu cầu sinh viên review cách áp dụng FR-22; chưa tự coi native alert là tương đương.
6. Với D016, ghi trạng thái mạng ban đầu để khôi phục đúng sau thử nghiệm. Chỉ ngắt mạng khi đã tới được bước lưu với dữ liệu hợp lệ. Nếu validation đã chặn trước khi gọi mạng, ghi phụ thuộc thay vì tuyên bố đã thử lỗi mạng.
7. Ảnh Failed đặt tên theo ID và vector, ví dụ GUI-D-007-phone10.png; lưu ảnh gốc. Ghi liên kết/đường dẫn ảnh ở phần kết quả. Bug ID chỉ điền sau khi sinh viên tự viết và đối chiếu bug report.
8. Phiếu này do AI chuyển định dạng từ checklist đã Keep; không phải mục sinh viên tự bổ sung. Tích hợp lại Excel sau khi đối chiếu kết quả và ảnh; không thay thế bản AI gốc.

## Môi trường / phiên chạy

- Người thực hiện: __________
- Ngày / giờ / múi giờ: __________
- Model / Android / Expo Go: __________
- Hướng màn hình / kích thước: __________
- SUT commit / thay đổi local: __________
- Tài khoản thử (không ghi mật khẩu/token): __________

## GUI-D-001 - Tiêu đề và nhãn tiếng Việt

**Bước / input theo checklist:** Mở Hồ sơ trên Expo Go; đọc tiêu đề và nhãn.

**Kỳ vọng:** Tiêu đề đúng ngữ cảnh, nhãn tiếng Việt nhất quán. Không dùng oracle h1 cho native.

**Nguồn / heuristic:** FR-21 language; H2 / H2,H4

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-002 - Màu cập nhật và đăng xuất

**Bước / input theo checklist:** Quan sát hai nút khi đã đăng nhập.

**Kỳ vọng:** Cập nhật dùng xanh dương; hành động hủy/thoát dùng đỏ theo quy tắc GUI chung.

**Nguồn / heuristic:** FR-21 / H4

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-003 - Layout trên màn hình điện thoại

**Bước / input theo checklist:** Mở trên điện thoại, ghi device/OS/orientation; quan sát và cuộn.

**Kỳ vọng:** Không chồng/cắt nhãn hoặc input; nút cập nhật tiếp cận được bằng cuộn.

**Nguồn / heuristic:** strategies Compatibility; H8 / H8

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-004 - Nhận biết email chỉ đọc

**Bước / input theo checklist:** Quan sát email và thử chạm/chọn nhập.

**Kỳ vọng:** Email được nhận biết là không sửa được và không gây hiểu nhầm là trường cập nhật.

**Nguồn / heuristic:** FR-04; widget Text Boxes State / H4,H6

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-005 - Không sửa email qua GUI

**Bước / input theo checklist:** Thử gõ/dán vào email; cập nhật các trường khác rồi mở lại.

**Kỳ vọng:** Email không đổi qua UI.

**Nguồn / heuristic:** FR-04 / H5

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-006 - Tên tiếng Việt lưu nguyên vẹn

**Bước / input theo checklist:** Nhập Nguyễn Văn Ánh, lưu với điện thoại hợp lệ rồi mở lại.

**Kỳ vọng:** Tên có dấu không bị mất/ký tự lỗi sau lưu. Không tự quy định min/max length.

**Nguồn / heuristic:** FR-04; H2 / H2

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-007 - Biên độ dài số điện thoại

**Bước / input theo checklist:** Lần lượt nhập 091234567 / 0912345678 / 09123456789 / 091234567890 rồi lưu.

**Kỳ vọng:** 9/12 chữ số bị từ chối; 10/11 chữ số bắt đầu 0 được chấp nhận.

**Nguồn / heuristic:** FR-04 / H5,H9

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-008 - Điện thoại sai miền và kiểu bàn phím

**Bước / input theo checklist:** Chạm điện thoại; thử chuỗi 10 chữ số không bắt đầu 0 và chuỗi có chữ qua dán.

**Kỳ vọng:** Có bàn phím thuận nhập điện thoại; dữ liệu sai miền bị từ chối khi lưu. Không coi phone-pad là đủ validate.

**Nguồn / heuristic:** FR-04; widget Text Boxes Input type; H7 / H5,H7

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-009 - Địa chỉ nhiều dòng

**Bước / input theo checklist:** Dán địa chỉ tiếng Việt nhiều dòng, sửa rồi lưu với điện thoại hợp lệ.

**Kỳ vọng:** Địa chỉ nhập/sửa được, dữ liệu sau lưu giữ nội dung có nghĩa; không tràn che nút.

**Nguồn / heuristic:** FR-04; widget Text Boxes / H2,H7

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-010 - Đến hồ sơ từ điều hướng

**Bước / input theo checklist:** Sau đăng nhập, chạm biểu tượng/liên kết hồ sơ.

**Kỳ vọng:** Mở hồ sơ đúng người đang đăng nhập.

**Nguồn / heuristic:** FR-04; FR-20 / H3,H6

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-011 - Bàn phím không chặn thao tác lưu

**Bước / input theo checklist:** Mở bàn phím ở từng trường, cuộn, đóng bàn phím và chạm Cập nhật.

**Kỳ vọng:** Trường đang nhập và nút lưu có thể tiếp cận, không mắc kẹt bởi bàn phím.

**Nguồn / heuristic:** strategies Compatibility; H3/H7 / H3,H7

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-012 - Đăng xuất đúng nhãn và hiệu lực

**Bước / input theo checklist:** Quan sát nhãn; chạm đăng xuất rồi mở lại hồ sơ.

**Kỳ vọng:** Nhãn là Đăng xuất; không còn hiển thị hồ sơ riêng như phiên đang đăng nhập, có đường tới login.

**Nguồn / heuristic:** FR-23; FR-04 / H3,H4

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-013 - Phản hồi cập nhật thành công

**Bước / input theo checklist:** Cập nhật bộ dữ liệu hợp lệ; quan sát phản hồi rồi rời/mở lại hồ sơ.

**Kỳ vọng:** Có phản hồi thành công và dữ liệu mới được giữ khi mở lại.

**Nguồn / heuristic:** FR-04; H1 / H1

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-014 - Sửa điện thoại sau lỗi

**Bước / input theo checklist:** Nhập điện thoại sai rồi lưu; sửa thành 0912345678 và lưu lại.

**Kỳ vọng:** Lỗi dễ hiểu, có thể sửa/thử lại; kết quả thành công thay trạng thái lỗi cũ.

**Nguồn / heuristic:** FR-04; H9 / H9

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-015 - Vị trí lỗi form mobile

**Bước / input theo checklist:** Gây lỗi validate, quan sát vị trí thông báo/feedback so với Cập nhật.

**Kỳ vọng:** Theo FR-22 lỗi phải ở trên nút submit; nếu chỉ dùng native alert, ghi khác biệt áp dụng để sinh viên review, không tự coi tương đương.

**Nguồn / heuristic:** FR-22 / H9

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |

## GUI-D-016 - Phục hồi cập nhật khi mất mạng

**Bước / input theo checklist:** Ngắt mạng thiết bị, thay dữ liệu và lưu; khôi phục mạng, mở lại rồi thử lưu.

**Kỳ vọng:** Có lỗi thay vì thành công giả; có thể thử lại; đối chiếu dữ liệu đã lưu thật.

**Nguồn / heuristic:** H1/H9; strategies Integration / H1,H9

| Trường ghi nhận | Nội dung |
| --- | --- |
| Thời điểm / tiền điều kiện / input thực tế |  |
| Kết quả | Not run |
| Thực tế quan sát |  |
| Ảnh / vector / phụ thuộc / điểm cần review |  |
| Bug ID (nếu có) |  |
