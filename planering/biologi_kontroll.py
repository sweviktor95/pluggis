# -*- coding: utf-8 -*-
"""Kontroll av biologiplaneringen (område 1–4) mot kunskapskrav och häften.
Kör från repots rot:  python3 planering/biologi_kontroll.py
Skriver planering/biologi-kontroll-1-4.md och skriver luckor på skärmen. Ändrar inga andra filer.

Del 1: kunskapskrav (årskurs 9, E/C/A) kopplade till delområden och moment (KRAV i biologi_krav.py).
Del 2: planeringens begrepp (kärnmoment + labbpass = ska finnas i lättläst OCH grundtext;
       'Om tid / fördjupning' = ska finnas i grundtext eller fördjupning) kontrollerade mot häftenas text,
       med definition (ur häftets begreppslista, annars förslag i biologi_krav.NYA)."""
import sys, re, subprocess, os, collections
sys.path.insert(0, "planering"); sys.path.insert(0, "kallor-biologi")
import biologi_plan25 as P
import biologi_krav as K

HAFTE = "hafte"
OMR = {1: ("1-vetenskap", "omrade1", "ch01n"), 2: ("2-cellen", "omrade2", "ch02n"),
       3: ("3-mangfald", "omrade3", "ch03n"), 4: ("4-ekologi", "omrade4", "ch04n")}

def norm(s): return re.sub(r"\s+", " ", s.lower().replace("­", "").replace("-\n", ""))
def pdftext(n, niva):
    f = f"{HAFTE}/biologi-{OMR[n][0]}-{niva}.pdf"
    return norm(subprocess.run(["pdftotext", f, "-"], capture_output=True, text=True).stdout)
def stam(t):
    t = norm(t).strip()
    return t[:max(4, len(t) - 2)]
def finns(term, text):
    return any(stam(v) in text for v in K.VAR.get(term, [term]))
def finns_syn(term, text):
    return any(norm(v) in text for v in K.SYN.get(term, []))

def termer(strang):
    """Delar upp ett begreppsfält i enskilda begrepp."""
    for a, b in K.SPLIT.items(): strang = strang.replace(a, b)
    ut = []
    for t in strang.split(","):
        t = t.strip()
        if t and t not in K.SKIPPA: ut.append(t)
    return ut

def definitioner(n):
    import importlib
    sys.path.insert(0, f"kallor-biologi/{OMR[n][1]}")
    M = importlib.import_module(OMR[n][2]); sys.path.pop(0)
    return {norm(a): b for a, b in M.BEGR}
ALLA = {}
def hitta_def(term, D):
    if not ALLA:
        for m in OMR: ALLA.update({k: b for k, b in definitioner(m).items() if k not in ALLA})
    for kalla in (D, ALLA):
        for v in K.VAR.get(term, [term]):
            v = norm(v)
            for k, b in kalla.items():
                if k == v or (len(k) >= 5 and abs(len(k) - len(v)) <= 3 and (k.startswith(v) or v.startswith(k))): return b
    return K.NYA.get(term)

