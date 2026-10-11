# -*- coding: utf-8 -*-
# Historia kapitel 1: Historiens verktyg (åk 7)
T = dict(
 nr=1, namn="Historiens verktyg", under="Källor, tid, orsaker och hur vi använder det förflutna",
 kort="Historia · Kapitel 1", fil="historia-01-verktyg", arskurs=7, nodeid="historia-verktyg",
 mal=["förklara vad historia är och varför vi läser den",
      "placera händelser och epoker i kronologisk ordning på en tidslinje",
      "skilja mellan primärkällor och sekundärkällor",
      "granska en källa med hjälp av äkthet, tid, beroende och tendens",
      "resonera om orsaker och konsekvenser till en händelse",
      "beskriva vad som förändras och vad som består över tid",
      "förklara vad historiebruk är och ge exempel från vår egen tid",
      "förstå att olika människor kan minnas och berätta samma händelse på olika sätt"],
 fundera="Tänk på något som hände i din familj för länge sedan, till exempel en flytt eller en släktträff. Hur vet du att det hände? Vem har berättat det för dig, och skulle någon annan berätta det på ett annat sätt?",
)

S = []

S.append(dict(id="vad", nr="1.1", ikon="📜", titel="Vad är historia?",
 intro="Historia är både det som hänt och de berättelser vi bygger om det. Ingen kan resa tillbaka i tiden. Därför måste vi arbeta som detektiver och följa spår.",
 block=[
  ("p","Ordet <strong>historia</strong> kommer från grekiskan och betydde ursprungligen ”att undersöka”. Det passar bra. En historiker undersöker vad som hänt, varför det hände och vad det ledde till."),
  ("p","Historia betyder två saker. Dels är det <em>det förflutna</em>, alltså allt som faktiskt hänt. Dels är det <em>berättelserna om det förflutna</em>, det som historiker, museer, filmer och läroböcker (som den här) presenterar. Det förflutna är mycket större än vad någon kan berätta. Därför måste alla berättelser välja ut vissa saker och utelämna andra."),
  ("ruta","tank","Vem blir det en berättelse om?","Under väldigt lång tid skrevs historia mest om kungar, krigare och rika män. Vanliga människor, kvinnor och slavar lämnade färre skrivna spår, och deras liv fick därför mindre plats. Idag försöker många historiker ta reda på mer om dem också."),
  ("p","Varför ska man då läsa historia? Ett skäl är att förstå dagens värld. Skolan, lagarna, matvanorna och till och med ordet ”demokrati” har en historia. Ett annat skäl är att träna sig att tänka kritiskt: vem berättar, vad vill hen, och hur vet vi att det stämmer?"),
  ("p","I skolans kursplan kallas detta att utveckla sitt <strong>historiemedvetande</strong>. Det betyder att du förstår hur det förflutna, nutiden och framtiden hänger ihop. Du får också öva på att ställa frågor till källor, använda historiska begrepp och granska hur historia används."),
  ("ruta","fakta","Förhistoria och historisk tid","Tiden före skriften kallas ofta <strong>förhistoria</strong>. Då kan vi bara studera sådant som finns kvar i marken, som verktyg, gravar och rester av hus. Efter att skriften uppfunnits kan vi också läsa människors egna ord. Skriftens uppkomst är därför en viktig gräns."),
  ("kolla",["Vad betyder ordet historia ursprungligen?","Förklara skillnaden mellan ”det förflutna” och ”berättelser om det förflutna”.","Nämn två skäl till att man läser historia."]),
 ],
 svar=["”Att undersöka”.","Det förflutna är allt som hänt. Berättelserna är det någon väljer ut och berättar om det.","T.ex. förstå nutiden, träna källkritik och kritiskt tänkande."],
))

S.append(dict(id="tid", nr="1.2", ikon="⏳", titel="Tid och tidslinjer",
 intro="Historia handlar om ordning. Vad hände först, och vad hände sen? Att kunna placera händelser i tid kallas kronologi, och tidslinjen är historikerns bästa hjälpmedel.",
 block=[
  ("p","<strong>Kronologi</strong> betyder att man ordnar händelser i den ordning de hände. Vi räknar årtal från Kristi födelse enligt den kristna kalendern. Åren före kallas <strong>f.Kr.</strong> (före Kristus) och åren efter <strong>e.Kr.</strong> (efter Kristus). Många använder idag också förkortningarna fvt och vt (före och efter vår tideräkning), som betyder samma sak."),
  ("ruta","tank","Räkna baklänges","För årtal f.Kr. går det ”tvärtom”: år 500 f.Kr. ligger <em>före</em> år 100 f.Kr. Det finns inget år 0. Räkningen går direkt från 1 f.Kr. till 1 e.Kr."),
  ("p","Historiker delar upp det förflutna i <strong>epoker</strong>, alltså långa tidsperioder med gemensamma drag. Gränserna är ungefärliga och olika länder har olika tider. Här är en vanlig indelning:"),
  ("tab",["Epok","Ungefärlig tid","Kännetecken"],[
    ["Forntid (stenålder, bronsålder, järnålder)","Från de första människorna till ca 800 f.Kr. (i Norden till ca år 1050)","Jakt och jordbruk, första städerna, verktyg av sten och metall"],
    ["Antiken","Ca 800 f.Kr.–500 e.Kr.","Grekland och Rom, stadsstater och stora riken"],
    ["Medeltiden","Ca 500–1500","Kyrkan och adeln har stor makt, byar och slott"],
    ["Tidigmodern tid","Ca 1500–1800","Boktryckarkonstens genomslag, upptäcktsresor, reformation, stater växer"],
    ["Nyare tid","Ca 1800 till idag","Industrisamhälle, världskrig, demokrati, internet"]]),
  ("tidslinje",[("Ca 3000 f.Kr.","Skrift används i Mesopotamien och Egypten"),("776 f.Kr.","De första olympiska spelen enligt traditionen"),("Ca 800–1050","Vikingatiden i Norden"),("1523","Gustav Vasa väljs till kung av Sverige"),("1628","Regalskeppet Vasa sjunker"),("1989","Idén till webben läggs fram"),("Idag","Du läser detta kapitel")]),
  ("p","Epokerna är ett verktyg, inte en naturlag. Ingen människa vaknade en morgon och sa: ”Nu är det medeltid!” Gränserna sätts i efterhand av dem som studerar tiden, och de kan diskuteras. Det man ser som viktigt avgör var man drar strecket."),
  ("kolla",["Vilket kommer först: 300 f.Kr. eller 100 f.Kr.?","Vad är en epok?","Varför är gränserna mellan epoker bara ungefärliga?"]),
 ],
 svar=["300 f.Kr. (det är äldre).","En lång tidsperiod med gemensamma drag.","Eftersom de sätts i efterhand, ändras långsamt och ser olika ut i olika länder."],
))

