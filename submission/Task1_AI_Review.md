# Task 1 — Phiếu review dành cho sinh viên

Trạng thái: người dùng trả lời **“Keep”** cho bản AI đầu 68 mục trong chat. Hiểu là giữ lại các mục hiện có; chưa có lý do chi tiết hoặc mục tự bổ sung được cung cấp. Quyết định giữ được ghi theo lời người dùng, không tự tạo nhận xét hoặc đóng góp độc lập của sinh viên.

Nguồn AI gốc: `ai/task1_initial_checklist.md` và `.json`; working copy: `GUI_Checklist.xlsx`. Căn cứ: đề HW03 §6 Task 1 và hướng dẫn AI-first/human review; guide do sinh viên tổng hợp tại `skills/gui-testing-guide/`.

## Cách review

1. Đọc checklist theo từng feature, đối chiếu đặc tả và guide. Với từng ID, chọn Keep / Revise / Remove trong sheet AI Review và ghi căn cứ.
2. Với mục sửa, ghi kỳ vọng mới và lý do; giữ nguyên ID và bản AI gốc. Mục xóa vẫn giữ được truy vết trong review; thống kê thiết kế cuối chỉ tính scope đã duyệt.
3. Tự kiểm tra màn hình và bổ sung những mục AI chưa nêu. Dùng ID mới, ví dụ GUI-A-017; ghi rõ vì sao AI bỏ sót (prompt thiếu ngữ cảnh, giới hạn AI hoặc đặc trưng UI) và nguồn đối chiếu. Không gọi các gợi ý AI trong intake/kế hoạch là phát hiện độc lập.
4. Điền reviewer/thời điểm thật, cập nhật cột Student review trong Checklist sau khi đã review. Không đánh dấu execution Passed từ review tài liệu.

## Bảng sinh viên điền

| Item ID / ID mới | Quyết định | Lý do và nguồn | Nội dung sửa/thêm | Vì sao AI bỏ sót nếu thêm | Người review / thời điểm |
| --- | --- | --- | --- | --- | --- |

Quyết định chung đã nhận: GUI-A-001…016, GUI-B-001…008, GUI-C-001…028 và GUI-D-001…016 = Keep. Nguyên văn trả lời: “Keep”. Chưa có timestamp gửi tin nhắn được xuất; không suy diễn thời điểm nhận thành timestamp gốc. Các ô lý do, sửa/thêm, người review và thời điểm cụ thể vẫn chờ dữ liệu thật.

## Các câu hỏi cần quyết định trước khi chạy

- Cách chốt oracle cho số tiền có phần thập phân ở GUI-B-005?
- Với native alert ở GUI-D-015, cách áp dụng quy định FR-22 có căn cứ nào?
- Những mục heuristic có phù hợp với bài giảng và scope được chọn không?
- Widget nào còn thiếu happy path, input biên/lạ, error/recovery hoặc keyboard/native interaction áp dụng được?

Danh sách trên là câu hỏi AI gợi ý để review, không phải kết quả phản biện của sinh viên. Phần tự bổ sung và giải thích theo đề vẫn chưa hoàn thành; không gọi quyết định Keep là bằng chứng đã tự bổ sung mục AI bỏ sót.
