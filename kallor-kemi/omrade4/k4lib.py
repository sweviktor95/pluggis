from kfig4_common import *
PC = "#d9534a"; NC = "#8a97a1"; EC = "#2f6aa3"
ARROW = f'<defs><marker id="a3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="{INK}"/></marker></defs>'

def nuc(cx, cy, p, n, r=15, seed=3):
    rnd = random.Random(seed); items = ['p'] * p + ['n'] * n; rnd.shuffle(items)
    pts = []; spread = r * (1 + 0.9 * math.sqrt(len(items)))
    for t in items:
        for _ in range(400):
            a = rnd.uniform(0, 6.283); d = rnd.uniform(0, spread) ** 1 * 0.6 + 0
            x = cx + d * math.cos(a); y = cy + d * math.sin(a)
            if all((x - u) ** 2 + (y - v) ** 2 >= (1.75 * r) ** 2 for u, v, _ in pts): pts.append((x, y, t)); break
        else:
            spread += 4; pts.append((cx + rnd.uniform(-spread, spread) * .6, cy + rnd.uniform(-spread, spread) * .6, t))
    return ''.join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{PC if t=="p" else NC}" stroke="#fff" stroke-width="2.5"/>' for x, y, t in pts)
def atom(cx, cy, p, n, shells, r=15, R0=95, dR=62, er=11, lab=True, seed=3, rot=0.3):
    s = ''
    for k in range(len(shells)):
        s += f'<circle cx="{cx}" cy="{cy}" r="{R0+k*dR}" fill="none" stroke="#b9c3ca" stroke-width="3" stroke-dasharray="3 0"/>'
    s += nuc(cx, cy, p, n, r, seed)
    for k, m in enumerate(shells):
        for i in range(m):
            a = rot + 6.283 * i / m + k * 0.5
            s += f'<circle cx="{cx+(R0+k*dR)*math.cos(a):.0f}" cy="{cy+(R0+k*dR)*math.sin(a):.0f}" r="{er}" fill="{EC}" stroke="#fff" stroke-width="2.5"/>'
    return s
def legend(x, y, size=26, gap=190):
    s = ''
    for i, (c, t) in enumerate([(PC, "proton (+)"), (NC, "neutron (0)"), (EC, "elektron (−)")]):
        s += f'<circle cx="{x+i*gap}" cy="{y}" r="11" fill="{c}"/>' + T(x + i * gap + 20, y + 9, t, size, INK, "400", "start")
