# -*- coding: utf-8 -*-
import sys, math, random
sys.path.insert(0, '/tmp/kem')
import cellkit as K
from cellkit import T, svg, render
K.OUT = '/tmp/kem/fig03k/'
INK = "#24323c"; MUT = "#5d6b75"; RED = "#a8322a"; DRED = "#7a1f1f"; BG = "#fbf3f1"; LINE = "#7b8f9c"

def glass_fill(x, y, w, h, level, col="#bcd9ec", rx=8):
    """Bägare/cylinder utan skala: glasögon med vätska."""
    return ''
def beaker(x, y, w, h, level=0.5, col="#bcd9ec", ticks=True):
    o = f'<path d="M{x-8},{y-6} L{x},{y} L{x},{y+h-10} Q{x},{y+h} {x+10},{y+h} L{x+w-10},{y+h} Q{x+w},{y+h} {x+w},{y+h-10} L{x+w},{y} L{x+w+8},{y-6}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="5" stroke-linejoin="round"/>'
    ly = y + h * (1 - level)
    o += f'<path d="M{x+3},{ly} L{x+w-3},{ly} L{x+w-3},{y+h-9} Q{x+w-3},{y+h-3} {x+w-11},{y+h-3} L{x+11},{y+h-3} Q{x+3},{y+h-3} {x+3},{y+h-9}Z" fill="{col}" opacity=".9"/>'
    if ticks:
        for k in range(1, 4):
            o += f'<path d="M{x+6},{y+h*k/4.5} h{w*0.22}" stroke="{LINE}" stroke-width="3"/>'
    o += f'<path d="M{x+14},{y+12} v{h*0.55}" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".7"/>'
    return o
def cylinder(x, y, w, h, level=0.5, col="#bcd9ec", nt=10):
    o = f'<path d="M{x-6},{y-5} L{x},{y} L{x},{y+h} L{x+w},{y+h} L{x+w},{y} L{x+w+6},{y-5}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="5" stroke-linejoin="round"/>'
    o += f'<path d="M{x-w*0.9},{y+h+16} L{x+w*1.9},{y+h+16} L{x+w*1.6},{y+h} L{x-w*0.6},{y+h}Z" fill="#cfd8de" stroke="{LINE}" stroke-width="4"/>'
    ly = y + h * (1 - level)
    o += f'<path d="M{x+3},{ly} Q{x+w/2},{ly+7} {x+w-3},{ly} L{x+w-3},{y+h-3} L{x+3},{y+h-3}Z" fill="{col}" opacity=".9"/>'
    for k in range(1, nt):
        yy = y + h * k / nt
        o += f'<path d="M{x+4},{yy} h{w*(0.5 if k%5==0 else 0.3)}" stroke="{LINE}" stroke-width="2.6"/>'
    o += f'<path d="M{x+9},{y+8} v{h*0.7}" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".7"/>'
    return o
def flask(x, y, w, h, level=0.35, col="#cde8c0"):
    nw = w * 0.26
    o = f'<path d="M{x+w/2-nw/2-6},{y-6} L{x+w/2-nw/2},{y} L{x+w/2-nw/2},{y+h*0.38} L{x},{y+h-8} Q{x-4},{y+h} {x+10},{y+h} L{x+w-10},{y+h} Q{x+w+4},{y+h} {x+w},{y+h-8} L{x+w/2+nw/2},{y+h*0.38} L{x+w/2+nw/2},{y} L{x+w/2+nw/2+6},{y-6}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="5" stroke-linejoin="round"/>'
    ly = y + h * (1 - level)
    # trapets för vätska
    t = (ly - (y + h * 0.38)) / (h * 0.62)
    lw = nw + (w - nw) * max(t, 0)
    o += f'<path d="M{x+w/2-lw/2+3},{ly} L{x+w/2+lw/2-3},{ly} L{x+w-6},{y+h-5} L{x+8},{y+h-5}Z" fill="{col}" opacity=".9"/>'
    o += f'<path d="M{x+w*0.3},{y+h*0.5} L{x+w*0.18},{y+h*0.82}" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"/>'
    return o
