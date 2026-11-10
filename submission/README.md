# HW03 - Submission workspace

Task 1 đã chốt kết quả thực thi trong phạm vi hiện tại; hồ sơ Task 1 chưa đủ điều kiện hoàn tất toàn bộ. Task 2/3 và bộ nộp cuối chưa hoàn thành.

## Tổng kết Task 1

| Feature | Mục active | Passed | Failed |
| --- | --- | --- | --- |
| A - FR-02 Login/lockout (Web) | 16 | 6 | 10 |
| B - FR-09 Apply Coupon (Web) | 8 | 5 | 3 |
| C - FR-17 Admin Coupons | 28 | 15 | 13 |
| D - FR-04 Mobile Profile | 13 | 8 | 5 |
| Tổng | 65 | 34 | 31 |

- Đủ IA-01…04; 65/65 mục active đã kết luận, không còn Not run/Blocked/Spec-gap.
- Bản AI ban đầu 68 mục được bảo toàn. D006/D009/D016 đã Remove theo yêu cầu người dùng, còn dòng lịch sử trong Excel/JSON; không tính vào 65 mục active.
- D015 chốt Passed theo FR-22: nội dung lỗi nằm phía trên Submit; nguồn không bắt buộc inline. Đây là review oracle trên ảnh đã có, không phải một lượt chạy mới.
- Có 55 Web scenario runs; Mobile có 7 nhóm ca active và 12 upload ảnh. Không cộng upload hoặc ánh xạ tiêu chí thành số lần chạy độc lập.
- 31 mục Failed có ảnh local; chưa xác định số bug duy nhất, không gọi 31 Failed là 31 bug.

## Tài liệu và bằng chứng

| Hồ sơ | Vai trò |
| --- | --- |
| `Task1_Execution_Report.md/.pdf` | Kết quả, phương pháp/fixture, trạng thái từng ID, ma trận widget × heuristic và bảng nghiệm thu Task 1 |
| `GUI_Checklist.xlsx` | Summary, Checklist, Execution, AI Review; 65 active + 3 Removed để truy vết |
| `ai/task1_initial_checklist.md/.json/.pdf` | Bản AI đầu 68 mục, không sửa theo kết quả chạy |
| `Task1_AI_Review.md/.pdf` | Keep ban đầu và các quyết định mới; 64 Keep / 1 Revise / 3 Remove; phần tự thêm còn thiếu |
| `Task1_Mobile_Manual_Form.md/.pdf` | Template trống cho 13 mục active / 7 nhóm ca; không thay kết quả thực thi hiện tại |
| `Task1_Plan.md/.pdf`, `Task1_Intake.md/.pdf` | Kế hoạch/intake lịch sử theo phạm vi thiết kế ban đầu |
| `mobile_case_revisions.json` | Quyết định Remove và làm rõ oracle D015; không coi là student additions |
| `evidence/gui/*_execution.json` | Web latest/history và Mobile quan sát thật + lịch sử revision |
| `evidence/gui/T1A_*/`, `T1B_*/`, `T1C_*/` | Playwright JSON và ảnh Web gốc |
| `evidence/gui/T1D_MANUAL_01/` | 12 PNG Mobile gốc, manifest SHA-256 |
| `evidence/gui/task1_report_checkpoint.json` | Counts, đối chiếu workbook và SHA-256 nguồn hiện tại |
| `ai/prompt_log.md` | Log hoạt động PARTIAL, không phải transcript nguyên văn đầy đủ |

## Giới hạn cần giữ khi diễn giải

Mobile do sinh viên thao tác và cung cấp kết quả; AI chép/đối chiếu. Ảnh 9 thay ảnh 6 dán nhầm cho 1912345678; ảnh 8 là tắt mạng, ảnh 12 sau bật mạng; ảnh 11 sau Thoát và ảnh 10 sau đăng nhập lại theo xác nhận người dùng. Hash cho thấy các nhóm 2/3, 4/5/7 và 9/10/12 giống nguyên byte; không coi là các frame độc lập. Các vector biên dùng ảnh alert đại diện kết hợp lời người thực hiện; timestamp/build Mobile chưa được cung cấp đầy đủ.

