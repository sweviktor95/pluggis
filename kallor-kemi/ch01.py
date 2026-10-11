# -*- coding: utf-8 -*-
# Kemi kapitel 1: Kemi och vetenskap (åk 7–9)
T = dict(
 nr=1, namn="Kemi och vetenskap", under="Vad kemi är, hur man undersöker systematiskt, kemins modeller och historia samt hur man granskar information",
 kort="Kemi · Kapitel 1", fil="kemi-01-kemi-och-vetenskap", arskurs="7–9", nodeid="kemi-vetenskap",
 mal=["förklara vad kemi är och ge exempel på kemi i vardagen, i naturen, i samhället och i kroppen",
      "skilja mellan ämne, material och blandning och förklara vad ordet kemikalie betyder",
      "formulera en undersökbar fråga och planera en rättvis undersökning där en sak ändras i taget",
      "mäta, dokumentera i tabell och diagram och värdera resultat och felkällor",
      "tolka varningsmärkning på kemiska produkter och följa säkerhetsregler i labbet",
      "förklara vad en förklaringsmodell är och varför modeller förenklas och ändras",
      "berätta om hur kemin växte fram från alkemin, med Lavoisier och Mendelejev som exempel",
      "granska information om kemi, skilja påståenden från åsikter och argumentera i en miljö- eller hälsofråga"],
 fundera="Reklam säger ibland att en produkt är ”kemikaliefri”. Vad tror du att ordet kemikalie betyder, och kan något som du kan ta på egentligen vara fritt från kemikalier?",
)

S = []

S.append(dict(id="vad-ar-kemi", nr="1.1", ikon="🧪", titel="Vad är kemi?",
 intro="Kemi handlar om vad allt är gjort av, hur ämnen kan ändras och varför. Det gäller allt från en kaka i ugnen till dig själv.",
 block=[
  ("p","<strong>Kemi</strong> är naturvetenskapen om ämnens uppbyggnad, egenskaper och omvandlingar. Kemister vill veta vad något består av, varför det beter sig som det gör och hur man kan få det att förändras. Därför dyker kemi upp överallt, inte bara i labbet."),
  ("p","Kemi är en <strong>naturvetenskap</strong>. Det betyder att man försöker svara på frågor om naturen genom att göra observationer och undersökningar som andra kan upprepa och kontrollera. Det som inte går att pröva på det sättet hör till andra sätt att förklara världen, till exempel tro eller konst."),
  ("tab",["Var finns kemin?","Exempel på kemi"],[
    ["I vardagen","Ett ägg som stelnar när det steks. Tvål som löser fett. Bröd som jäser. Järn som rostar."],
    ["I naturen","Växter som bygger socker av koldioxid och vatten med hjälp av solljus. Regn som löser upp kalksten. Löv som ändrar färg på hösten."],
    ["I samhället","Nya läkemedel, batterier i mobiler, rening av dricksvatten, material som tål kyla och hetta."],
    ["I kroppen","Maten bryts ned till små delar som kroppen tar upp. Syre från luften används när cellerna frigör energi."]]),
  ("p","Kemi kan också hjälpa oss att fatta kloka beslut. Hur ska vi rena vatten, minska utsläpp och återvinna material? Kunskaper i kemi behövs för att kunna ta ställning i sådana frågor."),
  ("ruta","visste","Visste du?","Mer än hälften av en människas kropp är vatten, H<sub>2</sub>O. Den enkla formeln visar att varje vattenmolekyl har två väteatomer och en syreatom."),
  ("kolla",["Vad handlar kemi om?","Ge ett exempel på kemi i naturen och ett i kroppen.","Varför är kemi en naturvetenskap?"]),
 ],
 svar=["Vad ämnen består av, deras egenskaper och hur de kan omvandlas till andra ämnen.","T.ex. fotosyntes i växter (natur) och att maten bryts ned vid matsmältningen (kropp).","Man ställer frågor om naturen och prövar svaren med observationer och undersökningar som andra kan kontrollera."],
))

S.append(dict(id="amnen", nr="1.2", ikon="🧂", titel="Ämnen, material och blandningar",
 intro="Allt omkring dig består av ämnen. Men vad är skillnaden mellan ett ämne, ett material och en blandning?",
 block=[
  ("p","Ett <strong>ämne</strong> är en sorts material med bestämda egenskaper, till exempel vatten, järn, socker eller koldioxid. Rent socker är ett ämne. Ett <strong>material</strong> är det något är gjort av, som trä, plast eller glas, och kan innehålla flera ämnen."),
  ("bild","k1_blandningar","Partikelbild av ett grundämne, en kemisk förening och en blandning."),
  ("p","Ämnen känner vi igen på sina <strong>egenskaper</strong>: hur de ser ut, om de är fasta, flytande eller gas, om de löser sig i vatten, vid vilken temperatur de smälter och om de leder ström. Vatten smälter till exempel vid 0 °C och kokar vid ungefär 100 °C (vid normalt lufttryck)."),
  ("p","De flesta saker vi möter är <strong>blandningar</strong>. Luft är en blandning av gaser, saltvatten är en blandning av salt och vatten och granit är en blandning av olika mineral. I en blandning behåller varje ämne sina egenskaper, och man kan ofta skilja dem åt, till exempel genom att filtrera eller låta vatten avdunsta."),
  ("tab",["Exempel","Rent ämne eller blandning?"],[
    ["Destillerat vatten","Rent ämne (i stort sett)"],
    ["Bordssalt","Mest ämnet natriumklorid, ofta med små tillsatser"],
    ["Läsk","Blandning av vatten, socker, kolsyra, smakämnen med mera"],
    ["Luft","Blandning, mest kväve och syre"]]),
  ("ruta","fakta","Vad är en kemikalie?","I lagstiftningen används ordet <strong>kemikalie</strong> för alla ämnen och blandningar, alltså även vatten, socker och salt. Allt runt omkring oss består alltså av kemikalier. I vardagen använder många ordet om sådant som är konstgjort eller farligt, men det är inte vad ordet betyder i kemin."),
  ("ruta","tank","Naturligt eller konstgjort?","Ett ämne är inte farligt för att det är konstgjort och inte ofarligt för att det är naturligt. Svamp kan innehålla starka gifter, och många läkemedel är gjorda i labb. Det som avgör är ämnets egenskaper och hur mycket man utsätts för."),
  ("kolla",["Vad är skillnaden mellan ett ämne och en blandning?","Är vatten en kemikalie? Förklara.","Ge två egenskaper som kan användas för att känna igen ett ämne."]),
 ],
 svar=["Ett ämne har bestämda egenskaper. En blandning innehåller flera ämnen som behåller sina egenskaper.","Ja. Ordet kemikalie betyder ämnen och blandningar, och vatten är ett ämne.","T.ex. smältpunkt, kokpunkt, löslighet i vatten eller om det leder ström."],
))

