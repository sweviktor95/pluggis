import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Wedge
from matplotlib import font_manager as fm
plt.rcParams['font.family']='Carlito'
OUT='/tmp/kem/fig01k/'
N=["Merkurius","Venus","Jorden","Mars","Jupiter","Saturnus","Uranus","Neptunus"]
D=[4879,12104,12742,6779,139820,116460,50724,49244]
A=[57.9,108.2,149.6,227.9,778.6,1433.5,2872.5,4495.1]  # miljoner km
SUN=1392700
COL=["#9a9a9a","#e3c07a","#3f7fd0","#c8553a","#d9a066","#e6cf94","#8fd3d8","#4a63d6"]

# ---------- bild 1: allt i skala (svart)
W,H=2000,520
img=np.zeros((H,W))
x0=60; ppk=(1900-x0)/(A[-1]*1e6)
def dot(cx,cy,dkm):
    r=dkm*ppk/2; area=np.pi*r*r
    ix=int(round(cx)); iy=int(round(cy))
    img[iy-1:iy+2, ix-1:ix+2]+=0  # placeholder
    img[iy,ix]=min(1.0,img[iy,ix]+area)   # pixel lyser i proportion till sin verkliga area
cy=200
dot(x0,cy,SUN)
for a,d in zip(A,D): dot(x0+a*1e6*ppk,cy,d)
fig=plt.figure(figsize=(W/200,H/200),dpi=200,facecolor='black')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(H,0); ax.axis('off'); ax.set_facecolor('black')
ax.imshow(img,cmap='gray',vmin=0,vmax=1,extent=(0,W,H,0),interpolation='nearest',aspect='auto')
# etiketter
def lab(x,txt,lvl,col='#bbbbbb'):
    y=cy+38+lvl*30
    ax.plot([x,x],[cy+10,y-14],color='#555',lw=.6)
    ax.text(x,y,txt,color=col,ha='center',va='top',fontsize=8)
pos=[x0]+[x0+a*1e6*ppk for a in A]
names=["Solen"]+N
lv=[0,1,2,3,4,0,1,0,1]
for x,n,l in zip(pos,names,lv): lab(x,n,l)
# skalstock
sb=1000e6*ppk
ax.plot([x0,x0+sb],[470,470],color='#888',lw=1)
ax.plot([x0,x0],[464,476],color='#888',lw=1);ax.plot([x0+sb,x0+sb],[464,476],color='#888',lw=1)
ax.text(x0+sb/2,458,"1 miljard km",color='#888',ha='center',va='bottom',fontsize=8)
ax.text(W-40,500,"Solen är här mindre än en halv pixel bred.",color='#666',ha='right',fontsize=7.5)
fig.savefig(OUT+'sol_skala.png',facecolor='black'); plt.close(fig)

# ---------- bild 2: Solen och planeterna sida vid sida, rätt storleksförhållande
W,H=2000,1400
fig=plt.figure(figsize=(W/200,H/200),dpi=200,facecolor='white')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(H,0); ax.axis('off')
SD=1300; k=SD/SUN; cy=H/2-20
ax.add_patch(Circle((30+SD/2,cy),SD/2,fc='#f5b83a',ec='none'))
ax.text(30+SD/2,cy,"Solen\n1 392 700 km",ha='center',va='center',fontsize=26,weight='bold',color='#5a3a00',linespacing=1.3)
x=30+SD+30; gap=18
cxs=[]
for i,(n,d,c) in enumerate(zip(N,D,COL)):
    r=d*k/2; cx=x+r
    ax.add_patch(Circle((cx,cy),r,fc=c,ec='none')); cxs.append((cx,r))
    x+=2*r+gap
# nummer ovanför/under med streck
for i,(cx,r) in enumerate(cxs):
    up=(i%2==0)
    y=cy-r-70-(i//2)*0 if up else cy+r+70
    ax.plot([cx,cx],[cy-r-4 if up else cy+r+4, y+(26 if up else -26)],color='#999',lw=.8)
    ax.text(cx,y,str(i+1),ha='center',va='center',fontsize=19,weight='bold',color='#222')
# teckenförklaring
ly=cy+260
ax.text(1400,ly-70,"Planeterna (diameter)",fontsize=22,weight='bold',color='#222',va='center')
for i,(n,d,c) in enumerate(zip(N,D,COL)):
    yy=ly+i*56
    ax.add_patch(Circle((1425,yy),14,fc=c,ec='none'))
    ax.text(1455,yy,f"{i+1}  {n}",fontsize=20,va='center',color='#222')
    ax.text(1990,yy,f"{d:,}".replace(',',' ')+" km",fontsize=20,va='center',ha='right',color='#555')
fig.savefig(OUT+'sol_storlek.png',facecolor='white'); plt.close(fig)

# ---------- bild 3: utjämnade storlekar (som i vanliga bilder)
W,H=2000,640
fig=plt.figure(figsize=(W/200,H/200),dpi=200,facecolor='#0b1030')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(H,0); ax.axis('off')
rng=np.random.default_rng(3)
ax.scatter(rng.uniform(0,W,160),rng.uniform(0,H,160),s=rng.uniform(.3,2.2,160),c='white',alpha=.6,lw=0)
cy=300
ax.add_patch(Wedge((0,cy),210,-90,90,fc='#f5b83a',ec='none'))
xs=np.linspace(330,1900,8)
Rm=[16,24,26,19,62,52,38,37]
for n,xx,r,c in zip(N,xs,Rm,COL):
    ax.add_patch(Circle((xx,cy),r,fc=c,ec='none'))
    if n=="Saturnus":
        ax.add_patch(Ellipse((xx,cy),r*3.0,r*0.7,fc='none',ec='#d8c28a',lw=1.6))
    ax.text(xx,cy+78,n,ha='center',va='top',fontsize=8.5,color='white')
ax.text(110,cy+235,"Solen",ha='center',va='top',fontsize=8.5,color='#f5b83a')
ax.text(W/2,40,"Så brukar solsystemet ritas: storlekar och avstånd är utjämnade",ha='center',va='top',fontsize=11,weight='bold',color='white')
fig.savefig(OUT+'sol_modell.png',facecolor='#0b1030'); plt.close(fig)