def kontroll():
    rapport = []; w = rapport.append; luckor = collections.defaultdict(list)
    # ---------------- Del 1: kunskapskrav ----------------
    w("# Biologi åk 7–9: kontroll av planeringen, område 1–4\n")
    w("Genereras av `planering/biologi_kontroll.py` (ändra data i `planering/biologi_krav.py`). Källa för kunskapskraven: Skolverkets kursplan i biologi, betygskriterier för slutet av årskurs 9.\n")
    w("## 1. Kunskapskrav kopplade till delområden\n")
    w("Kunskapskraven är sex delar (KK1–KK6). Tabellen visar var i område 1–4 varje del övas och bedöms. **Tydlig** = ett kärnmoment eller labbpass tränar det uttryckligen. **Svag** = det ligger bara i nivåtexten (E→A), i ett 'Om tid'-moment eller i ett labbpass som bara delvis tränar det.\n")
    w("| Del | Kunskapskrav (E / C / A) |"); w("|---|---|")
    for k, (rub, e, c, a) in K.KK.items():
        w(f"| **{k}** {rub} | **E:** {e}<br>**C:** {c}<br>**A:** {a} |")
    w("")
    w("| Delområde | " + " | ".join(K.KK) + " |"); w("|---|" + "---|" * len(K.KK))
    tyd = collections.defaultdict(list); sva = collections.defaultdict(list)
    delnamn = {d[0]: d[1] for a in P.NEW[:4] for d in a[3]}
    for dn, m in K.MAP.items():
        celler = []
        for k in K.KK:
            if k in m:
                styrka, bevis = m[k]
                (tyd if styrka == "T" else sva)[k].append(dn)
                celler.append(("**T** " if styrka == "T" else "s ") + bevis)
            else: celler.append("")
        w(f"| {dn} {delnamn[dn]} | " + " | ".join(celler) + " |")
    w("\nT = tydlig, s = svag.\n")
    w("| Del | Tydligt i | Bara svagt i | Bedömning |"); w("|---|---|---|---|")
    for k, (rub, *_ ) in K.KK.items():
        t, s = tyd[k], sva[k]
        if len(t) >= 2: b = "Täckt"
        elif len(t) == 1: b = "Sårbart: bara ett tillfälle"
        else: b = "Lucka i område 1–4"
        if b != "Täckt": luckor["kunskapskrav"].append(f"{k} {rub}: {b} (tydligt i {', '.join(t) or '–'}; svagt i {', '.join(s) or '–'})")
        w(f"| {k} {rub} | {', '.join(t) or '–'} | {', '.join(s) or '–'} | {b} |")
    w("")
    for n in K.NOTER: w(n)
    w("")
    # ---------------- Del 2: begrepp ----------------
    w("## 2. Planeringens begrepp mot häftena\n")
    w("Kontrollen söker begreppets ordstam i häftenas text (pdf). **Ord** = begreppet finns. **Syn.** = bara ett närliggande uttryck finns (begreppet bör ändå stå med). **–** = saknas. Kärnmoment och labbpass ska finnas i både lättläst och grundtext; 'Om tid' ska finnas i grundtext eller fördjupning.\n")
    tot = collections.Counter()
    for a in P.NEW[:4]:
        n = a[0]; L = pdftext(n, "lattlast"); G = pdftext(n, "vanlig"); F = pdftext(n, "fordjupning"); D = definitioner(n)
        w(f"### Område {n}. {a[1]}\n")
        w("| Delområde / moment | Begrepp | Lättläst | Grund | Fördjupning | Definition |"); w("|---|---|---|---|---|---|")
        sedda = set()
        for d in a[3]:
            rader = [(f"{d[0]} {mom_titel(i)}", P.mom(i)["begrepp"], True) for i in d[5]]
            if d[0] in P.LAB25: rader.append((f"{d[0]} Labb: {P.LAB25[d[0]][0]}", P.LAB25[d[0]][5], True))
            rader += [(f"{d[0]} (om tid) {mom_titel(i)}", P.mom(i)["begrepp"], False) for i in d[6]]
            for titel, beg, karna in rader:
                for t in termer(beg):
                    if (t, karna) in sedda or (t in [x for x, _ in sedda]): continue
                    sedda.add((t, karna))
                    l = "Ord" if finns(t, L) else ("Syn." if finns_syn(t, L) else "–")
                    g = "Ord" if finns(t, G) else ("Syn." if finns_syn(t, G) else "–")
                    f = "Ord" if finns(t, F) else ("Syn." if finns_syn(t, F) else "–")
                    df = hitta_def(t, D)
                    krav_l = karna; krav_g = karna or True
                    fel = []
                    if karna and l != "Ord": fel.append(f"lättläst ({l})")
                    if karna and g != "Ord": fel.append(f"grund ({g})")
                    if not karna and g != "Ord" and f != "Ord": fel.append(f"grund/fördjupning ({g}/{f})")
                    if fel: luckor[f"begrepp område {n}"].append(f"{t}  [{titel}]: saknas/svagt i " + ", ".join(fel))
                    if karna and not df: luckor[f"definition område {n}"].append(t)
                    tot["kärna" if karna else "om tid"] += 1
                    w(f"| {titel} | {'**'+t+'**' if karna else t} | {l} | {g} | {f} | {df or ('*(definition saknas)*' if karna else '–')} |")
        w("")
    w("## 3. Luckor att besluta om\n")
    for k, v in luckor.items():
        w(f"**{k}** ({len(v)})\n")
        for x in v: w(f"- {x}")
        w("")
    os.makedirs("planering", exist_ok=True)
    open("planering/biologi-kontroll-1-4.md", "w", encoding="utf-8").write("\n".join(rapport) + "\n")
    return luckor, tot

def mom_titel(i): return P.mom(i)["titel"]

if __name__ == "__main__":
    luckor, tot = kontroll()
    print("begrepp kontrollerade:", dict(tot))
    for k, v in luckor.items():
        print(f"\n{k} ({len(v)})")
        for x in v: print("  -", x)