S.append(dict(id="undersokning", nr="1.3", ikon="🔬", titel="Så gör man en systematisk undersökning",
 intro="Kemister svarar på sina frågor genom att undersöka. En bra undersökning är planerad så att man kan lita på svaret.",
 block=[
  ("p","Allt börjar med en <strong>undersökbar fråga</strong>, alltså en fråga som går att svara på genom att mäta eller observera. ”Är socker gott?” går inte att mäta. ”Hur påverkar vattnets temperatur hur snabbt socker löser sig?” går att undersöka."),
  ("p","Sedan formulerar man en <strong>hypotes</strong>, en förklaring eller förutsägelse som du kan pröva. Den bör ha ett ”därför att”, till exempel: ”Sockret löser sig snabbare i varmt vatten, därför att partiklarna rör sig snabbare.” En hypotes kan visa sig vara fel, och det är också ett resultat."),
  ("bild","k1_undersokning","Undersökningens steg med exemplet socker i vatten. Värderingen leder ofta till nya frågor."),
  ("p","Det viktigaste i planeringen är <strong>variablerna</strong>. Den du ändrar kallas <em>oberoende variabel</em>. Det du mäter kallas <em>beroende variabel</em>. Allt annat måste hållas lika, annars vet du inte vad som gav skillnaden. Det kallas att ändra <strong>en sak i taget</strong>."),
  ("ruta","exempel","Exempel","Fråga: Hur påverkar vattnets temperatur lösningstiden för socker? Ändrar: temperaturen. Mäter: tiden tills inget socker syns. Lika: mängd socker, mängd vatten, glas och omrörning."),
  ("ruta","tank","Upprepa!","Gör helst varje försök minst tre gånger och räkna ut medelvärdet. Då påverkar en enstaka slarvig mätning resultatet mindre."),
  ("kolla",["Varför ska en hypotes ha en motivering?","Vad är oberoende och beroende variabel?","Varför ska man bara ändra en sak i taget?"]),
 ],
 svar=["Så att den bygger på en tänkt förklaring och går att pröva, inte bara en gissning.","Oberoende: det du ändrar. Beroende: det du mäter.","Annars vet man inte vilken förändring som orsakade skillnaden i resultatet."],
))

S.append(dict(id="mata", nr="1.4", ikon="📊", titel="Mäta, dokumentera och värdera",
 intro="En undersökning blir användbar först när resultaten är noggrant uppmätta, tydligt redovisade och kritiskt värderade.",
 block=[
  ("p","Kemister använder många <strong>verktyg</strong>. Analoga verktyg är till exempel mätglas, våg med visare, termometer med vätska och pH-papper. Digitala verktyg är digital våg, temperatursond, tidtagarur i mobilen, och datorprogram där man samlar in och ritar upp mätdata."),
  ("p","Skriv alltid ned mätvärdena <strong>direkt</strong> och med enhet (g, ml, °C, s). Ett vanligt sätt är en tabell. Här är ett påhittat exempel från en undersökning med socker, tre försök per temperatur."),
  ("tab",["Vattnets temperatur (°C)","Försök 1 (s)","Försök 2 (s)","Försök 3 (s)","Medelvärde (s)"],[
    ["20","84","90","87","87"],
    ["35","52","49","55","52"],
    ["50","31","35","30","32"]]),
  ("p","Ett <strong>diagram</strong> gör mönster lättare att se. Sätt det du ändrade (temperatur) på x-axeln och det du mätte (tid) på y-axeln, och namnge axlarna med enhet. I ett kalkylblad skriver du in tabellen och använder en formel för medelvärdet, till exempel =MEDEL(B2:D2), och låter programmet göra diagrammet."),
  ("bild","k1_diagram","Medelvärdet av lösningstiden vid tre temperaturer (tabellen ovan). Ju varmare vatten, desto kortare tid."),
  ("p","Till sist <strong>värderar</strong> du. Stämde resultatet med hypotesen? Vilka <strong>felkällor</strong> kan ha påverkat? Det kan vara att vattnet kyldes under försöket, att sockerkornen var olika stora eller att tiden avlästes olika varje gång. Skilj på slumpmässiga fel, som varierar, och systematiska fel, som alltid går åt samma håll."),
  ("ruta","fakta","Rapportens delar","En kort rapport har oftast: frågeställning, hypotes, material och metod, resultat (tabell och diagram), slutsats och diskussion om felkällor och förbättringar."),
  ("kolla",["Varför skriver man ned mätvärden direkt?","Vad ska stå på diagrammets axlar?","Ge två exempel på felkällor i en undersökning med lösningstid."]),
 ],
 svar=["För att inte glömma eller komma ihåg fel, och för att kunna lita på resultaten.","Det du ändrade på x-axeln och det du mätte på y-axeln, båda med namn och enhet.","T.ex. att vattnet kyls under försöket, olika stora sockerkorn eller att tiden läses av olika."],
))

S.append(dict(id="sakerhet", nr="1.5", ikon="🥽", titel="Säkerhet och varningsmärkning",
 intro="Ett bra experiment är ett säkert experiment. Du ska veta hur du skyddar dig och hur du läser märkningen på kemiska produkter.",
 block=[
  ("p","Några grundregler gäller alltid i labb: använd <strong>skyddsglasögon</strong>, bind upp långt hår, ät och drick aldrig i labbet och smaka aldrig på något. Läs hela instruktionen innan du börjar, ha ventilation och följ lärarens anvisningar. Varmt vatten hanterar du varsamt, och spill torkar du upp direkt."),
  ("p","Kemiska produkter som kan vara farliga har en <strong>varningsmärkning</strong> enligt EU:s regler som kallas CLP. Märkningen har vita rutor med röd kant som står på spetsen, så kallade <strong>faropiktogram</strong>, ett signalord (<em>Fara</em> eller <em>Varning</em>) samt text om fara och hur du skyddar dig."),
  ("tab",["Piktogram","Betyder"],[
    ["Låga","Brandfarligt"],
    ["Låga över cirkel","Kan hjälpa en brand att sprida sig (oxiderande)"],
    ["Frätande (ämne som droppar på hand och metall)","Frätande, kan ge frätskador på hud och ögon"],
    ["Dödskalle med korslagda ben","Akut giftigt"],
    ["Utropstecken","Irriterande eller skadligt i mindre grad"],
    ["Figur med stjärna på bröstet","Allvarlig fara för hälsan på lång sikt"],
    ["Död fisk och träd","Farligt för miljön, särskilt vattenlevande djur"]]),
  ("p","Det finns nio piktogram. Tabellen visar sju av dem. De andra två är bomb som exploderar (explosivt) och gasflaska (gas under tryck). Du ser dem ofta på avloppsrengöring, tändvätska, sprayburkar och bekämpningsmedel."),
  ("bild","k1_symboler","Sju av de nio faropiktogrammen i förenklad bild."),
  ("ruta","tank","Farligt eller riskabelt?","<strong>Fara</strong> är vad ett ämne kan göra. <strong>Risk</strong> är hur sannolikt det är att något händer, och det beror på hur mycket du utsätts för och hur du hanterar ämnet. Ett frätande ämne som är väl förvarat och används med skydd ger liten risk."),
  ("kolla",["Nämn tre grundregler i labbet.","Vad menas med signalorden Fara och Varning?","Vad är skillnaden mellan fara och risk?"]),
 ],
 svar=["T.ex. skyddsglasögon, smaka aldrig, upptorkat spill, ventilation, bundet hår.","De visar hur allvarlig faran är. Fara är den allvarligare nivån, Varning den lindrigare.","Fara är vad ämnet kan göra, risk är hur sannolikt det är att det händer vid användningen."],
))

