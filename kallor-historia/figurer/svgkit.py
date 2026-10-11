# -*- coding: utf-8 -*-
"""Liten verktygslåda för förklarande SVG-figurer (stil som biologibokens diagram)."""
from xml.sax.saxutils import escape as esc
INK="#24323c"; MUTED="#5d6b75"; BG="#faf6ec"
GREEN="#8bbd6b"; YELLOW="#f2c744"; ORANGE="#ec9248"; RED="#c64f3f"; BLUE="#3b7ba8"; NAVY="#26506f"; TEAL="#4fa9a5"; PURPLE="#8a6bb0"; SAND="#e7d7b1"; GREY="#b9c2c8"; LIGHTBLUE="#dcebf3"
FONT="Carlito, Lato, 'DejaVu Sans', sans-serif"
def fig(w,h,body,title=""):
    """Returnerar en komplett svg-sträng. w,h = viewBox-storlek."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}" font-family="{FONT}">'
            f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker></defs>'
            f'<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>{body}</svg>')
def text(x,y,s,size=18,fill=INK,anchor="middle",weight="400",italic=False):
    st=' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{st}>{esc(s)}</text>'
def lines(x,y,ls,size=18,fill=INK,anchor="middle",weight="400",lh=None):
    lh=lh or size*1.25; return "".join(text(x,y+i*lh,s,size,fill,anchor,weight if i==0 else "400") for i,s in enumerate(ls))
def box(x,y,w,h,ls,fill=LIGHTBLUE,stroke=None,size=17,tc=INK,r=12,title_bold=True):
    """Rundad ruta med 1–3 rader text (första raden fet)."""
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="2.5"' if stroke else "")+'/>'
    if isinstance(ls,str): ls=[ls]
    n=len(ls); lh=size*1.25; y0=y+h/2-(n-1)*lh/2+size*0.35
    for i,l in enumerate(ls): s+=text(x+w/2,y0+i*lh,l,size,tc,"middle","700" if (i==0 and title_bold) else "400")
    return s
def arrow(x1,y1,x2,y2,color=MUTED,width=3,dash=False):
    d=' stroke-dasharray="7 6"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" marker-end="url(#ah)"{d}/>'
def curve(d,color=MUTED,width=3,dash=False):
    da=' stroke-dasharray="7 6"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" marker-end="url(#ah)"{da}/>'
def circle(x,y,r,fill=BLUE,stroke=None,sw=2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else "")+'/>'
def rect(x,y,w,h,fill=SAND,stroke=None,r=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="2"' if stroke else "")+'/>'
def line(x1,y1,x2,y2,color=INK,width=2,dash=False):
    d=' stroke-dasharray="6 5"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}/>'
def badge(x,y,n,fill=NAVY,r=15):
    return circle(x,y,r,fill)+text(x,y+6,str(n),16,"#fff","middle","700")
def title(w,s,y=34,size=22): return text(w/2,y,s,size,INK,"middle","700")
def path(d,fill="none",stroke=INK,sw=2): return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
