# -*- coding: utf-8 -*-
"""Kemi område 2 Materia och partiklar – lättläst version (byggd per moment)."""
FIG = '/tmp/kem/fig02k/'
NR = 2
SLUG = "kemi-materia"
TAB = "2"
NAMN = "Materia och partiklar"
NDEL = 9
UNDER = "Allt består av partiklar"
INTRO_L = ["I det här kapitlet lär du dig vad allt är gjort av.",
           "Du lär dig mäta densitet och förstå varför is flyter. Du lär dig partikelmodellen, skillnaden mellan ämnen och blandningar och hur man skiljer ämnen åt.",
           "Namn och siffror i exemplen är påhittade, om inget annat står."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Start: vad materia är",
        "Delområde 2.1 Ämnen, blandningar och partikelmodellen: egenskaper, partikelmodellen, rena ämnen och blandningar",
        "Delområde 2.2 Separations- och analysmetoder: filtrering, destillation, kromatografi och fällning"]
ORD_FIG = None
ORD_EXTRA = [("materia", "allt som har massa och tar plats"), ("ämne", "en sorts material, till exempel vatten eller järn"), ("egenskap", "något som kännetecknar ett ämne"),
             ("densitet", "hur mycket massa ett ämne har per volym"), ("smältpunkt", "temperaturen då ett fast ämne blir flytande"), ("kokpunkt", "temperaturen då en vätska kokar"),
             ("löslighet", "hur mycket som går att lösa i vatten"), ("partikel", "en mycket liten bit som allt är uppbyggt av"), ("tillstånd", "fast, flytande eller gas"),
             ("diffusion", "partiklar som sprider sig själva"), ("tryck", "gaspartiklarnas slag mot väggarna"), ("rent ämne", "bara en sorts partikel"),
             ("blandning", "minst två ämnen tillsammans"), ("lösning", "ett ämne som är löst i ett annat"), ("filtrering", "man skiljer fast ämne från vätska"),
             ("destillation", "man skiljer ämnen som kokar vid olika temperatur"), ("kromatografi", "man skiljer färger som vandrar olika långt"), ("fällning", "ett fast ämne som bildas när lösningar blandas")]

TB_DENS = ('<table class="tb"><tr><th>Ämne</th><th>Densitet (g/cm³)</th></tr>'
           '<tr><td>Olivolja</td><td>0,91</td></tr><tr><td>Is</td><td>0,92</td></tr><tr><td>Vatten</td><td>1,0</td></tr><tr><td>Aluminium</td><td>2,7</td></tr><tr><td>Järn</td><td>7,8</td></tr></table>')
TB_TILL = ('<table class="tb"><tr><th></th><th>Fast</th><th>Vätska</th><th>Gas</th></tr>'
           '<tr><td>Avstånd</td><td>tätt</td><td>nära</td><td>långt isär</td></tr><tr><td>Rörelse</td><td>vibrerar</td><td>glider</td><td>rör sig snabbt</td></tr></table>')
TB_LABB1 = ('<table class="tb"><tr><th>Föremål</th><th>Massa (g)</th><th>Volym (cm³)</th><th>Densitet (g/cm³)</th><th>Flyter eller sjunker?</th></tr>'
            '<tr><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td></tr></table>')
TB_LABB2 = ('<table class="tb"><tr><th>Ämne</th><th>Massa före (g)</th><th>Massa efter (g)</th></tr>'
            '<tr><td>Sand</td><td>10</td><td></td></tr><tr><td>Salt</td><td>5</td><td></td></tr></table>')

