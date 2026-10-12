# -*- coding: utf-8 -*-
"""Område 4 Ekologi – lättläst version (nya ramverket, byggd per moment)."""
FIG = '/tmp/bio/fig04n/'
NR = 4
SLUG = "ekologi"
TAB = "4"
NAMN = "Ekologi"
NDEL = 13
UNDER = "Vem äter vem – och vart tar energin vägen?"
INTRO_L = ["I det här kapitlet lär du dig hur allt i naturen hänger ihop.",
           "Du lär dig vem som äter vem, hur energin och ämnena går runt och varför det finns lagom många djur på en plats.",
           "Namn och siffror i exemplen är påhittade, om inget annat står."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Delområde 4.1 Ekosystem och energi: levande och icke-levande delar, producenter, konsumenter och nedbrytare, näringskedjor och hur energin minskar",
        "Delområde 4.2 Materiens kretslopp: hur ämnen går runt, kolets kretslopp och nedbrytning",
        "Delområde 4.3 Populationer och samspel: hur antalet djur ändras, vad som begränsar dem och hur arter påverkar varandra"]
ORD_FIG = None
ORD_EXTRA = [("ekologi", "läran om hur allt i naturen påverkar varandra"), ("population", "alla djur av en art på en plats"),
             ("ekosystem", "allt levande och icke-levande på en plats, till exempel en sjö"), ("producent", "gör egen mat av solljus, till exempel en växt"),
             ("konsument", "äter andra organismer för att få energi"), ("nedbrytare", "bryter ner det som är dött, till exempel svampar och bakterier"),
             ("näringskedja", "visar vem som äter vem"), ("näringsväv", "många näringskedjor som hänger ihop"),
             ("biomassa", "hur mycket levande material som finns, mätt i vikt"), ("kretslopp", "ämnen som går runt och används om och om igen"),
             ("fotosyntes", "när växter gör mat av solljus, vatten och koldioxid"), ("cellandning", "när celler använder mat och syre för att få energi"),
             ("förna", "döda löv och barr på marken"), ("begränsande faktor", "något som gör att en population inte kan växa mer"),
             ("bärkraft", "så många individer som miljön orkar försörja"), ("konkurrens", "när djur tävlar om samma mat eller plats"),
             ("symbios", "samarbete där båda har nytta"), ("nisch", "artens roll på platsen. Vad den äter och var den lever")]

TB_NIVA = ('<table class="tb"><tr><th>Nivå</th><th>Betyder</th><th>Exempel</th></tr>'
           '<tr><td>Individ</td><td>ett enda djur eller en enda växt</td><td>en hare</td></tr>'
           '<tr><td>Population</td><td>alla individer av en art på en plats</td><td>alla harar i en skog</td></tr>'
           '<tr><td>Ekosystem</td><td>allt levande och icke-levande på en plats</td><td>skogen</td></tr>'
           '<tr><td>Biosfär</td><td>allt liv på jorden</td><td>hela jorden</td></tr></table>')
TB_FAKTOR = ('<table class="tb"><tr><th>Levande (biotiska)</th><th>Icke-levande (abiotiska)</th></tr>'
             '<tr><td>växter, djur, svampar, bakterier</td><td>solljus, vatten, temperatur, luft, jord</td></tr></table>')
TB_ENERGI = ('<table class="tb"><tr><th>Led</th><th>Energi (kJ)</th></tr>'
             '<tr><td>Växter</td><td class="n">10 000</td></tr><tr><td>Växtätare</td><td class="n">1 000</td></tr>'
             '<tr><td>Rovdjur</td><td class="n">100</td></tr></table>')
TB_RIS = ('<table class="tb"><tr><th>Led</th><th>Ris (g) vid 10 %</th></tr>'
          '<tr><td>Producent</td><td class="n">1 000</td></tr><tr><td>Växtätare</td><td class="n">100</td></tr>'
          '<tr><td>Rovdjur</td><td class="n">10</td></tr><tr><td>Toppkonsument</td><td class="n">1</td></tr></table>')
TB_NEDBR = ('<table class="tb"><tr><th>Det här ger snabbare nedbrytning</th><th>Det här ger långsammare</th></tr>'
            '<tr><td>varmt</td><td>kallt</td></tr><tr><td>lagom fuktigt</td><td>för torrt</td></tr>'
            '<tr><td>mycket syre</td><td>lite syre</td></tr><tr><td>mjuka löv</td><td>trä och barr</td></tr></table>')
TB_TE = ('<table class="tb"><tr><th>Plats</th><th>Före (g)</th><th>Efter (g)</th><th>Förlust (%)</th></tr>'
         '<tr><td>Skogsjord</td><td></td><td></td><td></td></tr><tr><td>Gräsmatta</td><td></td><td></td><td></td></tr>'
         '<tr><td>Sand</td><td></td><td></td><td></td></tr></table>')
