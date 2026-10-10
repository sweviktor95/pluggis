# -*- coding: utf-8 -*-
# Kapitel 11 – Andra världskriget (Pluggis historia åk 9)
# Fakta hålls konsekventa med simuleringarna andra-varldskriget.html och dagen-d.html.
T = dict(
 nr=11, namn="Andra världskriget", under="Orsaker, krigsår, motstånd, följder och Sveriges roll",
 fil="historia-11-andra-varldskriget", arskurs=9, nodeid="historia-andra-varldskriget",
 mal=["förklara orsakerna till andra världskrigets utbrott, bland annat Versaillesfreden, depressionen och eftergiftspolitiken",
      "beskriva krigets förlopp och vändpunkter från Polen 1939 till kapitulationerna 1945",
      "diskutera de etiska frågorna kring atombomberna mot Hiroshima och Nagasaki",
      "beskriva hemmafronten och motståndet i flera länder",
      "förklara krigets konsekvenser: miljontals döda, FN, Nürnbergrättegångarna och Europas delning",
      "granska Sveriges roll under kriget ur flera perspektiv",
      "analysera hur kriget minns och används i olika länder idag"],
 fundera="Sverige var inte med i kriget, men kriget påverkade ändå vardagen här. Vad tror du att svenskar kunde märka av? Skriv tre saker innan du läser.",
)

S = []

S.append(dict(id="orsaker", nr="11.1", ikon="🧭", titel="Varför började kriget? Orsakerna",
 intro="Andra världskriget hade inte en enda orsak. Flera saker byggde upp till en katastrof.",
 block=[
  ("p","Efter att första världskriget slutat 1918 slöts <strong>Versaillesfreden</strong> 1919. Tyskland fick skulden för kriget, förlorade land, fick begränsa sin armé och skulle betala stora skadestånd. Många tyskar kände sig förödmjukade. Det blev en grogrund för hat och revanschlust."),
  ("p","Sedan kom <strong>depressionen</strong> efter börskraschen 1929. Miljoner blev arbetslösa och många förlorade tron på demokratin. I flera länder tog diktatorer makten, i Italien Mussolini, i Tyskland Hitler och i Japan styrde en militär ledning allt mer (se kapitel 10)."),
  ("p","Hitler bröt mot fredsfördraget. 1935 införde han värnplikt, 1936 skickade han trupper in i Rhenlandet och i mars 1938 införlivade han Österrike. Han krävde sedan området <strong>Sudetenland</strong> av Tjeckoslovakien, där många tyskspråkiga bodde."),
  ("p","Storbritannien och Frankrike ville undvika ännu ett krig och valde <strong>eftergiftspolitik</strong>: de gav efter i hopp om fred. I <strong>Münchenavtalet</strong>, som skrevs under natten till 30 september 1938, fick Hitler Sudetenland. Tjeckoslovakien blev inte ens inbjudet till mötet. I mars 1939 ockuperade Tyskland ändå de tjeckiska delarna av landet."),
  ("ruta","tank","Orsak och följd","Fråga dig: Var eftergiftspolitiken en orsak till kriget eller ett försök att förhindra det? Historiker är inte överens. Vissa menar att Hitler borde ha stoppats tidigare, andra att länderna behövde tid och inte var redo."),
  ("kolla",["Nämn två saker som låg till grund för kriget.","Vad är eftergiftspolitik?","Vad innebar Münchenavtalet?"]),
 ],
 svar=["T.ex. Versaillesfreden, depressionen, diktatorers aggression.","Att ge efter för krav i hopp om att undvika krig.","Hitler fick Sudetenland av Tjeckoslovakien, utan att landet själv fick vara med och bestämma."],
))

S.append(dict(id="tidigt", nr="11.2", ikon="💥", titel="1939–1940: Polen, blixtkriget och Frankrike",
 intro="Kriget började med ett anfall mot Polen. På ett år hade Tyskland erövrat stora delar av västra Europa.",
 block=[
  ("p","Den 23 augusti 1939 skrev Tyskland och Sovjetunionen under en pakt om att inte anfalla varandra. I hemlighet delade de upp Östeuropa mellan sig. Den <strong>1 september 1939</strong> anföll Tyskland Polen, och två dagar senare förklarade Storbritannien och Frankrike krig mot Tyskland. Den 17 september anföll även Sovjetunionen Polen från öster."),
  ("p","Tyskland använde <strong>blixtkrig</strong>: snabba anfall med stridsvagnar och flygplan som bröt igenom fiendens försvar. Det var raka motsatsen till skyttegravskriget under första världskriget. Warszawa kapitulerade den 28 september."),
  ("tidslinje",[("1 sep 1939","Tyskland anfaller Polen"),("30 nov 1939","Sovjetunionen anfaller Finland (vinterkriget)"),("9 apr 1940","Tyskland anfaller Danmark och Norge"),("10 maj 1940","Anfall mot Nederländerna, Belgien, Frankrike"),("22 juni 1940","Frankrike skriver under vapenstillestånd")]),
  ("p","Den 9 april 1940 ockuperades Danmark på några timmar. Norge gjorde motstånd i två månader. Därefter anföll Tyskland i väst. Vid <strong>Dunkerque</strong> blev de allierade instängda mot havet, men omkring 338 000 soldater evakuerades till England. Paris föll den 14 juni, och Frankrike kapitulerade."),
  ("ruta","fakta","De allierade och axelmakterna","De som stred mot Tyskland kallas <strong>de allierade</strong>: främst Storbritannien, Frankrike, senare Sovjetunionen och USA. Tyskland, Italien och Japan kallas <strong>axelmakterna</strong>."),
  ("bild","ww2","Andra världskriget drabbade nästan hela världen."),
  ("kolla",["Vilket datum började kriget i Europa?","Vad är blixtkrig?","Vad hände vid Dunkerque?"]),
 ],
 svar=["1 september 1939.","Snabba anfall med stridsvagnar och flyg som bröt igenom fiendens försvar.","Omkring 338 000 allierade soldater evakuerades till England."],
))