DELOMR = {"2.1": "Ämnen, blandningar och partikelmodellen", "2.2": "Separations- och analysmetoder"}
DELAR = [
 dict(titel="Vad är materia?", prog="Start · Vad är materia?",
  fore=["<strong>Materia</strong> är allt som har massa och tar plats. Stenar, vatten, träd och du själv är materia. Luft är också materia.", "Materia finns som <strong>fast</strong>, <strong>flytande</strong> och <strong>gas</strong>. Det kallas tillstånd."],
  fig="v_oversikt.png", figw="95%",
  efter=["Vatten kan vara is, flytande vatten eller vattenånga. Det är samma ämne.", "Kemister förklarar tillstånden med en modell. Den kallas <strong>partikelmodellen</strong>. Allt består av små partiklar som rör sig."],
  kom="Materia är allt som har massa och tar plats. Allt består av partiklar.",
  ova=[("ringa", "Vad är materia?", ["Allt som har massa och tar plats", "Bara fasta saker", "Bara saker du kan se"]),
       ("sf", "Kryssa i rätt ruta.", ["Luft är materia.", "Vatten kan vara fast, flytande eller gas.", "Is och vatten är olika ämnen."]),
       ("fyll", ["gas", "partiklar", "fast"], ["Is är ett ______________ ämne.", "Vattenånga är en ______________.", "Allt består av små ______________."]),
       ("skriv", "Nämn något som är materia och som du inte kan se.", "Ett exempel är", 2)]),

 dict(titel="Ämnen och material", prog="Delområde 2.1 · Ämnen och material",
  fore=["Ett <strong>ämne</strong> känns igen på sina <strong>egenskaper</strong>. Fyra viktiga egenskaper är densitet, smältpunkt, kokpunkt och löslighet.", "<strong>Densitet</strong> är hur mycket massa ett ämne har per volym.", "<strong>densitet = massa / volym</strong>",
        "<strong>Exempel:</strong> Ett metallstycke väger 54 g och har volymen 20 cm³. Densiteten är 54 / 20 = 2,7 g/cm³. Det är aluminium."],
  fig="v_vattenforskj.png", figw="70%",
  efter=["Ett föremål <strong>flyter</strong> om dess densitet är lägre än vätskans. Det <strong>sjunker</strong> om den är högre.", TB_DENS,
         "<strong>Smältpunkten</strong> är temperaturen då ett fast ämne blir flytande. Is smälter vid 0 °C. <strong>Kokpunkten</strong> är temperaturen då en vätska kokar. Vatten kokar vid 100 °C.",
         "<strong>Löslighet</strong> säger hur mycket som går att lösa i vatten. Sand löser sig inte. När inget mer kan lösas är lösningen <strong>mättad</strong>."],
  fig2="v_flyta.png", fig2w="95%", n1=2,
  kom="Densitet = massa / volym. Lägre densitet än vätskan: flyter. Högre: sjunker.",
  ova=[("ringa", "Ett föremål har massan 40 g och volymen 5 cm³. Vilken är densiteten?", ["5 g/cm³", "8 g/cm³", "35 g/cm³"]),
       ("sf", "Kryssa i rätt ruta.", ["Is flyter på vatten.", "En järnbult flyter på vatten.", "Vatten kokar vid 100 °C."]),
       ("streck", "Dra streck till rätt mening.", ["Densitet", "Smältpunkt", "Kokpunkt"], ["då en vätska kokar", "massa per volym", "då ett fast ämne blir flytande"]),
       ("skriv", "Ett metallstycke väger 27 g och har volymen 10 cm³. Räkna ut densiteten. Flyter det på vatten?", "Densiteten är", 3)]),

 dict(titel="Partikelmodellen", prog="Delområde 2.1 · Partikelmodellen",
  fore=["<strong>Partikelmodellen</strong> säger tre saker:", "<ol class='st'><li>Allt består av små partiklar.</li><li>Partiklarna rör sig hela tiden.</li><li>Det finns tomrum mellan partiklarna.</li></ol>"],
  fig="v_partikel.png", figw="95%",
  efter=["När ett ämne värms rör sig partiklarna snabbare. Då kan ämnet byta tillstånd: <b>smälta</b>, <b>förånga</b> eller <b>sublimera</b>. När det kyls kan det <b>kondensera</b> eller <b>stelna</b>.",
         "Medan ett ämne smälter eller kokar ligger temperaturen still.", "<strong>Diffusion</strong> är att partiklar sprider sig själva. Därför känner du doften av mat i ett annat rum.",
         "Modellen är en förenkling. Den visar inte krafterna mellan partiklarna eller hur de egentligen ser ut."],
  fig2="v_tillstand.png", fig2w="56%", n1=2,
  kom="Fast: tätt och vibrerar. Vätska: nära och glider. Gas: långt isär och snabbt.",
  ova=[("ringa", "Hur ligger partiklarna i en gas?", ["Långt ifrån varandra", "Tätt i ett mönster", "Alla står stilla"]),
       ("streck", "Dra streck till rätt tillståndsförändring.", ["Fast till vätska", "Vätska till gas", "Gas till vätska"], ["kondensation", "smältning", "förångning"]),
       ("sf", "Kryssa i rätt ruta.", ["Partiklarna rör sig hela tiden.", "Temperaturen stiger medan is smälter.", "Doft sprids genom diffusion."]),
       ("fyll", ["snabbare", "tomrum", "diffusion"], ["Det finns ______________ mellan partiklarna.", "Vid högre temperatur rör sig partiklarna ______________.", "Att partiklar sprider sig kallas ______________."])]),

 dict(titel="Rena ämnen och blandningar", prog="Delområde 2.1 · Rena ämnen och blandningar",
  fore=["Ett <strong>rent ämne</strong> har bara en sorts partikel. En <strong>blandning</strong> har minst två ämnen.", "I en <strong>homogen</strong> blandning ser det likadant ut överallt. I en <strong>heterogen</strong> blandning ser du delarna."],
  fig="v_blandning.png", figw="95%",
  efter=["Saltvatten är en <strong>lösning</strong>. Vatten är <b>lösningsmedel</b> och salt är <b>löst ämne</b>.", "En <strong>legering</strong> är en blandning av metaller. Mässing är koppar och zink.",
         "När du blandar försvinner ingenting. Löser du 5 g salt i 100 g vatten väger lösningen 105 g."],
  kom="Rent ämne: en sorts partikel. Blandning: minst två. Massan bevaras när man blandar.",
  ova=[("ringa", "Vilken blandning är heterogen?", ["Sand i vatten", "Saltvatten", "Luft"]),
       ("sf", "Kryssa i rätt ruta.", ["Saltvatten är en lösning.", "Ett rent ämne har många sorters partiklar.", "En legering är en blandning av metaller."]),
       ("fyll", ["lösningsmedel", "105", "blandning"], ["I saltvatten är vatten ______________.", "5 g salt och 100 g vatten ger ______________ g saltvatten.", "Minst två ämnen är en ______________."]),
       ("skriv", "Ge ett exempel på en blandning du har hemma.", "Ett exempel är", 2)]),

 dict(titel="Labb 2.1 Densitet och flyta eller sjunka", prog="Delområde 2.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Kan man förutsäga om ett föremål flyter genom att räkna ut densiteten?", "Du behöver: våg, mätcylinder, vatten, saltlösning, små föremål, skyddsglasögon."],
  fig="v_labb1.png", figw="95%",
  efter=["<ol class='st'><li>Väg föremålet.</li><li>Mät volymen med vattenförskjutning.</li><li>Räkna ut densiteten.</li><li>Gissa: flyter eller sjunker?</li><li>Prova i vatten.</li><li>Prova ett föremål i saltlösning.</li></ol>", TB_LABB1,
         "<strong>Säkerhet:</strong> Ha skyddsglasögon. Torka upp spill. Använd bara vatten och saltlösning. Smaka inte."],
  kom="Flyter om densiteten är lägre än 1,0 g/cm³ (vattnets densitet).",
  ova=[("fyll", ["massa", "volym", "densitet"], ["Jag vägde föremålets ______________.", "Jag mätte ______________ med vattenförskjutning.", "Jag räknade ut ______________."]),
       ("skriv", "Stämde din gissning? Skriv vad som hände.", "Min gissning", 3),
       ("skriv", "Varför är det lättare att flyta i saltvatten?", "Det beror på", 2)]),

 dict(titel="Filtrering, avdunstning och sedimentering", prog="Delområde 2.2 · Filtrering och avdunstning",
  fore=["Ämnena i en blandning går att <strong>separera</strong>. Hur du gör beror på vad som skiljer dem.", "<strong>Filtrering</strong> skiljer olösligt fast ämne från vätska. Det som blir kvar i filtret är <b>residuet</b>. Vätskan som går igenom är <b>filtratet</b>."],
  fig="v_filtrering.png", figw="70%",
  efter=["Saltet är löst och går igenom filtret. Då kan du <strong>indunsta</strong> vattnet. Vattnet blir ånga och saltet blir kvar.", "<strong>Sedimentering</strong> är att tunga partiklar sjunker till botten. Du kan hälla av vätskan.",
         "Sand, salt och vatten: först filtrering, sedan indunstning."],
  fig2="v_flode.png", fig2w="95%", n1=2,
  kom="Filtrering skiljer fast ämne från vätska. Indunstning ger tillbaka löst ämne.",
  ova=[("ringa", "Vad blir kvar i filtret när du filtrerar sand i vatten?", ["Sanden", "Saltet", "Vattnet"]),
       ("sf", "Kryssa i rätt ruta.", ["Salt går att filtrera bort från saltvatten.", "Vid indunstning blir saltet kvar.", "Filtratet är vätskan som går igenom."]),
       ("fyll", ["residu", "filtrat", "indunsta"], ["Det som blir kvar i filtret är ______________.", "Vätskan som går igenom är ______________.", "För att få tillbaka salt kan du ______________."]),
       ("siffror", "Sätt i ordning. Skriv 1, 2 och 3.", ["Indunsta filtratet", "Blanda sand, salt och vatten", "Filtrera"])]),

 dict(titel="Destillation och kromatografi", prog="Delområde 2.2 · Destillation och kromatografi",
  fore=["<strong>Destillation</strong> skiljer ämnen som har olika kokpunkt. Ämnet med lägst kokpunkt blir gas först. Gasen kyls i en kylare och blir vätska igen.", "Med saltvatten blir bara vattnet gas. Saltet blir kvar. Du får rent vatten."],
  fig="v_destillation.png", figw="95%",
  efter=["Etanol kokar vid 78 °C och vatten vid 100 °C. I en blandning kokar etanol först.", "<strong>Kromatografi</strong> skiljer färger. Vattnet sugs upp i filterpapper och tar med färgerna. Olika färgämnen vandrar olika långt."],
  fig2="v_kromatografi.png", fig2w="95%", n1=2,
  kom="Destillation: olika kokpunkter. Kromatografi: ämnen som vandrar olika långt.",
  ova=[("ringa", "Vilket ämne kokar först i en blandning av etanol och vatten?", ["Etanol", "Vatten", "Båda samtidigt"]),
       ("streck", "Dra streck till rätt metod.", ["Rent vatten från saltvatten", "Se vilka färger en tusch innehåller", "Sand från vatten"], ["filtrering", "destillation", "kromatografi"]),
       ("sf", "Kryssa i rätt ruta.", ["Kylaren gör ångan till vätska.", "Pennstrecket ska vara under vattenytan.", "Olika färger kan vandra olika långt."]),
       ("fyll", ["kylare", "kokpunkter", "papper"], ["Destillation utnyttjar olika ______________.", "Ångan kyls i en ______________.", "Vid kromatografi sugs vattnet upp i ______________."])]),

 dict(titel="Identifiera ämnen och fällning", prog="Delområde 2.2 · Identifiera ämnen och fällning",
  fore=["Man kan <strong>identifiera</strong> ett ämne genom att mäta egenskaper och jämföra med en tabell.", "Ett metallstycke med densiteten 2,7 g/cm³ är troligen aluminium.", "En egenskap räcker sällan. Mät flera."],
  fig=None,
  efter=["En <strong>fällning</strong> är ett fast ämne som bildas när du blandar två klara lösningar. Blandningen blir grumlig.", "Fällning används i reningsverk. Man får fosfat i avloppsvatten att bilda ett fast ämne. Det kan sedan filtreras bort.",
         "En analys kan visa <i>vad</i> som finns, men inte alltid <i>hur mycket</i>. Provet kan också vara förorenat."],
  fig2="v_felling.png", fig2w="95%", n1=2,
  kom="Mät flera egenskaper. En fällning är ett fast ämne som bildas när lösningar blandas.",
  ova=[("ringa", "Varför mäter man flera egenskaper?", ["Flera ämnen kan ha samma värde på en egenskap", "Det är roligare", "En egenskap är alltid fel"]),
       ("sf", "Kryssa i rätt ruta.", ["En fällning är ett fast ämne som bildas.", "En analys säger alltid hur mycket det finns.", "Fällning används för att rena vatten."]),
       ("fyll", ["fällning", "identifiera", "egenskaper"], ["Att ta reda på vad ett ämne är kallas att ______________.", "Man jämför ______________ med en tabell.", "Ett fast ämne som bildas vid blandning är en ______________."]),
       ("skriv", "Du får ett vitt pulver. Hur kan du ta reda på om det är salt eller socker utan att smaka?", "Jag kan", 3)]),

 dict(titel="Labb 2.2 Separera sand, salt och vatten", prog="Delområde 2.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Hur separerar man sand, salt och vatten, och hur mycket får man tillbaka?", "Du behöver: blandning (10 g sand, 5 g salt, 100 ml vatten), våg, tratt, filterpapper, bägare, skål, värmeplatta, tång, skyddsglasögon."],
  fig="v_labb2.png", figw="95%",
  efter=["<ol class='st'><li>Filtrera blandningen.</li><li>Låt sanden torka. Väg den.</li><li>Indunsta filtratet i en skål. Stäng av innan allt vatten är borta.</li><li>Låt skålen svalna. Väg saltet.</li><li>Gör kromatografi med färgpennor som extra uppgift.</li></ol>", TB_LABB2,
         "<strong>Säkerhet:</strong> Ha skyddsglasögon. Skålen blir mycket varm: använd tång. Smaka inget. Samla håret."],
  kom="Först filtrering för sanden. Sedan indunstning för saltet.",
  ova=[("fyll", ["sanden", "saltet", "filtrat"], ["Filtret fångade ______________.", "Vid indunstningen blev ______________ kvar.", "Vätskan som gick igenom är ______________."]),
       ("skriv", "Hur mycket sand och salt fick du tillbaka? Skriv dina värden.", "Jag fick", 2),
       ("skriv", "Varför fick du inte tillbaka exakt allt?", "Det beror på", 2)]),
]

