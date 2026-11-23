# -*- coding: utf-8 -*-
"""Gör Tänk tillbaka, Löst exempel, Fyll i själv och Gör själv interaktiva på sajten (kemi kapitel 2)."""
import re

ANS = {
 "Vad är materia?": "Allt som har massa och tar plats.",
 "Är luft materia? Hur vet du det?": "Ja. Luft har massa och tar plats. Det märks när du blåser upp en ballong.",
 "Hur räknar du ut densitet?": "Densitet = massa / volym.",
 "Vad är smältpunkt och kokpunkt?": "Smältpunkt: temperaturen då ett fast ämne blir flytande. Kokpunkt: temperaturen då en vätska kokar.",
 "Vad händer med partiklarna när ett fast ämne smälter?": "De rör sig mer och lämnar sina platser i mönstret, men ligger fortfarande nära varandra.",
 "Förklara med partiklar varför doft sprids i ett rum.": "Doftpartiklarna är gas. De rör sig åt alla håll och blandar sig med luften (diffusion).",
 "Vad är en homogen och en heterogen blandning?": "Homogen: ser likadan ut överallt, t.ex. saltvatten. Heterogen: delarna syns, t.ex. sand i vatten.",
 "Hur mycket väger en lösning av 5 g salt i 100 g vatten?": "105 g. Massan bevaras när ett ämne löser sig.",
 "Varför går löst salt inte att filtrera bort?": "Lösta partiklar är så små att de går rakt igenom filtret.",
 "Hur får du tillbaka saltet ur saltvatten?": "Indunsta: vattnet avdunstar och saltet blir kvar.",
 "Vad utnyttjar destillation?": "Att ämnen har olika kokpunkter.",
 "Varför vandrar färger olika långt vid kromatografi?": "De löser sig olika bra i lösningsmedlet och fastnar olika mycket på papperet.",
 "Hur räknar du ut densitet, och vad avgör om ett föremål flyter?": "Densitet = massa / volym. Föremålet flyter om dess densitet är lägre än vätskans.",
 "Vilka tre tillstånd finns, och hur ligger partiklarna i vart och ett?": "Fast: tätt i ett mönster, vibrerar. Vätska: nära men glider förbi varandra. Gas: långt ifrån varandra, rör sig snabbt.",
 "Vad händer med partiklarna vid smältning?": "De rör sig mer och lämnar sina platser i mönstret, men ligger fortfarande nära varandra.",
 "Vad kallas övergångarna gas till vätska och vätska till gas?": "Gas till vätska: kondensation. Vätska till gas: förångning (kokning).",
 "Vad är lösning, löst ämne och lösningsmedel?": "Lösning: blandningen. Löst ämne: det som löses. Lösningsmedel: det som löser, t.ex. vatten.",
 "Hur skiljer du en homogen från en heterogen blandning?": "Går det att se delarna? Ja: heterogen. Nej: homogen.",
 "Vilka två metoder behövs för att få tillbaka både sand och salt?": "Filtrering för sanden och indunstning för saltet.",
 "Vad är destillation, och vilken skillnad utnyttjas?": "Att skilja vätskor genom att koka dem. Skillnaden i kokpunkt utnyttjas.",
 "Hur fungerar kromatografi?": "Färgämnena vandrar olika långt på papperet, så man ser vilka färger en blandning består av.",
 "Vad är en fällning?": "Ett fast ämne som bildas när lösningar blandas.",
 "Varför behöver man mäta flera egenskaper för att identifiera ett ämne?": "Flera ämnen kan ha samma värde på en egenskap.",
}
# (nyckel i texten, [accepterade svar per lucka], facit)
FY = [
 ("plastbit väger 46 g", [["46"], ["40"], ["1.15"], ["större"], ["sjunker", "nej", "inte"]], "46 / 40 = 1,15 g/cm³. Värdet är större än 1,0, så plastbiten sjunker."),
 ("Förklara varför sockerbiten", [["sprids", "sprider", "diffunder", "blandas"], ["rör sig", "rör"], ["sprids", "sprider", "blandas", "diffunder"]], "Sockerpartiklarna lossnar och sprids ut (diffunderar). Vattenpartiklarna rör sig hela tiden, så sockerpartiklarna blandas ut bland dem."),
 ("Sockerbiten i teet gör", [["lossnar"], ["diffusion"]], "Sockerpartiklarna lossnar från biten och sprider sig bland vattenpartiklarna. Det kallas diffusion."),
 ("müsli med mjölk", [["heterogen"], ["homogen", "blandning", "lösning"], ["rent"]], "Müsli med mjölk: heterogen blandning. Luft: homogen blandning. Bara syre: rent ämne."),
 ("kaffesump", [["filtrering", "filtrera"], ["residu"], ["filtrat"]], "Metod: filtrering. Det som blir kvar i filtret heter residu och det som rinner igenom heter filtrat."),
 ("kaffe med sump", [["filtrering", "filtrera"], ["residu"], ["filtrat"]], "Metoden heter filtrering. Residu blir kvar i filtret. Filtrat rinner igenom."),
 ("Aceton kokar vid 56", [["aceton"], ["lägre", "låg"]], "Aceton kommer först, eftersom dess kokpunkt (56 °C) är lägre än vattnets."),
 ("Aceton (56 °C)", [["aceton"], ["lägre", "låg"]], "Aceton kommer först, eftersom dess kokpunkt (56 °C) är lägre än vattnets."),
 ("Vilka ämnen kan du utesluta", [[], []], "Olösliga ämnen (t.ex. sand) och ämnen som påverkar indikatorn (syror, baser) kan uteslutas. Nästa test kan vara smältpunkt eller densitet."),
 ("Gör ett ", [["annat", "nytt"], []], "Gör ett annat test, till exempel att värma lite och se om det smälter eller blir brunt."),
]
GS = [
 ("140 g och har volymen 50", "140 / 50 = 2,8 g/cm³. Det är högre än vattnets 1,0 g/cm³, så stenen sjunker."),
 ("fortare att lösa i varmt te", "I varmt te rör sig partiklarna snabbare, så sockret lossnar och sprids ut fortare."),
 ("12 g socker i 200 g vatten", "212 g (12 + 200). Låt vattnet avdunsta (indunsta) så blir sockret kvar."),
 ("Ett kaffefilter släpper igenom", "Partiklarnas storlek. Kaffets lösta partiklar är mindre än hålen i filtret. Sumpens partiklar är större och stannar kvar."),
 ("svart bläck", "Bläcket är en blandning av minst tre färgämnen. Man kan inte veta vilka ämnen det är, och två ämnen kan vandra lika långt."),
 ("blandar två klara lösningar", "En fällning har bildats: ett fast ämne som bildas när lösningarna blandas."),
 ("liten, grund pöl", "En liten pöl har lite vatten som kyls snabbt hela vägen, så isen bildas genom hela pölen. I en djup sjö måste en stor vattenmassa kylas till 4 °C innan ytan kan frysa, och isen som bildas isolerar vattnet under."),
 ("platån vid kokning är längre", "Vid kokning ska partiklarna skiljas helt från varandra, vilket kräver mycket mer energi än att bryta loss dem ur mönstret vid smältning. Därför tar det längre tid."),
 ("30 g salt i 100 ml vatten", "Omättad: 30 g är mindre än 35,7 g, så allt löser sig och ytterligare 5,7 g skulle kunna lösas."),
 ("Lag B fick 3,9 g", "3,9 / 5,0 × 100 = 78 %. T.ex. salt som fastnat på filter och bägare, eller spill."),
 ("vandrade 4,5 cm", "Rf = 4,5 / 9,0 = 0,50. Rf 0,9 betyder att ämnet vandrade nästan lika långt som lösningsmedlet: det löser sig bra och fastnar lite på papperet."),
 ("smälter inte under 300", "Salt är troligast (smältpunkt 802 °C, socker bryts ned vid ca 190 °C). Man kan inte vara säker, eftersom flera andra salter också löser sig och har höga smältpunkter. Fler tester behövs."),
]
RUTA = re.compile(r'^<div class="ruta ruta-[a-z]+"><span class="ruta-rubrik">(.*?)</span>(.*)</div>$', re.S)
def _plain(h): return re.sub(r"<[^>]+>", "", h)

