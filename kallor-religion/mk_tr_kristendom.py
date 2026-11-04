# -*- coding: utf-8 -*-
"""Bygger simuleringar/tr-16-kristendomen.html med samma motor som övriga tidsresor (tr/motor.js)."""
import json, re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mall = open(f"{ROOT}/simuleringar/tr-04-rom.html", encoding="utf-8").read()

E = []
def etapp(x, tid, plats, rubrik, fakta, ord_, fraga, alt, forklaring, deko):
    # rätt svar står först i alt; blandas i motorn? Nej – motorn visar i given ordning, så vi lägger rätt svar på växlande plats.
    n = len(E)
    k = [0, 1, 2, 1, 0, 2, 1, 0, 2][n % 9] if fraga else None
    if fraga:
        a = alt[1:]; a.insert(k, alt[0]); alt = a
    E.append(dict(x_etikett=x, tid=tid, plats=plats, rubrik=rubrik, fakta=fakta, ord=ord_, fraga=fraga,
                  alt=alt, ratt=k, forklaring=forklaring, deko=deko))

etapp("30", "Omkring år 30", "Galileen och Jerusalem", "Jesus från Nasaret",
 ["Du står i Galileen, långt ut i Romarrikets utkant. Här lever Jesus, en judisk predikant. Han talar om Guds rike och om att man ska älska Gud och sin nästa. Han samlar lärjungar omkring sig.",
  "Romarna avrättar honom genom korsfästelse i Jerusalem, enligt de kristna skrifterna under ståthållaren Pontius Pilatus. Kristna tror att Jesus uppstod från de döda, och det firar de varje år vid påsk. Att Jesus avrättades nämns också av den romerske historikern Tacitus, men uppståndelsen berättas bara i de kristnas egna skrifter."],
 [["evangelium", "”goda budskapet”, de berättelser om Jesus som finns i Nya testamentet"], ["Kristus", "grekiska för ”den smorde”, ett ord för Messias"]],
 "Varför säger man ”kristna tror att Jesus uppstod” och inte bara ”Jesus uppstod”?",
 ["Uppståndelsen är en trosfråga som historiker inte kan bevisa, och den är grunden i den kristna tron", "Man vet inte alls om Jesus har funnits", "Det är bara katoliker som tror det"],
 "Historiker kan undersöka att Jesus levde och avrättades. Uppståndelsen är en trosföreställning, och när vi beskriver en religion skriver vi vad dess anhängare tror.",
 [["berg", -160, 1.0], ["palm", 40, 1.0], ["folkmassa", 170, 0.9]])

etapp("50", "Omkring år 50", "Antiochia och Rom", "Paulus och de första församlingarna",
 ["Efter Jesu död sprider hans anhängare budskapet. Paulus, en jude som först förföljde de kristna, reser runt i Romarriket och startar församlingar. I Antiochia kallas anhängarna kristna för första gången, enligt Apostlagärningarna.",
  "Paulus skriver brev till församlingarna. Breven ingår i Nya testamentet och hör till de äldsta kristna texterna. Kristna vägrar offra till kejsaren och blir ibland förföljda, till exempel efter branden i Rom år 64 under kejsar Nero."],
 [["församling", "grupp människor som samlas till gudstjänst och gemenskap"], ["mission", "att sprida sin tro till andra"]],
 "Hur spreds kristendomen först?",
 ["Genom resor, brev och nya församlingar längs Romarrikets vägar och handelsstråk", "Genom att kejsaren tvingade alla att bli kristna", "Genom tryckta böcker"],
 "Romarrikets vägar, gemensamma språk och handelsstäder gjorde det lätt att resa och sprida idéer. Kristendomen var länge en liten och ibland förbjuden rörelse.",
 [["hamn", -150, 1.0], ["marknad", 20, 1.0], ["segelfartyg", 190, 0.9]])

