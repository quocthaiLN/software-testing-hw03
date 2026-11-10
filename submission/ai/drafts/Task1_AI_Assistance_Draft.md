## Task 1 - Supporting Documents

## 1. Proposed checklist additions

Ba đề xuất bổ sung, đều Not run. Chưa được tính là student additions; sinh viên cần tự đánh giá sự phù hợp, tránh trùng và ghi đóng góp thực của mình. Kỳ vọng từ heuristic là tiêu chí đánh giá, không tự biến thành yêu cầu FR.

## AI-PROP-01 / dự kiến GUI-A-017 - Accessible name của ô đăng nhập

Nguồn: IA-02; H6/H7; guide Text Boxes State/Input type.

Bước: Mở /login; dùng accessibility tree hoặc trình đọc màn hình lần lượt focus email và mật khẩu. Kiểm tra tên truy cập gắn đúng trường, kể cả khi đã nhập dữ liệu.

Kỳ vọng: Người dùng nhận biết đúng tên trường khi focus; không chỉ dựa vào placeholder hoặc vị trí nhìn thấy.

Căn cứ đề xuất: Checklist đầu kiểm tra nhãn nhìn thấy, input type và Tab; chưa có phép kiểm tên truy cập theo ngữ nghĩa. Đây là phân tích thiếu sót do AI, chưa phải lý do do sinh viên tự viết.

Status: Not run. Student decision / actual / evidence: __________

## AI-PROP-02 / dự kiến GUI-B-009 - Thông báo coupon cho trình đọc màn hình

Nguồn: IA-04; H1/H9; guide Visibility of System Status.

Bước: Bật trình đọc màn hình, giữ focus tại Áp dụng; thử một mã hợp lệ và một mã không tồn tại. Quan sát việc thông báo trạng thái mà không phải dò lại cả trang.

Kỳ vọng: Phản hồi thành công/lỗi có thể được nhận biết qua công cụ hỗ trợ; nếu không, ghi quan sát và đánh giá theo heuristic.

Căn cứ đề xuất: B007/B008 đã kiểm loading/recovery, nhưng chưa kiểm cách công cụ hỗ trợ nhận thông báo.

Status: Not run. Student decision / actual / evidence: __________

## AI-PROP-03 / dự kiến GUI-C-029 - Hướng dẫn nhập mã và loại giảm giá

Nguồn: IA-02; H10; guide Help and Documentation.

Bước: Mở Admin Coupons; tìm trợ giúp cạnh code/type/value hoặc đường dẫn hướng dẫn; so nội dung với FR-17 trước khi nhập.

Kỳ vọng: Hướng dẫn nếu có phải đúng quy tắc code duy nhất, giá trị dương và loại phần trăm/cố định; ghi thiếu trợ giúp là quan sát heuristic, không tự coi mọi form bắt buộc tooltip.

Căn cứ đề xuất: Bản đầu tập trung kiểm validation và label; ma trận hiện chưa có mục H10. Không tự đưa giới hạn phần trăm/độ dài không có trong spec.

Status: Not run. Student decision / actual / evidence: __________

## 2. AI Audit Report - draft assessment

Theo AI-02: các nhãn giữ tiếng Anh, nội dung mới bằng tiếng Việt. Tool: Codex; model và timestamp gốc chưa xác minh. Các verdict dưới đây là dự thảo đánh giá, chưa được xác nhận. Thiếu prompt/output đầy đủ thì không coi bảng này là audit cuối.

| Student Information | Value |
| --- | --- |
| Student name / Student ID / Class | __________ |
| Assignment ID | HW03-AI |
| Date / Signature | __________ |

## Artifact #1 - initial checklist

(1) Prompt + Tool: bat dau thuc hien task 1 | Tool: Codex | Time: chưa xuất timestamp gốc.

(2) AI Output: ai/task1_initial_checklist.md/.json; nguyên văn bản đầu được lưu tại nguồn. Nội dung trên là định vị/tóm tắt, không thay output nguyên văn đầy đủ.

(3) Verdict: INCOMPLETE

(4) Reasoning: Guide yêu cầu truy vết widget × heuristic; matrix ban đầu chưa có H10, và các phần chỉ kiểm nhãn/Tab chưa bao phủ tên truy cập. Không phải mọi heuristic đều bắt buộc áp dụng.

(5) Student Fix / actual attribution: Sinh viên đã trả lời Keep;

## Artifact #2 - C006 narrow-viewport assertion

(1) Prompt + Tool: Prompt gốc cho riêng việc sửa assertion chưa được xuất; không tự dựng lại. | Tool: Codex | Time: chưa xuất timestamp gốc.

(2) AI Output: evidence/gui/admin_execution.json: giữ history hình học và kết quả cuối C006. Nội dung trên là định vị/tóm tắt, không thay output nguyên văn đầy đủ.

(3) Verdict: INVALID

(4) Reasoning: Guide Compatibility và Text Boxes yêu cầu đọc/nhập được. Geometry-only không đủ khi nội dung input có chiều rộng 0px; lần đo/ảnh sau đã khiến C006 Failed.

