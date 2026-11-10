HW03 gồm GUI checklist, đánh giá usability với người thật và kiểm thử đa nền tảng. Bài không chỉ yêu cầu thiết kế tài liệu: bạn phải thực thi, thu minh chứng, phân tích và ghi lại quá trình dùng AI.

Mình đã áp dụng skill bạn chỉ định, đọc toàn bộ đề và đối chiếu policy, biểu mẫu AI. Chưa tạo hoặc sửa bài nộp.

Nguồn đề chính: /home/le-nguyen-quoc-thai/src/school/testing/homework/hw03/2026.HW03.GUI Usability_En.pdf

1. Các yêu cầu bắt buộc
Phần	Việc cần hoàn thành	Điểm
Task 1 — GUI Checklist	Thiết kế, phản biện AI, thực thi checklist và báo lỗi	30
Task 2 — Usability	Thiết kế nghiên cứu, chạy 7 phiên với người thật, phân tích	40
Task 3 — Cross-platform	Thực hiện Task 1 trên ít nhất 3 nền tảng	20
Agent Skills	Skill tái sử dụng và video minh họa	10
Tổng	Tự đánh giá theo rubric	100


Task 1 — GUI Checklist
- Có hơn 40 mục, tức ít nhất 41, bao phủ đủ:
  - IA-01: chuẩn UI chung.
  - IA-02: biểu mẫu.
  - IA-03: điều hướng.
  - IA-04: phản hồi và trạng thái.
- Được chọn từ một màn hình, nhưng đề khuyến khích nhiều màn hình để tránh checklist nông hoặc lặp.
- Đọc bài giảng liên quan; dùng AI tạo bản đầu, sau đó bạn tự rà soát và bổ sung những mục AI bỏ sót.
- Với từng mục tự bổ sung, giải thích vì sao AI bỏ sót. Accessibility, RTL và dark mode chỉ là ví dụ, không phải danh mục bắt buộc.
- Chạy thực tế từng mục, đánh dấu Passed/Failed. Mỗi mục Failed phải có lý do trong cột Notes và screenshot.
- Báo tất cả bug phát hiện trong Markdown và GitHub Issues; mỗi issue có ảnh bug.
Đề xuất tổ chức: mỗi mục có mã, màn hình, IA, điều kiện kiểm tra, kết quả mong đợi, nền tảng, kết quả thực tế, Notes, ảnh và mã bug. Đây là cấu trúc gợi ý, không phải mẫu cột cố định của đề.

Task 2 — Usability Evaluation

Chọn một flow xuyên suốt, rồi thực hiện ba giai đoạn:
Giai đoạn	Yêu cầu
Chuẩn bị	Xác định mục tiêu; viết scenario theo mục tiêu người dùng; chuẩn bị SUS hoặc UEQ-S, hoặc thang tự thiết kế có lý giải; câu hỏi mở bao phủ clarity, error recovery, speed, trust
Tuyển và pilot	Tuyển 7 người thật phù hợp đối tượng, ngoài lớp đang làm HW03; chạy một buổi pilot và chỉnh kế hoạch trước các phiên chính thức
Thực hiện	7 phiên, mỗi người một phiên; yêu cầu think aloud; quan sát trung lập; chỉ hỗ trợ khi hoàn toàn bế tắc; ghi màn hình, audio khi có đồng ý, và ghi chú có cấu trúc
Phân tích	Chấm thang đo của 7 người; nhóm pain points; phân biệt bug đơn lẻ và vấn đề thiết kế hệ thống; xếp mức nghiêm trọng; đưa bug thật vào Markdown và GitHub Issues kèm ảnh


Các điểm cần giữ đúng:
- Scenario đưa ra mục tiêu, không hướng dẫn từng thao tác.
- Người không chuyên IT/testing được ưu tiên nhưng không bắt buộc.
- Có bảng tên và liên hệ có thể xác minh; đề nhắc che bốn chữ số giữa của số điện thoại.
- TA có thể gọi ngẫu nhiên 2 người. Giả danh khiến Task 2 bị 0 điểm.
- Không dùng phản hồi hoặc người tham gia do AI tạo.
Đề xuất: bố trí một người pilot riêng ngoài 7 phiên chính thức để tránh tranh luận về số phiên hợp lệ; đề chưa nói rõ có được dùng lại người pilot hay không.

Task 3 — Cross-browser/Cross-platform
- Chạy checklist của Task 1 trên ít nhất 3 nền tảng, không chỉ mở ứng dụng rồi chụp ảnh.
- Tổ hợp trình duyệt được nêu: Chrome + Firefox + Safari hoặc Android Chrome.
- Expo Go trên điện thoại thật được thay một nền tảng bắt buộc, chẳng hạn Safari.
- BrowserStack/LambdaTest trial được ưu tiên mạnh. Đề cho phương án cloud khác hoặc thiết bị thật khi trial hết hạn, kèm minh chứng rõ.
- Ảnh cần thể hiện browser/OS/device và URL localhost theo điều kiện minh chứng của đề.
- Mỗi screenshot có overlay username dạng email sinh viên.
- Phần chống gian lận còn yêu cầu ảnh thể hiện MSSV và họ tên trong form. Nên đáp ứng đồng thời cả hai yêu cầu.
2. Quy định chung và hiện trạng submission