S.append(dict(id="kallor", nr="1.3", ikon="🏺", titel="Källor – spår från det förflutna",
 intro="Allt vi vet om det förflutna kommer från källor. En källa är alla slags spår som berättar något om hur det var. Utan källor skulle historia bara vara gissningar.",
 block=[
  ("p","Källor kan vara nästan vad som helst: ett brev, en gammal karta, en pjäs, en lerkruka, ett foto, en skattelängd eller en runsten. Historiker delar ofta in dem på två sätt."),
  ("tab",["Typ","Betyder","Exempel"],[
    ["Skriftlig källa","Text av något slag","Brev, dagböcker, lagar, tidningar, kontrakt"],
    ["Föremål och byggnader","Något som människor gjort och använt","Verktyg, smycken, hus, gravar"],
    ["Bild och ljud","Målningar, foton, filmer, inspelningar","Grottmålning, porträtt, radiointervju"],
    ["Muntlig källa","Berättelser som förts vidare eller intervjuer","Släktens historier, minnen"]]),
  ("p","Det andra sättet är viktigare för källkritik. En <strong>primärkälla</strong> (förstahandskälla) är skapad av någon som var med, eller samtidigt med det som hände. Ett brev som en soldat skrev i skyttegraven är en primärkälla. En <strong>sekundärkälla</strong> (andrahandskälla) är skapad senare av någon som inte själv var med, till exempel den här läroboken."),
  ("ruta","exempel","Samma ämne, olika källor","Du vill veta hur en by i Norrbotten levde på 1700-talet. En kyrkbok med födda och döda är en primärkälla. En bok skriven år 2010 av en forskare som läst kyrkböckerna är en sekundärkälla. Båda är användbara, men på olika sätt."),
  ("ruta","historia","En stad av kyrkstugor","I Gammelstad utanför Luleå finns en kyrkstad med omkring 400 små stugor. Dit kom människor från hela socknen för att gå i kyrkan, eftersom resorna var långa. Stugorna, kyrkan och gamla dokument är alla källor till hur folk levde. Gammelstads kyrkstad blev världsarv 1996."),
  ("p","Ingen källa berättar hela sanningen. Vissa saker har förstörts, andra skrevs aldrig ned, och få vanliga människor lämnade egna brev efter sig. Därför har historiker ofta <strong>luckor</strong> i sin kunskap och måste kombinera många olika källor."),
  ("kolla",["Är en dagbok skriven under ett krig en primär- eller sekundärkälla?","Ge exempel på en källa som inte är en text.","Varför har historiker ofta luckor i sin kunskap?"]),
 ],
 svar=["Primärkälla.","T.ex. ett föremål, en byggnad, ett foto eller en film.","Mycket har förstörts eller aldrig skrivits ned, så vi har bara en del av spåren."],
))

S.append(dict(id="kallkritik", nr="1.4", ikon="🔍", titel="Källkritik – kan du lita på källan?",
 intro="Bara för att något står skrivet eller syns på en bild är det inte sant. Källkritik är att ställa frågor till en källa innan du använder den. Det behöver du i skolan, men också på nätet och i vardagen.",
 block=[
  ("p","Det finns fyra klassiska frågor. Kom ihåg fyra nyckelord: äkthet, tid, beroende och tendens."),
  ("tab",["Kriterium","Fråga du ställer","Exempel"],[
    ["Äkthet","Är källan det den utger sig för att vara? Kan den vara förfalskad?","En ”gammal karta” som visar sig vara tryckt förra året"],
    ["Tid (närhet)","Hur nära i tid och plats var upphovspersonen händelsen?","Ett ögonvittne är oftast närmare än en författare 500 år senare"],
    ["Beroende","Har källan fått sin information från någon annan källa?","Fem tidningar som alla skrivit av samma nyhetsbyrå är inte fem oberoende källor"],
    ["Tendens","Vill avsändaren få dig att tycka något särskilt?","En reklamfilm, ett politiskt tal eller en kung som låter skriva sin egen historia"]]),
  ("p","Historiker frågar dessutom: <strong>Vem skrev det, när och varför?</strong> Ett kungabrev, en blogg och en skolbok har olika syften. Det betyder inte att någon av dem är värdelös. En tendensiös källa kan vara en utmärkt källa, om man vill veta hur just den avsändaren tänkte."),
  ("kalla","Konstruerad källa: affisch","”Köp Superfärgens tvättmedel! Alla svenska hem har använt det sedan urminnes tider. Ingen annan duger.”","Konstruerad källa, ungefär från 1950-talet. Är det en reklamtext? Vem skrev den och varför? Hur skulle du kontrollera påståendet?"),
  ("ruta","fakta","Källkritik på nätet","På internet kan vem som helst publicera. Kolla vem som står bakom en sida, om flera oberoende källor säger samma sak, och när texten skrevs. Bilder kan vara redigerade eller sakna sitt sammanhang."),
  ("ruta","tank","Är en tendensiös källa värdelös?","Nej. En kunglig inskription som skryter om segrar säger inte bara hur striden gick utan också hur kungen ville bli sedd. Det är också historia."),
  ("kolla",["Vilka fyra kriterier används i källkritik?","Varför är en samtida källa oftast bättre än en som skrevs långt senare?","Vad menas med att källor är beroende av varandra?"]),
 ],
 svar=["Äkthet, tid (närhet), beroende och tendens.","Den som var med eller levde samtidigt har ofta bättre kunskap och minns mer exakt.","Att de hämtat sin information från samma ursprung, så de egentligen bara upprepar varandra."],
))

S.append(dict(id="orsak", nr="1.5", ikon="🔗", titel="Orsak och konsekvens",
 intro="Historiska händelser kommer sällan av en enda sak. De har flera orsaker, och de i sin tur leder till nya följder. Att reda ut det är en av historikerns viktigaste uppgifter.",
 block=[
  ("p","En <strong>orsak</strong> är något som bidrar till att något annat händer. En <strong>konsekvens</strong> är det som blir resultatet. Historiker brukar skilja mellan orsaker på lång sikt (förhållanden som funnits länge) och på kort sikt (det som direkt satte igång händelsen). Den sista, direkta händelsen kallas ofta <strong>utlösande orsak</strong>."),
  ("ruta","exempel","Varför sjönk Vasa 1628?","Regalskeppet Vasa sjönk på sin jungfrufärd i Stockholms hamn den 10 augusti 1628 och bärgades 1961. <em>Långsiktiga orsaker:</em> Sverige var i krig och behövde kraftfulla skepp. <em>Kortsiktiga orsaker:</em> skeppet var högt och smalt, hade tunga kanoner på flera däck och byggdes under tidspress. <em>Utlösande orsak:</em> en vindby när seglen sattes. <em>Konsekvenser:</em> förlusten av ett dyrt örlogsfartyg och sedan lärdomar om skeppsbyggnad."),
  ("p","Notera att forskare inte pekar ut en enda ”skyldig”. Kungen önskade ett kraftfullt skepp, byggmästarna saknade exakta beräkningar, och ingen vågade säga nej. Det är typiskt: flera orsaker samverkar."),
  ("p","Konsekvenser kan också vara olika slag. Vissa är <em>direkta</em> (kommer snabbt), andra <em>indirekta</em> (kommer senare). Vissa är <em>avsedda</em> och andra <em>oavsedda</em>. När boktryckarkonsten spreds ville tryckarna sälja böcker, men en oavsedd följd blev att idéer kunde spridas snabbare än någonsin."),
  ("ruta","tank","Tre frågor att ställa","1) Vad fanns det för långsiktiga bakgrundsfaktorer? 2) Vad var det som direkt satte igång det? 3) Vad blev följderna på kort och lång sikt, och för vem?"),
  ("kolla",["Vad är skillnaden mellan en orsak och en konsekvens?","Vad är en utlösande orsak?","Varför är det riskabelt att säga att en händelse hade ”en enda orsak”?"]),
 ],
 svar=["Orsaken bidrar till att något händer, konsekvensen är resultatet.","Den sista, direkta händelsen som sätter igång något.","Historiska händelser har nästan alltid flera orsaker som samverkar, så en ensam orsak förenklar för mycket."],
))