S.append(dict(id="varld", nr="11.3", ikon="🌍", titel="1940–1941: kriget blir ett världskrig",
 intro="Storbritannien stod ensamt kvar mot Tyskland. Så attackerade Tyskland Sovjetunionen, och Japan anföll USA.",
 block=[
  ("p","Efter Frankrikes fall ville Hitler invadera Storbritannien. Först måste Tyskland ta kontrollen över luften. Sommaren och hösten 1940 utkämpades <strong>slaget om Storbritannien</strong> mellan tyska Luftwaffe och brittiska RAF. Britterna hade radar som varnade i tid, och Tyskland misslyckades. Invasionen sköts upp. I stället bombades London och andra städer, det som kallas the Blitz. Storbritanniens premiärminister var sedan maj 1940 Winston Churchill."),
  ("p","Den <strong>22 juni 1941</strong> bröt Hitler pakten och anföll Sovjetunionen i <strong>Operation Barbarossa</strong>. Omkring tre miljoner tyska soldater deltog. Tyskarna nådde nästan fram till Moskva men stoppades i december av vinter och sovjetiska motanfall. Staden Leningrad belägrades i nästan 900 dagar. Finland deltog i anfallet i det som kallas fortsättningskriget."),
  ("p","Den <strong>7 december 1941</strong> anföll Japan den amerikanska flottbasen Pearl Harbor på Hawaii. Omkring 2 400 amerikaner dödades. USA gick då med i kriget, och några dagar senare förklarade Tyskland och Italien krig mot USA. Nu var kriget ett riktigt världskrig."),
  ("ruta","fakta","Varför anföll Japan?","Japan hade erövrat områden i Kina och ville ha råvaror som olja i Sydostasien. USA hade infört handelsrestriktioner. Japans ledare ville slå ut USA:s flotta innan den hann ingripa."),
  ("p","Japan erövrade under vintern 1941–1942 stora delar av Sydostasien och Stilla havet. Många civila drabbades hårt av den japanska ockupationen."),
  ("kolla",["Varför misslyckades Tyskland i slaget om Storbritannien?","Vad hette Tysklands anfall mot Sovjetunionen?","Varför blev kriget ett världskrig 1941?"]),
 ],
 svar=["Britterna hade radar och RAF höll stand, så Tyskland fick inte kontroll över luften.","Operation Barbarossa.","Japan anföll USA, som gick med i kriget, och Tyskland och Italien förklarade krig mot USA."],
))

S.append(dict(id="vandpunkt", nr="11.4", ikon="🔄", titel="Vändpunkterna 1942–1944",
 intro="År 1942–1943 förändrades kriget. De allierade tog initiativet, och 1944 öppnades en ny front i väst.",
 block=[
  ("p","I juni 1942 möttes japanska och amerikanska flottor vid ön <strong>Midway</strong> i Stilla havet. Amerikanerna hade knäckt Japans hemliga koder och visste vad som skulle hända. De sänkte fyra japanska hangarfartyg. Efter Midway var Japan på reträtt."),
  ("p","Samtidigt utkämpades <strong>slaget om Stalingrad</strong> vid floden Volga. Från augusti 1942 stred tyska och sovjetiska soldater om varje hus. Röda armén omringade den tyska sjätte armén, som kapitulerade den 2 februari 1943. Omkring två miljoner soldater och civila dödades eller skadades. Efter Stalingrad pressade Röda armén tyskarna västerut."),
  ("p","Den <strong>6 juni 1944</strong> landsteg omkring 156 000 allierade soldater i Normandie i Frankrike från havet och luften. Det kallas <strong>Dagen D</strong>, och operationen hette Overlord. Tyskarna väntade sig anfallet vid Calais och lurades av en påhittad armé. Priset var högt: omkring 10 000 allierade var döda, sårade eller saknades efter dagen. Nu måste Tyskland strida på två fronter. Paris befriades i augusti 1944."),
  ("tab",["Händelse","Plats","Datum","Varför viktig?"],[["Midway","Stilla havet","4 juni 1942","Japan förlorade fyra hangarfartyg"],["Stalingrad","Sovjetunionen","aug 1942–2 feb 1943","Tyskland på reträtt i öst"],["Dagen D","Normandie","6 juni 1944","Ny front i väst"]]),
  ("ruta","tank","Vad är en vändpunkt?","En händelse efter vilken utvecklingen går åt ett annat håll. Är det alltid tydligt när en vändpunkt sker? Historiker brukar säga att den ofta syns först i efterhand."),
  ("kolla",["Varför var Midway viktigt?","Varför räknas Stalingrad som en vändpunkt?","Vad var Dagen D?"]),
 ],
 svar=["Japan förlorade fyra hangarfartyg och gick sedan på reträtt.","Efter slaget var Tyskland på reträtt i öst.","Den allierade landstigningen i Normandie 6 juni 1944."],
))

S.append(dict(id="slut", nr="11.5", ikon="🕊️", titel="Krigets slut: Europa och Japan",
 intro="Kriget i Europa tog slut den 8 maj 1945. I Asien fortsatte det till sommaren. Slutet innehåller svåra etiska frågor.",
 block=[
  ("p","Våren 1945 rycker sovjetiska trupper in i Tyskland från öster och amerikanska och brittiska från väster. Hitler tar sitt liv den 30 april. Tyskland kapitulerar villkorslöst, och <strong>8 maj 1945</strong> firas som krigsslutet i Europa. Landet delas i fyra ockupationszoner."),
  ("p","I Stilla havet kämpade USA och dess allierade sig framåt ö för ö. Strider och bombningar kostade många liv. Den <strong>6 augusti 1945</strong> fällde USA en atombomb över <strong>Hiroshima</strong> och den <strong>9 augusti</strong> över <strong>Nagasaki</strong>. Omkring 200 000 människor dog före årets slut i de två städerna tillsammans, många av brännskador och strålning. Den 8 augusti förklarade Sovjetunionen krig mot Japan. Japan kapitulerade, och kapitulationen skrevs under den <strong>2 september 1945</strong>."),
  ("ruta","tank","Etiska frågor","Var det rätt att använda atombomberna? Vissa menar att bomberna förkortade kriget och räddade liv, eftersom en invasion av Japan hade kostat mycket. Andra menar att bomberna dödade civila och att Japan var på väg att ge upp. Historiker diskuterar fortfarande. Det finns inget enkelt svar."),
  ("p","För överlevande från bomberna, <em>hibakusha</em>, handlar frågan om livet efter. Många led av sjukdomar, och några mötte fördomar. Hiroshima och Nagasaki är idag symboler för kampen mot kärnvapen."),
  ("ruta","fakta","Datum att komma ihåg","8 maj 1945: kriget i Europa slutar. 6 och 9 augusti 1945: Hiroshima och Nagasaki. 2 september 1945: hela världskriget är slut."),
  ("kolla",["Vilket datum slutade kriget i Europa?","Vilka två städer drabbades av atombomber?","Ge ett argument för och ett emot att använda bomberna."]),
 ],
 svar=["8 maj 1945.","Hiroshima och Nagasaki.","För: kunde förkorta kriget. Emot: dödade många civila, Japan kanske redan var på väg att ge upp."],
))