TB_SAMSPEL = ('<table class="tb"><tr><th>Samspel</th><th>Betyder</th><th>Exempel</th></tr>'
              '<tr><td>Jakt</td><td>Rovdjuret får mat. Bytet dör.</td><td>lodjur och hare</td></tr>'
              '<tr><td>Konkurrens</td><td>Båda förlorar lite.</td><td>rödräv och fjällräv tävlar om mat</td></tr>'
              '<tr><td>Parasitism</td><td>Parasiten har nytta. Värden förlorar.</td><td>fästing på en hund</td></tr>'
              '<tr><td>Symbios</td><td>Båda har nytta.</td><td>lav: svamp och alg</td></tr></table>')

DELOMR = {"4.1": "Ekosystem och energi", "4.2": "Materiens kretslopp", "4.3": "Populationer och samspel"}
DELAR = [
 dict(titel="Vad är ekologi?", prog="Start · Vad är ekologi?",
  fore=["<strong>Ekologi</strong> är läran om hur allt i naturen påverkar varandra.", "Ekologer studerar naturen på olika nivåer. De kan följa en hare. De kan också räkna alla harar i en skog."] + [TB_NIVA],
  fig="l_levande.png",
  efter=["I naturen finns både levande och icke-levande saker.", "Levande: växter, djur, svampar och bakterier. Icke-levande: solljus, vatten, temperatur, luft och jord.",
         "Alla levande saker behöver de icke-levande. Växter behöver till exempel ljus och vatten för att växa."],
  kom="Ekologi är läran om hur allt i naturen påverkar varandra.",
  ova=[("ringa", "Vad är en population?", ["Alla individer av en art på en plats", "Ett enda djur", "Allt liv på jorden"]),
       ("sortera", "Är det levande eller icke-levande? Skriv L eller I i rutan.", ["Gran", "Solljus", "Hare", "Vatten", "Svamp", "Sten"]),
       ("fyll", ["ekologi", "population", "biosfär"], ["Läran om hur allt i naturen påverkar varandra kallas ______________.", "Alla harar i en skog är en ______________.", "Allt liv på jorden kallas ______________."]),
       ("skriv", "Vad behöver du själv från naturen för att leva? Skriv två saker.", "Jag behöver", 2)]),

 dict(titel="Vad är ett ekosystem?", prog="Delområde 4.1 · Vad är ett ekosystem?",
  fore=["Ett <strong>ekosystem</strong> är ett område med allt levande och allt icke-levande som finns där. En skog, en sjö och en äng är ekosystem.", "Det levande kallas <strong>biotiska faktorer</strong>. Det icke-levande kallas <strong>abiotiska faktorer</strong>."] + [TB_FAKTOR],
  fig="l_levande.png", figw="60%",
  efter=["Olika ekosystem ser olika ut. I en öken är det varmt och torrt. I en barrskog är det kallare och det regnar mer. Där finns olika växter och djur.",
         "Men alla ekosystem fungerar på samma sätt. Det finns växter som fångar solenergi. Det finns djur som äter. Och det finns nedbrytare."],
  kom="Ett ekosystem är levande och icke-levande saker på en plats.",
  ova=[("ringa", "Vilken är en abiotisk faktor?", ["Temperatur", "Räv", "Svamp"]),
       ("streck", "Dra streck till rätt grupp.", ["Biotisk", "Abiotisk"], ["vatten och ljus", "djur och växter"]),
       ("kryssa", "Vilka är ekosystem? Kryssa i rätt rutor.", ["En sjö", "En skog", "En ensam sten", "En äng"]),
       ("skriv", "Varför behöver ett ekosystem både levande och icke-levande delar?", "Det behövs eftersom", 2)]),

 dict(titel="Producenter, konsumenter och näringsvävar", prog="Delområde 4.1 · Producenter, konsumenter och näringsvävar",
  fore=["Alla levande saker har ett jobb i ekosystemet. Det finns tre grupper:"],
  fig="l_tre.png", figw="58%",
  efter=["<strong>Producenter</strong> gör egen mat av solljus. Det kallas <strong>fotosyntes</strong>. Växter är producenter.", "<strong>Konsumenter</strong> äter andra organismer. Haren är en växtätare. Räven är ett rovdjur.", "<strong>Nedbrytare</strong> bryter ner det döda. Svampar och bakterier är nedbrytare.",
         "En <strong>näringskedja</strong> visar vem som äter vem. Pilen pekar mot den som äter."],
  fig2="l_kedja.png", fig2w="52%", n1=4,
  efter2=["Men de flesta djur äter flera olika saker. Då hänger många kedjor ihop. Det kallas en <strong>näringsväv</strong>.", "En förändring kan sprida sig. Om en art försvinner kan flera andra arter påverkas. Det kallas en <strong>kaskadeffekt</strong>."],
  fig3="l_vav.png", fig3w="40%",
  kom="Producenter gör mat. Konsumenter äter. Nedbrytare bryter ner det döda. Pilen pekar mot den som äter.",
  ova=[("streck", "Vilken grupp hör de till? Dra streck.", ["Blåbär", "Räv", "Svamp"], ["nedbrytare", "producent", "konsument"]),
       ("siffror", "Sätt näringskedjan i rätt ordning. Börja med producenten. Skriv 1, 2, 3 och 4.", ["Gädda", "Växtplankton", "Djurplankton", "Abborre"]),
       ("ringa", "Titta på näringsväven. Alla sorkar försvinner. Vad händer med räven?", ["Räven får mindre mat", "Räven får mer mat", "Inget händer"]),
       ("sf", "Kryssa i rätt ruta.", ["Pilen pekar mot den som äter.", "Alla djur är producenter.", "Svampar kan vara nedbrytare."]),
       ("skriv3", "Gör en egen näringskedja med tre steg. Skriv namnen.")]),

 dict(titel="Energiflöde och biomassa", prog="Delområde 4.1 · Energiflöde och biomassa",
  fore=["Nästan allt liv får sin energi från <strong>solen</strong>. Växterna fångar solljuset. Sedan går energin vidare när någon äter.", "Men bara en liten del går vidare. Ungefär 10 procent förs vidare till nästa led. Resten blir värme."] + [TB_ENERGI],
  fig="l_pyramid.png",
  efter=["Djuren använder energin till att röra sig och hålla sig varma. Den blir till värme och kommer inte tillbaka.", "Därför är näringskedjor korta. Det finns mest energi hos växterna och minst hos rovdjuren.",
         "<strong>Biomassa</strong> är hur mycket levande material det finns, mätt i vikt. Det finns oftast mest biomassa hos växterna och minst hos rovdjuren."],
  kom="Energin kommer från solen. Ungefär 10 procent går vidare till nästa led. Resten blir värme.",
  ova=[("ringa", "Varifrån kommer energin från början?", ["Solen", "Jorden", "Rävarna"]),
       ("ringa", "Hur mycket energi går vidare till nästa led?", ["Ungefär 10 procent", "Allt", "Ingenting"]),
       ("fyll", ["värme", "solljuset", "biomassa"], ["Växterna fångar ______________.", "Det mesta av energin blir till ______________.", "Vikten av levande material kallas ______________."]),
       ("skriv", "Varför finns det så få rovdjur i en skog?", "Det finns få rovdjur eftersom", 2)]),

 dict(titel="Labb 4.1 Energi i en näringskedja – modellspel", prog="Delområde 4.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Hur mycket energi når det sista ledet i en näringskedja?", "Ni gör en modell. Riset är energi. Varje skål är ett led i kedjan. Ni behöver 1 000 g ris, en våg och fem skålar: Producent, Växtätare, Rovdjur, Toppkonsument och Värme."],
  fig=None,
  efter=["<ol class='st'><li>Väg upp 1 000 g ris i skålen Producent.</li><li>Flytta 10 procent (100 g) till Växtätare. Resten hälls i Värme.</li><li>Flytta 10 procent av växtätarens ris (10 g) till Rovdjur. Resten hälls i Värme.</li><li>Flytta 10 procent av rovdjurets ris (1 g) till Toppkonsument. Resten hälls i Värme.</li><li>Fyll i tabellen.</li></ol>",
         TB_RIS, "<strong>Säkerhet:</strong> Ät inte riset. Torka upp spill så att ingen halkar."],
  kom="Energin minskar för varje led. Det mesta blir värme.",
  ova=[("fyll", ["10", "värme", "1"], ["Varje led får ______________ procent.", "Resten av riset är ______________.", "Toppkonsumenten får bara ______________ gram."]),
       ("skriv", "Hur många gram ris nådde toppkonsumenten?", "Toppkonsumenten fick", 1),
       ("skriv", "Varför kan en näringskedja inte ha tio led?", "Det kan den inte eftersom", 2),
       ("skriv", "Nämn en sak som modellen gör enklare än verkligheten.", "Modellen förenklar", 2)]),

 dict(titel="Materia tillverkas inte och försvinner inte", prog="Delområde 4.2 · Materia tillverkas inte och försvinner inte",
  fore=["Energin försvinner som värme. Men <strong>materien</strong> försvinner inte. Materia är det som allt är byggt av.", "Samma ämnen används om och om igen. Det kallas ett <strong>kretslopp</strong>. Energin går en väg. Ämnena går runt."],
  fig="l_kretslopp.png",
  efter=["Växterna tar upp näring. Djuren äter växterna. Växter och djur dör. Nedbrytarna gör det döda till ny näring.",
         "Många tror att växter blir stora av jord. Så är det inte. På 1600-talet planterade van Helmont ett litet träd i en kruka med jord. Efter fem år hade trädet blivit mycket tyngre. Jorden hade nästan inte blivit lättare.",
         "Trädet byggs mest av <strong>koldioxid från luften</strong> och av vatten."],
  kom="Energi går en väg och blir värme. Ämnen går runt i ett kretslopp. Växter byggs mest av luft och vatten.",
  ova=[("siffror", "Sätt kretsloppet i rätt ordning. Börja med växten. Skriv 1, 2, 3 och 4.", ["Djuret dör", "Växten tar upp näring", "Nedbrytare gör näring", "Ett djur äter växten"]),
       ("sf", "Kryssa i rätt ruta.", ["Ämnen kan användas igen.", "Energi går runt i ett kretslopp.", "Växter byggs mest av jord."]),
       ("fyll", ["kretslopp", "luften", "värme"], ["Ämnen som går runt kallas ett ______________.", "Energi blir till ______________.", "Växten byggs mest av koldioxid från ______________."]),
       ("skriv", "Vad är skillnaden mellan energi och ämnen i naturen?", "Energin", 2)]),

 dict(titel="Kolets kretslopp", prog="Delområde 4.2 · Kolets kretslopp",
  fore=["Kol finns i allt levande. Kolet går runt mellan luften, växter, djur och marken. Det kallas <strong>kolets kretslopp</strong>."],
  fig=None,
  efter=["<ol class='st'><li><strong>Fotosyntes.</strong> Växter tar koldioxid från luften och bygger in kolet i mat.</li><li><strong>Näringskedjan.</strong> Djur äter växterna och får kolet.</li><li><strong>Cellandning.</strong> Växter och djur släpper ut koldioxid när de får energi av maten.</li><li><strong>Nedbrytning.</strong> Nedbrytare gör döda växter och djur till koldioxid.</li><li><strong>Förbränning.</strong> När vi bränner olja, kol och gas släpps koldioxid ut.</li></ol>",
         "När vi bränner olja och kol släpper vi ut mer koldioxid än växterna hinner ta upp. Det påverkar klimatet. Mer om det i område 5."],
  kom="Växter tar koldioxid från luften. Cellandning, nedbrytning och förbränning släpper ut den igen.",
  ova=[("ringa", "Vad tar växterna från luften?", ["Koldioxid", "Syre", "Sten"]),
       ("streck", "Dra streck till rätt förklaring.", ["Fotosyntes", "Cellandning", "Förbränning"], ["släpper ut koldioxid när vi bränner olja", "tar in koldioxid", "släpper ut koldioxid i alla levande"]),
       ("fyll", ["koldioxid", "nedbrytning", "kretslopp"], ["Växter tar in ______________.", "Döda växter bryts ner genom ______________.", "Kolet går runt i ett ______________."]),
       ("skriv", "Vad händer med kolet i ett träd som dör i skogen?", "Kolet", 2)]),

 dict(titel="Nedbrytning", prog="Delområde 4.2 · Nedbrytning",
  fore=["Utan nedbrytning skulle döda löv och djur ligga kvar för alltid. <strong>Nedbrytning</strong> betyder att dött material blir till enkla ämnen som kan användas igen.", "Daggmaskar och gråsuggor äter döda växtdelar och hackar sönder dem. Svampar och bakterier är nedbrytare. De gör resten.", "Döda löv och barr på marken kallas <strong>förna</strong>."],
  fig=None,
  efter=["Nedbrytare släpper ut koldioxid och näring. Växterna tar upp näringen igen.", "Nedbrytningen går olika fort:", TB_NEDBR,
         "I Norrbotten är det kallt och nedbrytningen går långsamt. I regnskogen är det varmt och fuktigt. Där går nedbrytningen mycket fort."],
  kom="Nedbrytare gör det döda till ny näring. Varmt och fuktigt gör att det går fortare.",
  ova=[("ringa", "Vilka är nedbrytare?", ["Svampar och bakterier", "Rävar", "Blåbär"]),
       ("sf", "Kryssa i rätt ruta.", ["Nedbrytning går fortare när det är varmt.", "Nedbrytning går fortast när det är torrt.", "Förna är döda löv och barr."]),
       ("fyll", ["näring", "förna", "kallt"], ["Döda löv och barr kallas ______________.", "Nedbrytare gör ny ______________.", "När det är ______________ går nedbrytningen långsamt."]),
       ("skriv", "Varför är nedbrytare viktiga för växterna?", "De är viktiga eftersom", 2)]),

 dict(titel="Labb 4.2 Nedbrytning i jord", prog="Delområde 4.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> I vilken jord bryts teet ner snabbast?", "Ni gräver ner tepåsar i tre sorters jord och väger dem före och efter. Ni behöver tepåsar, våg, spade och markörer."],
  fig="ekologi-tepasar.png", figw="55%",
  efter=["<ol class='st'><li>Märk och väg varje tepåse. Skriv ner vikten.</li><li>Gräv ner tre påsar i varje jord, 8 cm djupt.</li><li>Låt påsarna ligga kvar tills läraren säger till.</li><li>Gräv upp påsarna. Borsta av dem och låt dem torka.</li><li>Väg igen. Räkna ut hur många procent som har försvunnit.</li></ol>", TB_TE,
         "<strong>Säkerhet:</strong> Tvätta händerna efter jordarbete. Samla in alla påsar och markörer."],
  kom="Där nedbrytarna arbetar bäst försvinner mest av teet.",
  ova=[("fyll", ["tre", "väger", "procent"], ["Vi gräver ner ______________ påsar i varje jord.", "Vi ______________ påsarna före och efter.", "Vi räknar ut hur många ______________ som har försvunnit."]),
       ("skriv", "Var försvann mest te? Skriv din slutsats.", "Mest te försvann i", 2),
       ("skriv", "Varför ska man ha tre påsar i varje jord?", "Man ska ha tre påsar eftersom", 2),
       ("skriv", "Nämn en sak som kan ha gjort att resultatet blev fel.", "En felkälla är", 2)]),

 dict(titel="Populationer och förändring", prog="Delområde 4.3 · Populationer och förändring",
  fore=["En <strong>population</strong> är alla individer av en art på en plats. Antalet ändras hela tiden.", "Fyra saker avgör hur: födda, döda, inflyttning och utflyttning.",
        "Om det föds och flyttar in fler än det dör och flyttar ut, växer populationen. Annars minskar den."],
  fig=None,
  efter=["<span class='fake'>Påhittat exempel</span> I början av året finns det 200 harar i en skog. Under året föds 150. Det dör 120. Det flyttar in 20 och ut 30.", "200 + 150 − 120 + 20 − 30 = 220 harar. Populationen har växt.",
         "<h3>Lämmelår</h3>", "I fjällen varierar antalet lämlar mycket. Vissa år blir de många. Sedan kraschar populationen. Fjällräven äter lämlar. Därför blir det många fjällrävar efter ett lämmelår. Rovdjuren följer bytesdjuren."],
  kom="Födda och inflyttade ökar populationen. Döda och utflyttade minskar den.",
  ova=[("fyll", ["födda", "döda", "fler"], ["Nya individer kallas ______________.", "Individer som dör kallas ______________.", "Om det föds ______________ än det dör växer populationen."]),
       ("ringa", "Det finns 100 harar. Det föds 50 och dör 30. Ingen flyttar. Hur många blir det?", ["120", "80", "180"]),
       ("sf", "Kryssa i rätt ruta.", ["Fjällrävar blir fler efter ett lämmelår.", "Rovdjur och bytesdjur påverkar inte varandra.", "Utflyttning minskar en population."]),
       ("skriv", "Varför kommer många fjällrävar efter ett lämmelår?", "Det beror på att", 2)]),

 dict(titel="Begränsande faktorer", prog="Delområde 4.3 · Begränsande faktorer",
  fore=["Ingen population kan växa för alltid. Förr eller senare tar något slut: mat, vatten eller plats. Det kallas en <strong>begränsande faktor</strong>.", "Så många individer som miljön orkar försörja kallas <strong>bärkraft</strong>."],
  fig=None,
  efter=["Det här kan begränsa en population: mat och vatten, rovdjur, konkurrens, sjukdomar och väder.", "Flera faktorer kan samverka. En snörik vinter gör det svårt för rådjuren att hitta mat. Då svälter många.",
         "Om en population blir större än bärkraften kan den äta upp sin egen mat. Då kan den krascha."],
  kom="Något tar förr eller senare slut. Det begränsar populationen.",
  ova=[("kryssa", "Vad kan begränsa en population? Kryssa i rätt rutor.", ["Brist på mat", "Rovdjur", "Sjukdomar", "Att det är fint väder"]),
       ("ringa", "Vad betyder bärkraft?", ["Så många individer som miljön orkar försörja", "Hur starka djuren är", "Hur många rovdjur som finns"]),
       ("fyll", ["begränsande", "bärkraft", "krascha"], ["Något som sätter en gräns kallas en ______________ faktor.", "Miljöns gräns kallas ______________.", "Blir populationen för stor kan den ______________."]),
       ("skriv", "Du släpper ut 10 kaniner på en ö utan rovdjur. Vad kommer att begränsa dem?", "Det som begränsar dem är", 2)]),

 dict(titel="Konkurrens, jakt och samarbete", prog="Delområde 4.3 · Konkurrens, jakt och samarbete",
  fore=["Arter påverkar varandra på olika sätt:"] + [TB_SAMSPEL],
  fig=None,
  efter=["Varje art har också en <strong>nisch</strong>. Nischen är artens roll: vad den äter, var den söker mat och var den bor. Livsmiljön är som en adress. Nischen är som ett yrke.", "Två arter med samma nisch konkurrerar hårt. Därför har arter som bor på samma plats ofta olika nischer."],
  kom="Arter kan jaga, konkurrera, vara parasiter eller samarbeta. Varje art har en egen nisch.",
  ova=[("streck", "Vilket samspel är det? Dra streck.", ["Lodjur och hare", "Fästing och hund", "Svamp och alg i en lav"], ["symbios", "jakt", "parasitism"]),
       ("ringa", "Vad är en nisch?", ["Artens roll på platsen", "Ett bo", "En sorts föda"]),
       ("fyll", ["konkurrens", "symbios", "nisch"], ["När två arter tävlar om samma mat kallas det ______________.", "När båda arterna har nytta kallas det ______________.", "Artens roll på platsen kallas ______________."]),
       ("skriv", "Varför kan flera fågelarter bo i samma gran?", "De kan det eftersom", 2)]),

 dict(titel="Labb 4.3 Rovdjur–bytesmodell", prog="Delområde 4.3 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Hur ändras antalet rovdjur och bytesdjur?", "Ni gör en modell. Pappersbitar är bytesdjur. Några elever är rovdjur. Ni behöver 40 pappersbitar, ett stoppur, papper och penna."],
  fig=None,
  efter=["<ol class='st'><li>Börja med 20 bytesdjur på bordet och 2 rovdjur.</li><li>Varje rovdjur plockar bytesdjur med pekfinger och tumme i 10 sekunder. Räkna hur många.</li><li>Rovdjur som fångat färre än 3 svälter och slutar. Rovdjur som fångat 6 eller fler får en unge. En ny elev blir rovdjur.</li><li>De bytesdjur som är kvar förökar sig. Lägg dit lika många nya, men aldrig fler än 40 totalt.</li><li>Skriv antalen i en tabell. Gör åtta omgångar.</li></ol>",
         "<strong>Säkerhet:</strong> Ingen får springa. Plocka upp alla pappersbitar efteråt."],
  kom="Rovdjur och bytesdjur påverkar varandra. Antalet svänger upp och ner.",
  ova=[("fyll", ["rovdjur", "byten", "omgångar"], ["Pappersbitarna är ______________.", "Eleverna som plockar är ______________.", "Vi gör åtta ______________."]),
       ("rita", "Rita ett linjediagram. Omgång på x-axeln. Antal på y-axeln. Rita en linje för rovdjur och en för byten."),
       ("skriv", "Vad hände med antalet byten när antalet rovdjur ökade?", "Antalet byten", 2),
       ("skriv", "Nämn en sak som modellen gör enklare än verkligheten.", "Modellen förenklar", 2)]),
]
VIKTIGAST = [("l_ic1.png", "Ekologi är läran om hur allt i naturen påverkar varandra. Ett ekosystem är levande och icke-levande saker på en plats."),
             ("l_ic2.png", "Producenter gör mat. Konsumenter äter. Nedbrytare bryter ner det döda."),
             ("l_ic3.png", "En näringskedja visar vem som äter vem. Många kedjor blir en näringsväv."),
             ("l_ic4.png", "Energin kommer från solen. Ungefär 10 procent går vidare i varje led. Resten blir värme."),
             ("l_ic5.png", "Ämnen går runt i ett kretslopp. Kolet går runt mellan luften, växter, djur och marken."),
             (None, "Nedbrytare gör det döda till ny näring. Varmt och fuktigt ger snabbare nedbrytning."),
             (None, "Populationer ändras. Något tar förr eller senare slut och begränsar dem."),
             (None, "Arter jagar, konkurrerar, är parasiter eller samarbetar. Varje art har en egen nisch.")]