Theo [policy môn học](/home/le-nguyen-quoc-thai/src/school/testing/homework/policies.md) và [hướng dẫn repository](/home/le-nguyen-quoc-thai/src/school/testing/homework/AGENT.md):
- Bài cá nhân; nếu thuộc nhóm, đề HW03 vẫn yêu cầu không trùng màn hình chính hoặc usability flow giữa các thành viên.
- Báo cáo dạng text, kèm bản PDF; bảng Excel phải có phần tổng hợp trong Markdown.
- Commit rõ ràng cho mỗi bước; riêng HW03 nêu cả từng usability session. Nộp Git log dạng text; hướng dẫn repository chỉ định git log --graph --all --stat.
- Nộp Moodle, không chấp nhận trễ; deadline cụ thể phải xem submission link.
- Tối đa 20 file, mỗi file 20 MB trên submission link.
- Đề HW03 quy định thiếu bất kỳ tài liệu bắt buộc nào bị 0 điểm; sao chép giữa sinh viên, kể cả prompt, khiến cả hai bị 0.
- Có thể được chọn bảo vệ vấn đáp 5–7 phút, trong tuần sau deadline; tỷ lệ nêu trong HW03 là 30%.
Tên ZIP riêng của HW03:

<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>.zip

Điểm tự chấm gồm ba chữ số 000–100. Dùng mẫu cụ thể này cho HW03; mẫu chung trong policy không chứa phần GUIUsability.

Hiện [thư mục submission](/home/le-nguyen-quoc-thai/src/school/testing/homework/hw03/submission) trống:
Thành phần/định dạng	Hiện có và bằng chứng	Thiếu hoặc cần sửa
Đề PDF	Đủ — đọc được, 9 trang	—
Main report .md + .pdf	Thiếu	Nội dung cả GUI và usability
Excel checklist và test summary	Thiếu	≥41 mục, kết quả thực thi
Bug report và ảnh	Thiếu	Báo cáo local và ảnh đính kèm
GitHub Issues	Chưa xác minh	Chưa kiểm tra trang Issues
Hồ sơ 7 người và usability evidence	Thiếu	Scenario, ghi chú, câu trả lời, phân tích, recordings
Minh chứng ≥3 nền tảng	Thiếu	Screenshot đúng thông tin nhận diện
AI Audit, Critique, disclosure, prompt log	Thiếu	Nội dung và bản xuất theo yêu cầu
Git repository và commit log HW03	Thiếu — git -C hw03 không nhận diện repository	Khởi tạo và ghi lịch sử trong quá trình làm
Skills và video demo	Thiếu	Liên quan hạng mục 10 điểm
README và ZIP	Thiếu	Tự chấm, tổng kết, đóng gói


3. Bố cục báo cáo đề xuất

Tên file dưới đây là gợi ý:
1. MainReport.md + PDF:
   - Thông tin sinh viên, phạm vi màn hình/flow, SUT và môi trường.
   - Task 1: cách thiết kế, phản biện AI, checklist, thực thi và tổng kết.
   - Task 2: mục tiêu, scenario, participant profile, pilot, phương pháp, kết quả và phân tích.
   - Task 3: ma trận nền tảng, kết quả và khác biệt.
   - Agent Skills và video demo.
   - Kết luận, tài liệu tham khảo, disclosure.
   - Phụ lục A: AI Audit Report; phụ lục minh chứng.
2. BugReport.md + PDF: bug và liên kết issue tương ứng, kèm ảnh local.
3. AICritique.md + PDF.
4. GUIChecklist.xlsx.
5. Thư mục bằng chứng usability, ảnh và bản ghi.
6. README.md: bảng tự chấm và test summary.
7. git-log.txt, prompt log, biểu mẫu AI và skill.
README phải tổng hợp: số màn hình/flow, số checklist items designed/executed/passed/failed, số bug, số người tham gia và video demo. Nên tách số mục thiết kế khỏi số lượt thực thi trên các nền tảng để số liệu rõ ràng.

4. Hồ sơ AI phải chuẩn bị

HW03 yêu cầu cách làm AI-first nhưng có người kiểm tra, đạt G9.3 Analyse và G9.4 Collaborate. Lưu bản AI ban đầu để chứng minh bạn đã phát hiện, sửa và bổ sung gì; không gọi gợi ý tiếp theo của AI là phát hiện độc lập của mình.