S.append(dict(id="hemma", nr="11.6", ikon="🏠", titel="Hemmafronten och motståndet",
 intro="Kriget var inte bara soldater på slagfält. Vanliga människor drabbades, och många gjorde motstånd mot ockupationen.",
 block=[
  ("p","<strong>Hemmafronten</strong> är ett ord för det som hände hemma medan soldaterna stred. Fabriker tillverkade vapen, och när männen var ute i krig arbetade många kvinnor i industrin. Maten ransonerades, och i flera länder bombades städerna. Barn skickades ibland bort från storstäderna för att vara trygga."),
  ("p","Alla fick inte samma behandling. I USA placerades omkring 120 000 amerikaner av japansk härkomst i läger 1942, trots att de flesta var medborgare. I ockuperade länder tvingades många till arbete för ockupanten och levde på knappa ransoner."),
  ("p","<strong>Motståndsrörelser</strong> ägnade sig åt sabotage, spionage, hjälp till förföljda och tidningar som spred sanna nyheter. I Norge sprängdes bland annat anläggningar och man hjälpte människor över gränsen till Sverige. I Danmark ökade motståndet 1943, och i oktober 1943 hjälpte danskar mer än 7 000 judar över sundet till Sverige. I Frankrike verkade <em>résistance</em>, och i Jugoslavien och Sovjetunionen utförde partisaner gerillakrig."),
  ("ruta","historia","Olika sorters motstånd","Motstånd kunde vara att spränga en bro, men också att dölja en granne, sprida en tidning eller bara vägra samarbeta. Många riskerade sina liv. Några samarbetade med ockupanterna, och efter kriget diskuterades hur de skulle behandlas."),
  ("p","Även i Tyskland fanns motstånd. Studenter i gruppen Vita rosen delade ut flygblad, och i juli 1944 försökte en grupp officerare döda Hitler. Det misslyckades, och många av dem avrättades."),
  ("kolla",["Vad är hemmafronten?","Nämn två sätt att göra motstånd.","Vad hände med de danska judarna i oktober 1943?"]),
 ],
 svar=["Det som hände hemma i krigförande länder: produktion, ransonering, bombningar.","T.ex. sabotage, hjälpa förföljda, sprida tidningar, gömma människor.","Mer än 7 000 hjälptes över sundet till Sverige, ett litet antal greps."],
))

S.append(dict(id="folg", nr="11.7", ikon="🏛️", titel="Följderna: miljoner döda, FN och ett delat Europa",
 intro="Krigets följder präglade hela efterkrigstiden. Miljontals dog, och världen byggde nya organisationer för att förhindra nya krig.",
 block=[
  ("p","Uppskattningsvis <strong>70–85 miljoner</strong> människor dog i andra världskriget, de flesta civila. Det är den dödligaste konflikten i historien. Hela städer låg i ruiner, och miljontals människor var på flykt. En del av dödsfallen berodde på Förintelsen, där omkring sex miljoner judar mördades (se kapitel 12)."),
  ("p","I oktober 1945 bildades <strong>FN</strong>, Förenta nationerna, för att bevara freden. 1948 antog FN en konvention mot folkmord och en förklaring om mänskliga rättigheter."),
  ("p","Krigsförbrytare ställdes inför rätta. Vid <strong>Nürnbergrättegångarna</strong>, som inleddes i november 1945, åtalades 24 ledande nazister för brott mot freden, krigsbrott och brott mot mänskligheten. Rättegångarna var en nyhet i historien: ledare kunde nu hållas ansvariga. Liknande rättegångar hölls i Tokyo för japanska ledare."),
  ("p","Europa delades. Sovjetunionen och västmakterna kom i konflikt, och en <strong>järnridå</strong> delade Europa i ett östligt och ett västligt block. Tyskland delades 1949 i två stater. Det blev starten på <strong>kalla kriget</strong>."),
  ("ruta","tank","Kontinuitet och förändring","Vad förändrades efter 1945, och vad hade funnits länge? Nya organisationer som FN är en förändring. Konflikten mellan stormakter är mer av en kontinuitet. Försök hitta fler exempel."),
  ("tab",["Följd","Förklaring"],[["Miljoner döda","70–85 miljoner, de flesta civila"],["FN","Bildades oktober 1945"],["Rättegångar","Nürnberg från november 1945"],["Delat Europa","Järnridån och kalla kriget"]]),
  ("kolla",["Hur många dog ungefär i kriget?","Vad var syftet med FN?","Vad var Nürnbergrättegångarna?"]),
 ],
 svar=["Omkring 70–85 miljoner.","Att bevara freden och förhindra nya världskrig.","Rättegångar mot ledande nazister för bland annat brott mot mänskligheten."],
))

