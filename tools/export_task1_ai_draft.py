#!/usr/bin/env python3
"""AI-labelled assistance draft, never student testimony or executed results."""
import json
from pathlib import Path
from collections import Counter
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak
HW=Path(__file__).resolve().parents[1];SUB=HW/'submission';OUT=SUB/'ai/drafts/Task1_AI_Assistance_Draft'
blocks=[]
def h(x):blocks.append(('h',x))
def p(x):blocks.append(('p',x))
def table(head,rows):blocks.append(('t',(head,rows)))
def page():blocks.append(('page',None))
h('Task 1 - AI Assistance Draft')
p('DỰ THẢO DO AI VIẾT - CHƯA ĐƯỢC SINH VIÊN XÁC NHẬN. Không thay transcript, đóng góp độc lập, bug report hay chữ ký sinh viên. Không tự đưa các đề xuất dưới đây vào 65 mục đã kết luận. Dữ kiện hiện tại: 65 active, 34 Passed / 31 Failed; ba mục Removed giữ lịch sử.')
h('1. Proposed checklist additions')
p('Ba đề xuất AI bổ sung, đều Not run. Chưa được tính là student additions; sinh viên cần tự đánh giá sự phù hợp, tránh trùng và ghi đóng góp thực của mình. Kỳ vọng từ heuristic là tiêu chí đánh giá, không tự biến thành yêu cầu FR.')
proposals=[('AI-PROP-01 / dự kiến GUI-A-017','Accessible name của ô đăng nhập','IA-02; H6/H7; guide Text Boxes State/Input type.','Mở /login; dùng accessibility tree hoặc trình đọc màn hình lần lượt focus email và mật khẩu. Kiểm tra tên truy cập gắn đúng trường, kể cả khi đã nhập dữ liệu.','Người dùng nhận biết đúng tên trường khi focus; không chỉ dựa vào placeholder hoặc vị trí nhìn thấy.','Checklist đầu kiểm tra nhãn nhìn thấy, input type và Tab; chưa có phép kiểm tên truy cập theo ngữ nghĩa. Đây là phân tích thiếu sót do AI, chưa phải lý do do sinh viên tự viết.'),('AI-PROP-02 / dự kiến GUI-B-009','Thông báo coupon cho trình đọc màn hình','IA-04; H1/H9; guide Visibility of System Status.','Bật trình đọc màn hình, giữ focus tại Áp dụng; thử một mã hợp lệ và một mã không tồn tại. Quan sát việc thông báo trạng thái mà không phải dò lại cả trang.','Phản hồi thành công/lỗi có thể được nhận biết qua công cụ hỗ trợ; nếu không, ghi quan sát và đánh giá theo heuristic.','B007/B008 đã kiểm loading/recovery, nhưng chưa kiểm cách công cụ hỗ trợ nhận thông báo.'),('AI-PROP-03 / dự kiến GUI-C-029','Hướng dẫn nhập mã và loại giảm giá','IA-02; H10; guide Help and Documentation.','Mở Admin Coupons; tìm trợ giúp cạnh code/type/value hoặc đường dẫn hướng dẫn; so nội dung với FR-17 trước khi nhập.','Hướng dẫn nếu có phải đúng quy tắc code duy nhất, giá trị dương và loại phần trăm/cố định; ghi thiếu trợ giúp là quan sát heuristic, không tự coi mọi form bắt buộc tooltip.','Bản đầu tập trung kiểm validation và label; ma trận hiện chưa có mục H10. Không tự đưa giới hạn phần trăm/độ dài không có trong spec.')]
for code,title,source,steps,expected,reason in proposals:
 h(code+' - '+title);p('Nguồn: '+source);p('Bước: '+steps);p('Kỳ vọng: '+expected);p('AI reasoning: '+reason);p('Status: Not run. Student decision / actual / evidence: __________')
