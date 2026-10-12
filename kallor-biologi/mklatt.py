import sys
sys.path.insert(0,'/tmp/figs')
from svgkit import *
G1="#2f6b4f"
def panel(w,h,body,bg="#eaf3ec"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="Carlito, sans-serif"><rect width="{w}" height="{h}" rx="22" fill="{bg}"/>{body}<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#2f6b4f"/></marker></defs></svg>'
def tree(x,y,s=1,c="#3f7d4f"):
    return (f'<rect x="{x-4*s}" y="{y}" width="{8*s}" height="{18*s}" fill="#7a5a3a"/>'
            f'<polygon points="{x},{y-48*s} {x-22*s},{y-8*s} {x+22*s},{y-8*s}" fill="{c}"/>'
            f'<polygon points="{x},{y-30*s} {x-28*s},{y+6*s} {x+28*s},{y+6*s}" fill="{c}"/>')
def card(x,w,h,icon,cap,sub):
    return (f'<rect x="{x}" y="30" width="{w}" height="{h-60}" rx="18" fill="#fff"/>{icon}'
            f'<text x="{x+w/2}" y="{h-100}" font-size="30" font-weight="700" text-anchor="middle" fill="#24323c">{cap}</text>'
            f'<text x="{x+w/2}" y="{h-68}" font-size="22" text-anchor="middle" fill="#5d6b75">{sub}</text>')
# ---- Del 7: tre hot
W,H=1500,380
cw=450
ic1=(f'<circle cx="{25+cw/2}" cy="150" r="75" fill="#eaf3ec"/>'
     f'<rect x="{25+cw/2-9}" y="95" width="18" height="90" rx="9" fill="#fff" stroke="#9aa" stroke-width="3"/>'
     f'<circle cx="{25+cw/2}" cy="195" r="20" fill="#c64f3f"/><rect x="{25+cw/2-6}" y="110" width="12" height="85" rx="6" fill="#c64f3f"/>'
     f'<polygon points="{25+cw/2+50},120 {25+cw/2+70},90 {25+cw/2+90},120" fill="#c64f3f"/><rect x="{25+cw/2+62}" y="118" width="16" height="36" fill="#c64f3f"/>')
ic2=('<circle cx="750" cy="150" r="75" fill="#eaf3ec"/>'+tree(715,160,1.1)+tree(755,170,0.9)
     +'<rect x="780" y="150" width="34" height="24" rx="3" fill="#7a5a3a"/><ellipse cx="797" cy="150" rx="17" ry="6" fill="#c9a574"/>'
     +'<rect x="795" y="115" width="30" height="30" fill="#d9a06a"/><polygon points="790,115 810,97 830,115" fill="#a85a3a"/>')
ic3=''
cx=1275-100
ic3+=f'<circle cx="{cx}" cy="150" r="46" fill="#dce9f2"/><circle cx="{cx-14}" cy="142" r="7" fill="#3b7ba8"/><circle cx="{cx+10}" cy="162" r="7" fill="#3b7ba8"/>'
ic3+=f'<line x1="{cx+52}" y1="150" x2="{cx+108}" y2="150" stroke="#2f6b4f" stroke-width="6" marker-end="url(#ah)"/>'
cx2=cx+190
ic3+=f'<circle cx="{cx2}" cy="150" r="70" fill="#f6e1da"/>'
import random
random.seed(3)
pts=[(-30,-20),(10,-35),(35,-5),(-5,0),(-35,18),(18,28),(-10,40),(40,30),(-20,-45),(5,15)]
for i,(dx,dy) in enumerate(pts):
    ic3+=f'<circle cx="{cx2+dx}" cy="{150+dy}" r="8" fill="{"#c64f3f" if i%3 else "#3f7d4f"}"/>'
body=card(25,cw,H,ic1,"Varmare klimat","Arter flyttar norrut")+card(525,cw,H,ic2,"Livsmiljö försvinner","Skog blir åker och hus")+card(1025,cw,H,ic3,"Ny art kommer","Människan tar med den")
open('fig/l_hot.svg','w').write(panel(1500,380,body))
# ---- Del 8: lagom
cw=450
s1=tree(100+0,170,1.3)+tree(150,180,1.0)+'<rect x="200" y="170" width="38" height="26" rx="3" fill="#7a5a3a"/><ellipse cx="219" cy="170" rx="19" ry="7" fill="#c9a574"/>'
ic1=f'<g transform="translate({25+cw/2-170},0)">{s1}</g>'
w=''
for i in range(7):
    x=25+cw/2+500-130+i*0 
ic2='<g>'
bx=525+cw/2-85
for i in range(8):
    ic2+=f'<line x1="{bx+i*24}" y1="190" x2="{bx+i*24}" y2="115" stroke="#c9a026" stroke-width="5"/><ellipse cx="{bx+i*24}" cy="105" rx="7" ry="16" fill="#e3b32c"/>'
ic2+=f'<rect x="{bx-20}" y="192" width="{8*24+28}" height="12" rx="6" fill="#7a5a3a"/></g>'
fx=1025+cw/2
ic3=(f'<ellipse cx="{fx}" cy="150" rx="70" ry="32" fill="#8bbd6b"/><polygon points="{fx+62},150 {fx+105},118 {fx+105},182" fill="#8bbd6b"/>'
     f'<circle cx="{fx-40}" cy="142" r="6" fill="#24323c"/><path d="M{fx-120},205 q30,-14 60,0 t60,0 t60,0 t60,0" fill="none" stroke="#3b7ba8" stroke-width="5"/>')
H=470
body=card(25,cw,H,ic1,"Skog","Virke och papper")+card(525,cw,H,ic2,"Åker","Mat")+card(1025,cw,H,ic3,"Fiske","Fisk")
body+=f'<rect x="25" y="{H-56}" width="1450" height="42" rx="21" fill="{G1}"/><text x="750" y="{H-27}" font-size="26" font-weight="700" fill="#fff" text-anchor="middle">Ta ut lagom: inte mer än naturen hinner växa tillbaka</text>'
open('fig/l_lagom.svg','w').write(panel(1500,470,body,"#f6f1e3"))