S.append(dict(id="sverige", nr="11.8", ikon="🇸🇪", titel="Sverige under kriget: neutralitet med skuggsidor",
 intro="Sverige stod utanför kriget, men inte utanför dess följder. Det som Sverige gjorde bedöms på olika sätt.",
 block=[
  ("p","Sverige förklarade sig <strong>neutralt</strong>, alltså att inte ta ställning i kriget. Under vinterkriget 1939–1940 hjälpte Sverige Finland med vapen och omkring 8 000 frivilliga. Efter att Tyskland ockuperat Danmark och Norge 1940 var Sverige omringat av tyskt eller ockuperat territorium."),
  ("p","Sverige gav efter för tyska krav. Mellan 1940 och 1943 fick tyska soldater åka med tåg genom Sverige mellan Norge och Tyskland, den så kallade <strong>permittenttrafiken</strong>. Sommaren 1941 tilläts en tysk division resa från Norge till Finland. Sverige sålde också mycket järnmalm till Tyskland. Efter Stalingrad 1943 blev Sverige mer självständigt och sade upp permittenttrafiken. Samtidigt exporterade Sverige kullager och annat till de allierade."),
  ("p","Sverige tog emot många flyktingar. Omkring 50 000 norrmän flydde över gränsen, och i oktober 1943 tog Sverige emot nästan alla danska judar. Omkring 70 000 finska barn evakuerades under kriget, främst till Sverige, där de bodde hos svenska familjer. Omkring 7 000 av dem blev kvar. Våren 1945 räddade <strong>vita bussarna</strong>, en svensk Röda Korset-aktion under Folke Bernadotte, omkring 15 000 fångar ur tyska läger. Siffrorna varierar mellan källor."),
  ("ruta","tank","Flera perspektiv","Försvarare: Sverige var ett litet land i skuggan av Tyskland, och eftergifterna höll landet utanför kriget. Kritiker: Sverige hjälpte i praktiken Tysklands krigföring och agerade först när tyskarna var på reträtt. Båda har argument. Hur skulle du väga dem?"),
  ("ruta","fakta","Efter kriget","Kring årsskiftet 1945–1946 lämnade Sverige ut omkring 2 400 tyska och 146 baltiska soldater till Sovjetunionen. Det blev mycket omdiskuterat, och några av balterna försökte ta sina liv eller skadade sig för att slippa. Frågan om Sveriges ansvar har debatterats i decennier."),
  ("kolla",["Vad innebär neutralitet?","Vad var permittenttrafiken?","Ge ett argument för och ett emot Sveriges agerande."]),
 ],
 svar=["Att inte ta ställning i ett krig.","Tyska soldater på permission fick åka tåg genom Sverige mellan Norge och Tyskland, 1940–1943.","För: höll landet utanför kriget. Emot: gynnade Tysklands krigföring."],
))

F = []
F.append(dict(id="f1", nr="F1", ikon="⚛️", titel="Atombomberna – flera perspektiv",
 intro="Beslutet att använda atombomber är ett av historiens mest omdiskuterade. Här ser du hur olika röster kan tolkas.",
 block=[
  ("p","Argumenten för bomberna: USA ville avsluta kriget snabbt och undvika en invasion av Japan som kunde kosta många liv. Argumenten emot: många dödades som inte var soldater, och vissa forskare menar att Japan redan var nära kapitulation, särskilt efter att Sovjetunionen förklarade krig den 8 augusti."),
  ("kalla","Konstruerad källa – dagbok, japansk skolflicka, augusti 1945","Det var en vanlig morgon. Sedan blev himlen vit. Jag vet inte hur många som försvann. Min mamma letade efter oss i flera dagar.","Konstruerad källa baserad på vittnesmål från överlevande. Personen är påhittad."),
  ("p","Dagböcker och vittnesberättelser visar den mänskliga sidan, men de visar bara en del av bilden. Beslutsfattare skrev i protokoll och memoarer om sina avvägningar. Historiker läser båda slagen av källor och jämför."),
  ("ruta","tank","Nutidens perspektiv","Efter 1945 har kärnvapen aldrig använts i krig. Är det en följd av att världen sett vad de kan göra? Många menar det, men det är svårt att bevisa."),
  ("kolla",["Nämn ett argument för och ett emot bomberna.","Varför är vittnesberättelser värdefulla men inte tillräckliga?","Vilken typ av källa är en beslutsfattares memoarer?"]),
 ],
 svar=["För: förkorta kriget. Emot: civila offer, Japan nära kapitulation.","De visar människors upplevelser men representerar bara en del av händelsen.","En berättande källa skriven i efterhand, som kan färgas av att författaren vill rättfärdiga sig."],
))
F.append(dict(id="f2", nr="F2", ikon="📜", titel="Hur minns vi kriget? Historiebruk",
 intro="Olika länder minns kriget på olika sätt, och det påverkar politiken än idag.",
 block=[
  ("p","I Ryssland kallas kriget mot Tyskland <em>det stora fosterländska kriget</em>, och segerdagen firas den 9 maj. Där betonas Sovjetunionens enorma förluster och rollen i segern. Kritiker menar att det också används för att stärka dagens makthavare."),
  ("p","I Tyskland har man arbetat med att möta skulden och minnas offren. I Japan finns diskussion om hur kriget framställs i skolböcker och minnesplatser. I Frankrike firas 8 maj, och motståndsrörelsen har fått en särskild plats i det nationella minnet. Historiker påpekar att också samarbetet med ockupanterna länge var tabu."),
  ("p","I Sverige har bilden skiftat. Under efterkrigstiden betonades ofta att neutraliteten räddade landet. Senare har kritiska röster lyft eftergifterna mot Tyskland och flyktingpolitiken. Det visar att historien skrivs om när nya frågor ställs."),
  ("ruta","exempel","Frågor att ställa","Vem berättar historien? Vad lyfts fram, och vad hoppas man över? Varför berättas den just nu? Vem tjänar på berättelsen?"),
  ("kolla",["Hur minns Ryssland kriget?","Varför ändras bilden av kriget över tid?","Nämn en fråga du kan ställa för att granska historiebruk."]),
 ],
 svar=["Som det stora fosterländska kriget, med firande den 9 maj.","Nya frågor, nya källor och nya generationer ger nya perspektiv.","T.ex. Vem berättar? Varför nu? Vad utelämnas?"],
))
F.append(dict(id="f3", nr="F3", ikon="🇩🇰", titel="Danmark och Norge – olika vägar under ockupationen",
 intro="Danmark och Norge ockuperades samma dag, men ockupationen blev olika. Det visar att länder hade olika val.",
 block=[
  ("p","Danmark kapitulerade på några timmar och fick behålla sin regering en tid. Det kallas samarbetspolitik. Så länge landet var lugnt fick den danska regeringen styra. Först i augusti 1943 avgick regeringen, efter ökat motstånd och strejker."),
  ("p","I Norge gjorde kungen och regeringen motstånd och flydde till Storbritannien. Landet styrdes av tyskarna och en norsk samarbetsregering ledd av Vidkun Quisling. Quisling blev ett ord för förrädare."),
  ("tab",["","Danmark","Norge"],[["Ockupation","9 april 1940","9 april 1940"],["Motstånd mot invasionen","Några timmar","Cirka två månader"],["Regering","Samarbetspolitik till 1943","Exilregering i London"],["Judar","Räddades i oktober 1943","Omkring 770 deporterades 1942, många flydde till Sverige"]]),
  ("p","Historiker diskuterar fortfarande om den danska samarbetspolitiken var klok eller feg. Den räddade liv och skonade landet, men innebar också kompromisser med ockupanterna."),
  ("kolla",["Vad var skillnaden i ockupationen mellan Danmark och Norge?","Vem var Quisling?","Varför är samarbetspolitiken omdiskuterad?"]),
 ],
 svar=["Danmark fick behålla regering en tid, Norge fick exilregering och motstånd i två månader.","Norsk ledare som samarbetade med tyskarna.","Den skonade landet men innebar kompromisser med ockupanterna."],
))
F.append(dict(id="f4", nr="F4", ikon="🤔", titel="Var eftergiftspolitiken ett misstag?",
 intro="Eftergiftspolitiken är ett klassiskt ämne för historiker. Hur ska man bedöma beslut när man vet hur det gick?",
 block=[
  ("p","Minnet av första världskriget var starkt. Britter och fransmän ville inte se miljontals nya döda. Många trodde att Hitler bara ville rätta till orättvisor från Versailles. Dessutom behövde Storbritannien tid att bygga ut sitt flygvapen."),
  ("p","Kritiker svarar att Hitler borde ha stoppats tidigare, när Tyskland var svagare. Genom Münchenavtalet förlorade Tjeckoslovakien sina försvarsverk, och Hitler fick ett intryck av att Västmakterna inte skulle ingripa."),
  ("ruta","tank","Historiker och efterklokhet","Vi vet hur det gick, men de som beslutade visste det inte. Ett viktigt mål för en historiker är att förstå varför människor handlade som de gjorde, utan att glömma att resultatet blev katastrofalt."),
  ("p","Ordet <em>appeasement</em> (eftergiftspolitik) används idag ofta i debatter som en slags förolämpning: ”Du vill göra som i München”. Det är historiebruk. Fråga dig alltid om jämförelsen verkligen passar."),
  ("kolla",["Nämn två skäl till att Storbritannien och Frankrike valde eftergifter.","Varför har eftergiftspolitiken kritiserats?","Vad är problemet med att jämföra dagens händelser med München?"]),
 ],
 svar=["Rädsla för nytt krig och behov av tid att rusta upp.","Hitler stärktes och Tjeckoslovakien förlorade sitt försvar.","Situationerna är olika, och jämförelsen kan förenkla och skapa ett färdigt facit."],
))