S.append(dict(id="forandring", nr="1.6", ikon="🔄", titel="Kontinuitet och förändring",
 intro="Allt förändras, men inte allt på en gång. När vi jämför två tidpunkter ser vi både sådant som blivit annorlunda och sådant som är sig likt. Det är kontinuitet och förändring.",
 block=[
  ("p","<strong>Förändring</strong> är det som blir annorlunda mellan två tider. <strong>Kontinuitet</strong> är det som består eller fortsätter. Det mesta i historien innehåller bådadera. Frågan är alltid: <em>vad</em> förändrades, <em>hur mycket</em>, och <em>för vem</em>?"),
  ("tab",["Område","För 150 år sedan","Idag","Förändring eller kontinuitet?"],[
    ["Skolan","Folkskola, många barn slutade efter få år","Nio års obligatorisk grundskola","Förändring: längre utbildning för alla"],
    ["Mat","Gröt, bröd, fisk och potatis var vanligt","Mycket större utbud, men gröt och bröd finns kvar","Både och"],
    ["Att resa","Till fots, häst, tåg, båt","Bil, flyg, tåg","Förändring: mycket snabbare. Kontinuitet: tåg och båt används fortfarande"],
    ["Att behöva äta och sova","Ja","Ja","Kontinuitet"]]),
  ("p","Förändringar kan gå <strong>snabbt</strong> (en revolution) eller <strong>långsamt</strong> (som när klimatet ändras). De kan också vara <em>framsteg</em> för vissa men inte för andra. När ett samhälle byter från handverk till fabriker får vissa jobb och rikedom, medan andra förlorar sitt levebröd."),
  ("ruta","fakta","Hockey, fika och midsommar","Många saker vi tror är urgamla är faktiskt ganska nya, medan andra har äldre rötter än vi anar. Midsommar firades i Norden långt före hockeyn fanns. Se upp för ordet ”alltid”. ”Så har vi alltid gjort” stämmer sällan om man tittar efter."),
  ("ruta","tank","Mät förändringen","Hur stor en förändring är beror på vad man jämför. Om du jämför år 1900 med idag blir förändringarna stora. Jämför du i stället en vecka med nästa ser du kanske ingen skillnad."),
  ("kolla",["Förklara kontinuitet med ett eget exempel.","Ge ett exempel på en förändring som är bra för vissa men dåligt för andra.","Varför bör man vara försiktig med ordet ”alltid”?"]),
 ],
 svar=["T.ex. att människor fortfarande äter, bor i hus och firar högtider.","T.ex. fabriker gav jobb åt vissa men tog arbetet från hantverkare.","Eftersom saker sällan varit likadana hela tiden, och många traditioner är yngre än man tror."],
))

S.append(dict(id="bruk", nr="1.7", ikon="📣", titel="Historiebruk – hur historia används",
 intro="Historia finns överallt: i politiska tal, reklam, filmer, spel och på nationaldagen. Historiebruk handlar om hur och varför människor använder det förflutna idag.",
 block=[
  ("p","<strong>Historiebruk</strong> betyder att någon använder historia för ett syfte. Det kan vara för att förklara något, väcka stolthet, bekräfta vem man är, få dig att köpa något, rättfärdiga ett beslut eller få människor att ändra sig. Historia är alltså inte bara något som hände, utan också något som används."),
  ("tab",["Var?","Exempel","Möjligt syfte"],[
    ["Politik","En politiker säger: ”Vi har alltid varit ett fritt folk.”","Skapa gemenskap, stöd för en åsikt"],
    ["Reklam","En butik säljer ”gammaldags” godis som tillverkats sedan 1800-talet","Få dig att tro att varan är äkta och pålitlig"],
    ["Film och spel","Ett datorspel utspelar sig i antikens Grekland eller Egypten","Underhålla, tjäna pengar, men ibland också lära ut"],
    ["Högtider och monument","Nationaldagen firas 6 juni","Minnas viktiga händelser, skapa gemenskap"],
    ["Museer","En utställning om stenåldern","Berätta och förklara, men också välja vad som visas"]]),
  ("ruta","historia","Varför just den 6 juni?","Sveriges nationaldag firas den 6 juni för att Gustav Vasa valdes till kung 1523 och för att Sverige fick en ny grundlag 1809. Dagen blev helgdag 2005. Valet av datum är ett exempel på historiebruk: man har valt vilka händelser som ska symbolisera landet."),
  ("p","Spel och filmer är ofta underhållning och därför inte alltid korrekta. Kostymer, språk och händelser kan förenklas eller hittas på. Det betyder inte att de är dåliga, men du bör fråga: <em>vad är sant här, vad är påhittat, och varför?</em>"),
  ("ruta","tank","Fråga till alla berättelser","Vem berättar? Vilken del av historien visas, och vilken utelämnas? Vem tjänar på att den berättas just så? Och vad är jag själv beredd att tro?"),
  ("kolla",["Vad är historiebruk?","Ge ett exempel på historiebruk i reklam eller spel.","Varför kan historiebruk vara problematiskt?"]),
 ],
 svar=["Att någon använder det förflutna för ett syfte, t.ex. att förklara, skapa stolthet eller sälja något.","T.ex. en produkt som marknadsförs som ”traditionell” eller ett spel som utspelar sig i antiken.","Man kan välja ut eller förvränga fakta för att påverka människor."],
))

UPPG = [
 ("Sant eller falskt?","Avgör om påståendena stämmer.",["Historia är bara allt som hänt.","Ett brev skrivet av ett ögonvittne är en primärkälla.","Epoker har exakta, fasta gränser.","En tendens betyder att avsändaren vill påverka dig.","Det finns ett år 0 mellan 1 f.Kr. och 1 e.Kr."],None,"Falskt (det är också berättelser); sant; falskt; sant; falskt."),
 ("Ordna kronologiskt","Sätt i rätt ordning från äldst till yngst: Vasa sjunker, Gustav Vasa blir kung, de första olympiska spelen, vikingatiden.",[],None,"De första olympiska spelen (776 f.Kr.), vikingatiden (ca 800–1050), Gustav Vasa blir kung (1523), Vasa sjunker (1628)."),
 ("Primär eller sekundär?","Avgör om källan är primär eller sekundär.",["En dagbok från en fabriksarbetare år 1890","Din lärobok i historia","En film från 2020 om vikingar","Ett foto taget under ett krig","En lärares sammanfattning av 1800-talet"],None,"Primär; sekundär; sekundär; primär; sekundär."),
 ("Para ihop","Koppla begreppet till rätt förklaring.",["Kronologi","Epok","Tendens","Beroende","Historiebruk","Konsekvens"],["Att information kommer från en annan källa","Hur historia används i nutiden","Ordning i tid","Det som blir resultatet","En lång tidsperiod","Att avsändaren vill påverka"],"1 – C, 2 – E, 3 – F, 4 – A, 5 – B, 6 – D"),
 ("Källkritiska frågor","Du hittar ett brev från 1850-talet i ett gammalt hus. Skriv fyra frågor du vill ställa, en för varje kriterium (äkthet, tid, beroende, tendens).",[],None,"T.ex.: Är brevet äkta? Skrevs det av någon som var med? Har skribenten fått uppgifter av andra? Vill skribenten övertyga läsaren om något?"),
 ("Orsak och konsekvens","Välj en händelse (t.ex. att Vasa sjönk). Skriv en lång- och en kortsiktig orsak, en utlösande orsak och en konsekvens.",[],None,"Se exemplet i 1.5. Eleven ska kunna skilja de olika nivåerna."),
 ("Kontinuitet eller förändring?","Jämför skolan idag med skolan för 100 år sedan. Skriv två saker som förändrats och två som är lika.",[],None,"T.ex. förändring: skolplikt längre, fler ämnen, digitala verktyg. Kontinuitet: lärare, klassrum, betyg, bänkar, läxor."),
 ("Historiebruk","Hitta ett exempel på historiebruk (reklam, spel, film, politik eller högtid). Beskriv vad som visas, vad som lämnas utanför, vem som berättar och vilket syfte det kan ha.",[],None,"Bedöms: tydligt exempel, syfte, avsändare, urval."),
 ("Tidslinjen","Rita en tidslinje över ditt eget liv med minst sex händelser. Markera vilka händelser du själv minns och vilka du vet om från andras berättelser.",[],None,"Eleven skiljer mellan primär och sekundär kunskap (egna minnen kontra andras berättelser)."),
]