def _gor(rub, body):
    plain = _plain(body)
    if rub.startswith("Tänk tillbaka"):
        pos = sorted((plain.find(k), k) for k in ANS if k in plain)
        qs = [k for i, k in pos]
        if not qs: return None
        return {"typ": "tbak", "fraga": "Tänk tillbaka", "fragor": [{"f": q, "svar": ANS.get(_plain(q), "")} for q in qs]}
    if rub.startswith("Löst exempel"):
        delar = [d for d in re.split(r"<br\s*/?>", body) if _plain(d).strip()]
        if len(delar) < 2:
            delar = [d for d in re.split(r"(?<=[.?!:])\s+(?=[A-ZÅÄÖ0-9<])", body) if _plain(d).strip()]
        if len(delar) < 2: return None
        return {"typ": "lost", "fraga": "Löst exempel: " + delar[0], "steg": delar[1:]}
    if rub.startswith("Fyll i själv"):
        for key, ratt, facit in FY:
            if key in plain:
                antal = len(re.findall(r"_{3,}", body))
                text = re.sub(r"_{3,}", "§", body)
                text = re.sub(r"<strong>Halvfärdig uppgift\.</strong>\s*", "", text)
                text = text.replace("<br>", "<br><br>") if False else text
                return {"typ": "fyllfri", "fraga": "Fyll i själv", "text": text, "ratt": [r for r in (ratt + [[]] * antal)[:antal]], "forslag": facit}
        return None
    if rub.startswith("Gör själv"):
        for key, fac in GS:
            if key in plain:
                return {"typ": "fri", "fraga": "Gör själv: " + body, "forslag": fac}
        return None
    return None

def gor_interaktiv(niv):
    for v in niv.values():
        for sek in v["sektioner"]:
            ny = []; ov = []
            for t in sek.get("text", []):
                m = RUTA.match(t) if isinstance(t, str) else None
                o = _gor(m.group(1), m.group(2)) if m else None
                if o: ov.append(o)
                else: ny.append(t)
            if ov:
                sek["text"] = ny
                sek["ovningar"] = sek.get("ovningar", []) + ov
    return niv