S.append(dict(id="modeller", nr="1.6", ikon="🧩", titel="Modeller – förenklade förklaringar",
 intro="Kemister kan inte se atomer med blotta ögat. Därför använder de modeller som hjälper oss att förklara det vi observerar.",
 block=[
  ("p","En <strong>förklaringsmodell</strong> är en förenklad bild eller idé som förklarar och förutsäger hur något fungerar. Den är inte hela sanningen, utan ett verktyg. En karta är en bra jämförelse: den visar vägen men inte varje sten."),
  ("bild","k1_partikelmodell","Partikelmodellen för fast form, vätska och gas."),
  ("p","Ett viktigt exempel är <strong>partikelmodellen</strong>. Den säger att allt består av mycket små partiklar som är i ständig rörelse. I en fast form ligger partiklarna tätt och vibrerar på sina platser. I vätska glider de förbi varandra. I gas rör de sig fritt med stora avstånd."),
  ("p","Med modellen kan du förklara varför socker löser sig. Vattnets partiklar rör sig och drar loss sockermolekyler från sockerkornet. Varmare vatten betyder att partiklarna rör sig snabbare, och då går det oftast snabbare att lösa upp. Modellen hjälper dig alltså att förklara ett samband och göra en hypotes."),
  ("ruta","tank","Alla modeller har gränser","En modell passar för vissa frågor men inte för alla. Kulor som symboliserar partiklar kan visa gaser och vätskor. De säger däremot inget om hur partiklarna är uppbyggda inuti. Då behövs en annan modell, till exempel atommodellen med kärna och elektroner."),
  ("p","<strong>Modeller ändras</strong> när nya undersökningar ger resultat som den gamla modellen inte kan förklara. Då byggs modellen ut eller byts mot en bättre. Det betyder inte att den gamla var dum. Många gamla modeller fungerade bra för sin tid och används än idag för enklare frågor."),
  ("tab",["Modell","Bra för att förklara","Begränsning"],[
    ["Partikelmodell (kulor)","Fast, flytande och gas, lösning, diffusion","Visar inte hur partiklarna är uppbyggda"],
    ["Atommodell med kärna och elektroner","Hur atomer binds ihop","Förenklad bild av elektronerna"],
    ["Formler som H<sub>2</sub>O","Vilka atomer och hur många som ingår","Visar inte formen på molekylen"]]),
  ("kolla",["Vad är en förklaringsmodell?","Hur förklarar partikelmodellen att socker löser sig snabbare i varmt vatten?","Varför ändras modeller?"]),
 ],
 svar=["En förenklad bild eller idé som förklarar och förutsäger hur något fungerar.","I varmt vatten rör sig partiklarna snabbare och drar därför snabbare loss sockermolekyler från sockerkornet.","Nya undersökningar ger resultat som den gamla modellen inte kan förklara."],
))

S.append(dict(id="historia", nr="1.7", ikon="⚗️", titel="Från alkemi till periodiskt system",
 intro="Kemin har en lång historia. Idéerna har förändrats i takt med att människor har gjort nya undersökningar.",
 block=[
  ("p","<strong>Alkemin</strong> fanns i över tusen år, bland annat i Egypten, i den arabiska världen och i Europa. Alkemisterna provade metoder att blanda, värma och destillera ämnen. Många försökte göra oädla metaller till guld eller hitta ett livselixir. Det lyckades inte, men de utvecklade metoder och redskap som kemister använde senare."),
  ("p","Under 1700-talet förklarade många att brinnande ämnen avger ett ämne som kallades flogiston. <strong>Antoine Lavoisier</strong> (1743–1794) vägde ämnen före och efter förbränning. Han fann att förbränning innebär att ämnet reagerar med en del av luften, som han kallade syre (oxygen). Hans noggranna vägningar stödde att den totala massan är densamma före och efter en kemisk reaktion. Det kallas <strong>massans bevarande</strong>."),
  ("p","<strong>Dmitrij Mendelejev</strong> (1834–1907) ordnade 1869 de då kända grundämnena efter atommassa och efter likheter i egenskaper. Han lämnade luckor för ämnen som ännu inte hittats och förutsade deras egenskaper. När gallium (1875) och germanium (1886) upptäcktes passade de in, och det gjorde tabellen allmänt accepterad."),
  ("tidslinje",[("Antiken–medeltiden","Alkemi: metoder för att blanda, värma och destillera"),("1700-talet","Flogistonteorin förklarar förbränning"),("1770–1780-talen","Lavoisier visar att förbränning är reaktion med syre"),("1789","Lavoisiers lärobok om kemi utkommer"),("1869","Mendelejev presenterar periodiska systemet"),("1875","Gallium upptäcks, ett av Mendelejevs förutsagda ämnen"),("1886","Germanium upptäcks och stärker tabellens ställning")]),
  ("ruta","historia","Lavoisier och revolutionen","Lavoisier arbetade även med skatteuppbörd, vilket var illa sedd under den franska revolutionen. Han avrättades 1794. Ett citat om att ”republiken inte behöver lärda” brukar kopplas till domen, men forskare tror inte att det sades. Här ser du hur en bra historia kan behöva källkritik."),
  ("kolla",["Vad är massans bevarande?","Varför blev Mendelejevs periodiska system så trovärdigt?","Vad kan vi lära oss av att flogistonteorin byttes ut?"]),
 ],
 svar=["Den totala massan är densamma före och efter en kemisk reaktion.","Han förutsade att ämnen skulle finnas och beskrev deras egenskaper, och när gallium och germanium hittades stämde det.","Att naturvetenskapliga idéer kan bytas mot bättre när nya mätningar och undersökningar visar något annat."],
))

S.append(dict(id="kallkritik", nr="1.8", ikon="🧐", titel="Källkritik och argumentation",
 intro="Du möter påståenden om kemi i sociala medier, reklam och nyheter varje dag. Hur avgör du vad du kan lita på?",
 block=[
  ("p","<strong>Källkritik</strong> betyder att granska information. Ställ frågor om <strong>avsändaren</strong> (vem skriver och vad kan hen?), <strong>syftet</strong> (informera, sälja, påverka?), <strong>belägg</strong> (finns mätningar eller studier?), <strong>aktualitet</strong> (är det nytt eller gammalt?) och om informationen är <strong>relevant</strong> för din fråga."),
  ("bild","k1_kallkritik","Frågor att ställa när du granskar en källa."),
  ("tab",["Mer trovärdigt","Mer att vara försiktig med"],[
    ["Myndigheter, universitet och forskningsartiklar","Anonyma sidor och inlägg utan källor"],
    ["Källor som visar hur de vet något","Påståenden som ”alla vet” eller ”läkarna döljer”"],
    ["Flera oberoende källor säger samma","En enda källa som tjänar på att du tror på den"],
    ["Försiktiga formuleringar (”tyder på”)","Absoluta ord (”helt ofarligt”, ”100 procent”)"]]),
  ("p","Skilj mellan <strong>påståenden som kan prövas</strong> och <strong>åsikter</strong>. ”Vattnet kokar vid ungefär 100 °C” går att pröva. ”Plast är fult” är en åsikt. Åsikter kan vara viktiga, men de svarar inte på vad som är sant."),
  ("p","I miljö- och hälsofrågor behöver du kunna <strong>argumentera</strong>: ge ett påstående, ett skäl och ett belägg, och bemöta motargument. Ett exempel är reklam som lovar ”kemikaliefritt”. Eftersom allt är kemikalier kan inget vara kemikaliefritt. Ordet säger då ingenting om hur farlig produkten är."),
  ("ruta","exempel","Argument och motargument","Påstående: ”Naturliga produkter är alltid säkrare.” Motargument: Naturliga ämnen kan vara giftiga (t.ex. vissa svampar). Hur farligt något är beror på ämnet och mängden, inte på om det är naturligt."),
  ("ruta","tank","Vad skulle få dig att ändra dig?","Ett bra argument tar hänsyn till bevis. Fråga dig själv vilka belägg som skulle kunna få dig att ändra åsikt. Det är ett tecken på ett vetenskapligt sätt att tänka."),
  ("kolla",["Nämn tre frågor man kan ställa till en källa.","Är ”plast är fult” ett påstående som kan prövas?","Varför är ”kemikaliefritt” ett problematiskt ord?"]),
 ],
 svar=["T.ex. vem avsändaren är, vad syftet är, vilka belägg som finns, om informationen är aktuell.","Nej, det är en åsikt.","Allt består av kemikalier, så ordet kan inte vara sant. Det säger heller inget om hur farlig produkten är."],
))

