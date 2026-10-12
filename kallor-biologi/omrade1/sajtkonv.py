# -*- coding: utf-8 -*-
"""Gör om häftets HTML (en nivå av ett moment) till sajtens egna sidformat:
sektioner (rubrik, text, kontrollfrågor) + 'Bra att kunna'. Ingen PDF-layout följer med, bara innehållet."""
import re
from bs4 import BeautifulSoup, NavigableString, Tag

IKON = [(r"öva", "✏️"), (r"kolla|testa", "🤔"), (r"sammanfatt|viktigast", "📌"), (r"fråga|frågor", "❓"), (r"hypotes", "💡"),
        (r"argument", "💬"), (r"källa|information|sök", "🔎"), (r"modell|förklaring", "🧩"), (r"dokument|tabell|diagram|rapport", "📊"),
        (r"slutsats|resultat|värder|felkäll|osäker", "✅"), (r"försök|variabel|rättvis|labb|undersök|experiment|test", "🧪"),
        (r"upptäck|historia|pasteur|semmelweis|marshall|warren|tidslinje", "🔭"), (r"biolog|vetenskap|organism|liv", "🌱")]
RUTA = {"begrepp": None, "fundera": ("tank", "Fundera"), "tank": ("tank", "Tänk till"), "visste": ("visste", "Visste du?"),
        "varning": ("varning", "Tänk på"), "klimat": ("fakta", "Fakta")}

def ikon(t):
    for pat, i in IKON:
        if re.search(pat, t.lower()): return i
    return "📖"

