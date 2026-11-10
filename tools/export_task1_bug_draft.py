#!/usr/bin/env python3
"""AI-authored bug draft requested explicitly; not student-authored submission."""
import json,re
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak
HW=Path(__file__).resolve().parents[1];SUB=HW/'submission';OUT=SUB/'ai/drafts/Task1_Bug_Report_AI_Draft'
original={r['id']:r for r in json.loads((SUB/'ai/task1_initial_checklist.json').read_text())['items']}
records={};source={}
for name in ['login','apply','admin','mobile']:
 for r in json.loads((SUB/f'evidence/gui/{name}_execution.json').read_text())['latest']:
  if r['status']=='Failed':records[r['itemId']]=r;source[r['itemId']]=f'evidence/gui/{name}_execution.json'
assert len(records)==31
facts={
'GUI-A-001':('Tiêu đề hiển thị Đăng Ký khi mở trang đăng nhập','Heading hiển thị “Đăng Ký” thay vì nội dung đăng nhập.'),
'GUI-A-002':('Không có h1 khi mở trang đăng nhập','Locator heading level 1 trả về 0 phần tử; kỳ vọng 1.'),
'GUI-A-003':('Nút gửi hiển thị Sign In khi mở form tiếng Việt','Nút gửi mang nhãn “Sign In”; nhãn “Username” cũng xuất hiện trong ảnh/text quan sát.'),
'GUI-A-005':('Ô email dùng type text khi mở form đăng nhập','DOM trả type="text" thay vì "email". Assertion type thất bại trước các kiểm tra tiếp theo.'),
'GUI-A-006':('Ô mật khẩu dùng type text khi nhập mật khẩu','DOM trả type="text" thay vì "password"; trường chứa mật khẩu thử GuiDemo123!.'),
'GUI-A-007':('Nhãn bắt buộc thiếu dấu sao trên form đăng nhập','Nhãn “Username” không chứa dấu *. Không suy rằng mọi nhãn sau assertion đầu đều đã được kiểm.'),
'GUI-A-010':('Focus đầu tiên không theo thứ tự đã định khi nhấn Tab','Sau Tab, link EShop không được focus như thứ tự trên-xuống đang kiểm; DOM nút gửi có tabindex="1" trong hồ sơ. Không suy nguyên nhân gốc.'),
'GUI-A-014':('Thông báo lỗi nằm dưới nút gửi khi đăng nhập sai','Phép đo đáy error=565, vị trí đầu nút submit=425; điều kiện error.bottom ≤ submit.top không đạt.'),
'GUI-A-015':('Đăng nhập đúng bị chặn sau hai lần sai thay vì ba','Trên các tài khoản riêng, đăng nhập đúng sau 1/2/3 lần sai nhận HTTP 200/403/403. Sau hai lần sai vẫn ở /login.'),
'GUI-A-016':('Đăng nhập đúng vẫn bị chặn sau thời gian khóa hơn 30 giây','Sau thời gian đo 31.179 ms vẫn HTTP 403 và còn ở /login; không khẳng định thời gian khóa thực tế tối đa.'),
'GUI-B-004':('Không tìm thấy breadcrumb khi mở Checkout','Locator navigation có accessible name breadcrumb/đường dẫn không xuất hiện. Cần giữ giới hạn locator ngữ nghĩa khi diễn giải.'),
'GUI-B-005':('Áp dụng mã sai tại biên tổng đơn và công thức giảm giá','SAVE10 tổng 300000 trả 400; tổng 300001 trả discount -2700009 và final 3000010. BIGBUY tổng 500000 trả 400; tổng 500001 giảm 50000, final 450001. Đây là các quan sát, không suy rounding policy.'),
'GUI-B-006':('Mã được áp dụng khi request thiếu hoặc hết hạn xác thực','Các vector missing-auth và expired-jwt trả HTTP 200 dù kỳ vọng bị từ chối. JWT hết hạn là fixture public demo key, thay riêng header; không coi đây là chứng minh mọi đường khai thác.'),
'GUI-C-002':('h1 không mô tả Coupons khi mở tab Mã Giảm Giá','h1 duy nhất mang nội dung “EShop Admin”, không khớp ngữ cảnh Mã Giảm Giá theo tiêu chí.'),
'GUI-C-003':('Màu nút Tạo không đạt quy tắc xanh dương','Điều kiện kênh blue lớn hơn red và green trả false. Assertion dừng trước phép kiểm màu nút Xóa; không kết luận màu Xóa từ lần chạy này.'),
'GUI-C-006':('Ô nhập không hiển thị nổi một ký tự ở viewport 390px','Phép đo available content width=0px trong khi glyph đầu khoảng 8.896–9.152px; ảnh QA xác nhận ô bị co. Kết quả geometry-only trước đây đã superseded.'),
'GUI-C-007':('Form tạo coupon không có label thường trực','Locator form label trả 0, kỳ vọng 6. Assertion dừng trước các kiểm tra tiếp theo về dấu *.'),
'GUI-C-008':('Mã chỉ gồm khoảng trắng được lưu khi tạo coupon','Vector code chỉ chứa khoảng trắng được lưu: saved=true trong khi shouldAccept=false.'),
'GUI-C-011':('Giá trị giảm âm được lưu khi tạo coupon','Vector discount_value=-1 được lưu dù kỳ vọng từ chối. Các vector đầy đủ nằm trong JSON gốc.'),
'GUI-C-012':('Ngưỡng đơn âm được lưu khi tạo coupon','Vector min_order_amount=-1 được lưu dù kỳ vọng từ chối.'),
'GUI-C-014':('Ngưỡng đơn bỏ trống vẫn được lưu khi tạo coupon','Vector min_order_amount rỗng được lưu dù kỳ vọng từ chối; không suy mọi trường trống có cùng hành vi.'),
'GUI-C-021':('Tab Coupons không nhận focus khi điều hướng bàn phím','Sau tối đa 18 lần Tab, phần tử tab Coupons chưa thành document.activeElement. Đây là đường Tab được kiểm, không kết luận tất cả cơ chế bàn phím.'),
'GUI-C-024':('Không thấy phản hồi rõ khi tạo mã coupon trùng','Sau submit mã trùng, locator thông báo /mã.*tồn tại|trùng mã|không thể tạo/i không hiển thị; cần đối chiếu ảnh và text raw, không suy rằng backend đã tạo bản trùng.'),
'GUI-C-025':('Không có xác nhận hoặc Undo khi xóa coupon','Không quan sát confirm/cancel hay Undo trong scenario xóa mã thử. Không gọi đây là yêu cầu FR-17 bắt buộc nếu nguồn chỉ là heuristic.'),
'GUI-C-027':('Thiếu thông báo empty-state khi danh sách coupon rỗng','Với GET coupons được fulfill danh sách rỗng có kiểm soát, tbody có 0 dòng nhưng không thấy message chưa có mã/không có mã/danh sách trống. Không xóa dữ liệu dùng chung.'),
'GUI-C-028':('Thiếu thông báo tải lỗi khi request coupon bị ngắt','GET /api/coupons bị abort có kiểm soát; không thấy lỗi tải/thử lại. Assertion đầu hỏng; các nhánh recovery/create/delete phía sau chưa được chạy.'),
'GUI-D-007':('Số điện thoại đúng miền bị từ chối khi lưu Mobile Profile','Theo người thực hiện, 0912345678 và 09123456789 đều báo lỗi; ảnh alert ghi “Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.” Cả vector 9/12 cũng bị từ chối đúng kỳ vọng. Ảnh đại diện, không phải frame riêng từng vector.'),
'GUI-D-008':('Số không bắt đầu 0 được chấp nhận khi lưu Mobile Profile','Người dùng xác nhận 1912345678 lưu thành công, dùng ảnh 9; 09abc45678 báo lỗi ở ảnh 7. Không kết luận phần bàn phím điện thoại đã đạt.'),
'GUI-D-012':('Nút hiển thị Thoát thay Đăng xuất trên Mobile Profile','Ảnh nút ghi “Thoát”. Người dùng xác nhận sau bấm đến đăng nhập và sau đăng nhập lại mở Profile được; báo cáo này chỉ nêu sai nhãn, không khẳng định logout mất hiệu lực.')}
# Same observed rejection is consolidated; other shared root causes remain unproven.
groups=[]
for oid in sorted(records):
 if oid in {'GUI-D-013','GUI-D-014'}:continue
 ids=[oid,'GUI-D-013','GUI-D-014'] if oid=='GUI-D-007' else [oid]
 groups.append(ids)