page();h('2. AI Audit Report - draft assessment')
p('Theo AI-02: các nhãn giữ tiếng Anh, nội dung mới bằng tiếng Việt. Tool: Codex; model và timestamp gốc chưa xác minh. Các verdict sau là đánh giá do AI đề xuất, chưa phải nhận xét sinh viên. Thiếu prompt/output đầy đủ thì không coi bảng này là audit cuối.')
table(['Student Information','Value'],[['Student name / Student ID / Class','__________'],['Assignment ID','HW03-AI'],['Date / Signature','__________']])
audits=[('Artifact #1 - initial checklist','bat dau thuc hien task 1','ai/task1_initial_checklist.md/.json; nguyên văn bản đầu được lưu tại nguồn.','INCOMPLETE','Guide yêu cầu truy vết widget × heuristic; matrix ban đầu chưa có H10, và các phần chỉ kiểm nhãn/Tab chưa bao phủ tên truy cập. Không phải mọi heuristic đều bắt buộc áp dụng.','Sinh viên đã trả lời Keep; các đề xuất bổ sung hiện do AI viết, chưa có student additions.'),('Artifact #2 - C006 narrow-viewport assertion','Prompt gốc cho riêng việc sửa assertion chưa được xuất; không tự dựng lại.','evidence/gui/admin_execution.json: giữ history hình học và kết quả cuối C006.','INVALID','Guide Compatibility và Text Boxes yêu cầu đọc/nhập được. Geometry-only không đủ khi nội dung input có chiều rộng 0px; lần đo/ảnh sau đã khiến C006 Failed.','AI đã sửa assertion sau visual QA; không ghi là sinh viên tự sửa code.'),('Artifact #3 - D015 oracle','Roi hay ra soat va hoat thanh task 1','mobile_case_revisions.json và mobile_execution.json; lịch sử Spec-gap giữ nguyên.','INCOMPLETE','FR-22 chỉ yêu cầu lỗi trên Submit, không quy định inline. D015 được chốt Passed về vị trí từ ảnh có sẵn; không phải chạy mới.','AI sửa cách diễn giải; chưa có lời xác nhận đánh giá của sinh viên.'),('Artifact #4 - scope removal','Loai bo luon cac truong hop nay','GUI_Checklist.xlsx; 65 active, 3 Removed, không tái đánh số ID.','VALID','HW03 §6 yêu cầu >40 và đủ IA-01…04. 65 active đáp ứng số lượng và IA; AGENTS workflow yêu cầu bảo toàn bằng chứng, không gán Passed cho phần bị bỏ.','Người dùng quyết định loại; AI áp dụng thay đổi và giữ lịch sử.')]
for name,prompt,output,verdict,reason,fix in audits:
 h(name);p('(1) Prompt + Tool: '+prompt+' | Tool: Codex | Time: chưa xuất timestamp gốc.');p('(2) AI Output: '+output+' Nội dung trên là định vị/tóm tắt, không thay output nguyên văn đầy đủ.');p('(3) Verdict: '+verdict);p('(4) Reasoning: '+reason);p('(5) Student Fix / actual attribution: '+fix)
