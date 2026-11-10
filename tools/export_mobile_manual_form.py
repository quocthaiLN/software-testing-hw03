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
# Eight execution cases retain traceability to the original sixteen criteria.
GROUPS = [
    ('MOB-01', 'Mở hồ sơ và kiểm tra giao diện', ['001','002','010'],
     'Sau đăng nhập, mở Hồ sơ. Kiểm tra đúng tài khoản, tiêu đề/nhãn tiếng Việt; quan sát màu Cập nhật và Đăng xuất.',
     'Đúng hồ sơ; nhãn nhất quán; Cập nhật xanh dương, hành động thoát đỏ. Chưa bấm đăng xuất.'),
    ('MOB-02', 'Bố cục và bàn phím', ['003','011'],
     'Trên điện thoại thật, cuộn toàn form; mở bàn phím ở tên, điện thoại và địa chỉ, cuộn rồi đóng bàn phím.',
     'Không chồng/cắt nội dung; tiếp cận được trường đang nhập và nút Cập nhật, không mắc kẹt bởi bàn phím.'),
    ('MOB-03', 'Email chỉ đọc', ['004','005'],
     'Quan sát email; thử chạm, gõ và dán giá trị khác. Ghi email ban đầu; đối chiếu lại sau ca MOB-04.',
     'Nhận biết được email chỉ đọc; không sửa được qua GUI; email vẫn nguyên sau cập nhật các trường khác.'),
    ('MOB-04', 'Lưu hồ sơ và kiểm tra cô lập', ['013'],
     'D013: nhập bộ hồ sơ với điện thoại 0912345678, bấm Cập nhật và quan sát phản hồi; đối chiếu dữ liệu sau mở lại nếu lưu được.',
     'Có phản hồi thành công và dữ liệu được giữ khi mở lại. Không dùng số sai miền để kết luận lưu hợp lệ đạt. D006/D009 đã loại khỏi scope.') ,
    ('MOB-05', 'Biên số điện thoại', ['007'],
     'Giữ các trường khác hợp lệ. Lần lượt nhập và lưu: 091234567 (9), 0912345678 (10), 09123456789 (11), 091234567890 (12 chữ số). Ghi riêng kết quả từng giá trị.',
     '9 và 12 chữ số bị từ chối; 10 và 11 chữ số bắt đầu 0 được chấp nhận. Không bỏ hai biên hợp lệ khi gặp lỗi.'),
    ('MOB-06', 'Sai miền, thông báo lỗi và sửa lại', ['008','014','015'],
     'Kiểm tra bàn phím điện thoại; thử lưu 1912345678 và dán 09abc45678. Ghi nội dung/vị trí lỗi, sau đó sửa thành 0912345678 và lưu lại.',
     'Bàn phím thuận nhập số; cả hai dữ liệu sai miền bị từ chối; lỗi dễ hiểu, sửa và thử lại được. FR-22 yêu cầu lỗi trên nút submit; native Alert được đánh giá theo vị trí, FR-22 không bắt buộc inline.'),
    ('MOB-08', 'Đăng xuất', ['012'],
     'Thực hiện cuối cùng: quan sát nhãn Đăng xuất, chạm nút rồi thử mở lại Hồ sơ.',
     'Nhãn là Đăng xuất; phiên đã thoát không còn xem hồ sơ riêng như đang đăng nhập; có đường tới đăng nhập.')
]
INTRO = [
    'Bản rút gọn gồm 7 nhóm ca thao tác cho 13 tiêu chí Mobile active; D006/D009/D016 đã Removed. Dùng chung bước mở màn hình, nhập/lưu và quan sát để giảm thao tác lặp. Vẫn ghi kết quả theo ID gốc để đối chiếu Excel; không tính nhóm ca thành tiêu chí mới.',
    'Phiếu trống cho Android thật / Expo Go; mọi kết quả vẫn Not run. Bản AI gốc giữ nguyên; Excel có 65 mục active đã kết luận và 3 dòng Removed để truy vết; Web giữ 26 Passed / 26 Failed.',
    'Dùng các nhóm MOB-01…06 và MOB-08 (MOB-07 đã loại), đăng xuất cuối cùng. Dùng tài khoản thử; ghi môi trường và dữ liệu thực tế. Passed chỉ khi quan sát đủ kỳ vọng; Failed cần ảnh và thực tế. Các tiêu chí cùng ca có thể có kết quả khác nhau.',
    'Nếu số hợp lệ bị từ chối, vẫn thử đủ bốn vector MOB-05. D006/D009/D016 đã loại, không cần chạy lại; không dùng kết quả đó để kết luận validation hoặc lưu bằng số hợp lệ FR-04 đạt. Phần chưa thể chạy ghi Blocked và ID phụ thuộc; oracle chưa rõ ghi Spec-gap.',
    'Mỗi ghi nhận phải nêu ID gốc và vector; ảnh ví dụ GUI-D-007-phone10.png. Không tự suy kết quả mọi tiêu chí từ một lần lưu. Bug ID chỉ điền sau khi sinh viên tự viết báo cáo.',
    'Đây là bản gộp do AI theo yêu cầu giảm số ca; không phải phần sinh viên tự bổ sung. Kết quả và bằng chứng để trống cho sinh viên điền sau.'
]
ENV = ['Người thực hiện: __________', 'Ngày / giờ / múi giờ: __________',
       'Model / Android / Expo Go: __________', 'Hướng màn hình / kích thước: __________',
       'SUT commit / thay đổi local: __________', 'Tài khoản thử (không ghi mật khẩu/token): __________']