assert len(groups)==29 and sum(map(len,groups))==31
for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
body=ParagraphStyle('body',fontName='DV',fontSize=9,leading=12,spaceAfter=7)
head=ParagraphStyle('head',parent=body,fontName='DVB',fontSize=12,leading=16,spaceAfter=9,keepWithNext=True)
para=lambda x,st=body:Paragraph(escape(str(x)),st)
intro='BẢN NHÁP MÔ TẢ LỖI DO AI VIẾT theo yêu cầu trực tiếp của người dùng. Không phải bug report 100% sinh viên tự viết theo AI-01 §11; chưa đủ điều kiện thay bản nộp của sinh viên. Có 29 nhóm dự thảo từ 31 mục Failed; chưa chứng minh 29 nguyên nhân gốc riêng biệt. Không có Issue được tạo, ảnh chưa được tải lên GitHub. Không có test mới được chạy.'
md=['# Task 1 - Bug Report AI Draft','',intro,''];story=[para('Task 1 - Bug Report AI Draft',head),para(intro),para('D007/D013/D014 cùng ghi nhận từ chối số đúng miền được gom một nhóm. Các vấn đề khác giữ riêng khi chưa có căn cứ đồng nhất nguyên nhân. Các mức severity là gợi ý của AI, chưa là đánh giá sinh viên.'),para('Dữ liệu Web có UTC trong JSON; Mobile chỉ có giờ trên ảnh/ngữ cảnh người thực hiện, không dựng timestamp đầy đủ. Bản baseline SUT Web và các thay đổi local đã công bố trong Task1_Execution_Report.')]
issues=[]
for number,ids in enumerate(groups,1):
 oid=ids[0];r=records[oid];item=original[oid];title,actual=facts[oid];bid=f'AI-DRAFT-{number:03}'
 severity='Major (AI đề xuất)' if oid in {'GUI-A-006','GUI-A-015','GUI-A-016','GUI-B-005','GUI-B-006','GUI-C-006','GUI-C-008','GUI-C-011','GUI-C-012','GUI-C-014','GUI-D-007','GUI-D-008'} else 'Minor (AI đề xuất)'
 env='Android thật / Expo Go theo người thực hiện; model/build/timestamp lần chạy chưa xác minh' if oid.startswith('GUI-D') else f"Linux / Edge headless {r['observed'].get('browser','')} / viewport {r['observed'].get('viewport',{})}"
 pre='Tài khoản thử test@eshop.com đã đăng nhập; không có token/mật khẩu cá nhân được yêu cầu.' if oid.startswith('GUI-D') else 'SUT local đang chạy; fixture/tài khoản/sản phẩm/coupon riêng theo script; đối chiếu giá trị chính xác trong raw JSON và file test được nêu dưới.'
 testfile={'A':'login.spec.mjs','B':'apply-coupon.spec.mjs','C':'coupons.spec.mjs'}.get(item['feature'])
 reproduction=item['steps']
 if testfile:reproduction+=f' Tái hiện bằng scenario {oid} trong tools/gui/tests/{testfile}; dùng GUI_RUN_ID mới. Fixture phải theo script, không dùng tài khoản dùng chung để thử khóa.'
 evidence=[]
 for id2 in ids:
  rr=records[id2]
  for shot in [rr.get('screenshot','')]+rr.get('screenshots',[]):
   if shot and shot not in evidence:evidence.append(shot)
 assert all((SUB/x).is_file() for x in evidence)
 expected=' '.join(dict.fromkeys(original[x]['expected'] for x in ids))
 sections=[('Module / Requirement',item['feature']+' / '+item['source']),('Related checklist IDs',', '.join(ids)),('Severity',severity),('Description',actual+' Không suy đoán nguyên nhân gốc từ assertion đơn lẻ.'),('Environment',env),('Preconditions',pre),('Steps to reproduce',reproduction),('Expected result',expected),('Actual result',actual),('Raw evidence',source[oid]+f"; Run ID {r.get('runId') or 'không có'}; observed time {r.get('startedAt') or 'chưa có timestamp đầy đủ'}"),('Screenshot files','; '.join(evidence)),('GitHub Issue','Chưa tạo; repository/URL chưa được cung cấp.')]
 md+=['## '+bid+' - '+title,'']
 story.append(PageBreak());story.append(para(bid+' - '+title,head))
 for label,value in sections:
  md +=['**'+label+':** '+value,''];story.append(para(label+': '+value))
 md += ['Ảnh gốc:']+[f'![{Path(x).name}](../../{x})'for x in evidence]+['']
 issuebody='AI-AUTHORED DRAFT — requires review; not student-authored submission.\n\n'+'\n\n'.join('### '+label+'\n'+value for label,value in sections if label!='GitHub Issue')
 issues.append(dict(draftId=bid,title=title,body=issuebody,relatedChecklistIds=ids,screenshotsToUpload=evidence,published=False,issueUrl=None,severityIsAIProposal=True))
OUT.with_suffix('.md').write_text('\n'.join(md)+'\n')
(OUT.parent/'github_issues_draft.json').write_text(json.dumps({'purpose':'Local unpublished issue drafts; no messages sent or Issues created','candidateGroups':29,'failedChecklistItems':31,'studentAuthorship':False,'issues':issues},ensure_ascii=False,indent=2)+'\n')
def footer(c,d):
 c.setFont('DV',8);c.setFillColor(colors.HexColor('#64748B'));c.drawString(42,25,'AI-authored bug draft - Không phải báo cáo sinh viên tự viết');c.drawRightString(A4[0]-42,25,str(d.page))
SimpleDocTemplate(str(OUT.with_suffix('.pdf')),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=45).build(story,onFirstPage=footer,onLaterPages=footer)
print('Generated 29 AI-authored candidate groups covering 31 actual failures; Issues unpublished.')