etapp("313", "År 313–380", "Romarriket", "Från förföljd till statsreligion",
 ["År 313 ger kejsar Konstantin och hans medkejsare Licinius de kristna frihet att utöva sin tro (Ediktet i Milano). År 325 kallar Konstantin biskopar till kyrkomötet i Nicaea. De enas om vad man ska tro om Jesus och Gud och skriver den nicenska trosbekännelsen.",
  "År 380 beslutar kejsar Theodosius att den nicenska tron ska gälla i riket, och kristendomen blir i praktiken statsreligion. Nu kan andra tolkningar förbjudas som kätteri."],
 [["trosbekännelse", "kort text som sammanfattar vad kristna tror"], ["statsreligion", "den religion som staten stöder och förespråkar"]],
 "Vad förändrades mellan år 313 och år 380?",
 ["Först fick kristna vara kristna utan förföljelse, sedan blev kristen tro rikets officiella tro", "Först förbjöds kristendomen, sedan tilläts den", "Ingenting förändrades"],
 "År 313 blev kristendomen tillåten, år 380 blev den statens religion. Då fick kyrkan makt, och det blev farligt att tro annorlunda.",
 [["kyrka", -150, 1.0], ["legionar", 20, 0.9], ["slott", 190, 0.9]])

etapp("1054", "År 1054", "Konstantinopel", "Kyrkan delas",
 ["Under hundratals år går kyrkan i öst och väst åt olika håll. I öster, med Konstantinopel som centrum, talas grekiska. I väster leder påven i Rom och man talar latin. De är oense om bland annat påvens makt och om en formulering i trosbekännelsen (filioque).",
  "År 1054 bannlyser sändebud från påven och patriarken i Konstantinopel varandra. Det brukar räknas som delningen i den ortodoxa och den katolska kyrkan, men splittringen skedde gradvis under lång tid."],
 [["ortodox", "kyrkorna som har sitt ursprung i öst, till exempel grekisk- och rysk-ortodoxa"], ["katolsk", "kyrkan som leds av påven i Rom"], ["huvudinriktning", "en stor gren av kristendomen"]],
 "Vilka två huvudinriktningar fanns i kristendomen efter 1054?",
 ["Den katolska kyrkan i väst och den ortodoxa kyrkan i öst", "Lutherska och reformerta kyrkor", "Pingstkyrkor och Svenska kyrkan"],
 "De lutherska och reformerta kyrkorna kom först efter reformationen på 1500-talet, och pingströrelsen på 1900-talet.",
 [["kyrka", -150, 1.0], ["mur", 40, 1.0], ["marknad", 190, 0.9]])

etapp("1164", "År 829–1164", "Birka och Uppsala", "Kristendomen når Norden",
 ["Kristendomen når Sverige långsamt. Missionären Ansgar kommer till Birka omkring år 830 men vinner få anhängare. Under vikingatiden och tidiga medeltiden bygger kungar och missionärer kyrkor, och runstenar får kors. Gammal asatro och ny tro lever en tid sida vid sida.",
  "År 1164 blir Uppsala ärkebiskopssäte. Sverige är nu en egen kyrkoprovins i den katolska kyrkan. Kyrkan blir viktig i vardagen: prästerna döper, viger och begraver, och kyrkan blir byns samlingsplats."],
 [["ärkebiskop", "den högsta biskopen i ett land eller en kyrkoprovins"], ["asatro", "den nordiska religionen från vikingatiden"]],
 "Vad betyder det att Uppsala blev ärkebiskopssäte år 1164?",
 ["Sverige fick en egen kyrkoprovins med en ärkebiskop som ledde kyrkan i landet", "Sverige blev lutherskt", "Alla svenskar blev kristna just det året"],
 "Kristnandet tog hundratals år och gick olika snabbt i olika delar av landet. Ärkebiskopssätet visar att kyrkan nu var väl organiserad.",
 [["gran", -150, 1.0], ["gravsten", -10, 0.9], ["kyrka", 130, 1.0], ["torp", 250, 0.9]])