c=Counter(a[3] for a in audits);h('Summary of AI Accuracy');table(['Metric','Count / Percentage'],[['Total AI-generated artifacts audited','4 / 100%']]+[[key,f'{c[key]} / {c[key]/4:.0%}']for key in ['VALID','INVALID','INCOMPLETE']]);p('Conclusion - AI-authored draft (not student confirmation): AI phù hợp để tạo cấu trúc kiểm thử, triển khai phép kiểm lặp lại và tổng hợp bằng chứng. Giá trị của công cụ phụ thuộc vào đặc tả, dữ liệu và assertion được chọn. Trường hợp C006 cho thấy phép đo dễ tự động hóa chưa chắc đo đúng khả năng sử dụng. D015 cho thấy suy diễn thêm điều kiện ngoài nguồn có thể làm kết luận sai. Vì vậy, cần kiểm tra lại oracle và xem bằng chứng trước khi chốt. Khi thiếu dữ liệu, phải giữ trạng thái chưa xác minh thay vì điền kết quả. Không dùng đầu ra AI làm bằng chứng cho hoạt động cá nhân chưa diễn ra. Mandatory Disclosure / Signature: chưa ký; không tự điền lời cam kết thay sinh viên.')
page();h('3. AI Critique - AI-authored draft')
p('Đoạn dưới do AI viết, không phải phản ánh cá nhân đã được sinh viên xác nhận. Sinh viên cần sửa theo trải nghiệm thật và công khai AI hỗ trợ; không đổi nhãn thành “tự viết hoàn toàn”.')
critique='''Quá trình kiểm thử Task 1 cho thấy AI hỗ trợ tốt việc tổ chức checklist, viết mã thực thi và tổng hợp bằng chứng. Khả năng ánh xạ từng mục sang yêu cầu, dữ liệu và ảnh giúp đối chiếu kết quả thuận tiện. Tuy nhiên, độ đầy đủ của tài liệu không bảo đảm kết luận chính xác.

Một hạn chế xuất hiện ở kiểm tra bố cục Admin Coupons: phép đo hình học ban đầu chưa chứng minh nội dung ô nhập có thể đọc được. Việc xem ảnh và kiểm tra vùng hiển thị ký tự đã làm thay đổi kết quả. Trường hợp này cho thấy assertion phải phản ánh trải nghiệm cần kiểm tra, thay vì chỉ đo một thuộc tính dễ lấy.

Ở Mobile, việc yêu cầu lưu hồ sơ bằng số điện thoại hợp lệ khiến một số phép kiểm phụ thuộc bị chặn. Tách dữ liệu hỗ trợ có thể giúp cô lập hành vi, nhưng không được dùng số sai miền để tuyên bố validation đúng. Ngoài ra, cách hiểu rằng thông báo lỗi phải inline đã thêm điều kiện không có trong FR-22. Việc đọc lại nguồn và xem ảnh giúp thu hẹp kết luận về đúng vị trí hiển thị.

Bài học là dùng AI để tăng tốc thiết kế và xử lý hồ sơ, đồng thời kiểm tra lại oracle, tiền điều kiện và bằng chứng. Cần phân biệt mục bị loại khỏi phạm vi với mục đạt, ảnh tải lên với lượt chạy độc lập, và góp ý AI với đóng góp của sinh viên.'''
words=len(critique.split());assert 200<=words<=300,words
for paragraph in critique.split('\n\n'):p(paragraph)
p(f'Độ dài bản nháp: {words} đơn vị phân tách bằng khoảng trắng. Chưa thay phần critique cuối đã được sinh viên review.')
page();h('4. AI Use Disclosure Form - draft facts')
h('1. Course & Student Info');table(['Field','Value'],[['Course','CS423 / CSC13003 - Software Testing'],['Assignment ID / Title','HW03-AI / GUI & Usability'],['AI Use Category (1–5)','Category ____; đề ghi Open, chưa có số được xác minh'],['Student name / Student ID / Date','__________']])
h('2. Disclosure Questions')
p('1. AI tool(s) used: Codex trong cuộc hội thoại này; sinh viên bổ sung công cụ khác nếu có. Không đoán model hoặc phiên bản.')
p('2. Stage(s): AI hỗ trợ outlining, drafting, revision, coding, phân tích dữ liệu thực thi và định dạng tài liệu. Mobile do sinh viên thao tác; Web harness do AI viết/chạy trong phiên được phép.')
p('3. Main prompts or tasks given to the AI (verbatim):')
for q in ['Ban hay rut gon so luong test tren mobile','Ban sua lai sdt trong test case cho phu hop voi 3 cai block di','Loai bo luon cac truong hop nay']:p('“'+q+'”')
p('Full transcript: chưa có bản xuất nguyên văn đầy đủ. ai/prompt_log.md hiện là activity summary PARTIAL, không thay Appendix A hoàn chỉnh.')
p('4. Specific parts AI contributed to: checklist đầu 68 mục, harness Web, tính toán/đối chiếu kết quả, chuyển ghi nhận Mobile sang hồ sơ, sửa phạm vi theo yêu cầu và các bản Markdown/PDF. Bộ dự thảo hiện tại gồm đề xuất thêm checklist, audit/critique/disclosure do AI viết; chưa có mục sinh viên tự thêm. Theo yêu cầu tiếp theo, AI đã viết riêng Task1_Bug_Report_AI_Draft: bản nháp lỗi do AI viết, không phải báo cáo 100% sinh viên tự viết.')
p('5. Review/verification recorded: sinh viên trả lời Keep, cung cấp ảnh và mô tả Mobile, sửa nhầm ảnh, yêu cầu sửa rồi loại ba ca. AI chạy kiểm tra số liệu, đối chiếu ảnh/source, kiểm tra hash và layout. Phần tự review/audit còn cần sinh viên xác nhận; không tự nhận sinh viên đã làm các bước kiểm tra bằng công cụ của AI.')
p('6. Citation: Codex [AI coding assistant], sử dụng trong HW03; sinh viên điền thông tin công cụ bổ sung được xác minh theo kiểu trích dẫn môn học. Không tạo version/timestamp thiếu.')
h('3. Statement of Honesty');p('Sinh viên đọc nội dung xác nhận của mẫu AI-03 trước khi ký. Bản này chưa phải tuyên bố đã ký. Student name / Student ID / Date / Signature: __________')
page();h('5. Bug report worksheet and evidence index')
p('AI-01 §11 yêu cầu bug descriptions do sinh viên viết 100%. Phần này là khung và danh mục bằng chứng. Bản nháp mô tả lỗi do AI đã được soạn riêng trong Task1_Bug_Report_AI_Draft.md/.pdf theo yêu cầu tiếp theo; chưa đáp ứng điều kiện student-written và không có Issue giả. 31 mục Failed không nhất thiết là 31 bug; sinh viên tự gom nguyên nhân trước khi tạo Bug ID.')
for x in ['Bug ID / Title','Related checklist IDs','Environment / Preconditions / Actual input','Steps to reproduce','Expected result / source','Actual result','Severity / justification','Screenshot / GitHub Issue URL']:p(x+': __________')
failed=[]
for name in ['login','apply','admin','mobile']:
 failed += [r for r in json.loads((SUB/f'evidence/gui/{name}_execution.json').read_text())['latest'] if r['status']=='Failed']