UPPG = [
 ("Para ihop","Koppla begreppet till förklaringen.",["Hypotes","Oberoende variabel","Beroende variabel","Felkälla","Förklaringsmodell","Massans bevarande"],["Det du mäter","Förenklad idé som förklarar och förutsäger","Tänkt förklaring som kan prövas","Total massa är lika före och efter reaktionen","Något som kan göra resultatet fel","Det du ändrar"],"1 – C, 2 – F, 3 – A, 4 – E, 5 – B, 6 – D"),
 ("Sant eller falskt?","Avgör om påståendena stämmer.",["Socker är en kemikalie.","Ett naturligt ämne kan inte vara giftigt.","I en blandning behåller ämnena sina egenskaper.","Lavoisier bidrog till att förklara att förbränning är en reaktion med syre.","Piktogrammet med utropstecken betyder akut giftigt."],None,"Sant; falskt (t.ex. vissa svampar är mycket giftiga); sant; sant; falskt (utropstecken betyder irriterande eller skadligt, dödskallen betyder akut giftigt)."),
 ("Är frågan undersökbar?","Avgör vilka frågor som går att undersöka med en mätning och motivera: (a) Vilket vatten är godast? (b) Hur påverkar mängden salt hur snabbt vatten fryser? (c) Är kemi viktigare än fysik?",[],None,"Bara (b) går att undersöka med mätningar. (a) och (c) är värderingar eller smak."),
 ("Variabler","En elev vill veta om omrörning påverkar hur snabbt socker löser sig. Ange oberoende variabel, beroende variabel och minst tre saker som ska hållas lika.",[],None,"Oberoende: omrörning (med/utan). Beroende: tiden tills sockret löst sig. Lika: mängd socker, mängd vatten, temperatur, glas, sockrets sort."),
 ("Rita diagram","Rita ett diagram av tabellen i avsnitt 1.4. Vad visar det om sambandet mellan temperatur och lösningstid?",[],None,"Temperatur på x-axeln, tid på y-axeln. Högre temperatur ger kortare lösningstid (i exemplet)."),
 ("Förklara med modell","Använd partikelmodellen för att förklara varför socker löser sig snabbare i varmt vatten än i kallt.",[],None,"Partiklarna rör sig snabbare i varmt vatten, träffar sockerkornen oftare och med mer energi, så sockermolekylerna lossnar och sprids snabbare."),
 ("Läs märkningen","Du hittar en flaska med en låga och ett utropstecken samt signalordet Varning. Vad betyder det och hur ska du hantera den?",[],None,"Brandfarligt och mindre farligt (irriterande/skadligt). Håll borta från värme och eld, ventilera, läs hela etiketten och använd skydd."),
 ("Modeller över tid","Förklara varför flogistonteorin byttes ut och vad det visar om hur naturvetenskap fungerar.",[],None,"Lavoisiers vägningar visade att metaller väger mer efter förbränning, vilket flogiston inte kunde förklara. Naturvetenskapen ändras när nya belägg kommer."),
 ("Kemikaliefritt?","En tvål säljs som ”helt kemikaliefri”. Skriv två argument som visar att påståendet är problematiskt.",[],None,"Allt består av kemikalier, även vatten och naturliga ämnen. Ordet säger inte något om hur farligt eller ofarligt ett ämne är, och kan användas för att sälja."),
 ("Källkritik","Du hittar ett inlägg: ”Ämnet X är farligt, dela!” Vilka frågor ställer du innan du delar det?",[],None,"Vem är avsändaren, vad är syftet, vilka belägg finns, är det aktuellt, vad säger myndigheter eller forskare, och finns det flera oberoende källor?"),
 ("Argumentera","Skriv ett argument för och ett mot: ”Alla plastpåsar ska förbjudas”. Använd ett skäl och ett belägg i varje.",[],None,"Bedöms: tydligt påstående, skäl och belägg i båda riktningar (t.ex. nedskräpning och resursanvändning mot hygien, återanvändning och alternativens egen miljöpåverkan)."),
]

BEGREPP = [
 ("Kemi","Vetenskapen om ämnens uppbyggnad, egenskaper och omvandlingar."),
 ("Ämne","En sorts material med bestämda egenskaper, t.ex. vatten."),
 ("Material","Det något är gjort av, t.ex. trä, plast eller glas."),
 ("Blandning","Flera ämnen tillsammans som behåller sina egenskaper."),
 ("Kemikalie","Ämne eller blandning; allt består av kemikalier."),
 ("Hypotes","Tänkt förklaring eller förutsägelse som kan prövas."),
 ("Variabel","Något som kan ändras eller mätas i en undersökning."),
 ("Felkälla","Något som kan göra resultatet felaktigt."),
 ("Medelvärde","Summan av mätvärdena delad med antalet."),
 ("Faropiktogram","Röd ruta med symbol som visar vilken fara ett ämne har."),
 ("Förklaringsmodell","Förenklad bild eller idé som förklarar och förutsäger."),
 ("Partikelmodell","Modell där allt består av små partiklar i rörelse."),
 ("Alkemi","Äldre tradition med blandning och destillation, föregångare till kemin."),
 ("Massans bevarande","Total massa är densamma före och efter en kemisk reaktion."),
 ("Periodiska systemet","Tabell som ordnar grundämnena efter egenskaper."),
 ("Källkritik","Att granska avsändare, syfte, belägg och aktualitet."),
]

SAMMAN = [
 "Kemi är naturvetenskapen om ämnens uppbyggnad, egenskaper och omvandlingar, och finns i vardagen, naturen, samhället och kroppen.",
 "Allt består av kemikalier: ordet betyder ämnen och blandningar, inte ”farligt” eller ”konstgjort”.",
 "En systematisk undersökning har en undersökbar fråga, en hypotes, en plan där man ändrar en sak i taget, mätningar och en värdering.",
 "Resultat redovisas i tabell, diagram och rapport, och man diskuterar felkällor. Digitala verktyg, som kalkylblad, underlättar.",
 "Varningsmärkning med piktogram och signalord visar faror. Fara är vad ämnet kan göra, risk är hur sannolikt det är att något händer.",
 "Modeller, som partikelmodellen, är förenklingar som förklarar och förutsäger, och de ändras när nya undersökningar kräver det.",
 "Kemin växte fram från alkemin. Lavoisier visade förbränningens roll och massans bevarande, och Mendelejevs periodiska system förutsade nya ämnen.",
 "Källkritik och argumentation: granska avsändare, syfte, belägg och aktualitet, och skilj påståenden som kan prövas från åsikter.",
]