BEGREPP = [
 ("Historia","Det som hänt, och berättelserna om det."),
 ("Kronologi","Händelser i den ordning de inträffade."),
 ("Tidslinje","Ett streck med årtal och händelser i ordning."),
 ("Epok","En lång tidsperiod med gemensamma drag."),
 ("f.Kr. / e.Kr.","Före respektive efter Kristi födelse i tideräkningen."),
 ("Källa","Alla spår som berättar något om det förflutna."),
 ("Primärkälla","Källa från samma tid som det som hände."),
 ("Sekundärkälla","Källa skapad senare av någon som inte var med."),
 ("Källkritik","Att granska om och hur man kan lita på en källa."),
 ("Tendens","Att avsändaren vill påverka mottagaren."),
 ("Orsak","Något som bidrar till att något annat händer."),
 ("Konsekvens","Följden av en händelse."),
 ("Kontinuitet","Det som består över tid."),
 ("Förändring","Det som blir annorlunda över tid."),
 ("Historiebruk","Hur människor använder historia för olika syften."),
 ("Historiemedvetande","Förståelsen av hur dåtid, nutid och framtid hänger ihop."),
]

SAMMAN = [
 "Historia är både det som hänt och de berättelser vi bygger om det. Berättelserna är alltid ett urval.",
 "Kronologi är att ordna händelser i tid. Epoker är långa tidsperioder med ungefärliga gränser.",
 "Källor är spår från det förflutna. Primärkällor är samtida, sekundärkällor skapas senare.",
 "Källkritik: äkthet, tid (närhet), beroende och tendens. Fråga vem som skrev, när och varför.",
 "Händelser har flera orsaker, på lång och kort sikt, och utlösande orsaker. Konsekvenser kan vara direkta, indirekta, avsedda eller oavsedda.",
 "Förändring och kontinuitet förekommer samtidigt. Fråga vad som förändrades, hur mycket och för vem.",
 "Historiebruk är att använda det förflutna för ett syfte: i politik, reklam, film, spel och högtider.",
]

TEST_A = [
 ("Vad är en primärkälla?",["En bok som sammanfattar flera böcker","En källa skapad samtidigt med eller av någon som var med på händelsen","En källa som alltid är sann","En källa som är över 100 år gammal"],1),
 ("Vilket årtal ligger närmast vår tid?",["500 f.Kr.","100 f.Kr.","100 e.Kr.","1 f.Kr."],2),
 ("Vilket av följande är ett exempel på tendens?",["En lärobok med sammanfattning","Ett kvitto från en butik","En reklamfilm som lovar att varan är bäst i världen","En väderrapport"],2),
 ("Vad betyder beroende i källkritik?",["Att källan hämtat uppgifter från en annan källa","Att källan är gammal","Att källan är dyr","Att källan är skriven på latin"],0),
 ("Vilket påstående beskriver en utlösande orsak bäst?",["En bakgrund som funnits i många år","En lång tidsperiod","Resultatet av en händelse","Den sista händelsen som direkt sätter igång något"],3),
 ("Vad menas med kontinuitet?",["Något som förändras snabbt","Något som bara hänt en gång","Något som består över tid","Något som slutar"],2),
 ("Varför firas Sveriges nationaldag den 6 juni?",["Gustav Vasa valdes till kung 1523 och en ny grundlag kom 1809","För att Sverige blev kristet då","För att andra världskriget slutade","För att vikingatiden började"],0),
 ("Vilket är ett exempel på historiebruk?",["En arkeolog som mäter ett skelett","En tidslinje på väggen","En ordlista","Ett datorspel som använder antiken för att sälja spelet"],3),
]
TEST_B = [
 ("Förklara skillnaden mellan primär- och sekundärkälla.","Primärkälla är samtida eller skapad av någon som var med. Sekundärkälla skapas senare av någon som inte var med."),
 ("Nämn de fyra källkritiska kriterierna.","Äkthet, tid (närhet), beroende, tendens."),
 ("Ge ett exempel på en långsiktig och en kortsiktig orsak till att Vasa sjönk.","Långsiktig: kriget gjorde att man ville ha kraftfulla skepp. Kortsiktig: skeppet var högt, smalt och tungt lastat med kanoner."),
 ("Förklara kontinuitet och förändring med ett exempel.","T.ex. skolan: förändring att alla går nio år i skolan, kontinuitet att lärare undervisar i klassrum."),
 ("Vad är historiebruk? Ge ett exempel.","Att använda historia för ett syfte, t.ex. i reklam, politik eller spel."),
 ("Varför kan man inte lita blint på en tendensiös källa, men ändå ha nytta av den?","Den ger inte en neutral bild men visar hur avsändaren ville bli uppfattad, vilket också är historia."),
]

KALLA = dict(
 text="”Jag skriver till dig från skyttegraven. Vi har inte sett solen på tre dagar. Leran är värst. Men jag hör att generalen säger att allt går som planerat, och att kriget snart är över. Jag tror inte på det.”",
 ursprung="Konstruerad källa, ett påhittat brev från en soldat under ett krig i början av 1900-talet. Brevet är skrivet till en syster hemma och är inte avsett att publiceras.",
 fragor=[
  ("Är källan en primär- eller sekundärkälla? Motivera.","Primärkälla: den är skriven av någon som själv var med, samtidigt med händelsen."),
  ("Vad kan vi lära oss om soldatens situation? Ge två saker.","T.ex. att det var kallt och lerigt, att soldaterna var trötta och att livet i skyttegraven var hårt."),
  ("Vilka tendenser kan finnas i brevet?","Soldaten kanske överdriver för att tala om hur hårt det är, eller att han är bitter mot ledningen. Brevet kan också vara censurerat eller anpassat för att inte oroa systern."),
  ("Vad skulle du vilja jämföra brevet med för att kontrollera det?","Andra soldaters brev och dagböcker, officiella rapporter och bilder från fronten."),
 ])

SKRIV = dict(
 uppgift="Välj en händelse eller ett föremål du känner till, till exempel att Vasa sjönk 1628, en runsten eller Gammelstads kyrkstad. Skriv en text på ca en sida där du (1) berättar kort vad som hände eller vad föremålet är, (2) förklarar vilka källor man kan använda och hur man kan granska dem, (3) beskriver orsaker och konsekvenser och (4) diskuterar hur historien används idag.",
 stod=[
  "E: Eleven berättar enkelt vad som hänt, nämner minst en primär- och en sekundärkälla och beskriver minst en orsak och en konsekvens. Eleven gör något enkelt källkritiskt påpekande, till exempel vem som skrivit källan.",
  "C: Eleven använder flera källkritiska kriterier (äkthet, tid, beroende, tendens) på konkreta källor. Eleven beskriver både långsiktiga och kortsiktiga orsaker och olika följder, och ger ett tydligt exempel på historiebruk med syfte.",
  "A: Eleven för ett nyanserat resonemang, väger källornas värde mot varandra, förklarar hur olika orsaker hänger ihop, visar hur synen på händelsen ändrats över tid och diskuterar vem som använder historien, hur och varför.",
 ])