(5) Student Fix / actual attribution: AI đã sửa assertion sau visual QA;

## Artifact #3 - D015 oracle

(1) Prompt + Tool: Roi hay ra soat va hoat thanh task 1 | Tool: Codex | Time: chưa xuất timestamp gốc.

(2) AI Output: mobile_case_revisions.json và mobile_execution.json; lịch sử Spec-gap giữ nguyên. Nội dung trên là định vị/tóm tắt, không thay output nguyên văn đầy đủ.

(3) Verdict: INCOMPLETE

(4) Reasoning: FR-22 chỉ yêu cầu lỗi trên Submit, không quy định inline. D015 được chốt Passed về vị trí từ ảnh có sẵn; không phải chạy mới.

(5) Student Fix / actual attribution: AI sửa cách diễn giải; chưa có lời xác nhận đánh giá của sinh viên.

## Artifact #4 - scope removal

(1) Prompt + Tool: Loai bo luon cac truong hop nay | Tool: Codex | Time: chưa xuất timestamp gốc.

(2) AI Output: GUI_Checklist.xlsx; 65 active, 3 Removed, không tái đánh số ID. Nội dung trên là định vị/tóm tắt, không thay output nguyên văn đầy đủ.

(3) Verdict: VALID

(4) Reasoning: HW03 §6 yêu cầu >40 và đủ IA-01…04. 65 active đáp ứng số lượng và IA; AGENTS workflow yêu cầu bảo toàn bằng chứng, không gán Passed cho phần bị bỏ.

(5) Student Fix / actual attribution: Người dùng quyết định loại; AI áp dụng thay đổi và giữ lịch sử.

## Summary of AI Accuracy

| Metric | Count / Percentage |
| --- | --- |
| Total AI-generated artifacts audited | 4 / 100% |
| VALID | 1 / 25% |
| INVALID | 1 / 25% |
| INCOMPLETE | 2 / 50% |

Conclusion - draft: AI phù hợp để tạo cấu trúc kiểm thử, triển khai phép kiểm lặp lại và tổng hợp bằng chứng. Giá trị của công cụ phụ thuộc vào đặc tả, dữ liệu và assertion được chọn. Trường hợp C006 cho thấy phép đo dễ tự động hóa chưa chắc đo đúng khả năng sử dụng. D015 cho thấy suy diễn thêm điều kiện ngoài nguồn có thể làm kết luận sai. Vì vậy, cần kiểm tra lại oracle và xem bằng chứng trước khi chốt. Khi thiếu dữ liệu, phải giữ trạng thái chưa xác minh thay vì điền kết quả. Không dùng đầu ra AI làm bằng chứng cho hoạt động cá nhân chưa diễn ra. Mandatory Disclosure / Signature: chưa ký; không tự điền lời cam kết thay sinh viên.

## 3. AI Critique

Quá trình kiểm thử Task 1 cho thấy AI hỗ trợ tốt việc tổ chức checklist, viết mã thực thi và tổng hợp bằng chứng. Khả năng ánh xạ từng mục sang yêu cầu, dữ liệu và ảnh giúp đối chiếu kết quả thuận tiện. Tuy nhiên, độ đầy đủ của tài liệu không bảo đảm kết luận chính xác.

Một hạn chế xuất hiện ở kiểm tra bố cục Admin Coupons: phép đo hình học ban đầu chưa chứng minh nội dung ô nhập có thể đọc được. Việc xem ảnh và kiểm tra vùng hiển thị ký tự đã làm thay đổi kết quả. Trường hợp này cho thấy assertion phải phản ánh trải nghiệm cần kiểm tra, thay vì chỉ đo một thuộc tính dễ lấy.

Ở Mobile, việc yêu cầu lưu hồ sơ bằng số điện thoại hợp lệ khiến một số phép kiểm phụ thuộc bị chặn. Tách dữ liệu hỗ trợ có thể giúp cô lập hành vi, nhưng không được dùng số sai miền để tuyên bố validation đúng. Ngoài ra, cách hiểu rằng thông báo lỗi phải inline đã thêm điều kiện không có trong FR-22. Việc đọc lại nguồn và xem ảnh giúp thu hẹp kết luận về đúng vị trí hiển thị.

Bài học là dùng AI để tăng tốc thiết kế và xử lý hồ sơ, đồng thời kiểm tra lại oracle, tiền điều kiện và bằng chứng. Cần phân biệt mục bị loại khỏi phạm vi với mục đạt, ảnh tải lên với lượt chạy độc lập, và góp ý AI với đóng góp của sinh viên.

Độ dài bản nháp: 269 đơn vị phân tách bằng khoảng trắng.

## 4. AI Use Disclosure Form - draft facts

## 1. Course & Student Info

| Field | Value |
| --- | --- |
| Course | CS423 / CSC13003 - Software Testing |
| Assignment ID / Title | HW03-AI / GUI & Usability |
| AI Use Category (1–5) | Category ____; đề ghi Open, chưa có số được xác minh |
| Student name / Student ID / Date | __________ |

## 2. Disclosure Questions

