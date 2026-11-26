# -*- coding: utf-8 -*-
"""Bråk och procent (åk 7). Egna frågor utifrån pluggbladets begrepp.
Bygger Blooket-CSV, Kahoot-xlsx, Jeopardy och flashcards. Siffror kontrolleras med Fraction."""
import csv, json, sys, re
from fractions import Fraction as F
import openpyxl
R = "/home/claude/pluggis/"
D = R + "planering/matematik-ak7-brak-procent/"
Q = []  # (fråga, rätt, [fel x3], tid)
def q(t, r, fel, tid=20):
    assert len(fel) == 3 and r not in fel and len(set(fel)) == 3, t
    assert len(t) <= 120 and all(len(x) <= 75 for x in [r] + fel), t
    Q.append((t, r, fel, tid))
# ---- Begrepp om bråk ----
q("Vad kallas talet under bråkstrecket?", "Nämnare", ["Täljare", "Kvot", "Summa"])
q("Vad visar nämnaren i bråket 5/8?", "Hur många lika stora delar helheten är delad i", ["Hur många delar man har", "Hur stor helheten är", "Hur många hela det finns"])
q("En kaka delas i 12 lika stora bitar. Sara äter 5 bitar. Vilket bråk har hon ätit?", "5/12", ["5/7", "12/5", "7/12"])
q("Vilket av bråken är större än 1?", "11/6", ["6/11", "3/8", "2/9"])
assert F(11, 6) > 1
q("Hur skrivs 17/5 i blandad form?", "3 2/5", ["2 3/5", "3 5/2", "5 2/3"], 30)
assert 3 + F(2, 5) == F(17, 5)
q("Hur skrivs 4 3/8 som ett bråk?", "35/8", ["43/8", "7/12", "27/8"], 30)
assert 4 + F(3, 8) == F(35, 8)
q("Vilket av talen är skrivet i blandad form?", "2 1/3", ["7/3", "0,25", "40 %"])
q("Vilket bråk är lika med 1 hel?", "9/9", ["1/9", "9/18", "0/9"])
# ---- Likvärdiga bråk, förlänga och förkorta ----
q("Vilket bråk är likvärdigt med 1/2?", "4/8", ["2/8", "1/4", "4/6"])
assert F(4, 8) == F(1, 2)
q("Förläng 2/3 med 4. Vilket bråk får du?", "8/12", ["6/7", "8/3", "2/12"])
assert F(8, 12) == F(2, 3)
q("Skriv 12/18 i enklaste form.", "2/3", ["6/9", "4/6", "3/2"], 30)
assert F(12, 18) == F(2, 3)
q("Vilket bråk är inte likvärdigt med 3/5?", "5/3", ["6/10", "9/15", "12/20"], 30)
assert F(5, 3) != F(3, 5) and F(6, 10) == F(3, 5) == F(9, 15) == F(12, 20)
q("Vad gör man när man förlänger ett bråk?", "Multiplicerar täljare och nämnare med samma tal", ["Adderar samma tal till täljare och nämnare", "Multiplicerar bara täljaren", "Dividerar bara nämnaren"], 30)
q("Vad gör man när man förkortar ett bråk?", "Dividerar täljare och nämnare med samma tal", ["Subtraherar samma tal från täljare och nämnare", "Dividerar bara täljaren", "Multiplicerar nämnaren"], 30)
q("Vilket tal kan du förkorta 20/30 med?", "10", ["3", "4", "7"])
assert 20 % 10 == 0 and 30 % 10 == 0
q("Vilket bråk är skrivet i enklaste form?", "5/12", ["6/8", "10/15", "9/12"])
# ---- Jämföra ----
q("Vilket av bråken är störst?", "3/4", ["3/5", "3/8", "3/10"])
assert max([F(3, 5), F(3, 8), F(3, 4), F(3, 10)]) == F(3, 4)
q("Vilket av bråken är minst?", "2/9", ["2/3", "2/5", "2/7"])
assert min([F(2, 3), F(2, 5), F(2, 9), F(2, 7)]) == F(2, 9)
q("Vilket tecken ska stå mellan 3/4 och 5/8?", ">", ["<", "=", "Det går inte att avgöra"], 30)
assert F(3, 4) > F(5, 8)
q("Vilken är den minsta gemensamma nämnaren för 1/4 och 1/6?", "12", ["24", "10", "2"], 30)
q("Vilken ordning är rätt, från minst till störst?", "1/3, 1/2, 3/4", ["1/2, 1/3, 3/4", "3/4, 1/2, 1/3", "1/3, 3/4, 1/2"], 30)
q("Vilken av nämnarna går att använda som gemensam nämnare för 2/3 och 3/5?", "15", ["8", "3", "5"], 30)
assert 15 % 3 == 0 and 15 % 5 == 0
# ---- Räkna med bråk ----
q("Beräkna 3/9 + 4/9", "7/9", ["7/18", "12/9", "1/9"])
assert F(3, 9) + F(4, 9) == F(7, 9)
q("Beräkna 7/10 − 3/10. Svara i enklaste form.", "2/5", ["4/10", "4/20", "10/4"], 30)
assert F(7, 10) - F(3, 10) == F(2, 5)
q("Beräkna 1/2 + 1/3", "5/6", ["2/5", "2/6", "1/5"], 30)
assert F(1, 2) + F(1, 3) == F(5, 6)
q("Beräkna 3/4 − 1/2", "1/4", ["2/2", "1/2", "3/2"], 30)
assert F(3, 4) - F(1, 2) == F(1, 4)
q("Beräkna 2/5 + 3/10", "7/10", ["5/15", "5/10", "6/50"], 30)
assert F(2, 5) + F(3, 10) == F(7, 10)
q("Beräkna 5/6 + 2/3. Svara i blandad form.", "1 1/2", ["7/9", "1 1/6", "2 1/2"], 40)
assert F(5, 6) + F(2, 3) == F(3, 2)
q("Kim har 3/4 liter saft och använder 1/8 liter. Hur mycket är kvar?", "5/8 liter", ["2/4 liter", "2/8 liter", "1/8 liter"], 40)
assert F(3, 4) - F(1, 8) == F(5, 8)
q("1/3 av eleverna spelar fotboll och 1/4 spelar bandy. Vilken del spelar någon av dem?", "7/12", ["2/7", "2/12", "1/12"], 40)
assert F(1, 3) + F(1, 4) == F(7, 12)
# ---- Procent, procentform, decimalform ----
q("Vad betyder 1 procent?", "En hundradel", ["En tiondel", "Hundra", "En tusendel"])
q("Hur skrivs 25 % som ett bråk i enklaste form?", "1/4", ["25/10", "1/25", "2/5"], 30)
assert F(25, 100) == F(1, 4)
q("Vilken decimalform har 40 %?", "0,4", ["4", "0,04", "40"])
q("Vilken procentform har 3/10?", "30 %", ["3 %", "0,3 %", "10 %"])
assert F(3, 10) == F(30, 100)
q("Hur skrivs 0,07 i procentform?", "7 %", ["70 %", "0,07 %", "0,7 %"], 30)
q("Vilket av talen är lika stort som 50 %?", "1/2", ["1/50", "5/100", "0,05"])
q("Hur skrivs 3/5 i procentform?", "60 %", ["35 %", "3,5 %", "30 %"], 30)
assert F(3, 5) == F(60, 100)
q("Vilket av talen är störst?", "0,45", ["40 %", "3/8", "1/3"], 40)
assert max([F(45, 100), F(40, 100), F(3, 8), F(1, 3)]) == F(45, 100)
q("Hur många procent motsvarar 3/4?", "75 %", ["34 %", "7,5 %", "25 %"], 30)
assert F(3, 4) == F(75, 100)
# ---- Andel, delen, det hela ----
q("I en klass om 25 elever har 10 blå jacka. Vilken andel har blå jacka?", "40 %", ["10 %", "25 %", "15 %"], 30)
assert F(10, 25) == F(40, 100)
q("Hur mycket är 10 % av 350?", "35", ["3,5", "10", "340"], 30)
assert F(350) * F(10, 100) == 35
q("Hur mycket är 25 % av 80?", "20", ["25", "55", "4"], 30)
assert 80 * F(25, 100) == 20
q("Hur mycket är 75 % av 120?", "90", ["30", "45", "75"], 40)
assert 120 * F(75, 100) == 90
q("20 % av 150 kr är 30 kr. Vilket tal är det hela?", "150 kr", ["20 %", "30 kr", "200 kr"])
q("En tröja kostar 400 kr. Rean är 30 %. Hur många kronor sänks priset?", "120 kr", ["30 kr", "280 kr", "130 kr"], 40)
assert 400 * F(30, 100) == 120
q("Av 60 elever cyklade 15. Vilken andel cyklade, i enklaste form?", "1/4", ["15/60", "1/15", "4/1"], 40)
assert F(15, 60) == F(1, 4)
q("Det hela är 200 och delen är 50. Hur många procent är delen?", "25 %", ["4 %", "150 %", "250 %"], 40)
assert F(50, 200) == F(25, 100)
q("30 % av ett tal är 60. Vilket är talet?", "200", ["18", "90", "20"], 40)
assert 60 / F(30, 100) == 200
q("En cykel kostar 800 kr och priset höjs med 5 %. Hur många kronor höjs priset?", "40 kr", ["4 kr", "400 kr", "840 kr"], 40)
assert 800 * F(5, 100) == 40
# ---- Tillägg efter kapitlets begreppstest, kapiteltest och basläger: multiplikation, bråkdel av antal, förändring ----
q("Vad händer med ett bråks värde när du förlänger det?", "Det ändras inte", ["Det ökar", "Det minskar", "Det fördubblas"])
q("Beräkna 4 · 1/5", "4/5", ["4/20", "5/4", "1/20"], 30)
assert 4 * F(1, 5) == F(4, 5)
q("Beräkna 2/3 · 3/4. Svara i enklaste form.", "1/2", ["5/7", "6/7", "5/12"], 40)
assert F(2, 3) * F(3, 4) == F(1, 2)
q("Hur mycket är 3/4 av 100?", "75", ["34", "25", "43"], 30)
assert F(3, 4) * 100 == 75
q("Hur mycket är 2/5 av 30?", "12", ["6", "15", "60"], 30)
assert F(2, 5) * 30 == 12
q("Av 15 kulor är 6 gula. Vilken andel är gula, i enklaste form?", "2/5", ["6/15", "3/5", "15/6"], 30)
assert F(6, 15) == F(2, 5)
q("Priset på en bok ökade från 50 kr till 60 kr. Med hur många procent ökade priset?", "20 %", ["10 %", "60 %", "120 %"], 40)
assert F(60 - 50, 50) == F(20, 100)
q("Priset sänktes från 80 kr till 60 kr. Med hur många procent sänktes priset?", "25 %", ["20 %", "75 %", "15 %"], 40)
assert F(80 - 60, 80) == F(25, 100)
q("Priset sjönk från 20 kr till 10 kr. Det är en minskning med", "50 %", ["10 %", "100 %", "200 %"], 30)
assert F(10, 20) == F(50, 100)
q("En hyra på 5 000 kr höjs med 4 %. Vilken blir den nya hyran?", "5 200 kr", ["200 kr", "5 004 kr", "4 800 kr"], 40)
assert 5000 * F(104, 100) == 5200
q("Jeans kostar 650 kr. Du får 20 % rabatt. Vad får du betala?", "520 kr", ["130 kr", "630 kr", "670 kr"], 40)
assert 650 * F(80, 100) == 520
q("10 % av ett tal är 9. Vilket är talet?", "90", ["0,9", "19", "900"], 30)
assert 9 / F(10, 100) == 90
q("Om 1 % är 3, hur mycket är då 100 %?", "300", ["3", "100", "30"], 30)
q("Hur mycket är 50 % av 64?", "32", ["50", "14", "64"], 20)
assert F(64) * F(50, 100) == 32
assert len(Q) >= 60, len(Q)