TEST = [("ringa", "Vilken är en producent?", ["Gran", "Räv", "Svamp"]),
        ("streck", "Dra streck till rätt förklaring.", ["Konsument", "Nedbrytare", "Näringsväv", "Kretslopp"], ["ämnen som går runt", "många kedjor som hänger ihop", "bryter ner det döda", "äter andra för att få energi"]),
        ("sf", "Kryssa i rätt ruta.", ["Nästan all energi kommer från solen.", "Det finns fler rovdjur än växter.", "Pilen i en näringskedja pekar mot den som äter.", "Energi går runt i ett kretslopp.", "Nedbrytning går fortare när det är varmt.", "Ingen population kan växa för alltid."]),
        ("rita", "Rita en näringskedja från skogen med tre eller fyra steg. Skriv namnen och rita pilar."),
        ("skriv2", "Många harar blir sjuka och dör. Vad händer med gräset? Vad händer med räven?", ["Gräset", "Räven"]),
        ("skriv", "Varför är nedbrytarna viktiga för växterna?", "Nedbrytarna är viktiga eftersom", 2),
        ("ringa", "Det finns 200 harar. Det föds 100 och dör 80. Ingen flyttar. Hur många blir det?", ["220", "180", "380"]),
        ("skriv", "Varför kan det inte finnas hur många djur som helst på en plats?", "Det kan det inte eftersom", 2)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 4 (Ekologi): ekosystem och faktorer, producenter, konsumenter och nedbrytare, näringskedjor och näringsvävar, energins flöde, "
                "materiens kretslopp (inklusive kolet), nedbrytning samt populationer, begränsande faktorer och samspel mellan arter. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå. Människans påverkan (miljögifter, övergödning, klimat och hållbar utveckling) kommer i område 5.")
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "13 delar (start, nio moment och tre labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Kom ihåg-ruta i varje del med det viktigaste i en mening.", "Övningar direkt efter varje del: ringa in, dra streck, fyll i med ordbank, sant/falskt, kryssa och skriv med meningsstart.",
                "Labbarna är skrivna så att de går att göra med enkel utrustning."]
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
HANDLEDNING_HTML = """
<h3>Handledning per moment</h3>
<h3 class="mm">Start. Vad är ekologi?</h3><p class="hl"><b>Mål:</b> eleven skiljer individ, population, ekosystem och biosfär. <b>Tips:</b> låt eleverna placera skolgården eller en egen favoritplats på nivåerna.</p>
<h3 class="mm">Vad är ett ekosystem?</h3><p class="hl"><b>E-mål:</b> eleven skiljer levande (biotiska) och icke-levande (abiotiska) faktorer. <b>Vanligt fel:</b> eleverna räknar bara djuren som ekosystemet. Betona att det icke-levande hör dit.</p>
<h3 class="mm">Producenter, konsumenter och näringsvävar</h3><p class="hl"><b>E-mål:</b> eleven placerar organismer som producent, konsument eller nedbrytare och ritar en näringskedja. <b>Vanligt fel:</b> pilen ritas åt fel håll. Pilen pekar mot den som äter. <b>Kommentar:</b> kaskadeffekt tas bara upp översiktligt här.</p>
<h3 class="mm">Energiflöde och biomassa</h3><p class="hl"><b>E-mål:</b> eleven vet att energin kommer från solen och att den minskar i varje led. <b>Kommentar:</b> 10 procent är ett genomsnitt. Biomassa är vikten av levande material, inte antal individer.</p>
<h3 class="mm">Labb 4.1 Energi i en näringskedja – modellspel</h3><p class="hl"><b>Material:</b> 1 000 g ris, våg, fem skålar. <b>Förväntat:</b> 1 000, 100, 10 och 1 g. <b>Vanligt fel:</b> eleverna blandar ihop procent och gram. Diskutera vad modellen förenklar.</p>
<h3 class="mm">Materia tillverkas inte och försvinner inte</h3><p class="hl"><b>E-mål:</b> eleven skiljer energins väg (ett flöde som slutar som värme) från ämnenas kretslopp. <b>Vanligt fel:</b> ”växter blir stora av jord”. Van Helmonts försök visar att trädet mest byggdes av vatten och luft.</p>
<h3 class="mm">Kolets kretslopp</h3><p class="hl"><b>E-mål:</b> eleven nämner fotosyntes som tar in koldioxid och cellandning, nedbrytning och förbränning som släpper ut den. Koppla till område 5 (klimat).</p>
<h3 class="mm">Nedbrytning</h3><p class="hl"><b>E-mål:</b> eleven förklarar att nedbrytare gör döda organismer till ny näring och nämner något som påverkar hastigheten. <b>Vanligt fel:</b> ”det ruttnar bort”. Materien försvinner inte, den görs om.</p>
<h3 class="mm">Labb 4.2 Nedbrytning i jord</h3><p class="hl"><b>Material:</b> tepåsar, våg, spade, tre jordtyper. <b>Förväntat:</b> mest viktförlust i fuktig skogsjord, minst i sand. Avvikande värden är en bra start för samtal om felkällor. <b>Bonuslabb:</b> Småkryp i förnan.</p>
<h3 class="mm">Populationer och förändring</h3><p class="hl"><b>E-mål:</b> eleven räknar ut förändringen med födda, döda, inflyttning och utflyttning. <b>Facit till hararna:</b> 200 + 150 − 120 + 20 − 30 = 220.</p>
<h3 class="mm">Begränsande faktorer</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på faktorer som begränsar en population och vet vad bärkraft är. <b>Vanligt fel:</b> eleverna tror att bärkraften är fast. Den ändras med väder och mat.</p>
<h3 class="mm">Konkurrens, jakt och samarbete</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på jakt, konkurrens, parasitism och symbios och förklarar nisch med egna ord. <b>Vanligt fel:</b> nisch och livsmiljö blandas ihop.</p>
<h3 class="mm">Labb 4.3 Rovdjur–bytesmodell</h3><p class="hl"><b>Material:</b> 40 pappersbitar eller bönor, stoppur. <b>Förväntat:</b> resultaten varierar. Ofta dör bytena ut eller rovdjuren svälter i början. Justera reglerna så att kurvorna svänger. Jämför med lämmelåren i grundtexten.</p>
"""
FACIT = [
 "<b>Start:</b> 1) Alla individer av en art på en plats. 2) Gran L, Solljus I, Hare L, Vatten I, Svamp L, Sten I. 3) ekologi, population, biosfär. 4) T.ex. mat, vatten, luft.",
 "<b>Vad är ett ekosystem?:</b> 1) Temperatur. 2) Biotisk – djur och växter; abiotisk – vatten och ljus. 3) En sjö, en skog, en äng. 4) Levande delar behöver de icke-levande, till exempel ljus och vatten.",
 "<b>Producenter, konsumenter och näringsvävar:</b> 1) Blåbär – producent; Räv – konsument; Svamp – nedbrytare. 2) Växtplankton 1, Djurplankton 2, Abborre 3, Gädda 4. 3) Räven får mindre mat. 4) Sant, falskt, sant. 5) T.ex. gräs, hare, räv.",
 "<b>Energiflöde och biomassa:</b> 1) Solen. 2) Ungefär 10 procent. 3) solljuset, värme, biomassa. 4) Energin minskar i varje led, så det räcker bara till få rovdjur.",
 "<b>Labb 4.1:</b> 1) 10, värme, 1. 2) 1 gram. 3) Energin minskar så mycket i varje led att det inte räcker till fler. 4) T.ex. att verkliga djur äter flera sorters föda eller att procenten varierar.",
 "<b>Materia tillverkas inte och försvinner inte:</b> 1) Djuret dör 3, Växten tar upp näring 1, Nedbrytare gör näring 4, Ett djur äter växten 2. 2) Sant, falskt, falskt. 3) kretslopp, värme, luften. 4) Energin går en väg och blir värme. Ämnena används om och om igen.",
 "<b>Kolets kretslopp:</b> 1) Koldioxid. 2) Fotosyntes – tar in koldioxid; Cellandning – släpper ut koldioxid i alla levande; Förbränning – släpper ut koldioxid när vi bränner olja. 3) koldioxid, nedbrytning, kretslopp. 4) Nedbrytare gör om det till koldioxid och näring.",
 "<b>Nedbrytning:</b> 1) Svampar och bakterier. 2) Sant, falskt, sant. 3) förna, näring, kallt. 4) De gör döda växter och djur till ny näring som växterna kan ta upp.",
 "<b>Labb 4.2:</b> 1) tre, väger, procent. 2) T.ex. ”Mest te försvann i skogsjord”. 3) För att slumpen mellan enskilda påsar ska jämnas ut. 4) T.ex. att påsarna låg olika djupt eller att jorden var olika fuktig.",
 "<b>Populationer och förändring:</b> 1) födda, döda, fler. 2) 120. 3) Sant, falskt, sant. 4) Fjällräven äter lämlar och får många valpar när det finns mycket mat.",
 "<b>Begränsande faktorer:</b> 1) Brist på mat, rovdjur, sjukdomar. 2) Så många individer som miljön orkar försörja. 3) begränsande, bärkraft, krascha. 4) T.ex. maten tar slut.",
 "<b>Konkurrens, jakt och samarbete:</b> 1) Lodjur och hare – jakt; Fästing och hund – parasitism; Svamp och alg i en lav – symbios. 2) Artens roll på platsen. 3) konkurrens, symbios, nisch. 4) De söker mat på olika ställen i granen och har olika nischer.",
 "<b>Labb 4.3:</b> 1) byten, rovdjur, omgångar. 2) Eget diagram med två linjer. 3) T.ex. ”Antalet byten minskade när rovdjuren blev fler”. 4) T.ex. att bytena inte kan gömma sig.",
 "<b>Testa dig:</b> 1) Gran. 2) Konsument – äter andra för att få energi; Nedbrytare – bryter ner det döda; Näringsväv – många kedjor som hänger ihop; Kretslopp – ämnen som går runt. 3) Sant, falskt, sant, falskt, sant, sant. 4) T.ex. gräs, hare, räv (pilar mot den som äter). 5) Gräset växer mer, räven får mindre mat och kan bli färre. 6) De gör döda växter och djur till ny näring som växterna tar upp. 7) 220. 8) Något tar förr eller senare slut, till exempel mat eller plats.",
]
