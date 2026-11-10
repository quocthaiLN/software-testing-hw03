#!/usr/bin/env python3
"""Print the preserved initial checklist without adding review or test results."""
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, PageBreak,
)

HW = Path(__file__).resolve().parents[1]
SOURCE = HW / 'submission/ai/task1_initial_checklist.json'
MARKDOWN = HW / 'submission/ai/task1_initial_checklist.md'
OUTPUT = HW / 'submission/ai/task1_initial_checklist.pdf'
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')


def text(value):
    """Plain Markdown presentation only; do not alter checklist meaning."""
    value = re.sub(r'\*\*(.*?)\*\*', r'\1', str(value))
    value = value.replace('`', '')
    value = value.translate(str.maketrans({'—': '-', '–': '-', '‑': '-'}))
    return escape(value).replace('\n', '<br/>')


def main():
    data = json.loads(SOURCE.read_text())
    assert len(data['items']) == 68
    assert all(r['status'] == 'Not run' for r in data['items'])
    pdfmetrics.registerFont(TTFont('DV', str(FONT_DIR / 'DejaVuSans.ttf')))
    pdfmetrics.registerFont(TTFont('DV-Bold', str(FONT_DIR / 'DejaVuSans-Bold.ttf')))
    base = ParagraphStyle('body', fontName='DV', fontSize=9.5, leading=14,
                          textColor=colors.HexColor('#243447'), alignment=TA_LEFT,
                          spaceAfter=7)
    title = ParagraphStyle('title', parent=base, fontName='DV-Bold',
                           fontSize=19, leading=25, spaceAfter=15)
    heading = ParagraphStyle('heading', parent=base, fontName='DV-Bold',
                             fontSize=13, leading=18, spaceBefore=10,
                             spaceAfter=9, keepWithNext=True)
    card = ParagraphStyle('card', parent=base, fontName='DV-Bold',
                          fontSize=10, leading=15, spaceAfter=4)
    small = ParagraphStyle('small', parent=base, fontSize=8.5, leading=12)
    label = ParagraphStyle('label', parent=base, fontName='DV-Bold',
                           fontSize=8.5, leading=12)
    page_width, page_height = A4
    margin = 42
    width = page_width - 2 * margin
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4,
                            leftMargin=margin, rightMargin=margin,
                            topMargin=46, bottomMargin=43,
                            title='HW03 Task 1 - Checklist AI bản đầu',
                            author='Codex - initial AI draft')
    story = []
    # Reproduce all introductory Markdown content before the feature tables.
    intro = MARKDOWN.read_text().split('\n## A -')[0]
    if '\n## A —' in intro:
        intro = intro.split('\n## A —')[0]
    for line in intro.splitlines():
        if not line.strip():
            continue
        if line.startswith('# '):
            story.append(Paragraph(text(line[2:]), title))
        elif line.startswith('## '):
            story.append(Paragraph(text(line[3:]), heading))
        else:
            story.append(Paragraph(text(line), base))
    names = {'A': 'Web Login - FR-02',
             'B': 'Web Checkout: Coupon - FR-09',
             'C': 'Admin Coupons - FR-17',
             'D': 'Mobile Profile - FR-04'}
    for feature, name in names.items():
        story.extend([PageBreak(), Paragraph(f'{feature}. {name}', heading)])
        for r in (x for x in data['items'] if x['feature'] == feature):
            fields = [
                ('IA / Widget', f"{r['ia']} / {r['widget']}"),
                ('Phase', r['phase']),
                ('Bước / input', r['steps']),
                ('Kỳ vọng', r['expected']),
                ('Nguồn', r['source']),
                ('Heuristic', r['heuristic']),
                ('Kết quả', r['status']),
            ]
            table = Table([[Paragraph(text(k), label), Paragraph(text(v), base)]
                           for k, v in fields], colWidths=[86, width - 86],
                          hAlign='LEFT')
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 7),
                ('RIGHTPADDING', (0, 0), (-1, -1), 7),
                ('TOPPADDING', (0, 0), (-1, -1), 3),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F0F4F8')),
                ('LINEBELOW', (0, -1), (-1, -1), .5,
                 colors.HexColor('#CBD5E1')),
            ]))
            story.append(KeepTogether([
                Paragraph(text(f"{r['id']}  {r['title']}"), card),
                table, Spacer(1, 12),
            ]))

    def footer(canvas, document):
        canvas.saveState()
        canvas.setFont('DV', 8)
        canvas.setFillColor(colors.HexColor('#64748B'))
        canvas.drawString(margin, page_height - 28,
                          'HW03 Task 1 - Initial AI draft - Pending student review')
        canvas.drawString(margin, 25, 'Not run - chưa có kết quả thực thi GUI')
        canvas.drawRightString(page_width - margin, 25, str(document.page))
        canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == '__main__':
    main()