etapp("1517", "År 1517", "Wittenberg", "Reformationen",
 ["Kyrkan i väst är mäktig men får kritik. En fråga gäller avlaten, tanken att man kan köpa efterskänkt straff för sina synder. Den tyske munken Martin Luther skriver år 1517 teser (påståenden) om detta. Enligt traditionen spikar han upp dem på kyrkporten i Wittenberg.",
  "Luther lär att människan blir rättfärdig genom tron och att Bibeln är högsta auktoritet. Med tryckpressen sprids hans skrifter snabbt, och Bibeln översätts till folkspråk. Det blir en ny huvudinriktning, protestantismen, och kyrkan i väst splittras."],
 [["reformation", "förändring av kyrkan på 1500-talet"], ["protestant", "kristen som följer reformationens tankar"], ["avlat", "att man kunde köpa efterskänkt straff för synder"]],
 "Vad var nytt med protestantismen?",
 ["Den betonade tron och Bibeln, och människor kunde läsa Bibeln på sitt eget språk", "Den ville avskaffa Bibeln", "Den lydde påven mer än förut"],
 "Protestanterna ansåg att Bibeln, inte påven, var högsta auktoritet. Tryckpressen och översättningarna hjälpte tanken att spridas.",
 [["tryckpress", -150, 1.0], ["bokhylla", 10, 1.0], ["kyrka", 170, 1.0]])

etapp("1527", "År 1527–1726", "Västerås och Uppsala", "Sverige blir lutherskt – en enhetskyrka",
 ["Kung Gustav Vasa vill stärka sin makt. På riksdagen i Västerås 1527 beslutas att kungen får ta över mycket av kyrkans gods, och Sverige lämnar den katolska kyrkan. År 1593 fastställs vid kyrkomötet i Uppsala att läran ska vara luthersk.",
  "Nu finns en enhetskyrka: alla förväntas tillhöra statskyrkan och gå i kyrkan, och prästen håller husförhör för att höra att alla kan sin kristendomskunskap. År 1726 förbjuder konventikelplakatet religiösa sammankomster utanför kyrkan."],
 [["statskyrka", "kyrka som staten stöder och styr"], ["enhetskyrka", "tanken att alla i landet ska tillhöra samma kyrka"], ["konventikel", "bönemöte utanför kyrkans gudstjänster"]],
 "Vad menas med att Sverige hade en enhetskyrka?",
 ["Nästan alla i landet förväntades tillhöra samma kyrka och ha samma lära", "Alla kyrkor i världen hade slagits ihop", "Kyrkan och staten var helt åtskilda"],
 "Enhetskyrkan innebar att tro och medborgarskap hörde ihop. Den som tänkte annorlunda kunde få problem.",
 [["slott", -150, 1.0], ["kyrka", 10, 1.0], ["torp", 170, 0.9]])

etapp("1860", "År 1858–1951", "Sverige", "Väckelse och frihet att välja",
 ["På 1800-talet växer väckelserörelser fram: människor samlas för bön och bibelläsning, ofta utanför kyrkan. Konventikelplakatet avskaffas 1858, och från rörelsen kommer frikyrkor som baptister och Svenska Missionsförbundet.",
  "Dissenterlagen 1860 ger rätt att lämna Svenska kyrkan om man går med i ett annat godkänt samfund. År 1951 ersätts dissenterlagarna av religionsfrihetslagen, och man får rätt att stå utanför alla trossamfund."],
 [["väckelse", "rörelse där människor vill förnya sin tro"], ["frikyrka", "kyrka som är fri från staten"], ["religionsfrihet", "rätten att tro, byta tro eller inte tro"]],
 "Vilken utveckling beskriver tiden 1858–1951 bäst?",
 ["Människor fick steg för steg större frihet att välja tro, till sist även att stå utanför alla samfund", "Staten förbjöd alla frikyrkor", "Alla svenskar tvingades gå med i Svenska kyrkan"],
 "Religionsfriheten kom i flera steg. Det är en viktig del av vägen från enhetskyrka till religiös mångfald.",
 [["trad", -160, 1.0], ["folkmassa", 0, 0.9], ["kyrka", 160, 0.9]])