F_UPPG = [
 ("●","Förklara med egna ord vad som skiljer axelmakterna från de allierade.",[],None,"Axelmakterna: Tyskland, Italien, Japan. De allierade: bl.a. Storbritannien, Frankrike, Sovjetunionen, USA."),
 ("●●","Förklara varför Stalingrad och Midway brukar kallas vändpunkter. Jämför dem.",[],None,"Båda var förluster som tvingade fienden på reträtt: Tyskland i öst, Japan i Stilla havet. Midway var en sjöstrid, Stalingrad en landstrid i en stad. Båda visade att axelmakterna kunde besegras."),
 ("●●","Jämför Danmark och Norge under ockupationen. Vad förklarar skillnaderna?",[],None,"Danmark kapitulerade snabbt, samarbetspolitik till 1943. Norge gjorde motstånd, exilregering och Quisling. Förklaringar: geografi, politiska beslut, tyska intressen."),
 ("●●●","Diskutera: Hade Sverige kunnat agera annorlunda under kriget? Använd minst två perspektiv och källor.",[],None,"Bedöms enligt SKRIV-stödet: perspektiv (försvarare och kritiker), konsekvenser, avvägningar och källor."),
]
F_SAMMAN = [
 "Atombombsbeslutet tolkas olika: förkorta kriget respektive döda många civila.",
 "Olika länder minns kriget på olika sätt, och minnet används politiskt.",
 "Danmark och Norge hade olika ockupationer: samarbetspolitik respektive exilregering och Quisling.",
 "Eftergiftspolitiken kan ses som ett misstag eller som ett försök att undvika krig.",
 "Historiker försöker förstå människors val utan att bara döma i efterhand.",
]
F_BEGR = [
 ("Hibakusha","Japanska ord för överlevande från atombomberna."),
 ("Samarbetspolitik","Politik där ett ockuperat land samarbetar med ockupanten."),
 ("Appeasement","Eftergiftspolitik."),
 ("Historiebruk","Hur historia används i olika syften."),
 ("Exilregering","Regering som flytt och verkar utanför landet."),
]

UPPG = [
 ("Para ihop","Koppla ihop datum och händelse.",["1 sep 1939","22 jun 1941","7 dec 1941","6 jun 1944","8 maj 1945"],["Pearl Harbor","Dagen D","Kriget i Europa slutar","Tyskland anfaller Polen","Operation Barbarossa"],"1 – D, 2 – E, 3 – A, 4 – B, 5 – C"),
 ("Orsaker","Förklara tre orsaker till att andra världskriget började.",[],None,"T.ex. Versaillesfreden, depressionen, Hitlers aggression, eftergiftspolitiken, Münchenavtalet, pakten med Sovjet."),
 ("Kronologi","Sätt i tidsordning: Dagen D, Stalingrad, Pearl Harbor, Frankrike faller, Hiroshima.",[],None,"Frankrike faller (1940); Pearl Harbor (1941); Stalingrad (1942–43); Dagen D (1944); Hiroshima (1945)."),
 ("Förklara begrepp","Förklara blixtkrig, hemmafront, neutralitet och motståndsrörelse.",[],None,"Se begreppslistan."),
 ("Kartövning","Rita en enkel karta över Europa 1942 och markera Tyskland, Storbritannien, Sovjetunionen, Sverige och Norge. Färglägg ockuperade områden.",[],None,"Kontrollera mot lärobokens karta."),
 ("Vändpunkt","Välj en vändpunkt och förklara varför den var viktig för krigets förlopp.",[],None,"Midway, Stalingrad eller Dagen D; eleven kopplar till följden att fienden gick på reträtt eller att en ny front öppnades."),
 ("Etik","Skriv en text där du jämför argument för och emot atombomberna.",[],None,"Se F1; bedöms på argument, motargument, begrepp och användning av källor."),
 ("Sverige","Förklara varför Sveriges agerande under kriget har kritiserats och försvarats.",[],None,"Försvar: litet land omringat, undvek krig. Kritik: permittenttrafik, malm, eftergifter. Efter 1943 mer självständigt, flyktingmottagande och vita bussarna."),
 ("Källkritik","Du hittar en dagbok skriven av en soldat 1944. Vilka frågor ställer du?",[],None,"Vem, när, varför, för vem; primärkälla men subjektiv; jämför med andra källor."),
 ("Diskutera","Varför är det viktigt att komma ihåg andra världskriget idag?",[],None,"Öppet svar; bedöms på motivering, exempel och reflektion."),
]