def tube(x, y, h, col="#bcd9ec", level=0.5, w=34):
    o = f'<path d="M{x-4},{y} L{x},{y+3} L{x},{y+h-w/2} A{w/2},{w/2} 0 0 0 {x+w},{y+h-w/2} L{x+w},{y+3} L{x+w+4},{y}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="4.5" stroke-linejoin="round"/>'
    ly = y + h * (1 - level)
    o += f'<path d="M{x+3},{ly} L{x+w-3},{ly} L{x+w-3},{y+h-w/2} A{w/2-3},{w/2-3} 0 0 1 {x+3},{y+h-w/2}Z" fill="{col}" opacity=".9"/>'
    return o
def thermometer(x, y, h, val=0.5, col="#d63a2e"):
    o = f'<rect x="{x}" y="{y}" width="26" height="{h}" rx="13" fill="#fff" stroke="{LINE}" stroke-width="4.5"/>'
    top = y + 18 + (h - 60) * (1 - val)
    o += f'<rect x="{x+9}" y="{top}" width="8" height="{y+h-top}" fill="{col}"/><circle cx="{x+13}" cy="{y+h+10}" r="20" fill="{col}" stroke="{LINE}" stroke-width="4.5"/>'
    o += f'<rect x="{x+6}" y="{y+h-12}" width="14" height="20" fill="{col}"/>'
    for k in range(8): o += f'<path d="M{x+30},{y+22+k*(h-60)/7} h{18 if k%2==0 else 11}" stroke="{LINE}" stroke-width="2.6"/>'
    return o
def balance(x, y, w, txt="152,4 g", tsz=30):
    o = f'<ellipse cx="{x+w/2}" cy="{y}" rx="{w*0.46}" ry="10" fill="#dfe4e8" stroke="{LINE}" stroke-width="4"/>'
    o += f'<path d="M{x},{y+26} L{x+w},{y+26} L{x+w*0.94},{y+78} L{x+w*0.06},{y+78}Z" fill="#eef1f3" stroke="{LINE}" stroke-width="4" stroke-linejoin="round"/>'
    o += f'<rect x="{x+w*0.2}" y="{y+36}" width="{w*0.6}" height="32" rx="6" fill="#26343d"/>' + T(x+w/2, y+60, txt, tsz, "#8fe08f", "700")
    return o
def goggles(x, y, s=1.0):
    o = f'<g transform="translate({x},{y}) scale({s})"><path d="M-95,-6 Q-100,-48 -52,-48 Q-6,-48 -4,-10 Q0,-14 4,-10 Q6,-48 52,-48 Q100,-48 95,-6 Q96,40 50,40 Q8,40 0,0 Q-8,40 -50,40 Q-96,40 -95,-6Z" fill="#dff0f8" fill-opacity=".75" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
    o += f'<path d="M-95,-6 Q-130,-8 -138,8 M95,-6 Q130,-8 138,8" stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M-70,-26 q16,-8 34,-4 M30,-26 q16,-8 34,-4" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/></g>'
    return o
def pipette(x, y, s=1.0, col="#e8625a"):
    return (f'<g transform="translate({x},{y}) rotate(-12) scale({s})"><path d="M0,0 q-18,-26 0,-46 q18,20 0,46z" fill="{col}"/><rect x="-10" y="0" width="20" height="120" rx="6" fill="#f2f7fa" stroke="{LINE}" stroke-width="4"/>'
            f'<path d="M-10,120 L0,170 L10,120" fill="#bcd9ec" stroke="{LINE}" stroke-width="4"/><rect x="-6" y="70" width="12" height="52" fill="#bcd9ec" opacity=".9"/></g>')
def bubble(x, y, r, op=.8):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" fill-opacity=".35" stroke="#8fb7d3" stroke-width="2.5" opacity="{op}"/>'
def shelf(x1, x2, y): return f'<path d="M{x1},{y} L{x2},{y}" stroke="#cdbdb8" stroke-width="7" stroke-linecap="round"/>'
def card(x, y, w, h, fill="#fff", stroke="#e3d5d1"): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'
