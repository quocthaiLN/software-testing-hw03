#!/usr/bin/env python3
"""Create an unexecuted Mobile recording form from the retained AI checklist."""
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle

HW = Path(__file__).resolve().parents[1]
OUT = HW / 'submission/Task1_Mobile_Manual_Form'
INTRO = [
    'Phiếu trống để ghi nhận kiểm thử thủ công trên Android thật / Expo Go. Không phải báo cáo kết quả. Tất cả 16 mục giữ trạng thái Not run cho đến khi có thao tác và quan sát thật.',
    'Dùng tài khoản thử của bạn. Ghi model, Android, Expo Go, hướng màn hình, thời gian và phiên bản SUT. Không dùng tài khoản hoặc thông tin cá nhân của người khác.',
    'Trước mỗi mục, đọc bước và kỳ vọng; ghi lại dữ liệu đầu vào thực sự sử dụng. Passed cần quan sát đủ toàn bộ kỳ vọng; Failed cần kết quả thực tế và ảnh. Chưa làm thì giữ Not run. Nếu bước trước chặn, ghi Blocked và ID phụ thuộc; nếu thiếu oracle, ghi Spec-gap để review.',
    'Nếu số điện thoại hợp lệ bị từ chối, vẫn thử đầy đủ bốn vector D007. Không đổi sang số sai đặc tả để gọi các mục lưu thành công là Passed. Các mục phụ thuộc lưu có thể bị chặn; ghi rõ phần nào đã thực hiện.',
    'Với D015, ghi nguyên văn thông báo và cách xuất hiện (inline/native alert). Checklist ban đầu yêu cầu sinh viên review cách áp dụng FR-22; chưa tự coi native alert là tương đương.',
    'Với D016, ghi trạng thái mạng ban đầu để khôi phục đúng sau thử nghiệm. Chỉ ngắt mạng khi đã tới được bước lưu với dữ liệu hợp lệ. Nếu validation đã chặn trước khi gọi mạng, ghi phụ thuộc thay vì tuyên bố đã thử lỗi mạng.',
    'Ảnh Failed đặt tên theo ID và vector, ví dụ GUI-D-007-phone10.png; lưu ảnh gốc. Ghi liên kết/đường dẫn ảnh ở phần kết quả. Bug ID chỉ điền sau khi sinh viên tự viết và đối chiếu bug report.',
    'Phiếu này do AI chuyển định dạng từ checklist đã Keep; không phải mục sinh viên tự bổ sung. Tích hợp lại Excel sau khi đối chiếu kết quả và ảnh; không thay thế bản AI gốc.'
]
ENV = ['Người thực hiện: __________', 'Ngày / giờ / múi giờ: __________',
       'Model / Android / Expo Go: __________', 'Hướng màn hình / kích thước: __________',
       'SUT commit / thay đổi local: __________', 'Tài khoản thử (không ghi mật khẩu/token): __________']
RECORD = [('Thời điểm / tiền điều kiện / input thực tế', ''),
          ('Kết quả', 'Not run'), ('Thực tế quan sát', ''),
          ('Ảnh / vector / phụ thuộc / điểm cần review', ''), ('Bug ID (nếu có)', '')]

def main():
    data=json.loads((HW/'submission/ai/task1_initial_checklist.json').read_text())
    items=[r for r in data['items'] if r['feature']=='D']
    assert len(items)==16 and all(r['status']=='Not run' for r in items)
    md=['# Task 1 - Phiếu ghi nhận Mobile thủ công', '', '## Hướng dẫn', '']
    md += [f'{i+1}. {s}' for i,s in enumerate(INTRO)]
    md += ['', '## Môi trường / phiên chạy', '']+[f'- {s}' for s in ENV]
    for r in items:
        md += ['', f"## {r['id']} - {r['title']}", '',
               f"**Bước / input theo checklist:** {r['steps']}", '',
               f"**Kỳ vọng:** {r['expected']}", '',
               f"**Nguồn / heuristic:** {r['source']} / {r['heuristic']}", '',
               '| Trường ghi nhận | Nội dung |', '| --- | --- |']
        md += [f'| {k} | {v} |' for k,v in RECORD]
    OUT.with_suffix('.md').write_text('\n'.join(md)+'\n')
    for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
    body=ParagraphStyle('body',fontName='DV',fontSize=9,leading=13,spaceAfter=6,textColor=colors.HexColor('#243447'))
    title=ParagraphStyle('title',parent=body,fontName='DVB',fontSize=17,leading=22,spaceAfter=12)
    head=ParagraphStyle('head',parent=body,fontName='DVB',fontSize=11,leading=15,spaceAfter=8)
    small=ParagraphStyle('small',parent=body,fontSize=8,leading=11)
    p=lambda s,style=body:Paragraph(escape(s).replace('\n','<br/>'),style)
    width=A4[0]-84
    story=[p('Task 1 - Phiếu Mobile thủ công',title)]
    story += [p(f'{i+1}. {s}') for i,s in enumerate(INTRO)]
    story += [Spacer(1,8),p('Môi trường / phiên chạy',head)]+[p(s) for s in ENV]
    for i,r in enumerate(items):
        if i%2==0:story.append(PageBreak())
        story += [p(f"{r['id']} - {r['title']}",head),p('Bước / input: '+r['steps']),
                  p('Kỳ vọng: '+r['expected']),p('Nguồn / heuristic: '+r['source']+' / '+r['heuristic'],small)]
        table=Table([[p(k,small),p(v,small)] for k,v in RECORD],colWidths=[155,width-155],rowHeights=[30,22,48,35,22])
        table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(0,-1),colors.HexColor('#F0F4F8')),
                                  ('GRID',(0,0),(-1,-1),.4,colors.HexColor('#CBD5E1')),('TOPPADDING',(0,0),(-1,-1),5)]))
        story += [table,Spacer(1,18)]
    def footer(c,d):
        c.setFont('DV',8);c.setFillColor(colors.HexColor('#64748B'))
        c.drawString(42,25,'Phiếu trống - chưa có kết quả Mobile')
        c.drawRightString(A4[0]-42,25,str(d.page))
    SimpleDocTemplate(str(OUT.with_suffix('.pdf')),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=40,
                      title='HW03 Task 1 - Mobile manual recording form').build(story,onFirstPage=footer,onLaterPages=footer)
    print('Generated blank Markdown/PDF form for 16 items; no result changed.')

if __name__=='__main__':main()