# ---- Blooket CSV + Kahoot xlsx (rätt svar flyttas runt) ----
KT = lambda t: t if t in (5, 10, 20, 30, 60, 90, 120, 240) else min([x for x in (5, 10, 20, 30, 60, 90, 120, 240) if x >= t] or [240])
sh = []
for i, (t, r, fel, tid) in enumerate(Q):
    k = (i * 3 + 1) % 4
    ans = fel[:]; ans.insert(k, r)
    sh.append((t, ans, tid, k + 1))
with open(D + "matematik-7-brak-procent-blooket.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, lineterminator="\r\n")
    w.writerow(["Blooket\nImport Template", "", "", "", "", "", "", ""])
    w.writerow(["Question #", "Question Text", "Answer 1", "Answer 2", "Answer 3 \n(Optional)", "Answer 4 \n(Optional)", "Time Limit (sec) \n(Max: 300 Seconds)", "Correct Answer(s) \n(Only Include Answer #)"])
    for i, (t, ans, tid, c) in enumerate(sh, 1):
        w.writerow([i, t] + ans + [tid, c])
wb = openpyxl.load_workbook(R + "planering/kemi-omrade2/kemi-2-kahoot.xlsx"); ws = wb.worksheets[0]
for r in range(9, ws.max_row + 1):
    for c in range(1, 9): ws.cell(r, c).value = None
for i, (t, ans, tid, c) in enumerate(sh):
    r = 9 + i; ws.cell(r, 1).value = i + 1; ws.cell(r, 2).value = t
    for j in range(4): ws.cell(r, 3 + j).value = ans[j]
    ws.cell(r, 7).value = KT(tid); ws.cell(r, 8).value = str(c)
wb.save(D + "matematik-7-brak-procent-kahoot.xlsx")

# ---- Jeopardy ----
KAT = [
 ("Begrepp om bråk", [
   ("Vad kallas talet över bråkstrecket?", "täljare"),
   ("Vad kallas talet under bråkstrecket?", "nämnare"),
   ("Skriv 13/4 i blandad form.", "3 1/4"),
   ("Skriv 2 2/5 som ett bråk.", "12/5"),
   ("Vad är skillnaden mellan 3/2 och 1 1/2? Ge ett exempel på när man vill använda vilken form.", "Samma tal. 1 1/2 är blandad form (hela och en del), 3/2 är bråkform med bara täljare och nämnare. Blandad form är lätt att föreställa sig, bråkform är lättare att räkna med.")]),
 ("Likvärdiga bråk", [
   ("Förläng 1/3 med 5.", "5/15"),
   ("Förkorta 6/8 så långt det går.", "3/4"),
   ("Skriv 36/48 i enklaste form.", "3/4"),
   ("Skriv ett bråk med nämnaren 20 som är likvärdigt med 3/4.", "15/20"),
   ("Varför ändras inte värdet när man förlänger eller förkortar ett bråk?", "Man multiplicerar eller dividerar täljare och nämnare med samma tal, alltså med 1 i praktiken. Andelen är lika stor, den delas bara upp i fler eller färre bitar.")]),
 ("Jämföra och räkna", [
   ("Vilket är störst, 1/2 eller 1/3?", "1/2"),
   ("Beräkna 2/9 + 5/9.", "7/9"),
   ("Beräkna 1/2 + 1/6.", "2/3"),
   ("Beräkna 2/3 · 3/4. Svara i enklaste form.", "1/2"),
   ("Hitta en gemensam nämnare för 3/8 och 5/12 och avgör vilket bråk som är störst.", "24: 3/8 = 9/24 och 5/12 = 10/24, så 5/12 är störst.")]),
 ("Procent och former", [
   ("Skriv 50 % som ett bråk.", "1/2"),
   ("Skriv 3/4 i procentform.", "75 %"),
   ("Skriv 0,6 i procentform.", "60 %"),
   ("Skriv 35 % i decimalform.", "0,35"),
   ("Skriv 3/8 i decimalform och i procentform.", "0,375 och 37,5 %")]),
 ("Andel, delen och det hela", [
   ("Hur mycket är 10 % av 90?", "9"),
   ("Hur mycket är 25 % av 60?", "15"),
   ("Priset på en bok ökar från 50 kr till 60 kr. Hur många procent ökar priset?", "20 %"),
   ("20 % av ett tal är 14. Vilket är det hela?", "70"),
   ("Ett par skor kostar 600 kr. Priset sänks med 15 %. Vilket är det nya priset?", "510 kr")]),
]
assert F(13, 4) == 3 + F(1, 4) and 2 + F(2, 5) == F(12, 5) and F(36, 48) == F(3, 4) and F(15, 20) == F(3, 4)
assert F(1, 2) + F(1, 6) == F(2, 3) and F(2, 3) * F(3, 4) == F(1, 2) and F(3, 8) == F(9, 24) and F(5, 12) == F(10, 24)
assert F(3, 8) * 100 == F(75, 2) and 0.1 * 90 == 9 and 0.25 * 60 == 15 and F(10, 50) == F(20, 100) and 14 / F(20, 100) == 70 and 600 * F(85, 100) == 510
data = [{"kat": k, "fr": [{"p": 100 * (i + 1), "q": qq, "a": a} for i, (qq, a) in enumerate(fr)]} for k, fr in KAT]
h = open(R + "simuleringar/jeopardy-kemi-2.html", encoding="utf8").read()
h = re.sub(r"var DATA=.*?\n", lambda m: "var DATA=" + json.dumps(data, ensure_ascii=False) + ";\n", h, count=1, flags=re.S)
h = h.replace("Jeopardy: Materia och partiklar (beta)", "Jeopardy: Bråk och procent (beta)")
h = h.replace('var NIV={100:"Lättläst",200:"Lättläst",300:"Grundtext",400:"Grundtext",500:"Fördjupning"};', 'var NIV={100:"Grundläggande",200:"Grundläggande",300:"Mellan",400:"Mellan",500:"Utmaning"};')
h = re.sub(r'<p class="note">.*?</p>', '<p class="note">Poängen visar svårigheten: 100–200 är grundläggande, 300–400 är mellan och 500 är en utmaning. Svaren är korta. Personer och exempel i frågorna är påhittade.</p>', h, count=1, flags=re.S)
assert "Materia" not in h and "Lättläst" not in h and "DATA=[" in h
open(R + "simuleringar/jeopardy-matematik-brak-procent.html", "w", encoding="utf8").write(h)

# ---- Flashcards (elevvyn) ----
BRAK = [
 ("Bråk", "En del av en helhet eller av flera hela. Skrivs med täljare över och nämnare under bråkstrecket, till exempel 3/5."),
 ("Täljare", "Talet över bråkstrecket. Det visar hur många delar man har."),
 ("Nämnare", "Talet under bråkstrecket. Det visar hur många lika stora delar helheten är delad i."),
 ("Bråkform", "Ett tal skrivet med täljare och nämnare, till exempel 7/4."),
 ("Blandad form", "Ett tal skrivet med hela och ett bråk, till exempel 1 3/4."),
 ("Likvärdiga bråk", "Bråk med olika täljare och nämnare men samma värde, till exempel 1/2 och 4/8."),
 ("Förlänga bråk", "Multiplicera täljare och nämnare med samma tal. Värdet ändras inte: 2/3 = 8/12."),
 ("Förkorta bråk", "Dividera täljare och nämnare med samma tal. Värdet ändras inte: 12/18 = 2/3."),
 ("Gemensam nämnare", "En nämnare som båda bråken kan skrivas med. Behövs för att jämföra, addera och subtrahera bråk med olika nämnare."),
 ("Multiplikation av bråk", "Multiplicera täljare med täljare och nämnare med nämnare, och förkorta sedan: 2/3 · 3/4 = 6/12 = 1/2."),
 ("Bråkdel av ett antal", "Multiplicera antalet med bråket: 3/4 av 100 = 3 · 100 / 4 = 75."),
 ("Enklaste form", "Bråket är förkortat så långt det går. Täljare och nämnare har ingen gemensam faktor förutom 1, till exempel 2/3."),
]
PROC = [
 ("Procent", "En hundradel. 1 % betyder 1/100, och 100 % är hela."),
 ("Procentform", "Ett tal skrivet med procenttecken, till exempel 25 %."),
 ("Decimalform", "Ett tal skrivet med decimaler, till exempel 0,25. Det är samma tal som 25 % och 1/4."),
 ("Andel", "Hur stor del något är av helheten. Kan skrivas som bråk, decimaltal eller procent."),
 ("Delen", "Den del av helheten man tittar på. I 20 % av 150 kr är delen 30 kr. Delen kan också vara en ökning eller minskning."),
 ("Det hela", "Helheten som delen räknas av, motsvarar 100 %. I 20 % av 150 kr är det hela 150 kr. Vid en förändring är det hela det ursprungliga värdet."),
 ("Procentuell förändring", "Förändringen delat med det ursprungliga värdet, skrivet i procent. Från 50 kr till 60 kr är ökningen 10/50 = 20 %."),
]
def js(var, key, titel, kort):
    obj = {"sektioner": [], "flash": {"begrepp": [{"term": a, "forklaring": b} for a, b in kort]}}
    return 'innehall["%s"] = %s;\n' % (key, json.dumps(obj, ensure_ascii=False, indent=1))
src = "// Flashcards för bråk och procent (åk 7). Begreppen kommer från provets begreppslista, förklaringarna är egna.\nvar innehall = window.innehall || {};\n\n"
src += js("", "matematik-ak7-brak-flash", "Flashcards", BRAK) + "\n" + js("", "matematik-ak7-procent-flash", "Flashcards", PROC)
open(R + "innehall/matematik-brak-procent-flashcards.js", "w", encoding="utf8").write(src)
print(len(Q), "frågor;", sum(len(c["fr"]) for c in data), "jeopardy;", len(BRAK) + len(PROC), "flashcards")