etapp("2000", "År 2000", "Sverige", "Kyrkan skiljs från staten",
 ["Den 1 januari 2000 slutar Svenska kyrkan vara statskyrka. Den blir ett trossamfund bland andra, men är fortfarande Sveriges största. Andelen medlemmar har minskat: vid utgången av 2025 hade Svenska kyrkan 5 365 542 medlemmar, 50,7 procent av befolkningen.",
  "Samtidigt har andra religioner och livsåskådningar, som islam, ortodox kristendom och humanism, blivit mer synliga. Det kallas religiös mångfald. När religion får mindre betydelse i samhället och i människors liv kallas det sekularisering."],
 [["sekularisering", "att religion får mindre betydelse i samhället och i människors liv"], ["religiös mångfald", "att människor i ett samhälle har många olika religioner och livsåskådningar"], ["humanism", "livsåskådning som utgår från människans värde utan en gud"]],
 "Vad betyder sekularisering?",
 ["Att religionen får mindre betydelse i samhället och i människors liv", "Att alla blir religiösa", "Att staten styr kyrkan"],
 "Sekularisering handlar om att religionens roll minskar, inte om att alla slutar tro. Många är fortfarande religiösa, och i Sverige finns både tro, tvivel och icke-tro.",
 [["riksdagshus", -150, 1.0], ["kyrka", 10, 1.0], ["folkmassa", 170, 0.9]])

etapp("Idag", "Idag", "Världen", "Kristendomen i dag",
 ["Kristendomen är världens största religion, med ungefär 2,3 miljarder anhängare år 2020, omkring 29 procent av jordens befolkning (Pew Research Center). Den största huvudinriktningen är den katolska, följd av protestantiska och ortodoxa kyrkor.",
  "Kristendomen växer mest i Afrika söder om Sahara, där 62 procent identifierade sig som kristna. I delar av Europa, bland annat Sverige, minskar andelen som är med i en kyrka. Kristendomen är därför både en gammal och en föränderlig religion."],
 [["huvudinriktning", "en stor gren av kristendomen: katolsk, ortodox, protestantisk"]],
 None, None, None,
 [["jordglob", -150, 1.1], ["kyrka", 20, 1.0], ["dator", 170, 0.9]])

SCEN = dict(titel="Tidsresa genom kristendomens historia", plats="Från Galileen till i dag", tid="Omkring år 30 – i dag",
            sky=["#d8e6f2", "#f2e3c6"], mark="#9a8a6a", walker=dict(typ="resenar"), etapper=E,
            diskutera="Kristendomen har påverkat svenskt samhälle, till exempel helgdagar, värderingar, byggnader och namn. Hur har den rollen förändrats från enhetskyrka till religiös mångfald? Hur kan människor med olika tro och livsåskådning leva tillsammans? Vilka mörka sidor, till exempel förföljelser av andra tolkningar och religioner, får vi inte glömma?",
            id="religion-kristendom")

h = mall.replace("Tidsresa genom Rom", SCEN["titel"]).replace("Rom och Medelhavet", SCEN["plats"]).replace("753 f.Kr. – 476 e.Kr.", SCEN["tid"])
h = re.sub(r"window\.SCEN=\{.*?\};</script>", lambda m: "window.SCEN=" + json.dumps(SCEN, ensure_ascii=False) + ";</script>", h, count=1, flags=re.S)
open(f"{ROOT}/simuleringar/tr-16-kristendomen.html", "w", encoding="utf-8").write(h)
# kontroller
assert len(E) == 10 and all(len(e["alt"]) == 3 and e["alt"][e["ratt"]] for e in E[:-1])
print("ok", len(h))