VIKTIGAST = [("l_ic1.png", "Materia är allt som har massa och tar plats. Den finns som fast, flytande och gas."),
             ("l_ic2.png", "Densitet = massa / volym. Lägre densitet än vätskan: flyter."),
             ("l_ic3.png", "Partikelmodellen: allt består av partiklar som rör sig, med tomrum emellan."),
             ("l_ic4.png", "Rent ämne har en sorts partikel. Blandning har minst två. Massan bevaras."),
             ("l_ic5.png", "Filtrering skiljer fast ämne från vätska. Indunstning ger tillbaka löst ämne."),
             ("l_ic6.png", "Destillation utnyttjar olika kokpunkter. Kromatografi skiljer färger."),
             ("l_ic7.png", "Identifiera ett ämne genom att mäta flera egenskaper och jämföra med en tabell."),
             ("l_ic8.png", "En fällning är ett fast ämne som bildas när lösningar blandas.")]
TEST = [("ringa", "Hur ligger partiklarna i ett fast ämne?", ["Tätt i ett mönster", "Långt ifrån varandra", "De rör sig fritt"]),
        ("streck", "Dra streck till rätt förklaring.", ["Densitet", "Filtrering", "Blandning", "Fällning"], ["minst två ämnen", "massa per volym", "ett fast ämne bildas", "skiljer fast från vätska"]),
        ("sf", "Kryssa i rätt ruta.", ["Is flyter på vatten.", "Temperaturen stiger medan is smälter.", "Saltvatten är en homogen blandning.", "Destillation utnyttjar olika kokpunkter.", "Luft är inte materia.", "Mässing är en legering."]),
        ("fyll", ["partiklar", "indunsta", "kondensation"], ["Allt består av ______________.", "Gas som blir vätska kallas ______________.", "För att få tillbaka salt kan du ______________ vattnet."]),
        ("siffror", "Sätt i ordning. Skriv 1, 2, 3 och 4.", ["Indunsta filtratet", "Filtrera", "Blanda sand, salt och vatten", "Väg saltet"]),
        ("skriv", "Räkna ut densiteten för ett föremål med massan 30 g och volymen 10 cm³.", "Densiteten är", 2),
        ("skriv", "Varför flyter is på vatten?", "Det beror på att", 2),
        ("skriv", "Hur kan du få rent vatten från saltvatten?", "Man kan", 3)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 2 (Materia och partiklar): ämnens egenskaper och densitet, partikelmodellen för fast, vätska och gas med tillståndsförändringar, rena ämnen och blandningar, samt separationsmetoderna filtrering, indunstning, destillation och kromatografi, identifiering av ämnen och fällning. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå. Atomer behandlas i kapitel 3.")
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "9 delar (start, sex moment och två labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Samma två delområden som grundtexten.", "Övningar med flera format: ringa in, dra streck, kryssa, fyll i, skriva och sätta i ordning.", "Kom ihåg-ruta i varje moment och en samlad Viktigast-sida."]
HANDLEDNING_HTML = """
<h3>Handledning per moment (lättläst)</h3>
<h3 class="mm">Vad är materia?</h3><p class="hl"><b>E-mål:</b> eleven vet att materia har massa och tar plats och finns som fast, flytande och gas. <b>Vanligt fel:</b> att luft inte är materia.</p>
<h3 class="mm">Ämnen och material</h3><p class="hl"><b>E-mål:</b> eleven räknar ut densitet med formeln och använder den för att avgöra flyta/sjunka. <b>Vanligt fel:</b> att tunga saker alltid sjunker.</p>
<h3 class="mm">Partikelmodellen</h3><p class="hl"><b>E-mål:</b> eleven beskriver hur partiklarna är i fast, vätska och gas och namnger tillståndsförändringarna. <b>Vanligt fel:</b> att partiklarna blir större vid värme.</p>
<h3 class="mm">Rena ämnen och blandningar</h3><p class="hl"><b>E-mål:</b> eleven skiljer rent ämne från blandning och ger exempel. <b>Vanligt fel:</b> att ”rent” betyder ”utan skadliga ämnen”.</p>
<h3 class="mm">Labb 2.1 Densitet och flyta eller sjunka</h3><p class="hl"><b>Material:</b> våg, mätcylinder, vatten, saltlösning (20 g salt i 100 ml vatten), små föremål. <b>Förväntat:</b> metall sjunker, trä och vissa plaster flyter. Luftbubblor på föremålet ger fel volym.</p>
<h3 class="mm">Filtrering, avdunstning och sedimentering</h3><p class="hl"><b>E-mål:</b> eleven väljer filtrering eller indunstning och motiverar. <b>Vanligt fel:</b> att salt kan filtreras bort.</p>
<h3 class="mm">Destillation och kromatografi</h3><p class="hl"><b>E-mål:</b> eleven beskriver kort hur metoderna fungerar. Destillation görs som lärardemo; kromatografi med filterpapper och vattenlösliga pennor.</p>
<h3 class="mm">Identifiera ämnen och fällning</h3><p class="hl"><b>E-mål:</b> eleven förklarar att flera egenskaper behövs och vad en fällning är. <b>Vanligt fel:</b> att en egenskap räcker.</p>
<h3 class="mm">Labb 2.2 Separera sand, salt och vatten</h3><p class="hl"><b>Material:</b> lärarförberedd blandning, tratt, filterpapper, skål, värmeplatta, tång. <b>Förväntat:</b> ca 9–10 g sand och 4–5 g salt. Stäng av värmen innan allt vatten är borta.</p>
"""
FACIT = [
 "<b>Start:</b> 1) Allt som har massa och tar plats. 2) Sant, sant, falskt. 3) fast, gas, partiklar. 4) T.ex. luft eller doft.",
 "<b>Ämnen och material:</b> 1) 40 / 5 = 8 g/cm³ (alternativ 2). 2) Sant, falskt, sant. 3) Densitet – massa per volym; Smältpunkt – då ett fast ämne blir flytande; Kokpunkt – då en vätska kokar. 4) 27 / 10 = 2,7 g/cm³. Det är mer än 1,0, så det sjunker.",
 "<b>Partikelmodellen:</b> 1) Långt ifrån varandra. 2) Fast till vätska – smältning; Vätska till gas – förångning; Gas till vätska – kondensation. 3) Sant, falskt, sant. 4) tomrum, snabbare, diffusion.",
 "<b>Rena ämnen och blandningar:</b> 1) Sand i vatten. 2) Sant, falskt, sant. 3) lösningsmedel, 105, blandning. 4) T.ex. saltvatten, te, jord eller luft.",
 "<b>Labb 2.1:</b> 1) massa, volym, densitet. 2) Egna resultat. 3) Saltvatten har högre densitet än vanligt vatten.",
 "<b>Filtrering, avdunstning och sedimentering:</b> 1) Sanden. 2) Falskt, sant, sant. 3) residu, filtrat, indunsta. 4) Blanda sand, salt och vatten 1; Filtrera 2; Indunsta filtratet 3.",
 "<b>Destillation och kromatografi:</b> 1) Etanol. 2) Rent vatten från saltvatten – destillation; Se vilka färger en tusch innehåller – kromatografi; Sand från vatten – filtrering. 3) Sant, falskt, sant. 4) kokpunkter, kylare, papper.",
 "<b>Identifiera ämnen och fällning:</b> 1) Flera ämnen kan ha samma värde på en egenskap. 2) Sant, falskt, sant. 3) identifiera, egenskaper, fällning. 4) T.ex. mäta löslighet i vatten, smältpunkt eller densitet och jämföra med en tabell.",
 "<b>Labb 2.2:</b> 1) sanden, saltet, filtrat. 2) Egna värden, ca 9–10 g sand och 4–5 g salt. 3) T.ex. sand som fastnat, salt som sprutat eller blivit kvar på bägaren.",
 "<b>Testa dig:</b> 1) Tätt i ett mönster. 2) Densitet – massa per volym; Filtrering – skiljer fast från vätska; Blandning – minst två ämnen; Fällning – ett fast ämne bildas. 3) Sant, falskt, sant, sant, falskt, sant. 4) partiklar, kondensation, indunsta. 5) Blanda sand, salt och vatten 1; Filtrera 2; Indunsta filtratet 3; Väg saltet 4. 6) 30 / 10 = 3 g/cm³. 7) Is har lägre densitet än vatten. 8) Destillera: värm, kyl ångan och samla vattnet. Saltet blir kvar.",
]
