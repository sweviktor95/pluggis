# -*- coding: utf-8 -*-
"""Område 3 Biologisk mångfald – lättläst version (nya ramverket, byggd per moment)."""
FIG = '/tmp/bio/fig03n/'
NR = 3
SLUG = "mangfald"
TAB = "3"
NAMN = "Biologisk mångfald"
NDEL = 9
UNDER = "Livets variation – och varför vi behöver den"
INTRO_L = ["I det här kapitlet lär du dig vad biologisk mångfald är.",
           "Du lär dig vad naturen gör för oss, vad som hotar den och hur forskare delar in allt levande i grupper. Du lär dig också att använda en nyckel för att bestämma träd.",
           "Namn och siffror i exemplen är påhittade, om inget annat står."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Start: vad biologisk mångfald är",
        "Delområde 3.1 Mångfald, hot och ekosystemtjänster: tre nivåer, vad naturen gör för oss och vad som hotar den",
        "Delområde 3.2 Gruppera och organismvärlden: riken, bestämningsnyckel och anpassningar"]
ORD_FIG = None
ORD_EXTRA = [("biologisk mångfald", "all variation av liv: gener, arter och ekosystem"), ("gen", "en del av arvsmassan som bestämmer en egenskap"), ("art", "en sort av växt, djur eller svamp"),
             ("population", "alla individer av en art i ett område"), ("ekosystem", "alla växter, djur och svampar i ett område och miljön de lever i"),
             ("ekosystemtjänst", "något naturen gör som vi har nytta av"), ("pollinering", "när pollen flyttas mellan blommor så att de kan bilda frön"),
             ("producent", "gör egen mat, till exempel en växt"), ("konsument", "äter andra organismer"), ("nedbrytare", "bryter ner döda växter och djur"),
             ("näringsväv", "många näringskedjor som hänger ihop"), ("rödlista", "lista över arter som kan dö ut"), ("invasiv art", "en främmande art som sprider sig och skadar naturen"),
             ("signalart", "en art som visar att miljön är värdefull"), ("rike", "en stor grupp av organismer, till exempel djur eller svampar"), ("lav", "en svamp och en alg som lever ihop"),
             ("bestämningsnyckel", "en serie val som leder till artens namn"), ("anpassning", "ett drag som hjälper en art att klara sin miljö"),
             ("naturligt urval", "de som passar bäst i miljön överlever och får fler ungar"), ("variation", "skillnader mellan individer av samma art")]

TB_NIVA = ('<table class="tb"><tr><th>Nivå</th><th>Exempel</th></tr>'
           '<tr><td>Gener</td><td>Tallar med olika gener</td></tr><tr><td>Arter</td><td>Tall, gran, räv, flugsvamp</td></tr>'
           '<tr><td>Ekosystem</td><td>Fjäll, skog, myr, älv</td></tr></table>')
TB_TJANST = ('<table class="tb"><tr><th>Typ</th><th>Exempel</th></tr>'
             '<tr><td>Försörjande</td><td>Bär, fisk, virke</td></tr><tr><td>Reglerande</td><td>Bin pollinerar. Myren renar vatten.</td></tr>'
             '<tr><td>Stödjande</td><td>Bördig jord, fotosyntes</td></tr><tr><td>Kulturella</td><td>Friluftsliv, fiske</td></tr></table>')
TB_HOT = ('<table class="tb"><tr><th>Hot</th><th>Exempel</th></tr>'
          '<tr><td>Ändrad markanvändning</td><td>Skog avverkas</td></tr><tr><td>Överuttag</td><td>Överfiske</td></tr>'
          '<tr><td>Klimatförändringar</td><td>Det blir varmare</td></tr><tr><td>Föroreningar</td><td>Plast i havet</td></tr>'
          '<tr><td>Invasiva arter</td><td>Blomsterlupin</td></tr></table>')
TB_RIKE = ('<table class="tb"><tr><th>Rike</th><th>Exempel</th><th>Näring</th></tr>'
           '<tr><td>Djur</td><td>Räv, älg</td><td>Äter andra</td></tr><tr><td>Växter</td><td>Tall, blåbär</td><td>Fotosyntes</td></tr>'
           '<tr><td>Svampar</td><td>Flugsvamp</td><td>Tar från död materia</td></tr><tr><td>Bakterier</td><td>Tarmbakterier</td><td>Olika sätt</td></tr>'
           '<tr><td>Encelliga med kärna</td><td>Amöba</td><td>Olika sätt</td></tr></table>')