RECORD = [('Thời điểm / tiền điều kiện / input thực tế', ''),
          ('Kết quả', 'Not run'), ('Thực tế quan sát', ''),
          ('Ảnh / vector / phụ thuộc / điểm cần review', ''), ('Bug ID (nếu có)', '')]

def main():
    data=json.loads((HW/'submission/ai/task1_initial_checklist.json').read_text())
    original=[r for r in data['items'] if r['feature']=='D']
    assert len(original)==16 and all(r['status']=='Not run' for r in original)
    by_id={r['id']:r for r in original}
    covered=[f'GUI-D-{n}' for g in GROUPS for n in g[2]]
    assert len(covered)==13 and set(covered)==set(by_id)-{'GUI-D-006','GUI-D-009','GUI-D-016'}
    items=[]
    for gid,title,ids,steps,expected in GROUPS:
        rows=[by_id[f'GUI-D-{n}'] for n in ids]
        items.append(dict(id=gid,title=title,steps=steps,expected=expected,
            originals=', '.join(r['id'] for r in rows),
            source='; '.join(dict.fromkeys(r['source'] for r in rows)),
            heuristic=','.join(sorted({h.strip() for r in rows for h in r['heuristic'].split(',')}))))
    md=['# Task 1 - Phiếu ghi nhận Mobile thủ công', '', '## Hướng dẫn', '']
    md += [f'{i+1}. {s}' for i,s in enumerate(INTRO)]
    md += ['', '## Môi trường / phiên chạy', '']+[f'- {s}' for s in ENV]
    for r in items:
        md += ['', f"## {r['id']} - {r['title']}", '',
               f"**Bước / input:** {r['steps'].replace(chr(10), '<br>')}", '',
               f"**Kỳ vọng:** {r['expected']}", '',
               f"**ID gốc:** {r['originals']}", '',
               f"**Nguồn / heuristic:** {r['source']} / {r['heuristic']}", '',
               '| Trường ghi nhận | Nội dung |', '| --- | --- |']
        md += [f'| {k} | {v} |' for k,v in RECORD if k!='Kết quả']
        md += [f"| Kết quả {oid} | Not run |" for oid in r['originals'].split(', ')]
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
                  p('Kỳ vọng: '+r['expected']),p('ID gốc: '+r['originals'],small),p('Nguồn / heuristic: '+r['source']+' / '+r['heuristic'],small)]
        records=[(k,v) for k,v in RECORD if k!='Kết quả']
        records += [(oid,'Not run') for oid in r['originals'].split(', ')]
        table=Table([[p(k,small),p(v,small)] for k,v in records],colWidths=[155,width-155])
        table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(0,-1),colors.HexColor('#F0F4F8')),
                                  ('GRID',(0,0),(-1,-1),.4,colors.HexColor('#CBD5E1')),('TOPPADDING',(0,0),(-1,-1),5)]))
        story += [table,Spacer(1,14)]
    def footer(c,d):
        c.setFont('DV',8);c.setFillColor(colors.HexColor('#64748B'))
        c.drawString(42,25,'Template 13 mục active - D006/D009/D016 đã loại')
        c.drawRightString(A4[0]-42,25,str(d.page))
    SimpleDocTemplate(str(OUT.with_suffix('.pdf')),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=40,
                      title='HW03 Task 1 - Mobile manual recording form').build(story,onFirstPage=footer,onLaterPages=footer)
    print('Generated 7 groups covering 13 active criteria; no result changed.')

if __name__=='__main__':main()