TEST_A = [
 ("Vad menas med en kemikalie i lagstiftningen?",["Bara farliga ämnen","Ämnen och blandningar","Bara konstgjorda ämnen","Bara vätskor"],1),
 ("Vilken fråga går att undersöka systematiskt?",["Vilken lukt är finast?","Hur påverkar temperaturen hur snabbt socker löser sig?","Är kemi roligare än fysik?","Vilken färg är snyggast?"],1),
 ("I en rättvis undersökning ska man",["ändra flera saker samtidigt","ändra en sak i taget och hålla resten lika","bara göra ett försök","välja resultat som passar hypotesen"],1),
 ("Vad är beroende variabel?",["Det du ändrar","Det du mäter","Det som är lika","Din hypotes"],1),
 ("Vad betyder piktogrammet med dödskalle och korslagda ben?",["Brandfarligt","Akut giftigt","Frätande","Miljöfarligt"],1),
 ("Vad visade Lavoisiers vägningar?",["Förbränning avger flogiston","Förbränning är en reaktion med syre och massan bevaras","Guld kan tillverkas av bly","Luft är ett grundämne"],1),
 ("Varför blev Mendelejevs periodiska system så uppmärksammat?",["Han ritade fina bilder","Det förutsade ämnen som sedan hittades","Det innehöll alla ämnen","Det byggde på alkemi"],1),
 ("Vilket påstående går att pröva?",["Plast är fult","Vatten kokar vid ungefär 100 °C vid normalt lufttryck","Kemi är tråkigt","Naturligt är bättre"],1),
]
TEST_B = [
 ("Förklara varför allt består av kemikalier och vad som är fel med ordet ”kemikaliefritt”.","Kemikalie betyder ämne eller blandning, även vatten och salt. Därför kan inget vara kemikaliefritt. Ordet säger inget om hur farligt något är."),
 ("Beskriv stegen i en systematisk undersökning.","Fråga, hypotes, planering (variabler), utförande med mätningar, resultat i tabell/diagram, värdering med felkällor."),
 ("Förklara skillnaden mellan fara och risk med ett exempel.","Fara är vad ämnet kan göra, risk är hur sannolikt det är. Frätande avloppsrens är farligt men ger låg risk om det förvaras och används rätt."),
 ("Varför är partikelmodellen en förenkling?","Den visar partiklar som kulor och säger inget om deras inre uppbyggnad. Den passar vissa frågor men andra kräver en annan modell, t.ex. atommodellen."),
 ("Hur visade Lavoisier att förbränning kräver syre?","Han vägde före och efter och såg att ämnena tog upp en del av luften. Det stödde också att massan bevaras."),
 ("Du får se en reklam som säger att en produkt är ”100 % naturlig och därför ofarlig”. Hur granskar du den?","Vem avsänder och vill sälja? Finns belägg? Naturligt betyder inte ofarligt, eftersom farlighet beror på ämne och mängd. Jämför med myndighetskällor."),
]

KALLA = dict(
 text="”Vår kräm är 100 % kemikaliefri och därför helt ofarlig. Naturligt är alltid bättre än syntetiskt, och forskare vill inte att du ska veta det. Köp idag!”",
 ursprung="Konstruerad källa baserad på vanliga reklamfraser. Den är ett påhittat exempel och inte hämtad från en verklig produkt.",
 fragor=[
  ("Vilket syfte har avsändaren troligen?","Att sälja produkten och få läsaren att köpa idag."),
  ("Vilka påståenden går att pröva och vilka är åsikter?","Att produkten är kemikaliefri går att granska och är fel eftersom allt är kemikalier. ”Naturligt är bättre” är delvis en åsikt, men går att pröva för enskilda ämnen. ”Forskare vill inte” är ett obelagt påstående."),
  ("Vilka tecken på dålig trovärdighet finns?","Absoluta ord (100 %, helt ofarlig, alltid), inga belägg, ingen avsändare som kan granskas, konspirationspåstående och press att köpa direkt."),
  ("Hur skulle du kontrollera påståendena?","Läsa innehållsförteckningen, söka hos myndigheter som Kemikalieinspektionen och jämföra med flera oberoende källor."),
 ])

SKRIV = dict(
 uppgift="Skriv en text på ca en sida: ”Är kemikalier farliga?” Förklara vad ordet kemikalie betyder, ge två exempel på ämnen som är ofarliga respektive farliga, förklara skillnaden mellan fara och risk, granska ett reklampåstående som ”kemikaliefritt” och ta ställning med minst två argument.",
 stod=[
  "E: Eleven förklarar enkelt att allt består av kemikalier, ger exempel på ofarliga och farliga ämnen och framför ett argument med viss underbyggnad.",
  "C: Eleven förklarar skillnaden mellan fara och risk, granskar reklampåståendet med kriterier som avsändare och belägg, och framför och bemöter argument med relativt god underbyggnad.",
  "A: Eleven för ett nyanserat resonemang där hen väger fara, mängd och exponering, resonerar om källors trovärdighet och relevans och drar en välgrundad slutsats med motargument.",
 ])

LAB = dict(
 titel="Kemilabbet: Vad påverkar hur snabbt socker löser sig i vatten?",
 syfte="Planera och genomföra en säker systematisk undersökning där en sak ändras i taget, dokumentera i tabell och diagram och värdera resultat och felkällor. Använd partikelmodellen för att förklara.",
 material="Strösocker, sockerbitar, kranvatten i två temperaturer (kallt och ljummet, högst ca 40 °C, förberett av läraren), genomskinliga glas eller plastmuggar, tesked, mätglas eller dl-mått, tidtagarur (mobil), skedar för omrörning, termometer, papper och penna eller dator, skyddsglasögon.",
 utforande=[
  "Sätt på skyddsglasögon. Smaka eller drick inte något i försöket. Använd inte hett vatten. Ljummet vatten förbereds av läraren.",
  "Välj EN sak att ändra: vattnets temperatur, omrörning, eller sockrets form (strösocker eller sockerbit). Skriv undersökningsfråga och hypotes med motivering (”därför att …”).",
  "Bestäm vad som ska vara lika: 100 ml vatten, 1 tesked strösocker (eller en sockerbit), samma sorts glas.",
  "Gör en tabell med rubriker och enheter för försök 1, 2 och 3 samt medelvärde.",
  "Mät upp vattnet och temperaturen. Tillsätt sockret och starta tiden direkt. Rör på samma sätt i alla försök om omrörning ingår.",
  "Stoppa tiden när du inte längre ser sockerkorn eller bitar. Skriv direkt in tiden i tabellen.",
  "Upprepa tre gånger för varje variant. Räkna ut medelvärde, till exempel =MEDEL(B2:D2) i ett kalkylblad, och gör ett stapel- eller linjediagram.",
  "Städa, torka upp spill och tvätta händerna. Skriv sedan slutsats och diskutera felkällor.",
 ],
 fragor=[
  ("Vilken var din oberoende och din beroende variabel?","Oberoende: det du ändrade (t.ex. temperatur). Beroende: tiden tills sockret löst sig."),
  ("Stämde resultatet med din hypotes? Förklara med partikelmodellen.","Oftast löser sig sockret snabbare i ljummet vatten, vid omrörning och som strösocker. Förklaring: partiklarna rör sig snabbare/möts oftare och större yta ger fler ställen där vattnet kan dra loss sockermolekyler."),
  ("Nämn tre felkällor och hur du kan minska dem.","T.ex. olika omrörning (rör lika), vatten som kyls (mät temperaturen), svårt att se när sista kornet försvinner (enas om ett kriterium), olika mängd socker (väg eller använd strykt tesked)."),
  ("Hur kunde du göra undersökningen bättre?","Fler försök, digital våg och termometer, flera temperaturer, samma person som läser av tiden."),
 ],
 bonus="BONUS för läraren: Låt grupperna välja olika variabler och jämför i helklass vilka som påverkar mest. Lägg in data i ett gemensamt kalkylblad för att visa värdet av fler mätningar. Tänk på att hålla vattentemperaturen låg (högst ca 40 °C), att inga elever smakar och att kranvatten används. Diskutera också vad som händer om man försöker lösa mer och mer socker (löslighetsgräns), som en uppföljande frågeställning.",
)