Các nguồn AI bổ sung có nghĩa vụ cụ thể:
Nguồn	Nội dung áp dụng
[AI Agreement — AI-01](/home/le-nguyen-quoc-thai/src/school/testing/homework/AI-Templates/[AI-01] - FIT@HCMUS - AI Agreement_En.docx)	Audit, prompt log có timestamp, Disclosure Form và disclosure cuối báo cáo; bug report phải do sinh viên viết 100%, AI không được soạn mô tả
[AI Audit — AI-02](/home/le-nguyen-quoc-thai/src/school/testing/homework/AI-Templates/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx)	Prompt và output nguyên văn hoặc ảnh output được gắn nhãn; tool, thời gian; verdict VALID/INVALID/INCOMPLETE; căn cứ từ bài giảng/ISTQB/RFC; bản sửa có đánh dấu; thống kê verdict; kết luận 80–150 từ; disclosure và phần ký
[AI Disclosure — AI-03](/home/le-nguyen-quoc-thai/src/school/testing/homework/AI-Templates/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx)	Khai báo công cụ, giai đoạn, phần AI đóng góp, cách xác minh, 2–3 prompt quan trọng nguyên văn, tham chiếu full log và chữ ký


Riêng đề HW03 bắt buộc:
- Audit ở phụ lục, ghi từng tương tác: công cụ, ngày giờ, prompt, output.
- AI Critique 200–300 từ: AI sai/thiên lệch/thiếu gì, vì sao, và nguyên tắc cộng tác rút ra.
- Không bịa timestamp, log, kết quả kiểm thử, participant hoặc screenshot.
[AI-05 Privacy Checklist](/home/le-nguyen-quoc-thai/src/school/testing/homework/AI-Templates/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx) dùng để rà trước nộp; đề HW03 không liệt kê riêng việc đính kèm checklist này. [AI-06 Acknowledgement](/home/le-nguyen-quoc-thai/src/school/testing/homework/AI-Templates/[AI-06] - FIT@HCMUS - AI Student Acknowledgement_En.docx) là biểu mẫu ký đầu khóa, không tự động thành tài liệu phải nộp lại mỗi homework.

5. Các điểm chưa xác minh hoặc cần làm rõ
- Deadline: chưa có trong workspace; cần đọc Moodle.
- Bài giảng GUI/usability và AI Usage Guideline: chưa tìm thấy. Vì vậy chưa đối chiếu được kỹ thuật giảng viên dạy và mọi cập nhật ngoài workspace.
- Agent Skills: phần nội dung gọi là “khuyến khích”, nhưng rubric dành 10 điểm. Đề xuất làm skill và video YouTube minh họa trọn một màn hình/flow nếu hướng tới đủ 100 điểm.
- Recording: phần thực hiện yêu cầu ghi màn hình, nhưng danh sách nộp ghi “where available”. Đề xuất ghi đủ 7 phiên; xin TA xác nhận nếu phiên nào không ghi được.
- Ảnh đa nền tảng: hai mục yêu cầu email overlay và MSSV/họ tên trong form. Đáp ứng cả hai; cách áp dụng cho màn hình không có form cần xác nhận.
- AI category: HW03 ghi “Open”, chưa ghi số category; không tự điền số chỉ từ suy đoán.
- AI Agreement có quy định riêng về người viết bug report; chữ “Open” trong HW03 không tuyên bố hủy quy định đó.
6. Kế hoạch thực hiện theo thứ tự
Bước	Công việc	Đầu ra/điều kiện hoàn thành
1	Xác nhận deadline, bài giảng, phạm vi không trùng; chuẩn bị Git và nền tảng	Scope, môi trường và lịch sử bắt đầu được ghi
2	Tuyển người, đặt lịch pilot và 7 phiên chính thức	Danh sách thật, phù hợp và có thể xác minh
3	AI tạo checklist đầu; bạn phản biện và bổ sung	≥41 mục có ý nghĩa, đủ 4 IA, giữ bản AI gốc
4	Chuẩn bị scenario, thang đo, câu hỏi và mẫu ghi chú; chạy pilot	Bộ công cụ đã sửa sau pilot
5	Thực thi checklist trên ≥3 nền tảng	Kết quả từng nền tảng, Notes, ảnh Failed và thông tin nhận diện
6	Bạn viết bug report, tạo GitHub Issues kèm ảnh	Liên kết checklist ↔ bug ↔ issue ↔ screenshot
7	Chạy 7 usability sessions, commit theo phiên	Ghi chú, câu trả lời thang đo và minh chứng thực tế
8	Tính điểm, nhóm pain points, xếp severity	Phân tích có căn cứ từ dữ liệu gốc
9	Hoàn thiện skill, quay demo; hoàn thiện hồ sơ AI	Skill/video, audit, critique và disclosure
10	Rà rubric, xuất PDF, tự chấm, xuất Git log và ZIP	Bộ nộp đọc được, đủ thành phần, đúng tên và dung lượng