TB_PROV = ('<table class="tb"><tr><th>Plats</th><th>Ruta 1</th><th>Ruta 2</th><th>Ruta 3</th></tr>'
           '<tr><td>Äng</td><td></td><td></td><td></td></tr><tr><td>Gräsmatta</td><td></td><td></td><td></td></tr></table>')
TB_TRAD = ('<table class="tb"><tr><th>Träd</th><th>Kännetecken</th><th>Namn</th></tr>'
           '<tr><td>1</td><td></td><td></td></tr><tr><td>2</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td></tr></table>')

DELOMR = {"3.1": "Mångfald, hot och ekosystemtjänster", "3.2": "Gruppera och organismvärlden"}
DELAR = [
 dict(titel="Vad är biologisk mångfald?", prog="Start · Vad är biologisk mångfald?",
  fore=["Hur många olika sorters liv finns i en skog? Det är <strong>biologisk mångfald</strong>.", "Forskare har hittat drygt två miljoner arter. Ingen vet hur många som finns totalt."],
  fig="mangfald-tre-nivaer.png", figw="90%",
  efter=["Mångfald är mer än antalet arter. Den finns på tre nivåer: <strong>gener</strong>, <strong>arter</strong> och <strong>ekosystem</strong>."],
  kom="Biologisk mångfald är variationen av liv. Den finns som gener, arter och ekosystem.",
  ova=[("ringa", "Vad betyder biologisk mångfald?", ["Variationen av liv", "Bara antalet djur", "Bara växter"]),
       ("sf", "Kryssa i rätt ruta.", ["Ingen vet exakt hur många arter det finns.", "Mångfald betyder bara antal arter.", "Skogen har många olika arter."]),
       ("fyll", ["mångfald", "arter", "ekosystem"], ["Biologisk ______________ är variationen av liv.", "Tall och gran är olika ______________.", "En skog och en myr är olika ______________."]),
       ("skriv", "Nämn tre arter som finns nära dig.", "Tre arter är", 2)]),

 dict(titel="Gener, arter och ekosystem", prog="Delområde 3.1 · Gener, arter och ekosystem",
  fore=["Mångfald finns på tre nivåer.", TB_NIVA],
  fig=None,
  efter=["<strong>Gener:</strong> Alla tallar är samma art, men deras gener är lite olika. Då kan någon tall klara torka eller kyla bättre.",
         "<strong>Arter:</strong> En <strong>art</strong> är individer som kan få ungar tillsammans. Alla individer av en art i ett område kallas en <strong>population</strong>.",
         "<strong>Ekosystem:</strong> Fjäll, skog och myr är olika ekosystem. Varje ekosystem har sina egna arter.",
         "Ett ekosystem med många arter klarar förändringar bättre. Om det blir färre sork kan räven äta något annat."],
  fig2="mangfald-naringsvav.png", fig2w="85%",
  kom="Mångfald finns som gener, arter och ekosystem. Många arter gör ekosystemet starkare.",
  ova=[("streck", "Dra streck till rätt nivå.", ["Gener", "Arter", "Ekosystem"], ["myr och skog", "tall och gran", "olika tallar"]),
       ("sf", "Kryssa i rätt ruta.", ["Alla individer av en art är exakt lika.", "Fler arter gör ett ekosystem starkare.", "Räven kan äta olika djur."]),
       ("fyll", ["population", "art", "gener"], ["Alla tallar i en skog är en ______________.", "Tall är en ______________.", "Tallar skiljer sig lite i sina ______________."]),
       ("skriv", "Varför är många arter bra för ett ekosystem?", "Det är bra eftersom", 2)]),

 dict(titel="Ekosystemtjänster", prog="Delområde 3.1 · Ekosystemtjänster",
  fore=["Naturen gör saker som vi har nytta av. Det kallas <strong>ekosystemtjänster</strong>.", TB_TJANST],
  fig="ekotjanster.png", figw="95%",
  efter=["Bin och humlor <strong>pollinerar</strong> blommor. Då kan blommorna bilda frön och bär. Utan pollinerare blir det mindre mat.",
         "Myrar tar upp vatten som en svamp. De renar vattnet och minskar översvämningar.",
         "Många olika arter gör tjänsterna säkrare. Om en art får det svårt kan andra ta över."],
  kom="Ekosystemtjänster är sådant naturen gör som vi har nytta av. Det finns fyra typer.",
  ova=[("streck", "Dra streck till rätt typ.", ["Försörjande", "Reglerande", "Stödjande", "Kulturella"], ["friluftsliv", "bär och fisk", "bördig jord", "bin pollinerar"]),
       ("ringa", "Vad gör en myr?", ["Renar vatten", "Gör ljus", "Tar bort alla arter"]),
       ("sf", "Kryssa i rätt ruta.", ["Pollinering behövs för många bär.", "Naturens tjänster kostar alltid pengar.", "Fler arter gör tjänsterna säkrare."]),
       ("skriv", "Ge ett exempel på en ekosystemtjänst.", "Ett exempel är", 2)]),

 dict(titel="Hoten mot mångfalden", prog="Delområde 3.1 · Hoten mot mångfalden",
  fore=["Arter dör ut i dag mycket snabbare än förr. FN:s experter säger att cirka en miljon arter är hotade. Orsaken är oftast människan.", TB_HOT],
  fig=None,
  efter=["Forskare gör en <strong>rödlista</strong>. Den visar vilka arter i Sverige som kan försvinna. I Rödlistan 2025 var 5 217 arter rödlistade.",
         "<strong>Fjällräven</strong> är hotad. Den jagades förr. Nu har den svårt att få mat, och rödräven tränger undan den.",
         "<strong>Gammal skog</strong> är hem för många arter. Garnlav är en <strong>signalart</strong>. Den visar att skogen är gammal och värdefull."],
  fig2="mangfald-fjallrav-rodrav.png", fig2w="80%",
  efter2=["Vi kan skydda arter med nationalparker och naturreservat. Vi kan också välja hållbart fiskad mat och låta en del av gräsmattan bli äng."],
  kom="Hoten är ändrad markanvändning, överuttag, klimatförändringar, föroreningar och invasiva arter. Rödlistan visar vilka arter som är hotade.",
  ova=[("ringa", "Vad visar rödlistan?", ["Vilka arter som kan dö ut", "Vilka arter som är störst", "Vilka arter som är farliga"]),
       ("sf", "Kryssa i rätt ruta.", ["Överfiske är ett hot.", "Garnlav visar att skogen är gammal.", "Alla arter är lika vanliga."]),
       ("fyll", ["klimatet", "skog", "invasiv"], ["Om ______________ blir varmare måste arter flytta.", "När gammal ______________ avverkas försvinner livsmiljöer.", "Blomsterlupin är en ______________ art."]),
       ("skriv", "Nämn två hot mot mångfalden.", "Två hot är", 2)]),

 dict(titel="Labb 3.1 Artinventering i en provruta", prog="Delområde 3.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Finns det fler växtarter på en äng än på en klippt gräsmatta?", "Du behöver: fyra pinnar, snöre, tumstock, mobil och papper."],
  fig="mangfald-provruta.png", figw="60%",
  efter=["<ol class='st'><li>Märk ut en ruta på 1 × 1 meter på ängen.</li><li>Räkna hur många olika växtarter som finns. Ta bilder och ge dem nummer.</li><li>Gör likadant på gräsmattan.</li><li>Gör tre rutor på varje plats.</li><li>Skriv resultatet i tabellen.</li></ol>", TB_PROV,
         "<strong>Säkerhet:</strong> Smaka inte på växter. Följ allemansrätten. Tvätta händerna efteråt."],
  kom="Man räknar i flera rutor för att få ett säkrare resultat.",
  ova=[("fyll", ["fler", "rutor", "arter"], ["Vi räknade ______________ som fanns i rutan.", "Vi gjorde tre ______________ på varje plats.", "Ängen hade ______________ arter än gräsmattan."]),
       ("skriv", "Stämde din gissning? Skriv vad som hände.", "Min gissning", 2),
       ("skriv", "Varför gör vi tre rutor och inte bara en?", "Vi gör tre rutor eftersom", 2)]),

 dict(titel="Rikena", prog="Delområde 3.2 · Rikena",
  fore=["Forskare delar in allt levande i grupper. De största grupperna kallas <strong>riken</strong>.", TB_RIKE],
  fig="rikena.png", figw="95%",
  efter=["Svampar är inte växter. De gör ingen fotosyntes. De bryter ner döda växter och djur.",
         "En <strong>lav</strong> är en svamp och en alg som lever ihop. De hjälper varandra.",
         "Varje art har ett <strong>vetenskapligt namn</strong> med två ord på latin. Tall heter <i>Pinus sylvestris</i>."],
  kom="Det finns fem riken: djur, växter, svampar, bakterier och encelliga organismer med cellkärna.",
  ova=[("streck", "Dra streck till rätt rike.", ["Räv", "Tall", "Flugsvamp", "Tarmbakterie"], ["Svampar", "Bakterier", "Växter", "Djur"]),
       ("sf", "Kryssa i rätt ruta.", ["Svampar är växter.", "En lav är en svamp och en alg.", "Varje art har ett latinskt namn."]),
       ("ringa", "Vilket rike gör fotosyntes?", ["Växter", "Djur", "Svampar"]),
       ("skriv", "Nämn tre av de fem rikena.", "Tre riken är", 2)]),

 dict(titel="Bestämningsnycklar", prog="Delområde 3.2 · Bestämningsnycklar",
  fore=["En <strong>bestämningsnyckel</strong> hjälper dig att ta reda på vad en art heter. Du gör ett val i taget med två alternativ."],
  fig="nyckel.png", figw="95%",
  efter=["Så gör du:", "<ol class='st'><li>Titta noga på trädet.</li><li>Läs det första valet. Vilket alternativ stämmer?</li><li>Följ pilen till nästa val.</li><li>Fortsätt tills du kommer fram till ett namn.</li><li>Kontrollera i en bok eller app.</li></ol>"],
  kom="En bestämningsnyckel leder dig steg för steg till artens namn. Du jämför kännetecken.",
  ova=[("ringa", "Vad är en bestämningsnyckel?", ["En serie val som leder till artens namn", "En nyckel till en dörr", "En lista på alla djur"]),
       ("sf", "Kryssa i rätt ruta.", ["Man väljer mellan två alternativ i taget.", "Man gissar utan att titta.", "Man kontrollerar svaret i en bok."]),
       ("fyll", ["barr", "kännetecken", "nyckeln"], ["Tall och gran har ______________.", "Man jämför ______________ på växten.", "Man följer ______________ steg för steg."]),
       ("skriv", "Vilket träd har barr som sitter ensamma runt kvisten? Använd nyckeln.", "Trädet är", 1)]),

 dict(titel="Anpassningar", prog="Delområde 3.2 · Anpassningar",
  fore=["En <strong>anpassning</strong> är ett drag som hjälper en art att klara sin miljö.", "Fjällräven har tjock päls och små öron. Då fryser den inte lika lätt. Renen har breda klövar som bär på snö."],
  fig=None,
  efter=["Individer av en art är inte exakt lika. Det kallas <strong>variation</strong>.", "De som passar bäst i miljön överlever oftare och får fler ungar. Draget går i arv. Det kallas <strong>naturligt urval</strong>.",
         "Exempel: ljusa fjärilar syns inte på ljus bark. Fåglarna tar de mörka först. Då blir de ljusa fler."],
  fig2="urval.png", fig2w="95%",
  kom="Anpassningar uppstår genom naturligt urval under många generationer. En individ bestämmer inte själv.",
  ova=[("ringa", "Vad är en anpassning?", ["Ett drag som hjälper arten i sin miljö", "En sjukdom", "Ett namn"]),
       ("sf", "Kryssa i rätt ruta.", ["Individer av samma art är olika.", "En individ väljer sin anpassning.", "Drag som passar blir vanligare."]),
       ("fyll", ["urval", "variation", "ungar"], ["Skillnader mellan individer kallas ______________.", "De som passar bäst får fler ______________.", "Det kallas naturligt ______________."]),
       ("skriv", "Ge ett exempel på en anpassning.", "Ett exempel är", 2)]),

 dict(titel="Labb 3.2 Artbestämning med nyckel", prog="Delområde 3.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Vilka träd finns på skolgården?", "Du behöver: nyckeln, mobil och papper."],
  fig=None,
  efter=["<ol class='st'><li>Välj ett träd. Ta bilder på trädet, barken och bladen.</li><li>Följ nyckeln steg för steg.</li><li>Skriv namnet på trädet.</li><li>Gör samma sak med tre träd till.</li><li>Skriv resultatet i tabellen.</li></ol>", TB_TRAD,
         "<strong>Säkerhet:</strong> Smaka inte på växter eller bär. Tvätta händerna efteråt."],
  kom="Kontrollera alltid namnet i en bok eller app.",
  ova=[("fyll", ["nyckeln", "kännetecken", "bilder"], ["Jag följde ______________ steg för steg.", "Jag tittade på trädets ______________.", "Jag tog ______________ för att komma ihåg."]),
       ("skriv", "Vilka träd hittade du?", "Jag hittade", 2),
       ("skriv", "Var något svårt? Skriv vad.", "Det var svårt att", 2)]),
]

