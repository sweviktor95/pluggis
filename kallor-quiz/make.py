# -*- coding: utf-8 -*-
import csv, random, re, sys, os, openpyxl
sys.path.insert(0,'/tmp/quiz')
from quizdata_bio import BIO
U='/root/.claude/uploads/55aa85b1-9b1a-5dfc-9495-7885cc4fcabd/'
TB=U+'04a76440-Blooket_Spreadsheet_Import_Template.xlsx'; TK=U+'5a8a1dc0-KahootQuizTemplate.xlsx'
R='/home/claude/pluggis/'
# kemi 1: första svaret är rätt i gamla CSV:n
K={}
rows=list(csv.reader(open(R+'planering/kemi-omrade1/kemi-1-blooket.csv',encoding='utf-8')))[1:]
K[1]=[(r[1],r[2],[x for x in r[3:6] if x],int(r[6])) for r in rows]
src=open('/home/claude/pluggis/kallor-quiz/kemi2_fragor.py',encoding='utf-8').read()
ns={}; exec(src[src.index('Q = ['):src.index('rows=[[')],ns)
K[2]=[(q,r,w,30 if q.startswith('Ett ') else 20) for q,r,w in ns['Q']]
SETS={('biologi',n):v for n,v in BIO.items()}; SETS.update({('kemi',n):v for n,v in K.items()})
KT=lambda t: t if t in (5,10,20,30,60,90,120,240) else min([x for x in (5,10,20,30,60,90,120,240) if x>=t] or [240])
def shuffled(qs,seed):
    rnd=random.Random(seed); out=[]; pos=[]
    for i,(q,r,w,t) in enumerate(qs):
        a=[r]+list(w); 
        # jämn fördelning av rätt svarsplats
        p=i%4 if len(a)==4 else rnd.randrange(len(a))
        others=a[1:]; rnd.shuffle(others)
        ans=others[:p]+[r]+others[p:]
        out.append((q,ans,t,p+1))
    return out
for (amne,n),qs in SETS.items():
    assert len(qs)>=15
    sh=shuffled(qs,hash((amne,n))%1000+7)
    for q,ans,t,c in sh:
        assert len(q)<=120,(q,len(q)); assert all(len(a)<=75 for a in ans),ans; assert len(set(ans))==len(ans)
    d=R+f'planering/{amne}-omrade{n}/'
    wb=openpyxl.load_workbook(TB); ws=wb.worksheets[0]
    for r in range(3,5):
        for c in range(2,9): ws.cell(r,c).value=None
    for i,(q,ans,t,c) in enumerate(sh):
        r=3+i; ws.cell(r,2).value=q
        for j in range(4): ws.cell(r,3+j).value=ans[j] if j<len(ans) else None
        ws.cell(r,7).value=t; ws.cell(r,8).value=c
    wb.save(d+f'{amne}-{n}-blooket.xlsx')
    wb=openpyxl.load_workbook(TK); ws=wb.worksheets[0]
    for c in range(2,9): ws.cell(9,c).value=None
    for i,(q,ans,t,c) in enumerate(sh):
        r=9+i; ws.cell(r,2).value=q
        for j in range(4): ws.cell(r,3+j).value=ans[j] if j<len(ans) else None
        ws.cell(r,7).value=KT(t); ws.cell(r,8).value=str(c)
    wb.save(d+f'{amne}-{n}-kahoot.xlsx')
    print(amne,n,len(sh))
