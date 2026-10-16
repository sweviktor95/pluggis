# -*- coding: utf-8 -*-
import math, random
from playwright.sync_api import sync_playwright
OUT='/tmp/kem/fig02n/'
INK="#24323c"; MUT="#5d6b75"
def render(name, svg, w, h, scale=3):
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path='/opt/pw-browsers/chromium'); pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=scale)
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.screenshot(path=OUT+name+'.png'); b.close()
    print(name)
def svg(W,H,body,bg="#faf7f2"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Carlito">'
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#5d6b75"/></marker><marker id="ah2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.2" markerHeight="3.2" orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>'
            f'<rect width="{W}" height="{H}" rx="20" fill="{bg}"/>{body}</svg>')
def T(x,y,s,size=30,fill=INK,w="400",a="middle",it=False):
    st=' font-style="italic"' if it else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}"{st}>{s}</text>'
def labels(W, left, right, ytop, ybot, size=32, lx=40, rx=None):
    """left/right: lista (text, ax, ay). Sorteras på ay så att linjerna inte korsas. Etikettens y sprids jämnt."""
    rx = rx or W-40
    o=''
    for side,items in (('L',left),('R',right)):
        items=sorted(items,key=lambda t:t[2]); n=len(items)
        for i,(t,ax,ay) in enumerate(items):
            ly = ytop+(ybot-ytop)*(i+0.5)/n if n>1 else (ytop+ybot)/2
            if side=='L':
                ex=lx+len(t)*size*0.52+14
                o+=T(lx,ly+size*0.35,t,size,INK,"700","start")
            else:
                ex=rx-len(t)*size*0.52-14
                o+=T(rx,ly+size*0.35,t,size,INK,"700","end")
            o+=f'<path d="M{ex:.0f},{ly:.0f} L{ax},{ay}" stroke="#5d6b75" stroke-width="2.2" fill="none"/><circle cx="{ax}" cy="{ay}" r="6" fill="#2f6b4f" stroke="#fff" stroke-width="2"/>'
    return o
def mito(x,y,rot=0,s=1):
    o=f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><ellipse rx="52" ry="28" fill="#f0a070" stroke="#c4622d" stroke-width="4"/>'
    o+='<path d="M-34,-18 L-34,6 M-18,-24 L-18,12 M-2,-26 L-2,16 M14,-24 L14,12 M30,-18 L30,6" stroke="#c4622d" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    return o+'</g>'
def chloro(x,y,rot=0,s=1):
    o=f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><ellipse rx="48" ry="26" fill="#6fbf6a" stroke="#2e7d3a" stroke-width="4"/>'
    for k in (-26,-9,8,25): o+=f'<rect x="{k-6}" y="-13" width="12" height="26" rx="4" fill="#3a9448"/>'
    return o+'</g>'
def nucleus(x,y,r):
    o=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#d9c8ee" stroke="#7a56b0" stroke-width="6"/><circle cx="{x-r*0.18}" cy="{y+r*0.1}" r="{r*0.3}" fill="#8a63bd"/>'
    o+=f'<path d="M{x-r*0.55},{y-r*0.45} q{r*0.18},-{r*0.2} {r*0.35},0 t{r*0.35},0 M{x+r*0.1},{y+r*0.55} q{r*0.18},-{r*0.2} {r*0.35},0 t{r*0.3},0" stroke="#5d3f8e" stroke-width="3.5" fill="none"/>'
    return o
def ribos(pts):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#26506f"/>' for x,y in pts)