LAB = dict(
 titel="Historikerns verkstad: Mystiska föremålet",
 syfte="Eleverna övar på att undersöka en källa, ställa källkritiska frågor och dra försiktiga slutsatser utifrån begränsat underlag.",
 material="Ett föremål per grupp (t.ex. gammal nyckel, mynt, äldre foto, hushållsapparat eller ett nutida föremål som eleverna inte känner igen), pappersark, penna, tillgång till internet eller bibliotek, mall med källkritiska frågor.",
 utforande=[
  "Dela in klassen i grupper om 3–4. Varje grupp får ett föremål eller en bild av ett föremål i en påse. Berätta inte vad det är.",
  "Beskriv föremålet noggrant: material, storlek, form, färg, skador, märken. Skriv bara det ni ser, inte vad ni tror.",
  "Ställ hypoteser: Vad kan det ha använts till? Vem kan ha använt det? Hur gammalt kan det vara? Skriv minst tre alternativ.",
  "Granska med äkthet, tid, beroende och tendens. Är det äkta? Vem gjorde det och när? Vad säger andra källor?",
  "Undersök med böcker eller internet. Vilken ny information hittar ni, och är den pålitlig?",
  "Presentera för klassen: vad är det, hur vet ni, hur säkra är ni, och vad vet ni inte?",
  "Avsluta med en gemensam diskussion om vad som var svårast och hur historiker hanterar osäkerhet.",
 ],
 fragor=[
  ("Vad var skillnaden mellan det ni såg och det ni gissade?","Det ni såg är observationer. Det ni gissade är tolkningar."),
  ("Vilka källor skulle behövas för att vara säkra?","Fler föremål av samma slag, texter eller bilder från samma tid, expertutlåtanden, dateringsmetoder."),
  ("Varför är det viktigt att redovisa vad man inte vet?","För att resultaten inte ska se säkrare ut än de är och för att andra ska kunna fortsätta undersöka."),
 ],
 bonus="BONUS för läraren: Använd föremål som har en lokal koppling (t.ex. från hembygdsföreningen eller ett museum, eller bilder från Digitaltmuseum.se). Låt några grupper få ett föremål som är en kopia eller modern imitation, så att äkthetsfrågan blir levande. Bedöm med fokus på resonemang, inte på att ”gissa rätt”.",
)

LARAR = [
 ("Koppling till Lgr22 (Historia)","Kapitlet tränar kursplanens syfte: historiemedvetande, historisk referensram och kronologi, historiska begrepp, förmåga att ställa frågor till källor och granska dem, samt att reflektera över historiebruk. Det centrala innehållet berörs genom att källor och källkritik samt historiebruk finns med i alla tre block (här tränas metoderna som kapitlen 2–15 bygger vidare på). Kunskapskraven: kunskaper om förändringsprocesser och historiska begrepp, resonemang om orsaker och konsekvenser, kontinuitet och förändring, källor och historiebruk."),
 ("Förslag på upplägg (8 lektioner)","1. Vad är historia? Brainstorm: berätta samma händelse från två perspektiv (1.1). 2. Tidslinje och epoker: klassen bygger en gemensam tidslinje (1.2). 3. Källor: primär/sekundär med föremål eller bilder (1.3). 4. Källkritik: öva äkthet, tid, beroende och tendens på fyra korta källor, gärna reklam och en nyhetsartikel (1.4). 5. Orsak och konsekvens: Vasa eller ett eget exempel (1.5). 6. Kontinuitet och förändring: jämför skolan, mat eller resande då och nu (1.6). 7. Historiebruk: analysera en reklam, ett spel eller en film (1.7). 8. Historikerns verkstad, test och tidsresan (SCEN)."),
 ("Vanliga missuppfattningar","”Primärkälla = sann källa.” Nej, även primärkällor kan ljuga eller ha tendens. ”Sekundärkälla = dålig källa.” Nej, de är ofta bäst på överblick. ”Historia är bara fakta och årtal.” Historia handlar om tolkning och urval. ”Tendens betyder att något är falskt.” Nej, det betyder att avsändaren vill påverka. ”Epoker har exakta gränser.” De är verktyg som historiker bestämt. Elever blandar också ihop orsak och konsekvens och tror ofta att det bara finns en förklaring."),
 ("Bedömningsstöd (E/C/A)","<strong>E:</strong> eleven kan i enkla drag beskriva begreppen, ordna händelser i tid, ge exempel på primär- och sekundärkällor och göra enkla källkritiska iakttagelser, samt beskriva en orsak, en följd och något som förändrats. <strong>C:</strong> eleven använder flera kriterier på konkreta källor, skiljer lång- och kortsiktiga orsaker, förklarar både kontinuitet och förändring och beskriver historiebruk med syfte. <strong>A:</strong> eleven gör välgrundade och nyanserade resonemang, väger källor mot varandra, förklarar samband mellan orsaker och visar hur historia används och med vilka intressen."),
 ("Blooket/Jeopardy: 10 bra kategorier","1. Begrepp (kronologi, epok, tendens). 2. Primär eller sekundär? 3. Årtal och epoker. 4. Källkritik i vardagen (nätet, reklam). 5. Orsak eller konsekvens? 6. Förändring eller kontinuitet? 7. Historiebruk i spel och film. 8. Sverige: Vasa, nationaldagen, Rökstenen, kyrkstaden. 9. Vem är jag? (arkeolog, historiker, museum). 10. Sant eller falskt. Exempel: ”En skriven berättelse från ett vittne” → primärkälla; ”Epok mellan antiken och tidigmodern tid” → medeltiden."),
]

