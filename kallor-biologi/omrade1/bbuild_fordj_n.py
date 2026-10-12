# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0,'/tmp/bio')
import bbuild_n as B
from bbuild_n import *
import importlib, os
M = importlib.import_module('ch'+os.environ.get('CH','04')+'_fordj')
from pypdf import PdfReader, PdfWriter

def first(pages):
    h = B.first_page(M, 'fordjupning', pages)
    h = h.replace('DET HÄR SKA DU LÄRA DIG', M.MAL_RUBRIK).replace(f'Kapitel {M.NR} · {M.NAMN}', f'Fördjupning {M.NR} · {M.NAMN}')
    return h

body = "".join(f'<section class="sec m{i}">{head(nr, t)}{inner}</section>' for i, (nr, t, inner) in enumerate(M.S, 1)) + M.uppg_html()
FOOT = f'Fördjupning {M.NR} · {M.NAMN}'
tmp = f'{OUT}/_fordj_body.pdf'
html_to_pdf(doc(body, FOOT, 2, tab=M.TAB, extra=B.named_foot_css(getattr(M,'FOOTS',[]))), tmp)
texts = page_texts(tmp)
def find(s):
    for i, t in enumerate(texts):
        if s in re.sub(r"\s+", " ", t[:400].replace("ﬂ","fl").replace("ﬁ","fi")): return i + 2
    return '?'
pages = [(nr, t, find(t)) for nr, t, _ in M.S]
a = find('Resonera och ta ställning'); pages.append(('', 'Resonera och ta ställning', f'{a}–{len(texts)+1}'))
p1 = f'{OUT}/_fordj_p1.pdf'
html_to_pdf(first(pages), p1)
def merge(files, name):
    w = PdfWriter()
    for f in files:
        for pg in PdfReader(f).pages: w.add_page(pg)
    w.write(name)
n1 = f'{OUT}/biologi-{M.NR}-{M.SLUG}-fordjupning.pdf'
merge([p1, tmp], n1)
t2 = f'{OUT}/_fordj_teacher.pdf'
html_to_pdf(doc(M.teacher_html(), FOOT, len(texts)+2, tab=M.TAB), t2)
merge([n1, t2], f'{OUT}/biologi-{M.NR}-{M.SLUG}-fordjupning-komplett.pdf')
print(pages)
