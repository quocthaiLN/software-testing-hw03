#!/usr/bin/env python3
"""Export existing planning/intake/review Markdown; do not fill student fields."""
import argparse
import json
import re
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

HW=Path(__file__).resolve().parents[1]
NAMES=['Task1_Plan','Task1_Intake','Task1_AI_Review']

def plain(value):
    s=re.sub(r'\*\*(.*?)\*\*',r'\1',str(value)).replace('`','')
    return s.translate(str.maketrans({'—':'-','–':'-','‑':'-'}))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--node',default='node');args=ap.parse_args()
    for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
    pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB',italic='DV',boldItalic='DVB')
    body=ParagraphStyle('body',fontName='DV',fontSize=9,leading=13,spaceAfter=8,textColor=colors.HexColor('#243447'))
    title=ParagraphStyle('title',parent=body,fontName='DVB',fontSize=16,leading=22,spaceAfter=13)
    heading=ParagraphStyle('heading',parent=body,fontName='DVB',fontSize=11.5,leading=16,spaceBefore=12,spaceAfter=9,keepWithNext=True)
    cell=ParagraphStyle('cell',parent=body,fontSize=7.7,leading=11,spaceAfter=0)
    bold=ParagraphStyle('bold',parent=cell,fontName='DVB')
    note=ParagraphStyle('note',parent=body,fontSize=8,leading=11,textColor=colors.HexColor('#64748B'))
    def p(s,style=body):return Paragraph(escape(plain(s)).replace('\n','<br/>'),style)
    width=A4[0]-84
    manifest=[]
    for name in NAMES:
        source=HW/'submission'/f'{name}.md'
        tokens=json.loads(subprocess.check_output([args.node,str(HW/'tools/markdown_tokens.mjs'),str(source)]))
        story=[];expected=[];table_index=0
        for tok in tokens:
            kind=tok['type']
            if kind=='space':continue
            if kind=='heading':
                expected.append(plain(tok['text']))
                story.append(p(tok['text'],title if tok['depth']==1 else heading))
                if tok['depth']==1:story.append(p('Bản PDF từ nguồn Markdown. Trạng thái trong kế hoạch/intake thuộc thời điểm thiết kế; kết quả thực thi mới xem Task1_Execution_Report.',note))
            elif kind=='paragraph':
                expected.append(plain(tok['text']));story.append(KeepTogether([p(tok['text'])]))
            elif kind=='list':
                for i,item in enumerate(tok['items']):
                    expected.append(plain(item['text']))
                    prefix=f'{int(tok.get("start") or 1)+i}. 'if tok['ordered']else '- '
                    story.append(KeepTogether([p(prefix+item['text'])]))
            elif kind=='table':
                header=[c['text']for c in tok['header']];rows=[[c['text']for c in row]for row in tok['rows']]
                expected += [plain(c)for row in [header]+rows for c in row]
                if len(header)==11 and header[0]=='Widget':
                    panels=[[0]+list(range(1,6)),[0]+list(range(6,11))]
                    for panel in panels:
                        story += [PageBreak(),p('Ma trận widget × heuristic - '+header[panel[1]]+' đến '+header[panel[-1]],heading)]
                        data=[[p(header[i],bold)for i in panel]]+[[p(row[i],cell)for i in panel]for row in rows]
                        t=Table(data,colWidths=[width*.17]+[width*.166]*5,repeatRows=1,hAlign='LEFT')
                        style_table(t);story += [t,Spacer(1,10)]
                else:
                    profiles={'Task1_Plan':[[.13,.20,.36,.31],[.25,.15,.15,.15,.15,.15],[.10,.46,.44],[.15,.26,.19,.27,.13]],
                              'Task1_Intake':[[.22,.23,.23,.32],[.17,.33,.50]],
                              'Task1_AI_Review':[[.16,.12,.18,.18,.19,.17]]}
                    fractions=profiles[name][table_index]
                    assert len(fractions)==len(header),(name,table_index)
                    data=[[p(c,bold)for c in header]]+[[p(c,cell)for c in row]for row in rows]
                    t=Table(data,colWidths=[width*x for x in fractions],repeatRows=1,hAlign='LEFT')
                    style_table(t);story += [t,Spacer(1,10)];table_index+=1
            else:raise ValueError('Unsupported Markdown token: '+kind)
        def footer(canvas,doc):
            canvas.setFont('DV',8);canvas.setFillColor(colors.HexColor('#64748B'))
            canvas.drawString(42,25,'HW03 - '+name+' - Bản sao PDF; không thêm kết quả')
            canvas.drawRightString(A4[0]-42,25,str(doc.page))
        out=source.with_suffix('.pdf')
        SimpleDocTemplate(str(out),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=42,title=name).build(story,onFirstPage=footer,onLaterPages=footer)
        manifest.append({'source':str(source),'output':str(out),'expectedText':expected})
    Path('/tmp/hw03-support-pdf-verification.json').write_text(json.dumps(manifest,ensure_ascii=False))
    print(json.dumps([{'document':Path(r['source']).stem,'textBlocks':len(r['expectedText'])}for r in manifest]))

def style_table(t):
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E2E8F0')),
                          ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F8FAFC')]),
                          ('GRID',(0,0),(-1,-1),.35,colors.HexColor('#CBD5E1')),
                          ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))

if __name__=='__main__':main()