KALLOR = [
 ("Skolverket – Kommentarmaterial till kursplanen i historia (syfte och centralt innehåll, Lgr22)","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
 ("Forum för levande historia – Källkritik, historiebruk och rasism (klassrumsmaterial)","https://www.levandehistoria.se/wp-content/uploads/2022/11/kallkritik_historiebruk_och_rasism_-_om_klassrumsmaterialet.pdf"),
 ("Store norske leksikon (SNL) – Rökstenen","https://snl.no/R%C3%B6kstenen"),
 ("Göteborgs universitet – Ny tolkning av Rökstenens runinskrift","https://www.gu.se/nyheter/ny-tolkning-av-rokstenens-runinskrift-andrar-bilden-av-vikingatiden"),
 ("UNESCO – Förvaltningsplan för världsarvet Gammelstads kyrkstad","https://whc.unesco.org/document/222094"),
 ("World History Encyclopedia – Rosetta Stone","https://worldhistory.org/Rosetta_Stone"),
 ("Göteborgs universitet – Vikingar reste runsten av rädsla för klimatkatastrof (Rökstenen, 2020)","https://www.gu.se/nyheter/vikingar-reste-runsten-av-radsla-for-klimatkatastrof"),
 ("World History Encyclopedia – Kinesiska muren (inklusive myten om rymden)","https://www.worldhistory.org/Great_Wall_of_China/"),
]

F = []
F.append(dict(id="f1", nr="F1", ikon="⛏️", titel="Så arbetar arkeologer och historiker",
 intro="Arkeologer och historiker undersöker båda det förflutna, men med olika material och metoder. Ofta behöver de varandra.",
 block=[
  ("p","<strong>Arkeologer</strong> studerar främst materiella spår: föremål, byggnader, gravar och avfall. De gräver försiktigt lager för lager och dokumenterar var allt hittas. Ett föremål utan känd plats säger mycket mindre än ett som hittats i ett tydligt sammanhang. Det är därför man inte ska gräva upp saker på egen hand."),
  ("p","<strong>Historiker</strong> arbetar främst med skrivna källor i arkiv och bibliotek, till exempel brev, protokoll och tidningar. De jämför källor, ställer frågor, letar efter mönster och formulerar tolkningar som de kan stödja med belägg."),
  ("tab",["Steg","Arkeolog","Historiker"],[
    ["Fråga","Hur levde man på platsen?","Varför fattades beslutet?"],
    ["Insamling","Gräver, mäter, fotograferar","Läser och kopierar dokument"],
    ["Datering","Kolisotopmetoden (C14) och lagerföljd","Datum i texter och jämförelse mellan källor"],
    ["Tolkning","Vad kan fynden betyda?","Vad kan texterna betyda?"],
    ["Redovisning","Rapport, utställning","Bok, artikel, föredrag"]]),
  ("ruta","fakta","Rosettastenen – nyckeln till hieroglyferna","Rosettastenen är en stentavla från år 196 f.Kr. med samma text på tre skriftsystem: egyptiska hieroglyfer, demotisk skrift och grekiska. Den hittades 1799 under Napoleons fälttåg i Egypten. Eftersom grekiska gick att läsa kunde Jean-François Champollion 1822 visa hur hieroglyferna fungerade. Idag finns stenen på British Museum i London."),
  ("ruta","tank","Ett sammanhang gör skillnaden","Tänk dig att du hittar ett mynt. Om du vet var, hur djupt och bredvid vad det låg kan forskare säga mycket. Om du bara har myntet i handen får de gissa mer."),
  ("kolla",["Vad är skillnaden mellan hur en arkeolog och en historiker oftast arbetar?","Varför är fyndplatsen så viktig?","Hur kunde grekiskan hjälpa Champollion?"]),
 ],
 svar=["Arkeologer studerar främst föremål och platser, historiker främst skrivna källor.","Den berättar sammanhang: tid, plats och vad föremålet fanns tillsammans med.","Grekiska kunde läsas, så den kunde användas för att tyda samma text på hieroglyfer."],
))
F.append(dict(id="f2", nr="F2", ikon="🗣️", titel="Minnen och olika perspektiv",
 intro="Två människor kan vara med om samma sak och ändå berätta olika. Det beror på att minnen, erfarenheter och intressen formar våra berättelser.",
 block=[
  ("p","<strong>Perspektiv</strong> är den utsiktspunkt man ser något från. En general, en soldat, en bonde och en barnmorska kan alla ha varit med om ett krig, men de berättar om helt olika saker. Ingen av dem ljuger nödvändigtvis. De har olika sidor av samma händelse."),
  ("p","Minnen förändras också med tiden. Vi glömmer, fyller i luckor och formar berättelser så att de blir begripliga. Därför är muntliga källor och minnesberättelser både värdefulla och försiktigt att tolka. Historiker jämför ofta minnen med andra källor."),
  ("ruta","exempel","Konstruerat exempel: fotbollsmatchen","Efter en match säger laget som förlorade att domaren var orättvis. Det andra laget säger att domaren dömde rätt. Åskådarna minns att det regnade mycket. Alla kanske berättar ärligt, men de lyfter olika saker. Vill du förstå matchen behöver du fler berättelser och gärna en film."),
  ("p","Det är också viktigt att fråga vilka röster som saknas. Under långa perioder skrevs historia av dem som hade makt, och människor som saknade makt hördes sällan. Idag söker forskare ofta efter fler perspektiv, till exempel genom att undersöka hur kvinnor, barn eller arbetare levde."),
  ("ruta","tank","Historisk empati","<strong>Historisk empati</strong> betyder att försöka förstå hur människor i en annan tid tänkte och kände, utan att ursäkta allt de gjorde. Du behöver inte tycka som dem för att förstå varför de handlade som de gjorde."),
  ("kolla",["Vad menas med perspektiv?","Varför kan två ärliga vittnen berätta olika?","Vad är historisk empati?"]),
 ],
 svar=["Den utsiktspunkt man ser något från.","De har sett olika saker, har olika erfarenheter och minns och tolkar på olika sätt.","Att försöka förstå hur människor i en annan tid tänkte och kände."],
))
F.append(dict(id="f3", nr="F3", ikon="🪨", titel="Rökstenen – en tolkning som ändras",
 intro="Rökstenen i Östergötland har en av Nordens längsta runinskrifter. Forskare har tolkat den på olika sätt genom åren, vilket visar hur historia kan förändras utan att nya källor dyker upp.",
 block=[
  ("p","Rökstenen står vid Röks kyrka i Ödeshögs kommun och är troligen från 800-talet. Bara ett fåtal runstenar har en så lång text. Inskriften har omkring 750 runor. Den har fascinerat forskare i över ett sekel, eftersom den innehåller anspelningar på berättelser som vi inte längre känner."),
  ("p","Den äldre forskningen läste stenen ofta som en berättelse om hjältar, kungar och strider, och som ett minnesmärke över en död son. År 2016 föreslog språkforskaren Per Holmberg vid Göteborgs universitet i stället att inskriften handlar om själva runskriften: att den gör det möjligt att bevara minnet av de döda. År 2020 la ett forskarlag fram ännu en tolkning: att gåtorna på stenen hänger ihop med oro för en klimatkatastrof efter en kall period. Tre tolkningar av samma sten visar att forskare kan komma fram till olika svar."),
  ("ruta","fakta","Fakta eller tolkning?","Att stenen finns, var den står och att den har runor är <em>fakta</em>. Vad texten betyder är <em>tolkning</em>. Tolkningar kan bli mer eller mindre övertygande, men de kan sällan bevisas helt. Lägg märke till hur ord som ”troligen” och ”föreslår” signalerar osäkerhet."),
  ("p","Det här är ett bra exempel på att historia inte är ett färdigt facit. Samma källa kan ge ny kunskap när nya frågor ställs eller när nya metoder används. Det betyder inte att alla tolkningar är lika bra. De bästa tolkningarna är de som stämmer med flest belägg och förklarar mest."),
  ("kolla",["Vad är skillnaden mellan fakta och tolkning i fallet Rökstenen?","Hur kan en tolkning ändras utan att nya källor hittas?","Varför är ordet ”troligen” viktigt i historia?"]),
 ],
 svar=["Att stenen finns och har runor är fakta. Vad inskriften betyder är tolkning.","Forskare ställer nya frågor och använder nya metoder på samma källa.","Det visar att man inte är helt säker och att tolkningen kan ändras."],
))
F.append(dict(id="f4", nr="F4", ikon="🛰️", titel="Myten om Kinesiska muren",
 intro="Många har hört att Kinesiska muren syns från rymden. Det stämmer inte. Exemplet visar hur en myt kan leva kvar och hur källkritik kan avslöja den.",
 block=[
  ("p","Påståendet att Kinesiska muren kan ses från månen eller rymden är ett av världens mest spridda historiska ”fakta”. Det är en myt. Redan år 1895, långt innan någon åkt ut i rymden, skrev den engelske författaren Henry Norman att muren var det enda mänskliga verket som skulle synas från månen. Ingen hade kunnat kontrollera det."),
  ("p","När astronauter senare tittat ned har de berättat att det är mycket svårt att se muren med blotta ögat. Den är lång men ofta smal och i samma färg som landskapet runtom."),
  ("ruta","fakta","Bakgrunden till muren","Den första sammanhängande muren lät kejsar Qin Shi Huangdi bygga omkring 221 f.Kr. Den låg längre norrut än dagens mur och bara lite av den finns kvar. Det mesta av muren som syns idag byggdes under Mingdynastin (1368–1644 e.Kr.). Med alla grenar mäts murens längd till ungefär 21 000 kilometer."),
  ("p","Hur lever en sådan myt vidare? Den är en bra historia, den upprepas i böcker och filmer och många kontrollerar aldrig. Det är beroende i praktiken: många författare skriver av varandra. Källkritiskt blir lärdomen: fråga efter vem som först sa något, och hur det kunde ha vetats."),
  ("kolla",["Vad är myten om Kinesiska muren?","Hur kan man avslöja en sådan myt?","Vilket källkritiskt kriterium hjälper myten att spridas?"]),
 ],
 svar=["Att muren syns från rymden eller månen.","Genom att spåra påståendets ursprung och jämföra med vad astronauter faktiskt kunnat se.","Beroende: folk skriver av varandra utan att kontrollera."],
))

F_UPPG = [
 ("●","Förklara med egna ord varför fyndplatsen är så viktig för en arkeolog.",[],None,"Platsen och lagret ger sammanhang: ålder, andra fynd och hur föremålet användes."),
 ("●●","Jämför ett vittnesmål och ett foto som källor till samma händelse. Vilka styrkor och svagheter har varje källa?",[],None,"Vittnesmål: personligt, kan ge motiv och känslor, men minnet kan svika och ha tendens. Foto: visar ögonblick men kan vara arrangerat, beskuret eller sakna sammanhang."),
 ("●●","Hitta ett exempel på en myt, till exempel Kinesiska muren. Visa hur den uppstod och spreds. Vilka källkritiska frågor hjälper dig att avslöja den?",[],None,"Fritt. Svaret ska ange ursprung, spridning och källkritiska frågor (vem sa det först? hur kunde man veta det? kontroll)."),
 ("●●●","Diskutera: Är det möjligt att skriva en helt objektiv historia? Använd begreppen urval, perspektiv och tendens.",[],None,"Argument: allt berättande kräver urval, och författare har perspektiv. Men man kan sträva efter att vara öppen med källor, redovisa osäkerhet och ta hänsyn till flera perspektiv."),
 ("●●●","Jämför hur Rökstenen kan tolkas som en hjältesaga, som en text om skriften eller som ett uttryck för oro för klimatet. Vad krävs för att en tolkning ska vara övertygande?",[],None,"Belägg i texten, jämförelse med andra runstenar, språklig kunskap, logik och att tolkningen förklarar mycket utan att bortse från fakta."),
]
F_SAMMAN = [
 "Arkeologer studerar föremål och platser, historiker främst texter. De kompletterar varandra.",
 "Perspektiv och minnen formar berättelser. Fler röster ger en rikare bild.",
 "Historisk empati är att förstå människor i andra tider, utan att behöva ursäkta dem.",
 "Fakta och tolkning är olika saker. Tolkningar kan ändras när frågor och metoder ändras.",
 "Myter kan leva länge när många skriver av varandra. Källkritik hjälper att spåra ursprunget.",
]
F_BEGR = [
 ("Arkeologi","Läran om det förflutna genom föremål och platser."),
 ("Perspektiv","Utsiktspunkten man ser något från."),
 ("Historisk empati","Att förstå människor i en annan tid."),
 ("Tolkning","En förklaring av vad källor betyder."),
 ("Myt","En spridd berättelse som inte stämmer."),
 ("Datering","Att bestämma hur gammalt något är."),
]

BLOOKET = [
 ("Vad betyder ordet historia från början?","Att undersöka","Att berätta saga","Att räkna år","Att gräva"),
 ("Vad kallas det när man ordnar händelser i den ordning de hände?","Kronologi","Epok","Tendens","Konsekvens"),
 ("Vad betyder f.Kr.?","Före Kristus","Efter kriget","Före kronan","Förr och nu"),
 ("Vilket år kom först?","200 f.Kr.","100 f.Kr.","1 e.Kr.","100 e.Kr."),
 ("Vilken tid brukar antiken sägas omfatta (ungefär)?","Ca 800 f.Kr.–500 e.Kr.","Ca 1500–1800","Ca 1900–2000","Ca 500–1500"),
 ("Vad kallas en lång tidsperiod med gemensamma drag?","Epok","Källa","Ögonblick","Beroende"),
 ("Vad är en primärkälla?","Samtida källa","Lärobok","Sammanfattning","Gissning"),
 ("Vilken är en sekundärkälla?","En lärobok","En dagbok från 1800","Ett fynd i en grav","Ett brev från en soldat"),
 ("Vilken fråga hör till kriteriet äkthet?","Är det förfalskat?","Vem tjänar på det?","När skrevs det?","Vem kopierade det?"),
 ("Vad betyder tendens i källkritik?","Avsändaren vill påverka","Källan är gammal","Källan är kopierad","Källan är dyr"),
 ("Vad betyder beroende i källkritik?","Källan bygger på en annan källa","Källan är äkta","Källan är skriven av barn","Källan är på latin"),
 ("Vilken källa är oftast närmast händelsen?","Ett ögonvittnes dagbok","En film 100 år senare","En lärobok","En blogg"),
 ("Vad kallas den sista, direkta händelsen som sätter igång något?","Utlösande orsak","Konsekvens","Kontinuitet","Epok"),
 ("Vilket år sjönk regalskeppet Vasa?","1628","1523","1912","1989"),
 ("Vilket år bärgades Vasa?","1961","1628","1523","1809"),
 ("Vad kallas det som består över tid?","Kontinuitet","Förändring","Tendens","Revolution"),
 ("Vilket är en förändring?","Alla barn går idag i skola i nio år","Folk behöver äta","Människor firar högtider","Familjer bor i hus"),
 ("Vad är historiebruk?","Att använda historia för ett syfte","Att gräva efter fynd","Att räkna årtal","Att kopiera böcker"),
 ("Varför firas nationaldagen 6 juni?","Gustav Vasa valdes 1523 och grundlag 1809","Vikingatiden slutade","Andra världskriget slutade","Skolan startade"),
 ("Vad kallas det när man försöker förstå människor i andra tider?","Historisk empati","Tendens","Kronologi","Datering"),
 ("Vad studerar arkeologer främst?","Studerar föremål och platser","Läser bara brev","Skriver reklam","Bygger museer"),
 ("Vad hjälpte Champollion att tyda hieroglyferna?","Rosettastenen","Vasa","Rökstenen","Hammurabis lag"),
 ("Stämmer det att Kinesiska muren syns från rymden?","Nej, det är en myt","Ja, alltid","Ja, men bara på natten","Bara från månen"),
 ("Vilken fråga är mest källkritisk?","Vem skrev det och varför?","Hur stor är den?","Vilken färg har den?","Var kan jag köpa den?"),
 ("Vad menas med perspektiv?","Den utsiktspunkt man ser något från","Ett årtal","Ett föremål","En mätmetod"),
 ("Vad kallas en forskares förslag på vad Rökstenens inskrift betyder?","Tolkning","Fakta","Myt","Förfalskning"),
]

JEOPARDY = {
 "Begrepp":[(100,"Ordning i tid.","Vad är kronologi?"),(200,"Lång tidsperiod med gemensamma drag.","Vad är en epok?"),(300,"Det som består över tid.","Vad är kontinuitet?"),(400,"Att avsändaren vill påverka dig.","Vad är tendens?"),(500,"Förståelse för hur dåtid, nutid och framtid hänger ihop.","Vad är historiemedvetande?")],
 "Källor":[(100,"En dagbok från en soldat.","Vad är en primärkälla?"),(200,"Din lärobok är en sådan källa.","Vad är en sekundärkälla?"),(300,"Spåret är inte en text, men ändå en källa.","Vad är ett föremål (t.ex. ett fynd)?"),(400,"Fråga som rör om källan är förfalskad.","Vad är äkthet?"),(500,"Fem tidningar som skrev av samma nyhetsbyrå.","Vad är beroende?")],
 "Orsak och följd":[(100,"Skeppet som sjönk 1628.","Vad är Vasa?"),(200,"Sista händelsen som sätter igång något.","Vad är utlösande orsak?"),(300,"Följd som ingen ville ha.","Vad är en oavsedd konsekvens?"),(400,"Orsaker som funnits länge.","Vad är långsiktiga orsaker?"),(500,"Så brukar historiker se på orsakerna till en händelse, i stället för att peka ut en enda.","Vad är att flera orsaker samverkar?")],
 "Tid":[(100,"Det första året i e.Kr.-räkningen, direkt efter 1 f.Kr.","Vad är år 1 e.Kr.?"),(200,"Epok mellan antiken och tidigmodern tid.","Vad är medeltiden?"),(300,"Året då Gustav Vasa valdes.","Vad är 1523?"),(400,"Det finns inget år med detta nummer mellan 1 f.Kr. och 1 e.Kr.","Vad är år 0?"),(500,"Året då Sverige fick en ny grundlag, något som nationaldagen också firar.","Vad är 1809?")],
 "Historiebruk":[(100,"Datum för Sveriges nationaldag.","Vad är 6 juni?"),(200,"Ett medium där antiken ofta används som kuliss.","Vad är datorspel/film?"),(300,"Det här vill en reklamfilm som säger 'sedan 1800-talet' ofta uppnå hos tittaren.","Vad är att skapa förtroende och sälja?"),(400,"Fråga: vem berättar och vem tjänar på det?","Vad är en källkritisk/historiebruksfråga?"),(500,"Myt om att Kinesiska muren syns från rymden.","Vad är en spridd myt utan stöd?")],
}

GRUPPER = [
 ("vad-och-tid","Vad är historia? Tid och källor","Vad historia är, hur vi mäter tid och vilka spår som berättar om det förflutna.",["vad","tid","kallor"]),
 ("granska","Granska och förklara","Hur du granskar källor och förklarar orsaker och förändringar.",["kallkritik","orsak","forandring"]),
 ("bruk","Använd historien","Hur historia används i samhället idag.",["bruk"]),
]

SCEN = dict(
 titel="Tidsresa: en historikers arbete", plats="Från arkivet till utställningen", tid="Ett undersökningsprojekt",
 sky=("#c9d6e3","#eadfc8"), mark="#7a6648",
 walker=dict(typ="resenar"),
 etapper=[
  dict(x_etikett="Arkivet", tid="Dag 1", plats="Ett arkiv", rubrik="Frågan och arkivet",
   fakta=["Du är historiker. Du vill veta hur människor levde i en liten stad för 200 år sedan. Du går till ett arkiv, där gamla papper sparas.","I arkivet finns tusentals brev och böcker. Du hinner inte läsa allt. Därför skriver du först en fråga: Vad arbetade och åt folk? Frågan visar vilka papper du ska läsa och vilka du kan lämna."],
   ord=[("arkiv","ett ställe där gamla papper och brev sparas"),("källa","något som berättar om det som hänt, till exempel ett brev")],
   fraga="Varför börjar historikern med en fråga?", alt=["För att kunna välja de papper som hjälper till att svara","För att kunna läsa allt i arkivet","För att få svaret utan att leta"], ratt=0,
   forklaring="Frågan hjälper dig att välja rätt källor. Du hinner inte läsa allt.", deko=[("bokhylla",-120,1.2),("slott",160,0.9)]),
  dict(x_etikett="Fyndet", tid="Dag 4", plats="En byggarbetsplats", rubrik="Ett arkeologiskt fynd",
   fakta=["Arkeologer gräver på en byggarbetsplats. De hittar bitar av en kruka och ett gammalt golv.","De mäter exakt var varje bit ligger och hur djupt. Ligger bitarna bredvid en gammal eldplats, vet de att krukan användes i ett kök. Om man lyfter upp saken utan att skriva ner var den låg, försvinner det beviset."],
   ord=[("arkeolog","forskare som gräver upp saker från förr")],
   fraga="Varför är det viktigt att skriva ner var ett fynd ligger?", alt=["Platsen visar hur och när saken användes","Då blir fyndet mer värt","Då hittar man fler krukor"], ratt=0,
   forklaring="Platsen runt fyndet berättar vad det användes till.", deko=[("amfora",-60,1.0),("torp",120,0.9),("trad",200,1.0)]),
  dict(x_etikett="Brevet", tid="Dag 9", plats="Ett dammigt förråd", rubrik="Brevet",
   fakta=["I en gammal kista hittar du ett brev från en handlare. Han skrev det själv för 200 år sedan.","En primärkälla är gjord av någon som var med när det hände. En sekundärkälla är gjord senare av någon som inte var med, till exempel en lärobok."],
   ord=[("primärkälla","källa från någon som var med när det hände"),("sekundärkälla","källa som skrivits senare av någon som inte var med")],
   fraga="Handlaren skrev brevet själv medan det hände. Vad är brevet för typ av källa?", alt=["Sekundärkälla","Primärkälla","Ingen källa alls"], ratt=1,
   forklaring="Brevet skrevs av någon som var med. Då är det en primärkälla.", deko=[("marknad",-100,1.0),("kyrka",150,0.9)]),
  dict(x_etikett="Datering", tid="Dag 14", plats="Laboratorium", rubrik="Hur gammalt är det?",
   fakta=["Nu vill du veta om brevet är äkta. Papperet och bläcket undersöks. Handstilen jämförs med andra brev.","Källkritik betyder att pröva en källa med frågor. Äkthet: är den verklig, och när skrevs den? Tendens: vill skribenten få dig att tro något? Närhet: var skribenten själv med?"],
   ord=[("källkritik","att pröva om man kan lita på en källa"),("äkthet","att något är riktigt och inte falskt")],
   fraga="Papper, bläck och handstil undersöks. Vilken källkritisk fråga prövar du?", alt=["Tendens","Äkthet och tid","Närhet"], ratt=1,
   forklaring="Du kontrollerar om brevet är äkta och när det skrevs.", deko=[("skola",-80,1.0),("dator",150,0.8)]),
  dict(x_etikett="Granskning", tid="Dag 20", plats="Arbetsrummet", rubrik="Kritisk granskning",
   fakta=["Du läser brevet noga. Handlaren skriver att hans konkurrent är en tjuv.","Handlaren tjänar på att konkurrenten får dåligt rykte. Det kallas tendens. Kanske har han överdrivit eller ljugit. Du vet inte om det stämmer."],
   ord=[("konkurrent","någon som säljer samma sak som du"),("tendens","att skribenten vill påverka dig eller tjäna på det")],
   fraga="Vad bör du göra med påståendet att konkurrenten är en tjuv?", alt=["Tro på det rakt av","Jämföra med andra källor","Slänga hela brevet"], ratt=1,
   forklaring="Handlaren kan ha tendens. Därför jämför du med andra källor.", deko=[("bokhylla",-110,1.1),("marknad",120,0.9)]),
  dict(x_etikett="Tolkning", tid="Dag 30", plats="Skrivbordet", rubrik="Orsaker och tolkning",
   fakta=["Du lägger ihop brevet, fynden och andra papper. Du ser att staden växte när handeln ökade.","Fakta är sådant du kan visa med källor, till exempel att brevet finns. En tolkning är din slutsats, till exempel varför staden växte. Du skriver tydligt vilket som är vilket."],
   ord=[("tolkning","en slutsats du drar utifrån källorna"),("belagt","visat med hjälp av källor")],
   fraga="Varför ska en historiker skilja på fakta och tolkning?", alt=["Så att läsaren ser vad som är belagt och vad som är en slutsats","Så att osäkra delar döljs","Så att texten blir längre"], ratt=0,
   forklaring="Då kan andra kontrollera vad som är belagt och vad som är en slutsats.", deko=[("hamn",-90,1.0),("segelfartyg",140,0.9)]),
  dict(x_etikett="Utställning", tid="Dag 60", plats="Ett museum", rubrik="Utställningen",
   fakta=["Brevet och fynden visas på ett museum. Du väljer vad som ska visas och hur du berättar det.","Besökarna ser en berättelse. Det du lämnar utanför syns inte. Därför är ett urval alltid ett val."],
   ord=[("urval","att välja ut en del och lämna resten")],
   fraga="", alt=[], ratt=0, forklaring="",
   deko=[("folkmassa",-60,1.0),("kamera",130,0.8),("bokhylla",210,1.0)]),
 ],
 diskutera="Vad väljer ett museum att visa, och vad kan hamna utanför? Hur kan du som besökare ta reda på mer om det du ser?",
)