LARAR = [
 ("Koppling till Lgr22 (Kemi)","Kapitlet behandlar kursplanens syfte om kemins begrepp och förklaringsmodeller, om att granska information, kommunicera och ta ställning i miljö- och hälsofrågor samt att genomföra systematiska undersökningar. Centralt innehåll i åk 7–9, Systematiska undersökningar och granskning av information: observationer och experiment med analoga och digitala verktyg, formulering av undersökningsbara frågor, planering, utförande, värdering och dokumentation med tabeller, diagram och rapporter. Dessutom sambandet mellan undersökningar och begrepp, förklaringsmodellernas historiska framväxt, användbarhet och föränderlighet, informationssökning och kritisk granskning samt argumentation i miljö- och hälsofrågor. Avsnitt 1.2 och 1.5 förbereder också om vardagskemikalier och märkning."),
 ("Förslag på upplägg (8 lektioner)","1. Vad är kemi, kemi i vardagen (1.1) med startfråga om ”kemikalier”. 2. Ämnen, material och blandningar (1.2). 3. Systematisk undersökning: fråga, hypotes, variabler (1.3). 4. Kemilabbet om sockrets lösning (LAB), planering och genomförande. 5. Mäta, dokumentera, tabell och diagram i kalkylblad, felkällor (1.4). 6. Säkerhet och varningsmärkning (1.5) med riktiga etiketter. 7. Modeller och kemins historia (1.6 och 1.7), tidslinje. 8. Källkritik och argumentation (1.8), analys av reklam, test."),
 ("Vanliga missuppfattningar","”Kemikalier är farliga/konstgjorda.” Allt består av kemikalier, och farlighet beror på ämne och mängd. ”Naturligt är alltid ofarligt.” Nej, det finns många naturliga gifter. ”En hypotes måste vara rätt.” En motbevisad hypotes är ett värdefullt resultat. ”En modell är en kopia av verkligheten.” Modeller är förenklingar som passar vissa frågor. ”Gamla modeller var dumma.” De fungerade för sin tid. ”Fara och risk är samma sak.” Risk beror på exponering. Elever ändrar ofta flera saker samtidigt för att spara tid, vilket gör att man inte kan dra någon slutsats."),
 ("Bedömningsstöd (E/C/A)","<strong>E:</strong> eleven planerar och genomför en undersökning på ett säkert och i huvudsak fungerande sätt, och gör enkla resonemang utifrån frågeställningen; beskriver en modell och ger exempel; söker information från olika källor och för enkla resonemang om trovärdighet; framför och bemöter argument med viss underbyggnad. <strong>C:</strong> eleven motiverar sin plan och variabler, dokumenterar tydligt, resonerar om felkällor på ett utvecklat sätt, använder partikelmodellen för att förklara samband, och för utvecklade resonemang om källors trovärdighet och relevans. <strong>A:</strong> eleven drar slutsatser som väger hypotes, resultat och osäkerhet, föreslår förbättringar, förklarar modellers användbarhet och föränderlighet med historiska exempel, och för välgrundade, nyanserade resonemang med argument och motargument."),
 ("Blooket/Jeopardy: bra kategorier","1. Vad är kemi. 2. Ämnen och blandningar. 3. Undersökning och variabler. 4. Märkning och säkerhet. 5. Modeller, historia och källkritik. Exempel: ”Det du ändrar i en undersökning” → oberoende variabel; ”Tecken på akut giftigt” → dödskalle med korslagda ben."),
]

KALLOR = [
 ("Encyclopaedia Britannica – History of the study of combustion (Lavoisier, syre och förbränning)","https://britannica.com/science/combustion/History-of-the-study-of-combustion"),
 ("Scerri (arXiv) – Mendeleev and the Periodic Table of Elements","https://arxiv.org/pdf/physics/0411080"),
 ("EU-OSHA – CLP, klassificering, märkning och förpackning av ämnen och blandningar","https://osha.europa.eu/sv/topics/ds/clp-classification-labelling-and-packaging-of-substances-and-mixtures"),
 ("Alingsås kommun – Faktablad om klassificering och märkning av kemiska produkter (CLP)","https://www.alingsas.se/wp-content/uploads/2020/04/faktablad-klassificering-markning-av-kemiska-produkter.pdf"),
 ("Kemikalieinspektionen – Märkning av kemiska produkter","https://www.kemi.se/lagar-och-regler/lagstiftningar-inom-kemikalieomradet/eu-gemensam-lagstiftning/clp-forordningen/markning-av-kemiska-produkter"),
 ("Kemikalieinspektionen – Vad betyder farosymbolerna?","https://www.kemi.se/publikationer/planscher-och-andra-trycksaker/vad-betyder-farosymbolerna"),
 ("Wikipedia – Antoine Lavoisier (vägvisare till primärkällor)","https://en.wikipedia.org/wiki/Antoine_Lavoisier"),
 ("Skolverket – Kommentarmaterial till kursplanen i fysik, 2022 (om modeller och källkritik, jämförbart för kemi)","https://www.skolverket.se/download/18.1cf74b4f183ff5ed375d78/1668518046135/pdf9865.pdf"),
 ("Kemilärarnas resurscentrum (Stockholms universitet) – Informationsbrev om Lgr22 i kemi","https://www.su.se/polopoly_fs/1.624892.1662399833!/menu/standard/file/Vad%20betyder%20Lgr22%20fo%CC%88r%20kemiundervisningen%3F.pdf"),
]