def inner(t):
    """Innehållet som HTML, utan klasser utom på påhittat-märkningen."""
    out = []
    for c in t.children:
        if isinstance(c, NavigableString): out.append(str(c).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
        elif c.name == "span" and "fake" in c.get("class", []): out.append('<span class="pahittat">%s</span>' % c.get_text())
        elif c.name == "br": out.append("<br>")
        elif c.name in ("strong", "b", "em", "i", "sub", "sup"):
            n = "strong" if c.name in ("strong", "b") else ("em" if c.name == "i" else c.name)
            out.append("<%s>%s</%s>" % (n, inner(c), n))
        elif c.name == "span": out.append(inner(c))
        else: out.append(inner(c))
    return "".join(out).strip()

def txt(t): return re.sub(r"\s+", " ", t.get_text(" ")).strip()
def cap(s): s = s.strip(); return s[:1].upper() + s[1:].lower() if s.isupper() else s

class Konv:
    def __init__(self, forsta):
        self.sek = []; self.cur = None; self.begr = {}; self.forsta = forsta
    def ny(self, titel):
        self.cur = {"ikon": ikon(titel), "titel": titel, "text": [], "fragor": []}
        self.sek.append(self.cur)
    def add(self, h):
        if self.cur is None: self.ny(self.forsta)
        self.cur["text"].append(h)

    def figur(self, d):
        img = d.find("img"); c = d.find(class_="cap")
        if not img: return
        alt = txt(c) if c else ""
        self.add('<figure class="sek-bild"><img src="%s" alt="%s">%s</figure>' % (img["src"], alt.replace('"', "&quot;"), ("<figcaption>%s</figcaption>" % inner(c)) if c else ""))

    def tabell(self, t):
        rows = []
        for tr in t.find_all("tr"):
            cells = []
            for c in tr.find_all(["th", "td"]):
                body = inner(c) if not c.find(class_="bx") else "☐"
                cells.append("<%s>%s</%s>" % (c.name, body, c.name))
            rows.append("<tr>%s</tr>" % "".join(cells))
        self.add('<div class="tabell-ram"><table class="tabell">%s</table></div>' % "".join(rows))

    def ruta(self, d, typ, rubrik):
        ps = []
        for c in d.children:
            if isinstance(c, Tag) and "rb" in c.get("class", []): continue
            if isinstance(c, Tag) and c.name in ("p", "div", "ul", "ol"): ps.append(inner(c) if c.name != "ul" else "")
        body = "<br>".join(x for x in ps if x) or inner(d)
        self.add('<div class="ruta ruta-%s"><span class="ruta-rubrik">%s</span>%s</div>' % (typ, rubrik, body))

    def ovning(self, d):
        hd = d.find(class_="hd") or d
        ty = hd.find(class_="ty"); q = hd.find(class_="q")
        s = ""
        if ty: s += "<strong>%s.</strong> " % cap(txt(ty))
        if q: s += inner(q)
        ex = ""
        ch = hd.find(class_="chips")
        if ch: ex += '<div class="alt">%s</div>' % " &nbsp;·&nbsp; ".join("<span>%s</span>" % txt(x) for x in ch.find_all("span"))
        bank = hd.find(class_="bank")
        if bank: ex += '<div class="alt">%s</div>' % txt(bank)
        nr = hd.find(class_="nrbox")
        if nr: ex += '<div class="alt">%s</div>' % " &nbsp;·&nbsp; ".join("<span>%s</span>" % txt(x) for x in nr.find_all("div"))
        fy = hd.find(class_="fy")
        if fy: ex += "".join("<p>%s</p>" % inner(p).replace("______________", "________") for p in fy.find_all("p"))
        dr = hd.find(class_="dr")
        if dr:
            it = [txt(x) for x in dr.find_all("div", recursive=False)]
            ex += '<div class="alt">%s</div>' % " &nbsp;·&nbsp; ".join("<span>%s</span>" % x for x in sorted(it))
        sf = hd.find(class_="sf")
        if sf: ex += "<div class=\"alt\"><span>Sant</span> &nbsp;·&nbsp; <span>Falskt</span></div>"
        return "<li>%s%s</li>" % (s, ex)

    def walk(self, n):
        for c in list(n.children):
            if isinstance(c, NavigableString):
                if c.strip(): self.add("<p>%s</p>" % str(c).strip())
                continue
            cl = c.get("class", []); nm = c.name
            if nm in ("style", "script", "img") or set(cl) & {"lp", "tab", "lines", "ln", "dots", "sh"}: continue
            if nm == "h2":
                t = txt(c)
                if "lh" in cl or True:
                    t = re.sub(r"^\d+(\.\d+)*\s+", "", t)
                    if t.lower().startswith("öva"): t = "Öva"
                    self.ny(t)
                continue
            if nm == "h3": self.ny(txt(c)); continue
            if nm == "p":
                if "note" in cl: self.add('<p class="not">%s</p>' % inner(c))
                elif "cap" in cl: self.add('<p class="not">%s</p>' % inner(c))
                else: self.add("<p>%s</p>" % inner(c))
                continue
            if nm in ("ul", "ol"):
                self.add("<%s>%s</%s>" % (nm, "".join("<li>%s</li>" % inner(li) for li in c.find_all("li", recursive=False)), nm)); continue
            if nm == "table": self.tabell(c); continue
            if nm == "section": self.walk(c); continue
            if nm == "div":
                if "fig" in cl: self.figur(c); continue
                if "bx" in cl:
                    kind = [k for k in cl if k != "bx"][0] if len(cl) > 1 else ""
                    if kind == "begrepp":
                        ts = c.find_all("b", class_="t")
                        for b in ts:
                            p = b.find_next_sibling("p")
                            self.begr[txt(b)] = inner(p) if p else ""
                        continue
                    typ, rub = RUTA.get(kind, ("fakta", "Fakta"))
                    rb = c.find(class_="rb")
                    self.ruta(c, typ, txt(rb) if rb else rub); continue
                if "kolla" in cl:
                    if self.cur is None: self.ny(self.forsta)
                    self.cur["fragor"] += [inner(li) for li in c.find_all("li")]; continue
                if "kom" in cl:
                    self.add('<div class="ruta ruta-visste"><span class="ruta-rubrik">Kom ihåg</span>%s</div>' % inner(c.find(class_="tx"))); continue
                if "cards" in cl:
                    kk = []
                    for k in c.find_all(class_="card"):
                        h = k.find(class_="h"); ht = txt(h); h.extract()
                        kk.append('<div class="kort"><strong>%s</strong>%s</div>' % (ht, inner(k)))
                    self.add('<div class="kort-rad">%s</div>' % "".join(kk)); continue
                if "sam" in cl:
                    self.add("<ul>%s</ul>" % "".join("<li>%s</li>" % inner(li) for li in c.find_all("li"))); continue
                if "begr" in cl or "ord2" in cl:
                    for d in c.find_all("div", recursive=False):
                        b = d.find("b")
                        if b: self.begr[txt(b)] = txt(d)[len(txt(b)):].strip()
                    continue
                if "vik" in cl:
                    s = c.find("span"); self.add('<ul class="viktigast"><li>%s</li></ul>' % inner(s)) if s else None; continue
                if "arg" in cl:
                    h = c.find(class_="h"); body = inner(c).replace(inner(h), "", 1).lstrip("<br>").strip() if h else inner(c)
                    self.add('<div class="ruta ruta-fakta"><span class="ruta-rubrik">%s</span>%s</div>' % (cap(txt(h)) if h else "Så argumenterar du", body)); continue
                if "ex1" in cl:
                    if self.cur is None or self.cur["titel"] != "Öva": self.ny("Öva")
                    last = self.cur["text"][-1] if self.cur["text"] else ""
                    li = self.ovning(c)
                    if last.startswith('<ol class="ovning"'): self.cur["text"][-1] = last[:-5] + li + "</ol>"
                    else: self.add('<ol class="ovning">%s</ol>' % li)
                    continue
                if "pill" in cl:
                    t_ = txt(c); h_, _, r_ = t_.partition("·"); self.ny((h_.strip() + " · " + r_.strip().lower().capitalize()) if r_ else t_); continue
                if "alts" in cl:
                    self.add('<ul class="alts">%s</ul>' % "".join("<li>%s</li>" % inner(x) for x in c.find_all("div", recursive=False))); continue
                if "q" in cl:
                    n_ = c.find(class_="n"); pts_all = c.find_all(class_="pts")
                    pt = txt(pts_all[0]) if pts_all else ""
                    for x in ([n_] if n_ else []) + pts_all: x.extract()
                    al = c.find(class_="alts")
                    altl = ""
                    if al:
                        altl = '<ul class="alts">%s</ul>' % "".join("<li>%s</li>" % inner(x) for x in al.find_all("div", recursive=False)); al.extract()
                    for x in c.find_all(class_="lines"): x.extract()
                    self.add('<p class="provfraga"><strong>%s</strong> %s%s</p>' % (txt(n_) if n_ else "", inner(c), (' <em class="poang">(%s)</em>' % pt) if pt else ""))
                    if altl: self.add(altl)
                    continue
                self.walk(c); continue
            if nm in ("span", "b", "strong", "em"):
                self.add("<p>%s</p>" % inner(c)); continue

def konvertera(html, forsta):
    k = Konv(forsta)
    k.walk(BeautifulSoup(html, "html.parser"))
    sek = [s for s in k.sek if s["text"] or s["fragor"]]
    for s in sek:
        s["text"] = [re.sub(r"\s*[●○]+\s*(?=<em class=\"poang\">)", " ", x) for x in s["text"]]
        if not s["fragor"]: del s["fragor"]
    d = {"sektioner": sek}
    if k.begr: d["begrepp"] = [{"term": t, "forklaring": f} for t, f in sorted(k.begr.items(), key=lambda x: x[0].lower())]
    return d
