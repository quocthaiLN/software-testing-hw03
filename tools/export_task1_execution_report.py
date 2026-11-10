#!/usr/bin/env python3
"""Summarize real GUI records; never generate student-authored bug descriptions."""
import hashlib
import json
import zipfile
from xml.etree import ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

HW=Path(__file__).resolve().parents[1]
SUB=HW/'submission'
OUT=SUB/'Task1_Execution_Report'
FEATURES={'A':'FR-02 - Web Login', 'B':'FR-09 - Web Apply Coupon',
          'C':'FR-17 - Admin Coupons', 'D':'FR-04 - Mobile Profile'}

def main():
    initial=json.loads((SUB/'ai/task1_initial_checklist.json').read_text())['items']
    assert len(initial)==68 and len({r['id'] for r in initial})==68
    sources={}; latest={}; history=[]
    for name in ['login','admin','apply']:
        path=SUB/'evidence/gui'/f'{name}_execution.json'
        data=json.loads(path.read_text());sources[name]=data
        for row in data['latest']:
            assert row['itemId'] not in latest
            latest[row['itemId']]=row
            assert row['status'] in ['Passed','Failed']
            if row['status']=='Failed':assert (SUB/row['screenshot']).is_file()
        history+=data['history']
    assert len(latest)==52 and len(history)==55
    web_latest=dict(latest)
    mobile_path=SUB/'evidence/gui/mobile_execution.json'
    mobile=json.loads(mobile_path.read_text()) if mobile_path.exists() else {'latest':[]}
    for row in mobile['latest']:
        assert row['itemId'].startswith('GUI-D-') and row['itemId'] not in latest
        assert row['status'] in ['Passed','Failed','Blocked','Spec-gap','Not run']
        if row['status']=='Failed':assert (SUB/row['screenshot']).is_file()
        latest[row['itemId']]=row
    status={r['id']:latest[r['id']]['status'] if r['id'] in latest else 'Not run' for r in initial}
    counts=Counter(status.values())
    concluded=counts['Passed']+counts['Failed']
    failed_images=sum(r['status']=='Failed' and (SUB/r['screenshot']).is_file() for r in latest.values())
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(SUB/'GUI_Checklist.xlsx') as z:
        strings=[''.join(t.text or '' for t in x.iter('{'+ns['s']+'}t'))
                 for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        values={}
        for c in ET.fromstring(z.read('xl/worksheets/sheet2.xml')).findall('.//s:c',ns):
            v=c.find('s:v',ns)
            if v is not None:values[c.get('r')]=strings[int(v.text)] if c.get('t')=='s' else v.text
        workbook_status={values.get('A'+str(i)):values.get('M'+str(i)) for i in range(7,75)}
        assert workbook_status==status, 'Workbook diverged from checkpoint; reconcile before export'
    blocks=[]
    def h(s):blocks.append(('h',s))
    def p(s):blocks.append(('p',s))
    def table(headers,rows,widths=None):blocks.append(('t',(headers,rows,widths)))
    def br():blocks.append(('br',None))
    h('Task 1 - Báo cáo thực thi GUI (bản đang hoàn thiện)')
    p('Mốc dữ liệu: các lượt chạy Web ngày 2026-11-10. Phạm vi thiết kế gồm bốn feature A/B/C/D. Task 1 chưa hoàn tất: Đã tích hợp kết quả Mobile do sinh viên cung cấp và 12 ảnh gốc; 3 tiêu chí còn Blocked và 1 Spec-gap. Báo cáo này tổng hợp hồ sơ thực thi, không thay bug report do sinh viên tự viết.')
    h('1. Thống kê hiện tại')
    summary=[]
    for f,name in FEATURES.items():
        rs=[r for r in initial if r['feature']==f];c=Counter(status[r['id']]for r in rs)
        summary.append([f+' / '+name,len(rs),c['Passed']+c['Failed'],c['Passed'],c['Failed'],c['Blocked']+c['Spec-gap'],c['Not run']])
    summary.append(['Tổng',68,concluded,counts['Passed'],counts['Failed'],counts['Blocked']+counts['Spec-gap'],counts['Not run']])
    table(['Feature','Thiết kế','Chốt P/F','Passed','Failed','Chờ B/S','Not run'],summary,[.35,.11,.11,.11,.11,.11,.10])
    p(f"{concluded}/68 mục đã chốt Passed/Failed; {counts['Passed']} Passed / {counts['Failed']} Failed / {counts['Blocked']} Blocked / {counts['Spec-gap']} Spec-gap / {counts['Not run']} Not run. Có 55 lượt scenario Web; 8 ca Mobile thủ công được ánh xạ vào 16 tiêu chí, không cộng 16 ánh xạ hoặc 12 ảnh thành số scenario runs.")
    p('Chờ B/S là tổng Blocked và Spec-gap; hai trạng thái vẫn tách riêng theo ID và Excel. Mọi tiêu chí Mobile đã có ghi nhận, nhưng ghi nhận một phần không đồng nghĩa hoàn tất kiểm tra. Số bug duy nhất chưa xác định; Failed không phải số bug đã khử trùng.')
    h('2. Phạm vi và cơ sở thiết kế')
    table(['Feature / màn hình','Nội dung trong phạm vi','Giới hạn'],[
      ['A / Web /login','Nhãn, input, focus/bàn phím, login, phản hồi sai/khóa và phục hồi','Tài khoản thử riêng; không khóa tài khoản demo dùng chung'],
      ['B / Web /checkout','Khối coupon, điều kiện C1-C5, công thức/biên, phản hồi và recovery','Cart là tiền điều kiện; không chốt đơn/thanh toán'],
      ['C / Admin Coupons','Tạo, xem, xóa coupon; form, bảng, navigation và trạng thái','FR-17 chi tiết chỉ yêu cầu Thêm/Xem/Xóa; không tự thêm Sửa'],
      ['D / Expo Go Profile','Email chỉ đọc, tên/điện thoại/địa chỉ, bàn phím/cuộn, lưu, đăng xuất','Kết quả thủ công một phần; không gồm lịch sử/hủy đơn']],[.21,.45,.34])
    p('Nguồn: đề HW03 §6 Task 1; EShop README v2.0 FR-02/04/09/17 và FR-21-24; API specification; bản tổng hợp bài giảng tại skills/gui-testing-guide do sinh viên chỉ định. Tiêu chí heuristic có H1-H10 để truy vết, không được tự gán thành yêu cầu nghiệp vụ. Domain/Boundary chọn input và trạng thái; GUI thật vẫn là đối tượng quan sát.')
    table(['IA','A','B','C','D','Tổng'],[[ia]+[sum(r['feature']==f and r['ia']==ia for r in initial)for f in FEATURES]+[sum(r['ia']==ia for r in initial)] for ia in ['IA-01','IA-02','IA-03','IA-04']],[.25,.15,.15,.15,.15,.15])
    p('Bản AI đầu 68 mục được bảo toàn tại ai/task1_initial_checklist.md/.json/.pdf. Sinh viên trả lời Keep cho các mục hiện có; quyết định này không chứng minh đã tự bổ sung mục hoặc viết lý do phản biện. Phần đó còn thiếu trong Task1_AI_Review.md.')
    br();h('3. Môi trường và phương pháp thực thi')
    table(['Thành phần','Giá trị / giới hạn'],[
      ['Web GUI đã chạy','Linux; Microsoft Edge headless 155.0.4283.45; viewport 1280×800; C006 thêm 390×844'],
      ['Địa chỉ cục bộ','Web http://localhost:5173; Admin http://localhost:5174; API http://localhost:3000/api'],
      ['SUT nền tại lúc chạy','85af3ba875c88283615e22cb108f13e2fccaf0e9; giữ các thay đổi local có sẵn, không khẳng định đây là checkout sạch'],
      ['Runner','Playwright; một worker; retries=0; Run ID mới mỗi lần; ảnh Failed và JSON quan sát thật'],
      ['Mobile thủ công','Android thật / Expo Go theo ngữ cảnh phiên; ảnh gốc 1080×2436, tài khoản test@eshop.com. Model/OS từ bước setup trước không tự chứng minh metadata lần chạy này; timestamp đầy đủ và build chưa được cung cấp.'],
      ['Task 3','Edge headless và viewport hẹp chưa thỏa ma trận Chrome/Firefox/Expo Go; không tuyên bố đã hoàn tất đa nền tảng']],[.26,.74])
    p('Trình tự thực thi: A → C → B; D chuyển sang sinh viên làm thủ công theo yêu cầu. Mỗi scenario Web có tiền điều kiện riêng; Mobile theo trình tự thủ công do sinh viên mô tả, có giới hạn bằng chứng ảnh tĩnh. API/SQLite chỉ hỗ trợ fixture và đối chiếu; kết luận GUI dựa trên giao diện và request/response thật. Nếu assertion đầu hỏng, các assertion phía sau chưa chạy không được coi là đạt.')
    table(['Trường hợp','Thiết lập được công bố'],[
      ['A - khóa tài khoản','Đăng ký user demo riêng cho từng tình huống. Kiểm tra số lần sai và mốc hơn 30 giây bằng quan sát có timestamp; không thay logic khóa.'],
      ['C - coupon thử','Code dùng prefix T1, ngoại trừ fixture whitespace được ghi rõ. C015 kiểm tra date input HTML, không chứng minh validation backend.'],
      ['C027 - empty state','Fulfill GET coupons bằng danh sách rỗng có kiểm soát chỉ cho trang test; không xóa coupon dùng chung.'],
      ['C028 - lỗi mạng','Abort GET coupons. Assertion phản hồi tải lỗi hỏng trước các nhánh recovery/tạo/xóa; các nhánh sau chưa được chứng minh.'],
      ['B - tổng giỏ hàng','Seed sản phẩm thật đúng giá; Home → Add to cart → Cart → Checkout. Không sửa ô tổng tiền để giả lập biên.'],
      ['B - điều kiện coupon','Coupon/user/lượt dùng riêng. Inactive đổi bằng SQLite parameterized theo đúng ID/code rồi API verify. Lượt dùng seed qua endpoint, không tuyên bố đã tạo đơn.'],
      ['B - auth và mạng','JWT hết hạn thay riêng header request bằng public demo key; backend trả lời thật. Pending giữ response thật bằng gate; recovery abort transport rồi khôi phục.']],[.27,.73])
    h('4. Lịch sử chạy và hiệu chỉnh')
    runrows=[]
    for run in sorted({r['suiteRun']for r in history}):
        rs=[r for r in history if r['suiteRun']==run];c=Counter(r['status']for r in rs)
        runrows.append([run,len(rs),c['Passed'],c['Failed'],min(r['startedAt']for r in rs)])
    table(['Suite Run ID','Scenario','Passed','Failed','Bắt đầu (UTC)'],runrows,[.31,.12,.12,.12,.33])
    p('T1C_20261110_01 bị lỗi guard lúc worker nạp config, trước mọi thao tác UI; giữ log riêng và loại khỏi tổng 55. A003 được thu hẹp assertion nhãn hành động tiếng Việt rồi vẫn Failed. C006 có hai kết quả hình học hẹp trước đó được giữ trong history; sau visual QA, assertion vùng hiển thị ký tự được bổ sung và run 04 Failed. Chỉ kết quả cuối theo ID được tính vào summary.')
    for f,name in FEATURES.items():
        if f!='A':br()
        h('5.'+f+' Kết quả theo mục - '+name)
        p('Đây là trạng thái checklist, không phải danh sách bug đã khử trùng. Bước, input và kỳ vọng gốc nằm trong checklist AI và workbook; actual, assertion và ảnh nằm trong hồ sơ raw tương ứng.' if f!='D' else 'Sinh viên xác nhận MOB-01/02/03 PASS; các trạng thái còn lại đối chiếu mô tả thao tác và ảnh thật. Bản phiếu vẫn là template trống; hồ sơ hiện tại nằm ở evidence/gui/mobile_execution.json. Ảnh 9 thay ảnh 6 cho số 1912345678; ảnh 8 lúc tắt mạng; ảnh 12 sau bật mạng; ảnh 11 sau Thoát và ảnh 10 sau đăng nhập lại.')
        table(['Item ID','Tiêu chí giữ lại','IA','Trạng thái'],[[r['id'],r['title'],r['ia'],status[r['id']]]for r in initial if r['feature']==f],[.20,.47,.13,.20])
    h('5.D.1 Ghi nhận Mobile theo ID gốc')
    p('Các dòng sau là bản chép/đối chiếu dữ liệu thực thi, không phải mô tả bug do AI soạn. Passed dựa trên xác nhận người thực hiện kết hợp ảnh; ảnh tĩnh không tự chứng minh mọi thao tác chạm, cuộn hay dán. Từng vector biên được người dùng xác nhận, ảnh alert là bằng chứng đại diện.')
    table(['ID / trạng thái','Quan sát và giới hạn','Ảnh gốc'],[[r['itemId']+' / '+r['status'],r['actual'],', '.join(Path(x).name for x in r['screenshots'])]for r in mobile['latest']],[.20,.62,.18])
    p('Các ảnh được lưu nguyên byte và SHA-256 trong evidence/gui/T1D_MANUAL_01/manifest.json. Giữ cả ảnh người dùng dán nhầm để bảo toàn nguồn; không dùng ảnh 6 làm bằng chứng 1912345678 thành công. Hash xác nhận ảnh 2/3, 4/5/7 và 9/10/12 giống nguyên byte. Ngữ cảnh khác nhau do sinh viên xác nhận; không tính upload thành các frame/lần chạy độc lập.')
    br();h('6. Độ phủ widget × heuristic')
    p('Mỗi ô là số mục thiết kế / số mục đã chốt P/F liên kết widget và heuristic. Đây là truy vết thiết kế, không phải số assertion đạt hoặc chứng nhận mọi trạng thái đã được thử. Dấu - nghĩa là chưa có ánh xạ. H10 chưa có mục; sinh viên cần xác định tính áp dụng và bổ sung khi review.')
    widgets=sorted({w.strip()for r in initial for w in r['widget'].split(',')})
    assert len(widgets)==31
    matrix=[]
    for w in widgets:
        vals=[w]
        for i in range(1,11):
            rs=[r for r in initial if w in r['widget'].split(',') and 'H'+str(i) in r['heuristic'].split(',')]
            vals.append(f'{len(rs)}/{sum(status[r["id"]] in ["Passed","Failed"] for r in rs)}'if rs else '-')
        matrix.append(vals)
    table(['Widget']+['H'+str(i)for i in range(1,11)],matrix,[.17]+[.083]*10)
    h('7. Oracle và giới hạn cần review')
    for s in [
      'FR-09 chưa nêu cách làm tròn tiền lẻ. Không dùng riêng khác biệt format số lẻ để khẳng định lỗi. Kết luận B005 không phụ thuộc việc chọn rounding policy; dữ liệu gốc giữ các vector và số tiền thật.',
      'FR-17 chưa yêu cầu percent ≤100, lượt là số nguyên hoặc ngày tạo luôn ở tương lai. Không thêm các oracle này để tăng số lỗi.',
      'D015: FR-22 yêu cầu lỗi trên submit; cách áp dụng cho native Alert vẫn cần sinh viên review. Ảnh 4/5/7 cho thấy native Alert; D015 được giữ Spec-gap chờ quyết định oracle.',
      'Các tiêu chí loading, ngăn gửi lặp, xác nhận/hoàn tác xóa là heuristic đã có nguồn. Không gọi chúng là điều kiện nghiệp vụ FR-17.',
      'Các scenario có nhiều biến thể không chứng minh mọi nhánh nếu dừng sớm; raw log và mã test là căn cứ xác định phần thực sự đã chạy.'
    ]:p(s)
    h('8. Hồ sơ bằng chứng và công việc còn lại')
    table(['Hồ sơ trong bộ nộp','Vai trò'],[
      ['GUI_Checklist.xlsx','Working checklist, Execution, Summary và AI Review; 68 trạng thái từ hồ sơ Web và Mobile khớp workbook ở checkpoint này.'],
      ['evidence/gui/login_execution.json','16 latest / 17 history; mỗi Failed latest trỏ tới ảnh thật.'],
      ['evidence/gui/admin_execution.json','28 latest / 30 history; giữ kết quả superseded và launcher bị loại.'],
      ['evidence/gui/apply_execution.json','8 latest / 8 history; giữ từng vector, fixture và request/response.'],
      ['evidence/gui/T1A_*, T1B_*, T1C_*','Playwright JSON, screenshot và attachment gốc; 26 Web Failed có ảnh local.'],
      ['evidence/gui/mobile_execution.json; T1D_MANUAL_01/','16 tiêu chí ánh xạ, 12 ảnh gốc và hash; 5 Mobile Failed có ảnh, một số ảnh đại diện nhiều vector theo lời người thực hiện.'],
      ['Task1_AI_Review.md; ai/prompt_log.md','Keep đã ghi nhận; review độc lập/audit/transcript đầy đủ còn thiếu. Prompt log hiện là bản tóm tắt PARTIAL.']],[.46,.54])
    for s in [
      'D006/D009 còn Blocked ở lưu hợp lệ và nhiều dòng; D016 đã có ảnh sau bật mạng nhưng dùng số sai miền 1912345678, còn Blocked cho oracle dữ liệu hợp lệ. D015 còn Spec-gap. Không suy persistence backend từ ảnh form; không tự sửa SUT để bỏ qua validation.',
      'Sinh viên tự review, sửa/bổ sung mục AI bỏ sót và ghi lý do. Không coi gợi ý hoặc phiếu AI tạo là đóng góp độc lập của sinh viên.',
      'Sinh viên tự viết bug report Markdown, severity và GitHub Issues kèm ảnh; khử trùng trước thống kê bug. Repository HW03 hiện chưa có remote, issue URL/Bug ID chưa có. Báo cáo này không soạn mô tả bug.',
      'Hoàn thiện transcript gốc, audit/disclosure/critique và thông tin sinh viên thật. Báo cáo hiện tại do AI tổng hợp dữ liệu thực thi; chưa phải bản sinh viên ký xác nhận.',
      'Hoàn thiện main report và PDF các tài liệu cần giữ, xuất Git log thật khi đóng gói. Task 2, Task 3 và tự chấm/ZIP chưa hoàn thành và không thuộc kết quả Task 1 ở checkpoint này.'
    ]:p(s)
    # Both formats are emitted from the same blocks, preventing summary drift.
    md=[]
    for kind,value in blocks:
        if kind=='h':md += [('' if not md else '\n')+('# 'if not md else '## ')+value,'']
        elif kind=='p':md += [value,'']
        elif kind=='t':
            headers,rows,_=value
            md += ['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
            md += ['| '+' | '.join(str(v).replace('|','/')for v in row)+' |'for row in rows]
            md += ['']
    OUT.with_suffix('.md').write_text('\n'.join(md)+'\n')
    for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
    base=ParagraphStyle('body',fontName='DV',fontSize=9,leading=13,spaceAfter=8,textColor=colors.HexColor('#243447'))
    heading=ParagraphStyle('head',parent=base,fontName='DVB',fontSize=12,leading=17,spaceBefore=10,spaceAfter=10,keepWithNext=True)
    cell=ParagraphStyle('cell',parent=base,fontSize=7.7,leading=11,spaceAfter=0)
    bold=ParagraphStyle('bold',parent=cell,fontName='DVB')
    width=A4[0]-84;story=[]
    def para(s,style=base):return Paragraph(escape(str(s)).replace('…','...'),style)
    for kind,value in blocks:
        if kind=='h':story.append(para(value,heading))
        elif kind=='p':story.append(KeepTogether([para(value)]))
        elif kind=='br':story.append(PageBreak())
        elif kind=='t':
            headers,rows,widths=value
            t=Table([[para(v,bold)for v in headers]]+[[para(v,cell)for v in row]for row in rows],
                    colWidths=[width*x for x in widths],repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E2E8F0')),
                                  ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F8FAFC')]),
                                  ('GRID',(0,0),(-1,-1),.35,colors.HexColor('#CBD5E1')),
                                  ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story += [t,Spacer(1,10)]
    def footer(c,d):
        c.setFont('DV',8);c.setFillColor(colors.HexColor('#64748B'))
        c.drawString(42,25,'HW03 Task 1 - Web + Mobile thủ công - Còn Blocked/Spec-gap')
        c.drawRightString(A4[0]-42,25,str(d.page))
    SimpleDocTemplate(str(OUT.with_suffix('.pdf')),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=42,
                      title='HW03 Task 1 - Interim GUI execution report',author='AI-assisted execution summary').build(story,onFirstPage=footer,onLaterPages=footer)
    paths=[SUB/'GUI_Checklist.xlsx',SUB/'ai/task1_initial_checklist.json']+[SUB/'evidence/gui'/f'{n}_execution.json'for n in sources]
    if mobile_path.exists():paths.append(mobile_path)
    checkpoint={'purpose':'Evidence checkpoint for interim Task 1 report, not completion approval',
                'generatedAt':datetime.now(timezone.utc).isoformat(),'counts':dict(Counter(status.values())),
                'designed':68,'executed':concluded,'scenarioRuns':55,'manualGroupedCases':8,
                'manualCriteriaRecorded':len(mobile['latest']),'failedLatestImagesPresent':failed_images,
                'workbookStatusesMatched':True,
                'sources':[{ 'path':str(p.relative_to(SUB)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in paths]}
    (SUB/'evidence/gui/task1_report_checkpoint.json').write_text(json.dumps(checkpoint,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(checkpoint['counts']))

if __name__=='__main__':main()
