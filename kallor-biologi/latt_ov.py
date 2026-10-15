# -*- coding: utf-8 -*-
"""Lättlästa övningar som interaktiva sajtövningar. Frågorna kommer från samma data som PDF:en (ch01n_latt.py);
rätta svar är hämtade ur facit i lärarversionen."""
import re, os

# (delens titel eller "TEST", nr) -> rätt svar
SVAR = {
 ("Vad är biologi?", 1): 0,
 ("Vad är biologi?", 2): ["djur", "växter", "livet i havet", "små organismer, som bakterier"],
 ("Vad är biologi?", 3): ["naturen", "labb", "kropp"],
 ("Från fråga till plan", 1): 1,
 ("Från fråga till plan", 2): ["ljuset", "hur hög krassen blir", "jord och vatten"],
 ("Från fråga till plan", 3): [0, 1, 3],
 ("Från fråga till plan", 4): [0, 2],
 ("Från fråga till plan", 5): "Då vet man vad som orsakade skillnaden.",
 ("Dokumentera", 1): 0,
 ("Dokumentera", 2): "Ett stapeldiagram med rubrik, två staplar (12 och 8) och axlar med namn och enhet (cm).",
 ("Dokumentera", 3): [4, 1, 3, 2],
 ("Dokumentera", 4): ["tabell", "rubrik", "enhet"],
 ("Värdera", 1): 0,
 ("Värdera", 2): [True, False, True],
 ("Värdera", 3): ["felkälla", "flera", "slutsatsen"],
 ("Värdera", 4): "Då är det mindre troligt att resultatet bara var en slump.",
 ("Labb 1.1 Reaktionstid", 1): ["fem", "tabell", "cm"],
 ("Labb 1.1 Reaktionstid", 2): "Ett eget stapeldiagram med rubrik och namn på axlarna.",
 ("Labb 1.1 Reaktionstid", 3): "Till exempel ”ungefär 0,2 sekunder”.",
 ("Labb 1.1 Reaktionstid", 4): "Till exempel att man såg kompisens hand, eller att linjalen hölls sned.",
 ("Vad kan vetenskap pröva?", 1): [0, 2],
 ("Vad kan vetenskap pröva?", 2): 0,
 ("Vad kan vetenskap pröva?", 3): ["belägg", "åsikt", "pseudovetenskap"],
 ("Vad kan vetenskap pröva?", 4): "Till exempel testa med lukter och se vilka som hittar dem.",
 ("När forskare ändrat sig", 1): ["små organismer kommer utifrån", "handtvätt minskar dödsfall", "magsår kommer av en bakterie"],
 ("När forskare ändrat sig", 2): 0,
 ("När forskare ändrat sig", 3): ["modell", "bakterie", "belägg"],
 ("När forskare ändrat sig", 4): "Nya undersökningar gav nya belägg.",
 ("Söka information och bedöma källor", 1): ["Vem har skrivit texten?", "Vill de sälja något?", "Är texten gammal?", "Står det på fler ställen?"],
 ("Söka information och bedöma källor", 2): 1,
 ("Söka information och bedöma källor", 3): ["trovärdig", "relevant", "belägg"],
 ("Söka information och bedöma källor", 4): "Kolla vem som har skrivit, om de vill sälja något, om det finns belägg och om fler källor säger samma sak.",
 ("TEST", 1): 0,
 ("TEST", 2): ["det man tror blir svaret, och varför", "det man mäter eller ser", "det man lär sig", "mätningar som visar något"],
 ("TEST", 3): [False, False, True, False],
 ("TEST", 4): 1,
 ("TEST", 5): "Ändra temperaturen. Lika: sorts bönor, antal, vatten, jord och ljus.",
 ("TEST", 6): "Göra om testet flera gånger, med fler bönor.",
 ("TEST", 7): "Den sjönk (från 11,4 % till 1,3 %).",
 ("TEST", 8): "Till exempel kolla vem som står bakom, om de vill sälja något och om pålitliga källor säger samma sak.",
}

if os.environ.get("CH") == "04n":
    from latt_svar04 import SVAR  # kapitel 4 har egna svar
elif os.environ.get("CH") == "03n":
    from latt_svar03 import SVAR  # kapitel 3 har egna svar

def _gap(s): return re.sub(r"_{3,}", "§", s)

def bygg(nyckel, n, e):
    """Gör om en övning (tuple ur ch01n_latt) till ett dict som sajten kan visa."""
    k = e[0]; s = SVAR.get((nyckel, n))
    if k == "sortera":
        return {"typ": "sf", "fraga": e[1].replace("Skriv L eller I i rutan.", "Svara sant eller falskt."), "pastaenden": [x + " är levande." for x in e[2]], "ratt": s}
    if k == "skriv3":
        return {"typ": "skriv2", "fraga": e[1], "falt": ["Steg 1:", "Steg 2:", "Steg 3:"], "forslag": s}
    if k == "ringa":
        return {"typ": "ringa", "fraga": e[1], "val": e[2], "ratt": s}
    if k == "streck":
        return {"typ": "streck", "fraga": e[1], "vanster": e[2], "hoger": sorted(e[3]), "ratt": s}
    if k == "kryssa":
        return {"typ": "kryssa", "fraga": e[1], "val": e[2], "ratt": s}
    if k == "sf":
        return {"typ": "sf", "fraga": e[1], "pastaenden": e[2], "ratt": s}
    if k == "fyll":
        return {"typ": "fyll", "fraga": "Välj rätt ord.", "ord": sorted(e[1]), "meningar": [_gap(x) for x in e[2]], "ratt": s}
    if k == "siffror":
        return {"typ": "siffror", "fraga": e[1], "delar": e[2], "ratt": s}
    if k == "skriv":
        return {"typ": "skriv", "fraga": e[1], "borja": e[2], "forslag": s}
    if k == "skriv2":
        return {"typ": "skriv2", "fraga": e[1], "falt": e[2], "forslag": s}
    if k == "rita":
        return {"typ": "rita", "fraga": e[1], "forslag": s}
    raise ValueError(k)

def sektion(titel, ikon, nyckel, lista):
    return {"ikon": ikon, "titel": titel, "text": [], "ovningar": [bygg(nyckel, n, e) for n, e in enumerate(lista, 1)]}