BEGREPP = [
 ("Versaillesfreden","Fredsavtalet 1919 efter första världskriget."),
 ("Eftergiftspolitik","Att ge efter för krav för att undvika krig."),
 ("Münchenavtalet","Avtal 1938 där Hitler fick Sudetenland."),
 ("Blixtkrig","Snabba anfall med stridsvagnar och flyg."),
 ("Axelmakterna","Tyskland, Italien och Japan."),
 ("De allierade","Länderna som stred mot axelmakterna."),
 ("Ockupation","När ett land tas över av en främmande makt."),
 ("Hemmafronten","Det som händer hemma under ett krig."),
 ("Motståndsrörelse","Grupp som kämpar mot en ockupant eller diktatur."),
 ("Partisaner","Gerillasoldater som stred bakom fiendens linjer."),
 ("Neutralitet","Att inte ta ställning i ett krig."),
 ("Permittenttrafiken","Tyska soldaters resor genom Sverige 1940–1943."),
 ("FN","Förenta nationerna, bildade 1945."),
 ("Järnridån","Gränsen mellan öst- och västblocket."),
 ("Kapitulation","Att ge upp i krig."),
]

SAMMAN = [
 "Orsaker: Versaillesfreden, depressionen, diktaturers aggression och eftergiftspolitik (München 1938).",
 "1 september 1939 anföll Tyskland Polen. Blixtkriget gav Tyskland Danmark, Norge och Frankrike 1940.",
 "Slaget om Storbritannien 1940 stoppade invasionsplanerna. 1941 anföll Tyskland Sovjetunionen och Japan USA.",
 "Vändpunkter: Midway (juni 1942), Stalingrad (februari 1943) och Dagen D (6 juni 1944).",
 "Kriget i Europa slutade 8 maj 1945. Efter atombomberna mot Hiroshima och Nagasaki kapitulerade Japan, 2 september 1945.",
 "Hemmafronten och motståndsrörelser präglade livet i många länder.",
 "Följder: 70–85 miljoner döda, FN, Nürnbergrättegångarna, delat Europa och kalla kriget.",
 "Sverige var neutralt men gjorde eftergifter (permittenttrafiken, malm) och tog emot flyktingar. Bedömningen varierar.",
]

TEST_A = [
 ("Vad innebar Münchenavtalet 1938?",["Polen delades","Tyskland kapitulerade","Hitler fick Sudetenland","USA gick med i kriget"],2),
 ("Vilket datum anföll Tyskland Polen?",["22 juni 1941","1 september 1939","6 juni 1944","8 maj 1945"],1),
 ("Vad kallades Tysklands snabba anfallstaktik?",["Ställningskrig","Gerillakrig","Blixtkrig","Eftergiftspolitik"],2),
 ("Vad var slaget om Storbritannien?",["En landstigning","En ubåtsstrid","Ett fredsmöte","En luftkamp 1940"],3),
 ("Vad hette det tyska anfallet mot Sovjetunionen 1941?",["Overlord","Barbarossa","Market Garden","Torch"],1),
 ("Vad var Dagen D?",["Japans kapitulation","Tysklands anfall mot Frankrike","Allierad landstigning i Normandie 6 juni 1944","Stalingrads fall"],2),
 ("Vilka städer drabbades av atombomber 1945?",["Tokyo och Osaka","Kyoto och Nagoya","Berlin och Dresden","Hiroshima och Nagasaki"],3),
 ("Vad innebar permittenttrafiken?",["Sverige blockerade hamnar","Tyska soldater på permission fick åka tåg genom Sverige","Svenska frivilliga reste till Finland","Sverige sålde vapen till USA"],1),
]
TEST_B = [
 ("Nämn två orsaker till att kriget började.","T.ex. Versaillesfreden, depressionen, aggression, eftergiftspolitik."),
 ("Varför kallas Stalingrad en vändpunkt?","Tyskland förlorade och var därefter på reträtt i öst."),
 ("Vad hände den 7 december 1941?","Japan anföll Pearl Harbor och USA gick med i kriget."),
 ("Ge ett argument för och ett emot atombomberna.","För: förkorta kriget. Emot: civila offer, Japan nära att ge upp."),
 ("Vad bildades 1945 för att förhindra nya krig?","FN."),
 ("Ge ett exempel på svensk hjälp och ett på svensk eftergift.","Hjälp: flyktingar, vita bussarna. Eftergift: permittenttrafik, järnmalm."),
]

KALLA = dict(
 text="Utdrag ur ett konstruerat brev från en kvinna i norra Norge till sin syster i Sverige, våren 1941: ”Vi har det bra, men det är svårt att få tag på kaffe, och soldaterna står vid varje hörn. Skicka inget som kan väcka misstankar. Jag hoppas att vi ses när det är över.”",
 ursprung="Konstruerad källa baserad på hur människor i ockuperade länder kunde skriva. Personerna är påhittade.",
 fragor=[
  ("Vilka tecken på ockupationen kan du se?","Brist på varor (kaffe), soldater överallt, försiktighet i brevskrivandet."),
  ("Varför kan brevet vara försiktigt skrivet?","Brev kunde läsas av censur, och författaren ville inte riskera något."),
  ("Hur trovärdig är källan för att förstå ockupationen? Motivera.","Närhet i tid och plats ger styrka, men det är en individs upplevelse och dessutom påverkad av censur. Man behöver fler källor."),
  ("Vilka andra källor skulle du jämföra med?","Dagböcker, tyska dokument, motståndsrörelsens skrifter, intervjuer i efterhand."),
 ])

