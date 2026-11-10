#!/usr/bin/env python3
"""Render current Markdown drafts read-only, preserving hand edits and Disclosure."""
import json,re,subprocess
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak
HW=Path(__file__).resolve().parents[1]
NODE='/home/le-nguyen-quoc-thai/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node'
for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
body=ParagraphStyle('body',fontName='DV',fontSize=9,leading=12.5,spaceAfter=7)
head=ParagraphStyle('head',parent=body,fontName='DVB',fontSize=11.5,leading=15,spaceBefore=9,spaceAfter=8,keepWithNext=True)
cell=ParagraphStyle('cell',parent=body,fontSize=8,leading=11,spaceAfter=0)
chain=ParagraphStyle('chain',parent=body,keepWithNext=True)
def plain(s):
 return re.sub(r'\*\*(.*?)\*\*',r'\1',str(s)).replace('`','')
def p(s,style=body):
 if style is body and str(s).startswith(('(1) Prompt','(2) AI Output','(3) Verdict','(4) Reasoning')):style=chain
 return Paragraph(escape(plain(s)).replace('\n','<br/>'),style)
def footer(c,d):
 c.setFont('DV',8);c.setFillColor(colors.HexColor('#64748B'));c.drawString(42,25,'HW03 - Bản dự thảo - Chưa phát hành');c.drawRightString(A4[0]-42,25,str(d.page))
verification=[]
for name in ['Task1_AI_Assistance_Draft','Task1_Bug_Report_AI_Draft']:
 source=HW/'submission/ai/drafts'/f'{name}.md'
 tokens=json.loads(subprocess.check_output([NODE,str(HW/'tools/markdown_tokens.mjs'),str(source)]))
 story=[];expected=[]
 for token in tokens:
  kind=token['type']
  if kind=='space':continue
  if kind=='heading':
   text=token['text']
   newpage=(name=='Task1_Bug_Report_AI_Draft' and text.startswith('AI-DRAFT-')) or (name=='Task1_AI_Assistance_Draft' and re.match(r'^[2345]\. (AI Audit Report|AI Critique|AI Use Disclosure Form|Bug report worksheet)',text))
   if newpage:story.append(PageBreak())
   story.append(p(text,head));expected.append(plain(text))
  elif kind=='paragraph':
   text=token['text']
   if re.search(r'!\[[^\]]*\]\(',text):
    # Originals remain linked/retained in Markdown and local evidence directories.
    for label in re.findall(r'!\[([^\]]*)\]\(',text):story.append(p('Ảnh gốc: '+label))
   else:story.append(p(text));expected.append(plain(text))
  elif kind=='list':
   for i,item in enumerate(token['items']):
    text=item['text'];prefix=(str(int(token.get('start')or 1)+i)+'. ')if token['ordered']else '- '
    story.append(p(prefix+text));expected.append(plain(text))
  elif kind=='table':
   header=[x['text'] for x in token['header']];rows=[[x['text']for x in row]for row in token['rows']]
   assert len(header)==2
   expected += [plain(x) for row in [header]+rows for x in row]
   table=Table([[p(x,cell) for x in header]]+[[p(x,cell)for x in row]for row in rows],colWidths=[170,A4[0]-84-170],repeatRows=1)
   table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E2E8F0')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#CBD5E1')),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story +=[table,Spacer(1,8)]
  else:raise ValueError('Unsupported token '+kind)
 SimpleDocTemplate(str(source.with_suffix('.pdf')),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=45).build(story,onFirstPage=footer,onLaterPages=footer)
 verification.append(dict(source=str(source),pdf=str(source.with_suffix('.pdf')),expected=expected))
Path('/tmp/task1-draft-pdf-verification.json').write_text(json.dumps(verification,ensure_ascii=False))
print('Rendered both current Markdown drafts without rewriting source.')