1. AI tool(s) used: Codex trong cuộc hội thoại này; sinh viên bổ sung công cụ khác nếu có. Không đoán model hoặc phiên bản.

2. Stage(s): AI hỗ trợ outlining, drafting, revision, coding, phân tích dữ liệu thực thi và định dạng tài liệu. Mobile do sinh viên thao tác;

3. Main prompts or tasks given to the AI (verbatim):

“Ban hay rut gon so luong test tren mobile”

“Ban sua lai sdt trong test case cho phu hop voi 3 cai block di”

“Loai bo luon cac truong hop nay”

Full transcript: chưa có bản xuất nguyên văn đầy đủ. ai/prompt_log.md hiện là activity summary PARTIAL, không thay Appendix A hoàn chỉnh.

4. Specific parts AI contributed to: Codex hỗ trợ checklist đầu 68 mục, harness Web, tính toán/đối chiếu kết quả, chuyển ghi nhận Mobile sang hồ sơ, sửa phạm vi và định dạng Markdown/PDF. Codex cũng soạn các đề xuất checklist bổ sung, dự thảo audit/kết luận/critique/disclosure và bản nháp mô tả lỗi Task1_Bug_Report_AI_Draft. Mobile do sinh viên thao tác và cung cấp ảnh/ghi nhận. Các đề xuất mới chưa được thực thi; chưa có phần bổ sung độc lập, chữ ký hay xác nhận review của sinh viên trong bộ dự thảo này.

5. Review/verification recorded: sinh viên trả lời Keep, cung cấp ảnh và mô tả Mobile, sửa nhầm ảnh, yêu cầu sửa rồi loại ba ca. AI chạy kiểm tra số liệu, đối chiếu ảnh/source, kiểm tra hash và layout. Phần tự review/audit còn cần sinh viên xác nhận; không tự nhận sinh viên đã làm các bước kiểm tra bằng công cụ của AI.

6. Citation: Codex [AI coding assistant], sử dụng trong HW03; sinh viên điền thông tin công cụ bổ sung được xác minh theo kiểu trích dẫn môn học. Không tạo version/timestamp thiếu.

## 3. Statement of Honesty

Sinh viên đọc nội dung xác nhận của mẫu AI-03 trước khi ký. Bản này chưa phải tuyên bố đã ký. Student name / Student ID / Date / Signature: __________

## 5. Bug report worksheet and evidence index

Phần này là khung và danh mục bằng chứng. Nội dung mô tả lỗi nằm tại Task1_Bug_Report_AI_Draft.md/.pdf; nguồn hỗ trợ được khai báo ở mục Disclosure. Issues chưa được tạo. 31 mục Failed không nhất thiết là 31 bug; sinh viên tự gom nguyên nhân trước khi tạo Bug ID.

Bug ID / Title: __________

Related checklist IDs: __________

Environment / Preconditions / Actual input: __________

Steps to reproduce: __________

Expected result / source: __________

Actual result: __________

Severity / justification: __________

Screenshot / GitHub Issue URL: __________

Danh mục JSON đi kèm giữ đường dẫn local đầy đủ. Bảng dưới là chỉ mục, không phải các bug đã được viết hoặc khử trùng.

| Checklist ID | Screenshot filename |
| --- | --- |
| GUI-A-001 | test-failed-1.png |
| GUI-A-002 | test-failed-1.png |
| GUI-A-003 | test-failed-1.png |
| GUI-A-005 | test-failed-1.png |
| GUI-A-006 | test-failed-1.png |
| GUI-A-007 | test-failed-1.png |
| GUI-A-010 | test-failed-1.png |
| GUI-A-014 | test-failed-1.png |
| GUI-A-015 | test-failed-1.png |
| GUI-A-016 | test-failed-1.png |
| GUI-B-004 | test-failed-1.png |
| GUI-B-005 | test-failed-1.png |
| GUI-B-006 | test-failed-1.png |
| GUI-C-002 | test-failed-1.png |
| GUI-C-003 | test-failed-1.png |
| GUI-C-006 | test-failed-1.png |
| GUI-C-007 | test-failed-1.png |
| GUI-C-008 | test-failed-1.png |
| GUI-C-011 | test-failed-1.png |
| GUI-C-012 | test-failed-1.png |
| GUI-C-014 | test-failed-1.png |
| GUI-C-021 | test-failed-1.png |
| GUI-C-024 | test-failed-1.png |
| GUI-C-025 | test-failed-1.png |
| GUI-C-027 | test-failed-1.png |
| GUI-C-028 | test-failed-1.png |
| GUI-D-007 | image-05.png |
| GUI-D-008 | image-07.png |
| GUI-D-012 | image-01.png |
| GUI-D-013 | image-04.png |
| GUI-D-014 | image-04.png |

## Việc cần sinh viên làm trước khi dùng bộ này

Review/sửa dự thảo theo trải nghiệm thật; tự viết bug descriptions; tự quyết định và bổ sung checklist; thực thi mục mới; cung cấp transcript đầy đủ; điền thông tin và ký thật. Không thay trạng thái acceptance chỉ vì đã có tài liệu AI dự thảo.