assert len(failed)==31
index=[{'itemId':r['itemId'],'screenshot':r['screenshot']}for r in sorted(failed,key=lambda r:r['itemId'])]
(OUT.parent/'failed_evidence_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
p('Danh mục JSON đi kèm giữ đường dẫn local đầy đủ. Bảng dưới là chỉ mục, không phải các bug đã được viết hoặc khử trùng.')
table(['Checklist ID','Screenshot filename'],[[r['itemId'],Path(r['screenshot']).name]for r in index])
h('Việc cần sinh viên làm trước khi dùng bộ này');p('Review/sửa dự thảo theo trải nghiệm thật; tự viết bug descriptions; tự quyết định và bổ sung checklist; thực thi mục mới; cung cấp transcript đầy đủ; điền thông tin và ký thật. Không thay trạng thái acceptance chỉ vì đã có tài liệu AI dự thảo.')
md=[]
for kind,value in blocks:
 if kind=='h':md+=['## '+value,'']
 elif kind=='p':md+=[value,'']
 elif kind=='t':
  header,rows=value;md+=['| '+' | '.join(header)+' |','| '+' | '.join('---'for _ in header)+' |']+['| '+' | '.join(str(x).replace('|','/')for x in row)+' |'for row in rows]+['']
OUT.with_suffix('.md').write_text('\n'.join(md)+'\n')
for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
body=ParagraphStyle('body',fontName='DV',fontSize=9,leading=12.5,spaceAfter=7)
head=ParagraphStyle('head',parent=body,fontName='DVB',fontSize=11.5,leading=15,spaceBefore=9,spaceAfter=8,keepWithNext=True)
cell=ParagraphStyle('cell',parent=body,fontSize=8,leading=11,spaceAfter=0)
chain=ParagraphStyle('chain',parent=body,keepWithNext=True)
def para(x,style=body):
 if style is body and str(x).startswith(('(1) Prompt','(2) AI Output','(3) Verdict','(4) Reasoning')):style=chain
 return Paragraph(escape(str(x)),style)
story=[]
for kind,value in blocks:
 if kind=='h':story.append(para(value,head))
 elif kind=='p':story.append(para(value))
 elif kind=='page':story.append(PageBreak())
 else:
  header,rows=value;t=Table([[para(x,cell)for x in header]]+[[para(x,cell)for x in row]for row in rows],colWidths=[170,A4[0]-84-170],repeatRows=1)
  t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E2E8F0')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#CBD5E1')),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story +=[t,Spacer(1,8)]
def footer(c,d):
 c.setFont('DV',8);c.setFillColor(colors.HexColor('#64748B'));c.drawString(42,25,'AI-authored draft - Chưa có xác nhận/chữ ký sinh viên');c.drawRightString(A4[0]-42,25,str(d.page))
SimpleDocTemplate(str(OUT.with_suffix('.pdf')),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=45).build(story,onFirstPage=footer,onLaterPages=footer)
print('Generated AI-labelled assistance draft; critique units:',words)