SKRIV = dict(
 uppgift="Förklara hur och varför andra världskriget vände 1942–1944. Använd minst två vändpunkter och ange orsaker och följder. Avsluta med en kort reflektion om hur kriget minns idag. 300–450 ord.",
 stod=[
  "E: Eleven beskriver minst två vändpunkter (t.ex. Midway, Stalingrad, Dagen D) och några följder.",
  "C: Eleven förklarar orsaker och följder, kopplar vändpunkterna till varandra (t.ex. två fronter) och använder begrepp som allierade, axelmakterna och front.",
  "A: Eleven väger vändpunkternas betydelse, nyanserar (t.ex. att vändpunkter ses i efterhand) och diskuterar hur kriget minns och används olika i olika länder.",
 ])

LAB = dict(
 titel="Historikerns verkstad: Sverige under kriget – rättegång i klassrummet",
 syfte="Eleverna övar att granska ett historiskt beslut ur flera perspektiv och att argumentera utifrån källor.",
 material="Korta konstruerade källutdrag (tidningsnotis, politikers protokoll, flyktings brev), roll-kort, tidslinje.",
 utforande=[
  "Läraren presenterar frågan: Gjorde Sverige rätt under kriget?",
  "Klassen delas i fyra grupper: försvarare, kritiker, flyktingar/hjälporganisationer och domare.",
  "Varje grupp får tre källutdrag och förbereder ett kort inlägg.",
  "Debatt: inlägg (2 min per grupp), frågor och svar.",
  "Domarna sammanfattar vad som talar för respektive emot och formulerar en slutsats.",
  "Alla skriver en kort reflektion om vad som var svårt att avgöra.",
 ],
 fragor=[
  ("Vad är skillnaden mellan att förstå och att försvara ett beslut?","Att förstå handlar om att förklara varför människor gjorde som de gjorde; att försvara är att ta ställning för att det var rätt."),
  ("Varför behövs flera källor för att bedöma Sveriges agerande?","En källa visar ett perspektiv; flera hjälper att väga olika syften och tolkningar."),
  ("Hur kan efterklokhet påverka bedömningen?","Vi vet hur det gick, vilket de som beslutade inte visste."),
 ],
 bonus="BONUS för läraren: Låt eleverna jämföra hur en svensk, en norsk och en finländsk text beskriver Sveriges roll. Bedöm källanalys (E: nämner avsändare och syfte, C: jämför perspektiv, A: värderar trovärdighet och drar slutsatser).",
)

LARAR = [
 ("Koppling till Lgr22 (historia åk 7–9)","Kapitlet täcker centralt innehåll om imperialism och världskrig ca 1850–1950, bland annat orsaker, förlopp och följder, hemmafronten och motstånd, samt Sveriges roll. Det övar förmågan att använda historiska begrepp, analysera orsak och konsekvens, förändring och kontinuitet, granska källor och reflektera över historiebruk."),
 ("Förslag på upplägg (8–10 lektioner)","1. Orsaker (11.1). 2. 1939–1940 (11.2). 3. Världskrig 1941 (11.3). 4. Vändpunkter (11.4), kartsimuleringen. 5. Dagen D som simulering. 6. Krigsslut och atombomberna (11.5) och F1. 7. Hemmafront och motstånd (11.6). 8. Följder (11.7). 9. Sverige (11.8) och LAB. 10. Repetition och test."),
 ("Vanliga missuppfattningar","”Sverige var helt neutralt”: neutraliteten innehöll eftergifter men också hjälp. ”Tyskland ensamt startade allt”: orsakerna är flera. ”Atombomberna avslutade kriget direkt”: flera faktorer påverkade. ”Alla länder i väst var demokratier”: Sovjetunionen var en diktatur men en allierad."),
 ("Bedömningsstöd (E/C/A)","E: eleven beskriver förlopp och följder och nämner några orsaker. C: eleven förklarar orsakssamband, jämför länder och bedömer källor. A: eleven väger orsaker, tolkar olika perspektiv, diskuterar historiebruk och drar välgrundade slutsatser."),
 ("Tips: Blooket och Jeopardy","Kategorier: 1 Orsaker, 2 Årtal, 3 Platser, 4 Personer, 5 Vändpunkter, 6 Hemmafront, 7 Motstånd, 8 Sverige, 9 Följder, 10 Begrepp. Exempel: ”Vilket datum var Dagen D?” (6 juni 1944). ”Vad hette tåget tyska soldater åkte med genom Sverige?” (permittenttåg)."),
]

KALLOR = [
 ("Store norske leksikon – Münchenavtalen (datum, deltagare, följder)","https://snl.no/M%C3%BCnchenavtalen"),
 ("Store norske leksikon – Permittenttrafikk (1940–1943)","https://snl.no/permittenttrafikk"),
 ("Malmö museer – Vad är de Vita bussarna? (antal räddade, räddningsaktionen 1945)","https://malmo.se/Uppleva-och-gora/Konst-och-museer/Malmo-museum/Utstallningar/Aktuella-utstallningar/Valkommen-till-Sverige/De-Vita-bussarna/Vad-ar-de-Vita-bussarna.html"),
 ("Britannica – Nuremberg trials (åtalspunkter)","https://www.britannica.com/print/article/422668"),
 ("Riksarkivet – Finska krigsbarn (omkring 70 000 barn, omkring 7 000 stannade)","https://riksarkivet.se/resurser/finska-krigsbarn"),
 ("Forum för levande historia – Aldrig mer om folkmord (Nürnberg, Lemkin, FN-konventionen)","https://www.levandehistoria.se/sites/default/files/material_file/miniutstallning-aldrig-mer-om-folkmord-tillganglig_1.pdf"),
 ("danishmuseum.org – utställning: Denmark October 1943, Rescue of the Danish Jews","https://www.danishmuseum.org/explore/exhibitions/denmark-october-1943-rescue-of-the-danish-jews"),
 ("Gedenkstätte Deutscher Widerstand – October 1943 (judarna i Danmark)","https://www.gdw-berlin.de/en/offers/exhibitions/exhibition/view-aus/135-oktober-1943-das-schicksal-der-juden-aus-daenemark"),
 ("Wikipedia – Swedish extradition of Baltic soldiers (endast vägvisare; utlämningen 1946)","https://en.wikipedia.org/wiki/Swedish_extradition_of_Baltic_soldiers"),
]

