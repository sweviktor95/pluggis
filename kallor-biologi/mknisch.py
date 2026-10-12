import sys
sys.path.insert(0,'/tmp/figs')
from svgkit import *
W,H=900,400
b=title(W,"Samma gran – olika nischer",y=36)
cx=250
t=rect(cx-14,255,28,120,"#7a5a3a")
for yy,ww in [(105,60),(150,90),(200,120),(250,150)]:
    t+=f'<polygon points="{cx},{yy-55} {cx-ww},{yy+25} {cx+ww},{yy+25}" fill="#3f7d4f"/>'
t+=f'<ellipse cx="{cx+118}" cy="262" rx="42" ry="20" fill="#f2c744" opacity=".5" stroke="#c9a026" stroke-width="2.5" stroke-dasharray="6 5"/>'
t+=f'<ellipse cx="{cx}" cy="325" rx="30" ry="46" fill="#ec9248" opacity=".5" stroke="#c4701f" stroke-width="2.5" stroke-dasharray="6 5"/>'
def bird(x,y,col):
    return (f'<ellipse cx="{x}" cy="{y}" rx="15" ry="10" fill="{col}"/><circle cx="{x+12}" cy="{y-7}" r="7" fill="{col}"/>'
            f'<polygon points="{x+18},{y-8} {x+27},{y-5} {x+18},{y-3}" fill="#e0782f"/><polygon points="{x-13},{y} {x-28},{y+5} {x-13},{y+6}" fill="{col}"/>'
            f'<circle cx="{x+14}" cy="{y-9}" r="1.6" fill="#fff"/>')
t+=bird(cx+122,260,"#e3b32c")+bird(cx+4,325,"#7a4a22")
lab=box(500,80,360,100,["Kungsfågel","Söker småkryp ytterst på grenarna","Nisch: grenspetsarna"],fill="#fbeab0",size=17)
lab+=box(500,205,360,100,["Trädkrypare","Klättrar på stammen och plockar","insekter ur barken. Nisch: stammen"],fill="#f9d9bc",size=17)
lab+=text(680,350,"Olika nischer → mindre konkurrens → fler arter får plats",16,"#24503f",weight="700")
lab+=line(cx+170,255,500,150,"#c9a026",2.5,True)+line(cx+34,325,500,265,"#c4701f",2.5,True)
open('/tmp/bio/fig/ekologi-nisch.svg','w').write(fig(W,H,b+t+lab,"Nischer i en gran"))