VIKTIGAST = [("l_ic1.png", "Biologisk mångfald är variationen av liv: gener, arter och ekosystem."),
             ("l_ic2.png", "Ekosystemtjänster är sådant naturen gör som vi har nytta av. Det finns fyra typer."),
             ("l_ic3.png", "Hoten är ändrad markanvändning, överuttag, klimatförändringar, föroreningar och invasiva arter. Rödlistan visar hotade arter."),
             ("l_ic4.png", "Fjällräven och gammal skog är exempel på mångfald som behöver skydd i Norrbotten."),
             ("l_ic5.png", "Det finns fem riken. En bestämningsnyckel leder till artens namn."),
             ("l_ic6.png", "Anpassningar uppstår genom naturligt urval under många generationer.")]
TEST = [("ringa", "Vad är genetisk mångfald?", ["Variation i gener inom en art", "Antalet ekosystem", "Antalet individer"]),
        ("streck", "Dra streck till rätt förklaring.", ["Art", "Population", "Ekosystem", "Rödlista"], ["lista över hotade arter", "alla individer av en art i ett område", "arter och miljö tillsammans", "individer som kan få ungar"]),
        ("sf", "Kryssa i rätt ruta.", ["Bin pollinerar blommor.", "Svampar är växter.", "Överfiske är ett hot.", "En individ väljer sin anpassning.", "Garnlav är en signalart.", "En nyckel har två alternativ i varje steg."]),
        ("fyll", ["rödlistan", "ekosystemtjänst", "bestämningsnyckel"], ["Forskarna visar hotade arter i ______________.", "Pollinering är en ______________.", "Med en ______________ kan man bestämma en art."]),
        ("siffror", "Sätt i ordning. Skriv 1, 2, 3 och 4.", ["Individerna som passar bäst får fler ungar", "Individerna är olika", "Draget blir vanligare", "Några passar miljön bättre"]),
        ("skriv", "Varför är många arter bra för naturen?", "Många arter är bra eftersom", 3),
        ("ringa", "Vilket rike gör fotosyntes?", ["Växter", "Djur", "Svampar"]),
        ("skriv", "Ge ett exempel på ett hot mot mångfalden.", "Ett hot är", 2)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 3 (Biologisk mångfald): tre nivåer av mångfald, ekosystemtjänster, hot mot mångfalden och rödlistan, hur organismer delas in i riken, bestämningsnyckel samt anpassning och naturligt urval i ord. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå. Näringsvävar och kretslopp fördjupas i kapitel 4 och evolution i kapitel 9.")
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "9 delar (start, sex moment och två labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Samma tre delområden som grundtexten.", "Övningar med flera format: ringa in, dra streck, kryssa, fyll i, skriva och rita.", "Kom ihåg-ruta i varje moment och en samlad Viktigast-sida."]
HANDLEDNING_HTML = """
<h3>Handledning per moment (lättläst)</h3>
<h3 class="mm">Vad är biologisk mångfald?</h3><p class="hl"><b>E-mål:</b> eleven vet att biologisk mångfald är variationen av liv och nämner de tre nivåerna. <b>Vanligt fel:</b> att mångfald bara är antalet arter.</p>
<h3 class="mm">Gener, arter och ekosystem</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på varje nivå och förklarar enkelt varför många arter gör ett ekosystem starkare. <b>Vanligt fel:</b> att alla individer av en art är lika.</p>
<h3 class="mm">Ekosystemtjänster</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på de fyra typerna. <b>Vanligt fel:</b> att tjänsterna bara är sådant man kan köpa.</p>
<h3 class="mm">Hoten mot mångfalden</h3><p class="hl"><b>E-mål:</b> eleven nämner hot med exempel och vet vad rödlistan visar. <b>Vanligt fel:</b> att rödlistan visar vilka arter som redan är utdöda.</p>
<h3 class="mm">Labb 3.1 Artinventering i en provruta</h3><p class="hl"><b>Material:</b> pinnar, snöre, tumstock, mobil. <b>Förväntat:</b> oftast fler arter på ängen. <b>Vanliga fel:</b> rutorna läggs olika, arter räknas dubbelt. Planera på sommarhalvåret.</p>
<h3 class="mm">Rikena</h3><p class="hl"><b>E-mål:</b> eleven nämner de fem rikena och skiljer svamp från växt. <b>Vanligt fel:</b> ”svampar är växter”.</p>
<h3 class="mm">Bestämningsnycklar</h3><p class="hl"><b>E-mål:</b> eleven använder en färdig nyckel. <b>Vanligt fel:</b> att eleven väljer efter känsla i stället för kännetecken.</p>
<h3 class="mm">Anpassningar</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på anpassningar och beskriver naturligt urval med enkla ord. <b>Vanligt fel:</b> att individer anpassar sig medvetet.</p>
<h3 class="mm">Labb 3.2 Artbestämning med nyckel</h3><p class="hl"><b>Material:</b> nyckeln, mobil, träd i närheten. <b>Förväntat:</b> tall, gran, björk, asp eller rönn. Planera efter vilka träd som finns vid skolan.</p>
"""
FACIT = [
 "<b>Start:</b> 1) Variationen av liv. 2) Sant, falskt, sant. 3) mångfald, arter, ekosystem. 4) Egna exempel.",
 "<b>Gener, arter och ekosystem:</b> 1) Gener – olika tallar; Arter – tall och gran; Ekosystem – myr och skog. 2) Falskt, sant, sant. 3) population, art, gener. 4) Fler arter kan ta över om en art försvinner.",
 "<b>Ekosystemtjänster:</b> 1) Försörjande – bär och fisk; Reglerande – bin pollinerar; Stödjande – bördig jord; Kulturella – friluftsliv. 2) Renar vatten. 3) Sant, falskt, sant. 4) T.ex. pollinering, vattenrening, bär, friluftsliv.",
 "<b>Hoten mot mångfalden:</b> 1) Vilka arter som kan dö ut. 2) Sant, sant, falskt. 3) klimatet, skog, invasiv. 4) T.ex. överfiske och avverkad skog.",
 "<b>Labb 3.1:</b> 1) arter, rutor, fler. 2) Egna resultat. 3) För att få ett säkrare resultat.",
 "<b>Rikena:</b> 1) Räv – Djur; Tall – Växter; Flugsvamp – Svampar; Tarmbakterie – Bakterier. 2) Falskt, sant, sant. 3) Växter. 4) T.ex. djur, växter, svampar.",
 "<b>Bestämningsnycklar:</b> 1) En serie val som leder till artens namn. 2) Sant, falskt, sant. 3) barr, kännetecken, nyckeln. 4) Gran.",
 "<b>Anpassningar:</b> 1) Ett drag som hjälper arten i sin miljö. 2) Sant, falskt, sant. 3) variation, ungar, urval. 4) T.ex. fjällrävens tjocka päls eller renens breda klövar.",
 "<b>Labb 3.2:</b> 1) nyckeln, kännetecken, bilder. 2) Egna resultat, t.ex. tall, gran, björk. 3) Egna svar.",
 "<b>Testa dig:</b> 1) Variation i gener inom en art. 2) Art – individer som kan få ungar; Population – alla individer av en art i ett område; Ekosystem – arter och miljö tillsammans; Rödlista – lista över hotade arter. 3) Sant, falskt, sant, falskt, sant, sant. 4) rödlistan, ekosystemtjänst, bestämningsnyckel. 5) Individerna är olika 1; Några passar miljön bättre 2; Individerna som passar bäst får fler ungar 3; Draget blir vanligare 4. 6) Fler arter kan ta över om en art försvinner, så naturen klarar förändringar bättre. 7) Växter. 8) T.ex. avverkad skog eller överfiske.",
]
