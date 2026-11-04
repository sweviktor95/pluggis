# -*- coding: utf-8 -*-
"""Blooket-CSV för Matematik 7 – Bråk. Räkneuppgifter beräknas och kontrolleras med Fraction."""
import csv
from fractions import Fraction as F
def fr(f):
    return f"{f.numerator}/{f.denominator}"
def blandad(f):
    h, r = divmod(f.numerator, f.denominator)
    return f"{h} {r}/{f.denominator}" if r else str(h)
Q = []  # (text, [rätt, fel1, fel2, fel3], tid)
def q(t, ratt, fel, tid=20):
    assert len(fel) == 3 and ratt not in fel
    Q.append((t, [ratt] + fel, tid))
# --- Bråkform ---
q("Vad kallas talet under bråkstrecket i ett bråk?", "Nämnare", ["Täljare", "Kvot", "Faktor"])
q("Vad kallas talet över bråkstrecket i ett bråk?", "Täljare", ["Nämnare", "Summa", "Produkt"])
q("I bråket 3/5: i hur många lika stora delar är helheten delad?", "5", ["3", "8", "2"])
q("En pizza är delad i 8 lika stora bitar. Lisa äter 3 bitar. Hur stor del av pizzan äter hon?", "3/8", ["3/5", "8/3", "5/8"])
q("Vilket bråk är lika med 1 hel?", "7/7", ["1/7", "0/7", "7/14"])
q("Vilket av bråken är större än 1?", "9/4", ["4/9", "3/3", "2/5"])
q("Hur skrivs 11/4 i blandad form?", "2 3/4", ["3 2/4", "2 1/4", "1 7/4"])
assert F(11,4) == 2 + F(3,4)
q("Hur skrivs 2 1/3 som ett bråk?", "7/3", ["3/7", "6/3", "2/3"])
assert 2 + F(1,3) == F(7,3)
q("Hur mycket är 1/4 av 20?", str(20//4), ["4", "80", "16"])
q("Hur mycket är 3/5 av 30?", str(30//5*3), ["6", "50", "15"])
q("Vilket decimaltal är lika med 3/4?", "0,75", ["0,34", "0,25", "3,4"])
assert F(3,4) == F(75,100)
q("Vilket bråk ligger mitt emellan 0 och 1 på tallinjen?", "1/2", ["1/4", "1/1", "2/1"])
q("Vad kallas ett bråk där täljaren är 1, till exempel 1/6?", "Stambråk", ["Blandat bråk", "Decimalbråk", "Skenbråk"])
# --- Jämföra ---
q("Vilket bråk är störst?", "5/8", ["3/8", "1/8", "2/8"])
q("Vilket tecken ska stå i rutan? 2/3 ☐ 3/4", "<", [">", "=", "Det går inte att jämföra"])
assert F(2,3) < F(3,4)
q("Hur ska bråken ordnas från minst till störst? 3/4, 1/2, 5/8", "1/2, 5/8, 3/4", ["3/4, 5/8, 1/2", "1/2, 3/4, 5/8", "5/8, 1/2, 3/4"])
assert sorted([F(3,4), F(1,2), F(5,8)]) == [F(1,2), F(5,8), F(3,4)]
q("Vilket bråk är större än 1/2?", "3/5", ["2/5", "3/7", "4/9"])
assert F(3,5) > F(1,2) and all(x < F(1,2) for x in (F(2,5), F(3,7), F(4,9)))
q("Vilket bråk ligger närmast 1?", "7/8", ["3/4", "5/6", "1/2"])
assert max([F(7,8), F(3,4), F(5,6), F(1,2)]) == F(7,8)
q("Varför är 1/6 mindre än 1/4?", "Helheten delas i fler delar, så varje del blir mindre", ["Eftersom 6 är mindre än 4", "Eftersom täljarna är lika", "Bråken är lika stora"])
q("Vilket bråk är lika med 0,25?", "1/4", ["1/2", "2/5", "1/25"])
q("Vilket bråk är minst?", "1/8", ["1/2", "1/3", "1/5"])
# --- Förlänga och förkorta ---
q("Förläng 2/3 med 4. Vilket bråk får du?", "8/12", ["6/7", "2/12", "8/3"])
q("Förläng 3/5 så att nämnaren blir 20. Vilket bråk får du?", "12/20", ["3/20", "15/20", "7/20"])
assert F(12,20) == F(3,5)
q("Vilket bråk är lika stort som 1/2?", "3/6", ["2/5", "4/9", "5/11"])
q("Förkorta 6/8 så långt det går.", "3/4", ["2/3", "6/4", "1/2"])
assert F(6,8) == F(3,4)
q("Förkorta 12/18 så långt det går.", "2/3", ["6/9", "4/6", "3/2"])
assert F(12,18) == F(2,3)
q("Förkorta 15/45 så långt det går.", "1/3", ["3/9", "5/15", "1/5"])
assert F(15,45) == F(1,3)
q("Vad gör man när man förkortar ett bråk?", "Delar täljare och nämnare med samma tal", ["Adderar samma tal till täljare och nämnare", "Multiplicerar bara täljaren", "Byter plats på täljare och nämnare"])
q("Vad händer med bråkets värde när man förlänger det?", "Det ändras inte", ["Det blir större", "Det blir mindre", "Det blir 1"])
q("Vilket av bråken går inte att förkorta?", "7/12", ["6/9", "8/12", "10/15"])
q("Förkorta 24/36 så långt det går.", "2/3", ["12/18", "6/9", "3/2"])
assert F(24,36) == F(2,3)
q("Vilka bråk är lika stora (ekvivalenta)?", "2/5 och 6/15", ["2/5 och 6/10", "3/4 och 6/12", "1/3 och 3/6"])
assert F(2,5) == F(6,15) and F(2,5) != F(6,10) and F(3,4) != F(6,12) and F(1,3) != F(3,6)
# --- Addition och subtraktion ---
q("Beräkna 2/7 + 3/7", fr(F(2,7)+F(3,7)), ["5/14", "6/7", "1/7"], 20)
q("Beräkna 5/8 − 2/8", fr(F(5,8)-F(2,8)), ["7/8", "3/16", "3/4"], 20)
q("Beräkna 1/2 + 1/4", fr(F(1,2)+F(1,4)), ["2/6", "1/6", "2/4"], 30)
q("Beräkna 1/3 + 1/6", fr(F(1,3)+F(1,6)), ["2/9", "1/9", "2/3"], 30)
q("Beräkna 1/2 + 1/3", fr(F(1,2)+F(1,3)), ["2/5", "1/5", "2/6"], 30)
q("Beräkna 2/3 + 1/4", fr(F(2,3)+F(1,4)), ["3/7", "3/12", "2/12"], 40)
q("Beräkna 3/4 − 1/3", fr(F(3,4)-F(1,3)), ["4/7", "2/12", "1/12"], 40)
q("Beräkna 5/6 − 1/2", fr(F(5,6)-F(1,2)), ["2/4", "4/6", "1/4"], 30)
q("Beräkna 3/5 + 4/5. Svara i blandad form.", blandad(F(3,5)+F(4,5)), ["7/10", "1 3/5", "1 7/5"], 30)
q("Beräkna 7/10 − 1/5", fr(F(7,10)-F(1,5)), ["6/5", "6/10", "7/5"], 30)
q("Beräkna 2/5 + 1/10", fr(F(2,5)+F(1,10)), ["3/15", "3/10", "2/5"], 30)
q("Vad gäller för nämnaren när man adderar bråk med samma nämnare, till exempel 2/9 + 4/9?", "Nämnaren behålls och täljarna adderas", ["Nämnarna adderas också", "Nämnarna multipliceras", "Täljarna multipliceras"])
q("Vilken är den minsta gemensamma nämnaren för 1/3 och 1/4?", "12", ["7", "6", "24"])
q("Adam äter 1/4 av en pizza och Bea äter 2/8. Hur stor del äter de tillsammans?", fr(F(1,4)+F(2,8)), ["3/12", "3/8", "1/4"], 40)
q("Mia har 3/4 liter saft. Hon dricker 1/2 liter. Hur mycket saft är kvar?", fr(F(3,4)-F(1,2)) + " liter", ["2/2 liter", "2/4 liter", "1/2 liter"], 40)

EXPECT = {"Beräkna 2/7 + 3/7": "5/7", "Beräkna 5/8 − 2/8": "3/8", "Beräkna 1/2 + 1/4": "3/4", "Beräkna 1/3 + 1/6": "1/2",
          "Beräkna 1/2 + 1/3": "5/6", "Beräkna 2/3 + 1/4": "11/12", "Beräkna 3/4 − 1/3": "5/12", "Beräkna 5/6 − 1/2": "1/3",
          "Beräkna 3/5 + 4/5. Svara i blandad form.": "1 2/5", "Beräkna 7/10 − 1/5": "1/2", "Beräkna 2/5 + 1/10": "1/2"}
for t, a, _ in Q:
    if t in EXPECT: assert a[0] == EXPECT[t], (t, a[0])
    assert len(t) <= 300 and all(len(x) <= 160 for x in a) and len(set(a)) == 4, t
# Rätt svar flyttas runt (position 1–4) så att mönstret inte går att gissa
import sys
out = sys.argv[1]
with open(out, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, lineterminator="\r\n")
    w.writerow(["Blooket\nImport Template", "", "", "", "", "", "", ""])
    w.writerow(["Question #", "Question Text", "Answer 1", "Answer 2", "Answer 3 \n(Optional)", "Answer 4 \n(Optional)", "Time Limit (sec) \n(Max: 300 Seconds)", "Correct Answer(s) \n(Only Include Answer #)"])
    for i, (t, a, tid) in enumerate(Q):
        k = (i * 3 + 1) % 4          # önskad position för rätt svar
        order = a[1:]; order.insert(k, a[0])
        w.writerow([i + 1, t] + order + [tid, k + 1])
print(len(Q), "frågor")