BLOOKET = [
 ("Vilket avtal 1919 gav Tyskland skulden för första världskriget?","Versaillesfreden","Münchenavtalet","Locarnoavtalet","Parisfreden 1856"),
 ("Vad kallas politiken att ge efter för krav för att undvika krig?","Eftergiftspolitik","Neutralitet","Blockad","Isolationism"),
 ("Vilket område fick Hitler genom Münchenavtalet 1938?","Sudetenland","Alsace","Schlesien","Danzig"),
 ("När anföll Tyskland Polen?","1 september 1939","22 juni 1941","6 juni 1944","9 april 1940"),
 ("Vad kallas Tysklands snabba anfallstaktik?","Blixtkrig","Gerillakrig","Ställningskrig","Sjökrig"),
 ("Vilka två länder förklarade krig mot Tyskland 3 september 1939?","Storbritannien och Frankrike","USA och Kanada","Sverige och Norge","Italien och Japan"),
 ("När anföll Tyskland Danmark och Norge?","9 april 1940","1 sep 1939","22 jun 1941","10 maj 1940"),
 ("Hur många soldater evakuerades vid Dunkerque (ungefär)?","Omkring 338 000","Omkring 3 000","Omkring 30 000","Omkring 3 miljoner"),
 ("Vilken teknik hjälpte britterna i slaget om Storbritannien?","Radar","Satelliter","Drönare","Atombomb"),
 ("Vad hette det tyska anfallet mot Sovjetunionen?","Operation Barbarossa","Operation Overlord","Operation Torch","Operation Sea Lion"),
 ("När anföll Japan Pearl Harbor?","7 december 1941","1 september 1939","6 juni 1944","2 september 1945"),
 ("Vilken flottbas anfölls av Japan 1941?","Pearl Harbor","Midway","Guam","Singapore"),
 ("Vad hjälpte USA att vinna slaget vid Midway?","De hade knäckt Japans koder","De hade fler soldater i Kina","Japan hade inga flygplan","De hade atombomber"),
 ("Vilken stad slogs man om från augusti 1942 till februari 1943?","Stalingrad","Moskva","Kiev","Minsk"),
 ("Vad hette den allierade invasionen i Normandie?","Operation Overlord","Operation Barbarossa","Operation Market Garden","Operation Dynamo"),
 ("När var Dagen D?","6 juni 1944","8 maj 1945","7 dec 1941","2 sep 1945"),
 ("Vilket land ansvarade för stranden Juno?","Kanada","USA","Frankrike","Australien"),
 ("När slutade kriget i Europa?","8 maj 1945","6 juni 1944","2 sep 1945","1 maj 1945"),
 ("Vilka två japanska städer drabbades av atombomber?","Hiroshima och Nagasaki","Tokyo och Osaka","Kyoto och Kobe","Sapporo och Nagoya"),
 ("När undertecknades Japans kapitulation?","2 september 1945","8 maj 1945","6 augusti 1945","15 mars 1945"),
 ("Hur många dog i kriget uppskattningsvis?","70–85 miljoner","7–8 miljoner","700 000","700 miljoner"),
 ("Vilken organisation bildades 1945?","FN","Nationernas förbund","Axelmakterna","Warszawapakten"),
 ("Vad hölls i Nürnberg från november 1945?","Rättegångar mot nazistledare","Fredskonferens","Val","Krigsplanering"),
 ("Vad kallades gränsen mellan öst och väst i Europa?","Järnridån","Maginotlinjen","Atlantvallen","Versaillesmuren"),
 ("Vad menas med permittenttrafiken?","Tyska soldater åkte tåg genom Sverige","Svenskar reste till Finland","Handel med USA","Fraktflyg"),
 ("Hur många frivilliga reste från Sverige till Finland i vinterkriget (ungefär)?","Omkring 8 000","Omkring 80","Omkring 80 000","Omkring 800 000"),
 ("Vad var vita bussarna?","Röda Korsets räddningsaktion 1945","Tyska militärtransporter","Flyktingtåg 1940","Sjukhusbussar i Stockholm"),
 ("Vilket land tog emot nästan alla danska judar 1943?","Sverige","Finland","Norge","Storbritannien"),
]

JEOPARDY = {
 "Orsaker":[(100,"Fredsavtalet 1919.","Versaillesfreden"),(200,"Eftergiftspolitik på engelska.","Appeasement"),(300,"Området Hitler fick 1938.","Sudetenland"),(400,"Året för Münchenavtalet.","1938"),(500,"Pakten som delade Östeuropa 1939.","Molotov–Ribbentroppakten")],
 "Krigsåren":[(100,"Datum då kriget började.","1 september 1939"),(200,"Operation 1941 mot Sovjet.","Barbarossa"),(300,"Plats för japanskt anfall 7 dec 1941.","Pearl Harbor"),(400,"Evakueringen 1940.","Dunkerque"),(500,"Antal soldater ungefär evakuerade vid Dunkerque.","338 000")],
 "Vändpunkter":[(100,"Datum för Dagen D.","6 juni 1944"),(200,"Slaget vid floden Volga.","Stalingrad"),(300,"Kodnamn för invasionen.","Overlord"),(400,"Slag i Stilla havet 1942.","Midway"),(500,"Operation som lurade tyskarna om Calais.","Fortitude")],
 "Slutet":[(100,"Datum för krigsslutet i Europa.","8 maj 1945"),(200,"Första staden som drabbades av atombomb.","Hiroshima"),(300,"Året för FN:s bildande.","1945"),(400,"Rättegångar mot nazistledare.","Nürnberg"),(500,"Antal döda ungefär.","70–85 miljoner")],
 "Sverige":[(100,"Att inte ta ställning i kriget.","Neutralitet"),(200,"Soldattrafik 1940–1943.","Permittenttrafiken"),(300,"Räddningsaktion 1945.","Vita bussarna"),(400,"Svensk som ledde vita bussarna.","Folke Bernadotte"),(500,"Antal norska flyktingar ungefär.","50 000")],
}

GRUPPER = [
 ("orsaker","Vägen till krig","Varför kriget bröt ut och hur Tyskland erövrade Europa.",["orsaker","tidigt"]),
 ("forlopp","Världskrig och vändpunkter","Kriget sprids över världen och vänder.",["varld","vandpunkt","slut"]),
 ("hemma","Människorna och följderna","Hemmafront, motstånd och efterkrigstid.",["hemma","folg"]),
 ("sverige","Sverige under kriget","Neutralitet, eftergifter och hjälp.",["sverige"]),
]

SCEN = None