F = []
F.append(dict(id="f1", nr="F1", ikon="📏", titel="Mätosäkerhet och felkällor",
 intro="Ingen mätning är exakt. Kemister vill veta hur mycket de kan lita på ett mätvärde.",
 block=[
  ("p","När du mäter en tid två gånger får du sällan exakt samma värde. Skillnaden beror på <strong>slumpmässiga fel</strong>, till exempel att du reagerar lite olika snabbt på stoppuret. Flera upprepningar och ett medelvärde minskar effekten av sådana fel."),
  ("p","<strong>Systematiska fel</strong> går alltid åt samma håll. En våg som visar 2 g för mycket gör alla mätningar för höga, oavsett hur många gånger du mäter. De upptäcker du genom att kontrollera instrumentet, till exempel genom att väga något du vet massan på."),
  ("tab",["Typ av fel","Exempel","Hur minskar man det?"],[
    ["Slumpmässigt","Varierande avläsning av tiden","Upprepa och beräkna medelvärde"],
    ["Systematiskt","Termometer som visar för högt","Kalibrera eller jämför med annat instrument"],
    ["Mänskligt misstag","Fel mängd vatten","Mät noga, dubbelkolla och anteckna direkt"]]),
  ("ruta","tank","Hur många siffror?","Skriv inte fler decimaler än verktyget kan ge. En våg som visar hela gram kan inte ge svaret 12,347 g. Falsk precision ger intryck av större säkerhet än du har."),
  ("kolla",["Vad skiljer slumpmässiga och systematiska fel?","Hur kan man upptäcka en våg som visar fel?","Varför är det dåligt att skriva för många decimaler?"]),
 ],
 svar=["Slumpmässiga varierar från gång till gång, systematiska går alltid åt samma håll.","Genom att väga något med känd massa och jämföra.","Det ger intryck av en större noggrannhet än mätningen har."],
))
F.append(dict(id="f2", nr="F2", ikon="☠️", titel="Dosen gör giftet",
 intro="Hur farligt något är beror inte bara på vilket ämne det är utan också på hur mycket du får i dig.",
 block=[
  ("p","Läkaren Paracelsus (1400–1500-talet) sägs ha formulerat idén att det är dosen som avgör om något är ett gift. Principen används än idag. Salt behövs av kroppen, men mycket stora mängder kan skada. Även vatten kan vara farligt om man dricker orimligt mycket på kort tid."),
  ("p","Därför skiljer man på <strong>fara</strong> och <strong>risk</strong>. Ett ämne kan ha en farlig egenskap, men risken beror på <strong>exponeringen</strong>: hur mycket, hur länge och på vilket sätt (via hud, mat eller luft) man utsätts. Det är därför man kan använda frätande rengöringsmedel med handskar och ventilation."),
  ("ruta","fakta","Särskilt känsliga","Barn, gravida och människor med vissa sjukdomar kan vara mer känsliga för vissa ämnen. Därför har myndigheter ofta gränsvärden som tar hänsyn till det."),
  ("ruta","tank","Svårt att veta","För vissa ämnen finns det osäkerhet om långsiktiga effekter eller blandningar av många ämnen. Då kan man välja att vara försiktig, och här blir det en värdering vad som är acceptabel risk."),
  ("kolla",["Vad menas med att dosen gör giftet?","Vad är exponering?","Varför kan frätande rengöringsmedel användas säkert?"]),
 ],
 svar=["Hur farligt något är beror på mängden man får i sig, inte bara på ämnet.","Hur mycket, hur länge och på vilket sätt man utsätts för ett ämne.","Med skydd, ventilation och rätt hantering blir exponeringen och därmed risken låg."],
))
F.append(dict(id="f3", nr="F3", ikon="🔥", titel="Flogistonteorin – en modell som fungerade ett tag",
 intro="Under 1700-talet var flogiston en populär förklaring till förbränning. Den var fel, men den var ändå vetenskap.",
 block=[
  ("p","Flogistonteorin sade att brinnande ämnen avger ett ämne, flogiston. Därför blev ämnet ”flogistonfattigt” och lämnade aska. Teorin förklarade varför trä brinner och varför metaller blir till rost, och den gav forskare en gemensam bild att arbeta med."),
  ("p","Problemet var att många metaller blir <em>tyngre</em> när de bränns eller rostar. Flogiston måste då ha negativ vikt, vilket var svårt att tro på. Lavoisiers noggranna vägningar och förklaringen att ämnet i stället tar upp en del av luften förklarade resultaten mer enkelt."),
  ("tab",["","Flogistonteorin","Syreteorin"],[
    ["Vid förbränning…","avges flogiston","reagerar ämnet med syre"],
    ["Massan efter förbränning av metall","svårt att förklara","ökar eftersom syre tas upp"],
    ["Status idag","Övergiven","Grunden för modern förbränningskemi"]]),
  ("ruta","historia","Förklaringar tar tid","Det gick flera decennier innan syreteorin vann acceptans. Forskare ändrar sig sällan över en natt, och nya modeller möts ofta med skepsis. Det är en del av hur naturvetenskap kontrolleras."),
  ("kolla",["Vad påstod flogistonteorin?","Varför var teorin problematisk?","Varför kallas flogistonteorin ändå vetenskaplig?"]),
 ],
 svar=["Att brinnande ämnen avger ett ämne som kallas flogiston.","Många metaller blir tyngre vid förbränning, vilket var svårt att förklara.","Den byggde på observationer, förklarade mycket och kunde prövas, och byttes ut när bättre belägg kom."],
))
F.append(dict(id="f4", nr="F4", ikon="📰", titel="Hur kontrolleras forskning?",
 intro="Forskare publicerar sina resultat så att andra kan granska och upprepa dem. Men inte allt som ser vetenskapligt ut är det.",
 block=[
  ("p","Forskare skriver artiklar där de beskriver metod, resultat och slutsatser. Före publicering i en vetenskaplig tidskrift granskas artikeln ofta av andra experter, så kallad <strong>kollegial granskning</strong> (peer review). Den fångar inte allt, men höjer kvaliteten."),
  ("p","Viktiga resultat bör kunna <strong>upprepas</strong> av andra forskargrupper. Om ingen får samma resultat blir man tveksam. Därför är det bättre att lita på flera oberoende studier än på en enda spektakulär upptäckt."),
  ("tab",["Tecken på vetenskaplig information","Tecken på pseudovetenskap"],[
    ["Metod och data redovisas","Hänvisar till ”experter” utan namn"],
    ["Osäkerhet nämns","Lovar enkla, säkra svar"],
    ["Kan granskas och prövas","Går inte att pröva eller ändrar sig efter kritik"],
    ["Ändras när nya belägg kommer","Håller fast vid påståendet vad som än visas"]]),
  ("ruta","tank","En studie räcker inte","Nyhetsrubriker som ”nytt ämne botar …” bygger ofta på en enskild studie, ibland på djur eller celler. Fråga hur stor studien var, vem som betalade och om andra fått samma resultat."),
  ("kolla",["Vad är kollegial granskning?","Varför är flera studier bättre än en?","Nämn ett tecken på pseudovetenskap."]),
 ],
 svar=["Att andra experter granskar en forskningsartikel före publicering.","Om flera oberoende grupper får samma resultat är det mer tillförlitligt.","T.ex. att inga belägg redovisas, att det lovar enkla säkra svar eller att det inte går att pröva."],
))

F_UPPG = [
 ("●","Förklara skillnaden mellan slumpmässiga och systematiska fel och ge ett exempel på varje.",[],None,"Slumpmässiga varierar (reaktionstid på stoppur). Systematiska går åt samma håll (felvisande termometer)."),
 ("●●","Förklara vad Paracelsus idé om dosen betyder för hur vi bedömer ”farliga kemikalier”.",[],None,"Man måste titta både på ämnets egenskaper och på hur mycket man utsätts för. Ett farligt ämne kan ge liten risk vid lite exponering."),
 ("●●","Varför var flogistonteorin en rimlig teori på sin tid och varför byttes den ut?",[],None,"Den förklarade många observationer och kunde användas, men kunde inte förklara att metaller blir tyngre. Lavoisiers vägningar och syreteorin förklarade det bättre."),
 ("●●●","Du ser rubriken ”Nytt ämne i vardagsprodukt orsakar cancer – en studie på möss”. Skriv fem frågor du vill ha svar på innan du tar ställning.",[],None,"Hur stor var studien? Vilka doser? Gäller det människor? Har andra fått samma resultat? Vem betalade/skriver? Vad säger myndigheter? Svar kan variera."),
 ("●●●","Argumentera för eller emot: ”Det är bättre att vara försiktig med ett ämne trots osäkra belägg.”",[],None,"För: skydda hälsa/miljö vid allvarliga, svåra skador. Mot: kostnader, att man kan förbjuda nyttiga ämnen. Bedöms efter nyansering och användning av belägg."),
]
F_SAMMAN = [
 "Mätningar har osäkerhet. Slumpmässiga fel minskar med upprepning, systematiska fel upptäcks genom kontroll av instrument.",
 "Dosen och exponeringen avgör risken. Fara och risk är olika saker.",
 "Flogistonteorin var en rimlig modell som byttes ut när Lavoisiers mätningar visade något annat.",
 "Forskning kontrolleras genom kollegial granskning och upprepning. Var försiktig med enskilda studier och pseudovetenskap.",
]
F_BEGR = [
 ("Slumpmässigt fel","Fel som varierar från mätning till mätning."),
 ("Systematiskt fel","Fel som alltid går åt samma håll."),
 ("Exponering","Hur mycket, hur länge och hur man utsätts för ett ämne."),
 ("Flogiston","Äldre tänkt ämne som skulle avges vid förbränning."),
 ("Kollegial granskning","Experter granskar en artikel före publicering (peer review)."),
 ("Pseudovetenskap","Påståenden som ser vetenskapliga ut men saknar prövning."),
]