Không thay đổi SUT hoặc quy tắc FR-04. 1912345678 được ứng dụng chấp nhận nhưng sai miền; các kết quả validation vẫn giữ đúng oracle số bắt đầu 0, dài 10–11 chữ số. Không tuyên bố các thao tác lưu Unicode/multiline/recovery đã hoàn tất sau khi loại ba mục đó. Edge headless/viewport hẹp chưa thỏa Task 3.

## Còn thiếu để hoàn tất Task 1

1. HW03-T1-03: sinh viên tự bổ sung mục AI bỏ sót và giải thích lý do, ngoài các quyết định Keep/Revise/Remove đã nhận.
2. HW03-T1-05: 29 Issue đã được tạo kèm ảnh và liên kết về 31 Failed. Mô tả hiện từ bản nháp có khai báo AI; điều kiện sinh viên tự viết của môn học chưa được xác nhận.
3. HW03-AI/DOC: full transcript, audit, disclosure/critique và thông tin/chữ ký thực của sinh viên theo các biểu mẫu áp dụng. Không tạo timestamp hoặc chữ ký thay người dùng.

Chưa có ZIP/điểm tự chấm; xuất Git log thật khi chuẩn bị bộ nộp. Mọi tài liệu giữ trong bộ nộp cuối cần bản PDF và kiểm tra nội dung/layout theo policies. Tiến độ và acceptance criteria: `../PROGRESS.md`, `../requirements_list.md`.


## AI-authored assistance drafts (not final student deliverables)

Theo yêu cầu trực tiếp “Tu sinh giup toi” và “Toi yeu cau ban lam het di”, AI đã soạn bộ tài liệu nháp đầy đủ từ dữ liệu hiện có:

- `ai/drafts/Task1_AI_Assistance_Draft.md/.pdf`: 3 đề xuất checklist chưa chạy, audit AI đề xuất cho 4 artifact (1 VALID / 1 INVALID / 2 INCOMPLETE), kết luận AI đề xuất, critique 269 đơn vị phân tách khoảng trắng, Disclosure và chỉ mục bằng chứng.
- `ai/drafts/Task1_Bug_Report_AI_Draft.md/.pdf`: 29 nhóm bug dự thảo ánh xạ 31 Failed; D007/D013/D014 gom theo cùng hiện tượng từ chối số đúng miền. Chưa chứng minh đây là 29 nguyên nhân gốc độc lập; severity là AI đề xuất.
- `ai/drafts/github_issues_draft.json`: payload nguồn và metadata phát hành; ảnh nhúng từ commit cố định; mọi `published=true`, có `issueUrl`, thời gian tạo thực và nội dung đã đăng. `failed_evidence_index.json` giữ đường dẫn đủ 31 mục.

Nguồn đóng góp của bộ dự thảo được khai báo tập trung tại mục Disclosure trong `ai/drafts/Task1_AI_Assistance_Draft.md/.pdf`; các nhãn tác giả lặp ở tiêu đề/chân trang được lược gọn. Khi sửa Markdown thủ công, dùng `tools/export_task1_draft_pdfs.py` để xuất PDF, tránh sinh lại nguồn bằng các builder ban đầu.


## GitHub Issues đã phát hành

Đã tạo và xác minh **29 Issue #1–#29** tại https://github.com/quocthaiLN/software-testing-hw03/issues. 31 mục Failed được ánh xạ đầy đủ trong Excel Execution (Bug ID / Issue URL); D007/D013/D014 dùng chung Issue #27. Đối chiếu public REST xác nhận nội dung đã đăng; tất cả 47 URL PNG được kiểm HTTP 200 và content-type image. Ảnh ghim commit `19cbfb0d5afac98f3d0aab56ef158254f297c682`. Metadata thật ở `evidence/gui/github_published_issues.json`; các kết luận test không thay đổi.
