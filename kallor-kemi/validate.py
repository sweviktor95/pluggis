# -*- coding: utf-8 -*-
import sys, importlib, re
sys.path.insert(0,'/tmp/kemi')
name=sys.argv[1]; m=importlib.import_module(name)
err=[]
def need(c,msg):
    if not c: err.append(msg)
for k in "T S UPPG BEGREPP SAMMAN TEST_A TEST_B KALLA SKRIV LAB LARAR KALLOR F F_UPPG F_SAMMAN F_BEGR BLOOKET JEOPARDY GRUPPER SCEN".split():
    need(hasattr(m,k),"saknar "+k)
if err: print("\n".join(err)); sys.exit(1)
T=m.T
for k in "nr namn under fil arskurs nodeid mal fundera".split(): need(k in T,"T."+k)
need(re.match(r"kemi-\d\d-",T.get("fil","")),"T.fil ska börja kemi-NN-")
need(T.get("arskurs") in ("7–9",),"arskurs ska vara \"7–9\"")
need(len(T.get("mal",[]))>=6,"mal 6+")
BL={"p","tab","ruta","list","tidslinje","kalla","bild","kolla"}
scenes=open('/tmp/kemi/SCENES.txt').read().split(":")[1].replace("\n","").split(",")
scenes=[s.strip() for s in scenes]
assets=[a.strip() for a in open('/tmp/kemi/ASSETS.txt').read().split("):")[1].split("\n")[0].split(",")]
def chk_sec(s,pre):
    for k in "id nr ikon titel intro block svar".split(): need(k in s,pre+" saknar "+k)
    ks=[b for b in s.get("block",[]) if b[0]=="kolla"]
    need(len(ks)==1,pre+": exakt ett kolla-block")
    if ks: need(len(ks[0][1])==len(s.get("svar",[])),pre+": svar != kolla")
    for b in s.get("block",[]):
        need(b[0] in BL,pre+": okänt block "+str(b[0]))
        if b[0]=="ruta": need(b[1] in("visste","fakta","tank","historia","exempel"),pre+": ruta-typ")
        if b[0]=="bild": need(b[1] in scenes,pre+": okänd scen "+str(b[1]))
        if b[0]=="tidslinje": need(3<=len(b[1])<=10,pre+": tidslinje 3–10 poster")
    words=len(re.sub(r"<[^>]+>"," "," ".join(str(b[1:]) for b in s["block"])).split())
    need(words>=110,pre+f": för kort ({words} ord)")
S=m.S; need(6<=len(S)<=8,f"6–8 sektioner (har {len(S)})")
for s in S: chk_sec(s,"S "+s.get("id","?"))
need(len(m.F)>=3,"F 3+ sektioner")
for s in m.F: chk_sec(s,"F "+s.get("id","?"))
ids=[s["id"] for s in S]; need(len(set(ids))==len(ids),"dubbla id")
g=[i for _,_,_,l in m.GRUPPER for i in l]
need(sorted(g)==sorted(ids),"GRUPPER ska täcka alla S-id exakt en gång")
need(3<=len(m.GRUPPER)<=4,"3–4 grupper")
need(len(m.UPPG)>=8,"UPPG 8+")
for u in m.UPPG: need(len(u)==5,"UPPG-tuple 5 element")
need(len(m.F_UPPG)>=4,"F_UPPG 4+")
need(len(m.BEGREPP)>=12,"BEGREPP 12+"); need(len(m.SAMMAN)>=6,"SAMMAN 6+")
need(len(m.TEST_A)==8,"TEST_A 8")
for q,o,i in m.TEST_A: need(len(o)==4 and 0<=i<4,"TEST_A format")
need(len(m.TEST_B)==6,"TEST_B 6")
need(len(m.KALLA.get("fragor",[]))>=3,"KALLA 3+ frågor")
need(len(m.SKRIV.get("stod",[]))==3,"SKRIV.stod 3")
for k in "titel syfte material utforande fragor bonus".split(): need(m.LAB.get(k),"LAB."+k)
need(len(m.LARAR)>=4,"LARAR 4+")
need(len(m.KALLOR)>=6 and all(u.startswith("http") for _,u in m.KALLOR),"KALLOR 6+ med http")
need(len(m.BLOOKET)>=24,"BLOOKET 24+")
for q in m.BLOOKET: need(len(q)==5 and len(q[0])<=300 and all(len(a)<=80 for a in q[1:]),"BLOOKET format/längd: "+str(q)[:40])
need(len(m.JEOPARDY)==5,"JEOPARDY 5 kategorier")
for c,l in m.JEOPARDY.items(): need([p for p,_,_ in l]==[100,200,300,400,500],"JEOPARDY poäng "+c)
sc=m.SCEN
need(sc is None,"SCEN ska vara None i kemi")
if sc is not None:
    for k in "titel plats tid sky mark walker etapper diskutera".split(): need(k in sc,"SCEN."+k)
    need(sc.get("walker",{}).get("typ") in("bonde","soldat","handlare","arbetare","medborgare","sjoman","resenar"),"walker.typ")
    need(len(sc.get("etapper",[]))==7,"SCEN 7 etapper")
    for i,e in enumerate(sc.get("etapper",[])):
        for k in "x_etikett tid plats rubrik fakta deko".split(): need(k in e,f"etapp {i}: {k}")
        if i<6:
            for k in "fraga alt ratt forklaring".split(): need(k in e,f"etapp {i}: {k}")
            need(len(e.get("alt",[]))==3 and 0<=e.get("ratt",9)<3,f"etapp {i}: 3 alt/ratt")
        for d in e.get("deko",[]): need(d[0] in assets,f"etapp {i}: okänt asset {d[0]}")
if err: print("\n".join(err)); sys.exit(1)
print("OK",name,"sektioner",len(S),"ord ca",sum(len(re.sub(r'<[^>]+>',' ',str(s['block'])).split()) for s in S))