BLOOKET = [
 ("Vad handlar kemi om?","Ämnens uppbyggnad, egenskaper och omvandlingar","Stjärnors rörelser","Växters släktskap","Kroppens muskler"),
 ("Vad menas med en kemikalie i lagstiftningen?","Ämnen och blandningar","Bara farliga ämnen","Bara konstgjorda ämnen","Bara giftiga gaser"),
 ("Är vatten en kemikalie?","Ja","Nej","Bara i havet","Bara i labb"),
 ("Vad är luft?","En blandning av gaser","Ett grundämne","Ett rent ämne","Ett salt"),
 ("Vad är en hypotes?","En tänkt förklaring som kan prövas","En bekräftad naturlag","En mätvärdestabell","En säkerhetsregel"),
 ("Vilken fråga går att undersöka?","Hur påverkar temperaturen lösningstiden?","Vilken smak är bäst?","Är kemi roligast?","Vem är snyggast?"),
 ("Vad kallas det du ändrar i en undersökning?","Oberoende variabel","Beroende variabel","Felkälla","Slutsats"),
 ("Vad kallas det du mäter?","Beroende variabel","Oberoende variabel","Hypotes","Rapport"),
 ("Varför ändrar man bara en sak i taget?","För att se vad som orsakar skillnaden","För att spara tid","För att få fler resultat","För att slippa tabell"),
 ("Hur minskar man påverkan av slumpfel?","Upprepa och räkna medelvärde","Mäta en gång","Byta hypotes","Stryka dåliga värden"),
 ("Vad ska stå på diagrammets axlar?","Namn och enhet","Bara siffror","Bara färger","Ingenting"),
 ("Vad är en felkälla?","Något som kan göra resultatet felaktigt","Ett kemiskt ämne","En typ av diagram","En säkerhetsregel"),
 ("Vad är en bra regel i labbet?","Smaka aldrig på något","Smaka på allt","Ta av glasögonen","Ät under försöket"),
 ("Vad bör du ha på dig för att skydda ögonen?","Skyddsglasögon","Mössa","Handskar på huvudet","Hörselskydd"),
 ("Vad betyder dödskalle med korslagda ben?","Akut giftigt","Brandfarligt","Miljöfarligt","Frätande"),
 ("Vad betyder låga som piktogram?","Brandfarligt","Frätande","Akut giftigt","Explosivt"),
 ("Vilket piktogram visar miljöfara?","Död fisk och träd","Utropstecken","Gasflaska","Låga"),
 ("Vilka signalord används i CLP-märkning?","Fara och Varning","Stopp och Gå","Ja och Nej","Röd och Grön"),
 ("Vad är skillnaden mellan fara och risk?","Risk är sannolikheten att något händer","De är exakt samma","Fara är sannolikheten","Risk är ett piktogram"),
 ("Vad är en förklaringsmodell?","En förenklad idé som förklarar och förutsäger","En exakt kopia av verkligheten","En mätapparat","En lag"),
 ("Vad säger partikelmodellen?","Allt består av små partiklar i rörelse","Allt är fast och orörligt","Materia kan försvinna","Allt består av flogiston"),
 ("Varför löser socker sig snabbare i varmt vatten enligt partikelmodellen?","Partiklarna rör sig snabbare","Partiklarna blir större","Vattnet blir tyngre","Sockret smälter"),
 ("Vad försökte många alkemister göra?","Göra oädla metaller till guld","Bygga raketer","Rena dricksvatten","Tillverka plast"),
 ("Vem visade att förbränning är reaktion med syre?","Lavoisier","Mendelejev","Paracelsus","Dalton"),
 ("Vad innebär massans bevarande?","Massan är lika före och efter en kemisk reaktion","Massan försvinner vid förbränning","Massan ökar alltid","Massan beror på färgen"),
 ("Vem skapade ett periodiskt system 1869?","Mendelejev","Lavoisier","Newton","Curie"),
 ("Vad förutsade Mendelejev med luckor i tabellen?","Att okända grundämnen skulle upptäckas","Att atomer inte finns","Att luft är ett ämne","Att guld kan tillverkas"),
 ("Vad är källkritik?","Att granska avsändare, syfte och belägg","Att alltid tro på källan","Att aldrig läsa texter","Att kopiera text"),
 ("Vilket är en åsikt?","Plast är fult","Vatten kokar vid ungefär 100 °C","Socker löser sig i vatten","Järn rostar"),
 ("Varför är ordet kemikaliefritt problematiskt?","Allt består av kemikalier","Det är ett svårt ord","Det är ett kemiskt ämne","Det betyder farligt"),
]

JEOPARDY = {
 "Kemi i världen": [
  (100,"Så kallas vetenskapen om ämnens uppbyggnad och omvandlingar.","Vad är kemi?"),
  (200,"Ämne eller blandning kallas på lagspråk för detta.","Vad är en kemikalie?"),
  (300,"Luft är ett exempel på denna sorts material med flera ämnen.","Vad är en blandning?"),
  (400,"Smältpunkt och löslighet är exempel på detta hos ett ämne.","Vad är egenskaper?"),
  (500,"Svara varför ”naturligt” inte betyder ”ofarligt”.","Vad är att farlighet beror på ämne och mängd?"),
 ],
 "Undersökningar": [
  (100,"Så kallas en tänkt förklaring som kan prövas.","Vad är en hypotes?"),
  (200,"Det du ändrar i en undersökning.","Vad är oberoende variabel?"),
  (300,"Det du mäter i en undersökning.","Vad är beroende variabel?"),
  (400,"Så minskar du slumpfel.","Vad är att upprepa och beräkna medelvärde?"),
  (500,"Så kallas något som kan ge fel i ditt resultat.","Vad är en felkälla?"),
 ],
 "Säkerhet och märkning": [
  (100,"Ska alltid användas för att skydda ögonen i labbet.","Vad är skyddsglasögon?"),
  (200,"Detta piktogram betyder akut giftigt.","Vad är dödskalle med korslagda ben?"),
  (300,"Två signalord i CLP.","Vad är Fara och Varning?"),
  (400,"Röd ram och symbol som visar fara.","Vad är ett faropiktogram?"),
  (500,"Vad ämnet kan göra jämfört med hur sannolikt det är att det händer.","Vad är skillnaden mellan fara och risk?"),
 ],
 "Modeller och historia": [
  (100,"Modell där allt består av små partiklar i rörelse.","Vad är partikelmodellen?"),
  (200,"Den franske kemisten som vägde ämnen före och efter förbränning.","Vem var Lavoisier?"),
  (300,"Det kallas att massan är lika före och efter en reaktion.","Vad är massans bevarande?"),
  (400,"Han ordnade grundämnena 1869 och lämnade luckor.","Vem var Mendelejev?"),
  (500,"Så kallas en äldre kemisk tradition som försökte göra guld.","Vad är alkemi?"),
 ],
 "Källkritik och argument": [
  (100,"Vem som skriver en text kallas så.","Vad är avsändaren?"),
  (200,"Vad avsändaren vill åstadkomma.","Vad är syftet?"),
  (300,"Plast är fult är ett exempel på detta.","Vad är en åsikt?"),
  (400,"Påstående, skäl och detta behövs i ett bra argument.","Vad är ett belägg?"),
  (500,"Varför kemikaliefritt inte kan stämma.","Vad är att allt består av kemikalier?"),
 ],
}

GRUPPER = [
 ("vad-ar-kemi","Vad är kemi?","Här får du veta vad kemi är, var den finns i vardagen, naturen, samhället och kroppen, och vad ämnen, material och kemikalier egentligen betyder.",["vad-ar-kemi","amnen"]),
 ("undersokningar","Undersökningar och labbsäkerhet","Så planerar, genomför och värderar du en systematisk undersökning, hur du mäter och redovisar och hur du arbetar säkert och läser varningsmärkning.",["undersokning","mata","sakerhet"]),
 ("modeller-historia","Kemins modeller och historia","Vad en förklaringsmodell är, hur partikelmodellen används och hur kemin växte fram från alkemi till Lavoisier och Mendelejev.",["modeller","historia"]),
 ("kallkritik-argument","Källkritik och argumentation","Så granskar du information om kemi, skiljer fakta från åsikter och argumenterar i frågor om miljö och hälsa.",["kallkritik"]),
]

SCEN = None
