# -*- coding: utf-8 -*-
"""Källan till planering/biologi.md. Kör: python3 planering/biologi_plan.py
Skriptet kontrollerar att varje kod i syfte och centralt innehåll täcks och skriver biologi.md.
Nivåer: OMRÅDE -> DELOMRÅDE (1-2 veckor) -> MOMENT (ca en lektion, vad som tas upp i texten)."""
import sys, collections

# ---- Koder -------------------------------------------------------------
SYFTE = {
 "S1": "Nyfikenhet och intresse; ställa frågor om natur och människa utifrån egna upplevelser och aktuella händelser",
 "S2": "Kunskaper om natur och människokropp; använda begrepp och förklaringsmodeller för att beskriva och förklara samband",
 "S3": "Naturvetenskapens världsbild med evolutionsteorin som grund; skilja naturvetenskapliga från andra sätt att förklara omvärlden",
 "S4": "Formulera egna och granska andras argument; kommunicera",
 "S5": "Hantera praktiska och etiska valsituationer i frågor om miljö och hälsa",
 "S6": "Söka svar med olika typer av källor; kritiskt tänkande och tilltro till den egna förmågan",
 "S7": "Egna systematiska undersökningar; påståenden kan prövas; kunskap växer fram med naturvetenskapliga arbetsmetoder",
 "S8": "Färdigheter i att hantera material, utrustning och digitala verktyg",
}
CI = {
 "NM1": "Livets uppkomst, utveckling och mångfald samt evolutionens mekanismer",
 "NM2": "Arvsmassans egenskaper; förhållandet mellan arv och miljö",
 "NM3": "Några gentekniska metoder; möjligheter, risker och etiska frågor",
 "NM4": "Lokala och globala ekosystem; samband mellan populationer och tillgängliga resurser",
 "NM5": "Fotosyntes, cellandning, materiens kretslopp och energins flöden",
 "NM6": "Människans påverkan lokalt och globalt; hållbar utveckling på individ- och samhällsnivå; biologisk mångfald och ekosystemtjänster",
 "KH1": "Kroppens celler samt några organ och organsystem: uppbyggnad, funktion och samverkan",
 "KH2": "Virus, bakterier, infektioner, smittspridning, antibiotikaresistens; förebygga och behandla infektionssjukdomar",
 "KH3": "Psykisk och fysisk hälsa: levnadsförhållanden, kost, sömn, motion, stress, beroendeframkallande medel; begränsa hälsoproblem på individ- och samhällsnivå",
 "KH4": "Reproduktion, sexualitet, identitet; relationer, kärlek, ansvar, samtycke, ömsesidighet; sexuellt överförbara sjukdomar och preventivmedel",
 "SU1": "Fältstudier och experiment (analoga och digitala verktyg): undersökningsbara frågor, planering, utförande, värdering, dokumentation (bilder, tabeller, diagram, rapporter)",
 "SU2": "Sambandet mellan undersökningar och begrepp/förklaringsmodeller; modellernas historiska framväxt, användbarhet och föränderlighet",
 "SU3": "Informationssökning, kritisk granskning och användning av biologiinformation",
 "SU4": "Argumentation och ställningstaganden i aktuella frågor om miljö och hälsa",
}
FORM = {
 "F1": "Begrepp och förklaringsmodeller (beskriva och förklara samband)",
 "F2": "Granska information, argumentera, ta ställning (miljö och hälsa)",
 "F3": "Planera, utföra och värdera systematiska undersökningar",
}
CODES = set(SYFTE) | set(CI) | set(FORM)

# ---- Planen -------------------------------------------------------------
# område: (nr, titel, idé, [delområden])
# delområde: (nr, titel, veckor, mål, nivå E->A, [moment])
# moment: (titel, vad som tas upp i texten, "koder")
P = []

P.append((1, "Biologi som vetenskap",
 "Hur vi vet det vi vet i biologi: att fråga, undersöka, värdera och granska. Läggs först eftersom allt annat bygger på det.", [
 ("1.1", "Biologi, frågor och sätt att förklara världen", 1,
  "Eleven kan beskriva vad biologi är, ställa frågor utifrån egna upplevelser och aktuella händelser och skilja undersökningsbara frågor från sådant som vetenskap inte kan pröva.",
  "E: ger exempel på undersökningsbara frågor. C: motiverar varför en fråga går att pröva eller inte. A: resonerar om skillnaden mellan naturvetenskapliga och andra sätt att förklara, med exempel.",
  [("Vad är biologi?", "Vad som kännetecknar liv, biologins grenar, vad biologer jobbar med (fält, labb, data).", "S1 S2 F1"),
   ("Från nyfikenhet till fråga", "Ställa frågor om natur och människa utifrån vardag och nyheter; göra om en fråga till en undersökningsbar fråga.", "S1 SU1 F3"),
   ("Vad kan vetenskap pröva?", "Påståenden som går/inte går att pröva, vad ett belägg är, skillnaden mot tro och åsikt, pseudovetenskap med exempel.", "S3 S6 SU3 F2")]),
 ("1.2", "Att undersöka systematiskt", 2,
  "Eleven kan planera, utföra, dokumentera och värdera en undersökning med en variabel i taget, säkert och med lämplig utrustning.",
  "E: genomför enligt plan och drar enkel slutsats. C: planerar rättvist försök och värderar felkällor. A: motiverar upplägget, föreslår förbättringar och diskuterar hur säker slutsatsen är.",
  [("Planera: fråga, förväntan, variabler", "Oberoende, beroende och kontrollerade variabler; hypotes/förväntan; rättvist försök.", "SU1 S7 F3"),
   ("Utföra: material, säkerhet, digitala verktyg", "Labbsäkerhet, mikroskop, mätredskap, sensorer och kalkylblad; fältstudie kontra experiment.", "SU1 S8 F3"),
   ("Dokumentera: tabell, diagram, rapport", "Rita tabell och diagram, välja diagramtyp, skriva en kort rapport med bilder.", "SU1 F3"),
   ("Värdera: slump, felkällor, slutsats", "Upprepade mätningar, felkällor, vad resultatet visar och inte visar; nytt försök.", "SU1 S7 F3"),
   ("Elevlab: Reaktionstid som rättvist försök", "Egen undersökning från fråga till rapport.", "SU1 S8 F3")]),
 ("1.3", "Kunskap växer och förändras", 1,
  "Eleven kan förklara hur undersökningar leder till nya begrepp och modeller och att modeller kan förändras.",
  "E: återger ett exempel på hur kunskap ändrats. C: kopplar ändringen till en undersökning. A: resonerar om modellens användbarhet och begränsningar.",
  [("Modeller och förklaringar", "Vad en förklaringsmodell är och används till; modeller förenklar och kan förbättras.", "SU2 S2 F1"),
   ("När forskare ändrat sig", "Pasteur och spontan uppkomst, Semmelweis och handtvätt, magsårsbakterien: hur belägg ändrar bilden.", "SU2 S7 F1"),
   ("Upptäckter som ändrat vår syn på naturen", "Mikroskopet, evolutionsteorin och DNA som exempel på förändrad världsbild.", "SU2 S3")]),
 ("1.4", "Information, källor och argument", 1,
  "Eleven kan söka information, bedöma källors trovärdighet och relevans och bygga ett enkelt argument.",
  "E: använder flera källor och resonerar enkelt om trovärdighet. C: motiverar bedömningen av källorna. A: väger källor mot varandra och bemöter motargument med belägg.",
  [("Söka information", "Söksätt, olika typer av källor (forskning, myndigheter, media, sociala medier), vem som står bakom.", "SU3 S6 F2"),
   ("Trovärdighet och relevans", "Kriterier för att granska källor; reklam, sponsring, vinklade rubriker.", "SU3 S6 F2"),
   ("Statistik och diagram i påståenden", "Läsa diagram, samband och orsak, urval och stickprov, vilseledande diagram.", "SU3 SU1 F2"),
   ("Argumentera", "Påstående, belägg, motargument och slutsats; skriftligt och muntligt.", "SU4 S4 F2")]),
]))

P.append((2, "Cellen och livets processer",
 "Cellen som livets enhet, energin som driver den, och vägen från cell till organism.", [
 ("2.1", "Cellen – livets byggsten", 2,
  "Eleven kan beskriva och jämföra celltyper och förklara organellernas uppgifter.",
  "E: namnger delar och uppgifter. C: jämför celltyper och kopplar byggnad till funktion. A: förklarar hur cellens delar samverkar i ett förlopp.",
  [("Cellteorin och mikroskopet", "Alla organismer består av celler; hur mikroskopet visade cellen; storleksskala.", "KH1 SU2 F1"),
   ("Djurcell och växtcell", "Cellkärna, cellmembran, cytoplasma, mitokondrier, kloroplaster, cellvägg, vakuol.", "KH1 F1"),
   ("Bakterier och encelliga organismer", "Cell utan cellkärna, skillnader mot djur- och växtceller, encelliga organismer.", "KH1 F1"),
   ("Transport över cellmembranet", "Diffusion och osmos med vardagsexempel och enkelt försök.", "KH1 F1 F3"),
   ("Gemensamt ursprung", "Varför alla celler liknar varandra; cellens uppkomst ur andra celler som del av evolutionsbilden.", "NM1 S3")]),
 ("2.2", "Fotosyntes", 2,
  "Eleven kan förklara fotosyntesen som omvandling av ljusenergi och materia och undersöka vad som påverkar den.",
  "E: anger ämnen in/ut. C: förklarar samband med ljus, CO2 och kloroplast. A: kopplar fotosyntesen till energiflöde och kretslopp i ekosystem.",
  [("Växten som producent", "Vad växten behöver och bildar; reaktionsformel i ord.", "NM5 F1"),
   ("Bladet och kloroplasten", "Bladets byggnad, klorofyll, klyvöppningar, var i cellen det sker.", "NM5 KH1 F1"),
   ("Vad påverkar fotosyntesen?", "Ljus, koldioxid, temperatur; planera och genomföra ett försök.", "NM5 SU1 F3"),
   ("Från glukos till växtens kropp", "Vad växten gör med sockret; energi lagras i kemiska bindningar.", "NM5 F1")]),
 ("2.3", "Cellandning och energi", 2,
  "Eleven kan förklara cellandning, jämföra den med fotosyntes och beskriva kretsloppet av kol och energi.",
  "E: anger ämnen in/ut. C: jämför cellandning och fotosyntes. A: kopplar processerna till kolets kretslopp och energiflöde.",
  [("Cellandning", "Ämnen in/ut, mitokondrien, att alla levande celler andas, energi till livsfunktioner.", "NM5 KH1 F1"),
   ("Jäsning", "Energi utan syre: jäst och mjölksyra; jämförelse med cellandning.", "NM5 F1"),
   ("Processerna tillsammans", "Fotosyntes och cellandning som varandras motsatser; kol och energi i kretslopp.", "NM5 F1"),
   ("Elevlab: Jäst eller vattenpest", "Undersök koldioxid- eller syrebildning; planera, genomför, värdera.", "NM5 SU1 S8 F3")]),
 ("2.4", "Från cell till organism", 1,
  "Eleven kan beskriva hur celler bygger upp vävnader, organ och organsystem och hur de samverkar.",
  "E: ger nivåordningen och exempel. C: förklarar samverkan mellan två organsystem. A: resonerar om hur en störning i ett system påverkar andra.",
  [("Specialiserade celler och vävnader", "Olika celltyper med olika uppgifter; vävnad och organ.", "KH1 F1"),
   ("Kroppens organsystem – översikt", "Vilka system kroppen har och vad de gör, som karta över kommande kapitel.", "KH1 F1"),
   ("Växtens organ", "Rot, stam, blad, blomma och deras uppgifter.", "KH1 F1")]),
]))

P.append((3, "Biologisk mångfald",
 "Den biologiska mångfaldens nivåer, hur organismer grupperas och namnges, vad som lever omkring oss och varför mångfalden är viktig.", [
 ("3.1", "Vad är biologisk mångfald?", 1,
  "Eleven kan beskriva mångfald på tre nivåer och ge exempel på var den är stor.",
  "E: namnger nivåerna. C: förklarar varför variationen inom arter spelar roll. A: jämför mångfald mellan platser och förklarar skillnaderna.",
  [("Gener, arter och ekosystem", "De tre nivåerna med exempel.", "NM1 NM6 F1"),
   ("Hur mäter man mångfald?", "Artantal, inventering, tabell och diagram.", "NM6 SU1 F3"),
   ("Var finns mångfalden?", "Regnskog, korallrev, Sveriges naturtyper; varför vissa platser har fler arter.", "NM1 NM4 F1")]),
 ("3.2", "Gruppera, namnge och bestämma arter", 2,
  "Eleven kan gruppera organismer systematiskt och bestämma en art med hjälp av nyckel.",
  "E: använder en färdig nyckel. C: förklarar principen för gruppering. A: motiverar en grupperings giltighet och hur släktskap och likhet hänger ihop.",
  [("Varför gruppera?", "Art, släkte, familj med exempel; vetenskapliga namn.", "NM1 F1"),
   ("Rikena", "Djur, växter, svampar, bakterier och encelliga organismer.", "NM1 F1"),
   ("Bestämningsnycklar", "Hur man använder och bygger en nyckel.", "SU1 F3"),
   ("Vanliga svenska arter", "Ett urval växter, svampar, djur att känna igen.", "NM1 F1")]),
 ("3.3", "Organismvärlden", 2,
  "Eleven kan beskriva huvudgrupper av växter, svampar och djur och deras anpassningar.",
  "E: beskriver kännetecken. C: kopplar kännetecken till livsmiljö. A: förklarar anpassningar som resultat av naturligt urval.",
  [("Alger, mossor och ormbunkar", "Sporväxter, deras livscykel i grova drag och var de lever.", "NM1 F1"),
   ("Fröväxter", "Barrväxter och blomväxter; pollinering och spridning.", "NM1 F1"),
   ("Svampar och lavar", "Nedbrytare, mykorrhiza och lavens samarbete.", "NM1 NM4 F1"),
   ("Ryggradslösa djur", "Leddjur, blötdjur, maskar m.fl.; mångfald.", "NM1 F1"),
   ("Ryggradsdjur", "Fiskar, groddjur, kräldjur, fåglar, däggdjur.", "NM1 F1"),
   ("Anpassningar", "Hur byggnad och beteende passar miljön; ett första möte med naturligt urval.", "NM1 S3 F1")]),
 ("3.4", "Varför är mångfalden viktig – och hotad?", 1,
  "Eleven kan förklara ekosystemtjänster och beskriva hoten mot mångfalden.",
  "E: ger exempel på tjänster och hot. C: kopplar hot till konsekvenser. A: väger olika intressen mot varandra och tar ställning med belägg.",
  [("Ekosystemtjänster", "Försörjande, reglerande, kulturella och stödjande tjänster med exempel.", "NM6 F1"),
   ("Hoten mot mångfalden", "Förlorade livsmiljöer, överutnyttjande, invasiva arter, klimat, föroreningar.", "NM6 F1"),
   ("Elevlab: Artinventering i närmiljön", "Fältstudie med nyckel; tabell och slutsats.", "NM6 SU1 S8 F3")]),
]))

P.append((4, "Ekologi",
 "Samspel i ekosystem: energi, kretslopp, populationer och resurser, lokalt och globalt.", [
 ("4.1", "Ekosystem och livsmiljöer", 1,
  "Eleven kan beskriva ekosystem, biotiska och abiotiska faktorer samt habitat och nisch.",
  "E: namnger faktorer. C: förklarar hur en faktor påverkar arter. A: resonerar om hur flera faktorer samverkar.",
  [("Vad är ett ekosystem?", "Levande och icke-levande delar; gränser och exempel.", "NM4 F1"),
   ("Lokala och globala ekosystem", "Skog, sjö, hav, fjäll, och världens större naturtyper.", "NM4 F1"),
   ("Habitat och nisch", "Var och hur en art lever; två arter, samma miljö.", "NM4 F1")]),
 ("4.2", "Energi och näringsvägar", 2,
  "Eleven kan förklara energiflöde genom näringskedjor och näringsvävar.",
  "E: bygger en näringskedja. C: förklarar energiförlust mellan nivåer. A: förutsäger följder av en förändring i en väv.",
  [("Producenter, konsumenter och nedbrytare", "Roller i ekosystemet.", "NM4 NM5 F1"),
   ("Näringskedjor och näringsvävar", "Rita och läsa; vem äter vem.", "NM4 F1"),
   ("Energiflöde och biomassa", "Energin minskar uppåt; varför det finns färre rovdjur än växtätare.", "NM5 F1"),
   ("Störs vävan – vad händer?", "Resonera om ett bortfall av en art.", "NM4 F2")]),
 ("4.3", "Materiens kretslopp", 2,
  "Eleven kan beskriva hur kol, kväve och vatten cirkulerar och varför materia inte försvinner.",
  "E: beskriver ett kretslopp. C: kopplar kretslopp till processer. A: resonerar om hur mänsklig påverkan stör kretsloppet.",
  [("Materia tillverkas inte och försvinner inte", "Atomerna återanvänds; kretslopp och energiflöde skiljs åt.", "NM5 F1"),
   ("Kolets kretslopp", "Fotosyntes, cellandning, förbränning, fossilt kol.", "NM5 F1"),
   ("Kvävets och vattnets kretslopp", "Kvävefixering, växternas upptag, vattnets väg genom organismer.", "NM5 F1"),
   ("Nedbrytning", "Nedbrytarnas roll; jordens bildning.", "NM5 F1")]),
 ("4.4", "Populationer och resurser", 2,
  "Eleven kan förklara hur populationer förändras och begränsas av resurser och samspel.",
  "E: beskriver faktorer. C: tolkar diagram över populationsförändring. A: motiverar prognoser och diskuterar osäkerhet.",
  [("Populationer och förändring", "Födelser, dödsfall, in- och utvandring; tillväxtkurvor.", "NM4 SU1 F1"),
   ("Begränsande faktorer", "Föda, plats, sjukdom; bärkraft.", "NM4 F1"),
   ("Konkurrens, jakt och samarbete", "Predation, parasitism, symbios; samutveckling som exempel på evolution.", "NM4 NM1 S3 F1"),
   ("Ekosystems känslighet", "Nyckelarter, störningar, återhämtning.", "NM4 F1"),
   ("Elevlab: Nedbrytning eller provyta", "Planera och genomför en fältstudie och värdera.", "NM4 SU1 S8 F3")]),
]))

P.append((5, "Människan och miljön",
 "Hur människan påverkar naturen och hur individer och samhället kan främja hållbar utveckling.", [
 ("5.1", "Människans påverkan på naturen", 2,
  "Eleven kan beskriva och förklara hur utsläpp, jord- och skogsbruk, fiske och invasiva arter påverkar ekosystem.",
  "E: beskriver en påverkan. C: förklarar orsakssamband. A: jämför flera påverkansfaktorer och deras omfattning.",
  [("Naturbruk", "Jordbruk, skogsbruk och fiske; nytta och påverkan.", "NM6 F1"),
   ("Miljögifter och bioackumulering", "Hur ämnen sprids och ansamlas i näringskedjan.", "NM6 NM5 F1"),
   ("Övergödning", "Orsaker och följder, exemplet Östersjön.", "NM6 F1"),
   ("Försurning och invasiva arter", "Orsaker, följder och åtgärder.", "NM6 F1")]),
 ("5.2", "Klimat och ekosystem", 1,
  "Eleven kan förklara växthuseffekten och klimatförändringarnas påverkan på natur.",
  "E: beskriver effekten. C: förklarar samband mellan utsläpp och följder. A: granskar information om klimat och värderar åtgärder.",
  [("Växthuseffekten", "Naturlig och förstärkt växthuseffekt.", "NM5 NM6 F1"),
   ("Följder för arter och ekosystem", "Förändrade utbredningsområden, korallblekning, havsförsurning.", "NM6 F1"),
   ("Kolsänkor och åtgärder", "Skog, hav, mark; vad som minskar utsläpp.", "NM5 NM6 F2")]),
 ("5.3", "Hållbar utveckling och ställningstagande", 2,
  "Eleven kan förklara hållbar utveckling och argumentera för val på individ- och samhällsnivå.",
  "E: framför enkelt argument med viss underbyggnad. C: bemöter motargument. A: väger etiska och naturvetenskapliga skäl mot varandra.",
  [("Vad är hållbar utveckling?", "Ekologisk, social och ekonomisk dimension.", "NM6 S5 F1"),
   ("Naturresurser och ekosystemtjänster", "Förnybart och icke-förnybart; vad vi får gratis av naturen.", "NM6 F1"),
   ("Vad kan jag och samhället göra?", "Konsumtion, mat, resor, lagar och naturskydd.", "NM6 S5 F2"),
   ("Argumentera i en miljöfråga", "Samla belägg, bemöta motargument, ta ställning.", "SU4 S4 S5 F2"),
   ("Elevlab: Vatten och övergödning", "Mät och värdera i ett modellförsök eller en fältstudie.", "NM6 SU1 S8 F3")]),
]))

P.append((6, "Mat och matspjälkning",
 "Näringsämnen, matspjälkningens organ och kopplingen mellan kost och hälsa.", [
 ("6.1", "Näringsämnen", 1,
  "Eleven kan beskriva näringsämnenas uppgifter i kroppen.",
  "E: ger uppgifter för några. C: förklarar samband mellan näringsämne och funktion. A: bedömer en måltids näringsinnehåll.",
  [("Kolhydrater, proteiner och fetter", "Uppgifter och källor.", "KH1 KH3 F1"),
   ("Vitaminer, mineraler, vatten och fibrer", "Vad kroppen behöver i små mängder.", "KH1 KH3 F1"),
   ("Energi i maten", "Energiinnehåll och energibehov.", "KH3 F1")]),
 ("6.2", "Matspjälkning", 2,
  "Eleven kan följa maten genom matspjälkningssystemet och förklara spjälkning och upptag.",
  "E: namnger organ och funktion. C: förklarar enzymer och upptag. A: kopplar byggnad till funktion och förklarar följder av en störning.",
  [("Matens väg", "Mun, matstrupe, mage, tunntarm, tjocktarm.", "KH1 F1"),
   ("Enzymer och spjälkning", "Vad enzymer gör; vad som påverkar dem.", "KH1 F1"),
   ("Upptag och tarmflora", "Tunntarmens yta; tarmbakteriernas roll.", "KH1 KH2 F1"),
   ("Elevlab: Enzymförsök", "Undersök spjälkning av stärkelse.", "KH1 SU1 S8 F3")]),
 ("6.3", "Kost och hälsa", 1,
  "Eleven kan granska påståenden om kost och förklara hur kosten påverkar hälsan.",
  "E: återger kostråd. C: motiverar kostråd med funktion i kroppen. A: granskar och bemöter ett kostpåstående med belägg.",
  [("Kostråd och energibalans", "Vad kostråd bygger på; vad som händer vid över- och underskott.", "KH3 F1"),
   ("Mat och miljö", "Matens klimat- och naturpåverkan.", "KH3 NM6 F2"),
   ("Granska kostpåståenden", "Dieter, kosttillskott, influerare.", "KH3 SU3 SU4 S6 F2")]),
]))

P.append((7, "Andning, blod och rörelse",
 "Syret ut i kroppen och hur system samverkar vid ansträngning.", [
 ("7.1", "Andningssystemet", 1,
  "Eleven kan förklara hur luft tas upp och gasutbytet fungerar.",
  "E: namnger delar. C: förklarar gasutbyte. A: förklarar hur andningen regleras och påverkas av sjukdom eller rökning.",
  [("Luftvägar och lungor", "Näsa till lungblåsor; gasutbyte.", "KH1 F1"),
   ("Andning och cellandning", "Kopplingen mellan lungorna och cellernas behov.", "KH1 NM5 F1")]),
 ("7.2", "Hjärta, blod och kärl", 2,
  "Eleven kan beskriva blodomloppet och blodets uppgifter.",
  "E: beskriver väg och delar. C: förklarar syretransport. A: kopplar byggnad till funktion och resonerar om hjärt-kärlsjukdom.",
  [("Hjärta och blodkärl", "Hjärtats byggnad, artärer, vener, kapillärer.", "KH1 F1"),
   ("Blodet", "Röda och vita blodkroppar, blodplättar, plasma.", "KH1 F1"),
   ("Blodomloppet och syretransport", "Lilla och stora kretsloppet.", "KH1 F1")]),
 ("7.3", "Muskler, skelett och samverkan", 1,
  "Eleven kan förklara hur system samverkar vid motion.",
  "E: beskriver några system. C: förklarar samverkan. A: förutsäger och förklarar kroppens reaktion på ansträngning.",
  [("Skelett och muskler", "Uppgifter och samarbete i rörelse.", "KH1 F1"),
   ("Samverkan vid ansträngning", "Andning, puls och blodflöde.", "KH1 KH3 F1"),
   ("Elevlab: Puls och andning vid belastning", "Planera och genomför en mätning; värdera.", "KH1 SU1 S8 F3")]),
]))

P.append((8, "Infektioner och immunförsvar",
 "Bakterier och virus, smitta, kroppens försvar, vaccin och antibiotika.", [
 ("8.1", "Bakterier och virus", 1,
  "Eleven kan jämföra bakterier och virus och beskriva deras betydelse.",
  "E: ger skillnader. C: förklarar hur de förökar sig. A: förklarar varför behandlingen skiljer sig.",
  [("Bakterier – nyttiga och skadliga", "Byggnad, förökning, nytta.", "KH2 F1"),
   ("Virus", "Byggnad och förökning i värdceller.", "KH2 F1")]),
 ("8.2", "Smitta och infektion", 1,
  "Eleven kan förklara smittvägar och hur infektioner förebyggs.",
  "E: beskriver smittvägar. C: förklarar förebyggande åtgärder. A: analyserar smittspridning och åtgärder på samhällsnivå.",
  [("Smittvägar", "Droppe, kontakt, mat, vektorer.", "KH2 F1"),
   ("Förebygga smitta", "Hygien, isolering, smittspårning; epidemi och pandemi.", "KH2 KH3 F1")]),
 ("8.3", "Kroppens försvar", 2,
  "Eleven kan beskriva immunförsvarets delar och minne.",
  "E: beskriver några delar. C: förklarar samverkan. A: förklarar immunsvaret vid ny och upprepad smitta.",
  [("Barriärer och första försvar", "Hud, slemhinnor, inflammation.", "KH2 F1"),
   ("Vita blodkroppar och antikroppar", "Hur kroppen känner igen och oskadliggör.", "KH2 F1"),
   ("Immunologiskt minne", "Varför man sällan blir sjuk två gånger i samma.", "KH2 F1")]),
 ("8.4", "Vaccin och antibiotika", 2,
  "Eleven kan förklara vaccin, antibiotika och resistens som evolution.",
  "E: beskriver vad vaccin/antibiotika gör. C: förklarar flockimmunitet och resistens. A: granskar påståenden och argumenterar för åtgärder.",
  [("Vaccination", "Hur vaccin fungerar och flockimmunitet.", "KH2 F1"),
   ("Antibiotika", "Verkar på bakterier, inte virus.", "KH2 F1"),
   ("Resistens", "Hur resistens uppstår genom naturligt urval; varför antibiotika ska användas rätt.", "KH2 NM1 S3 F1"),
   ("Granska påståenden om vaccin och smitta", "Källkritik och argument.", "KH2 SU3 SU4 S6 F2"),
   ("Elevlab: Smittspridningsmodell eller bakterietillväxt", "Planera, genomför och värdera.", "KH2 SU1 S8 F3")]),
]))

P.append((9, "Arv och genetik",
 "Arvsmassan, hur egenskaper ärvs och samspelet mellan arv och miljö.", [
 ("9.1", "Arvsmassan", 2,
  "Eleven kan beskriva DNA, gener och kromosomer och hur de hänger ihop.",
  "E: namnger begreppen. C: förklarar hur gener styr egenskaper. A: förklarar sambandet gen–protein–egenskap.",
  [("DNA", "Struktur och funktion i stora drag.", "NM2 F1"),
   ("Gener och kromosomer", "Gen, kromosom, genom.", "NM2 F1"),
   ("Från gen till egenskap", "Proteiner som mellanled.", "NM2 F1")]),
 ("9.2", "Celldelning och befruktning", 1,
  "Eleven kan skilja på kroppsceller och könsceller och förklara variation.",
  "E: beskriver delning. C: skiljer mitos och meios. A: förklarar hur variationen uppstår.",
  [("Celldelning", "Cellen delar sig; tillväxt och reparation.", "NM2 KH1 F1"),
   ("Könsceller och befruktning", "Halverat kromosomtal; ny kombination.", "NM2 F1")]),
 ("9.3", "Nedärvning", 2,
  "Eleven kan förklara nedärvning med dominanta och recessiva anlag och använda korsningsschema.",
  "E: tolkar enkla scheman. C: räknar sannolikheter. A: tolkar stamträd och förklarar undantag.",
  [("Anlag och alleler", "Dominant och recessiv; genotyp och fenotyp.", "NM2 F1"),
   ("Korsningsschema", "Sannolikheter vid en egenskap.", "NM2 F1"),
   ("Ärftliga sjukdomar och stamträd", "Hur en egenskap följer släkten.", "NM2 KH3 F1")]),
 ("9.4", "Arv, miljö och mutationer", 1,
  "Eleven kan förklara arv och miljö och mutationer.",
  "E: ger exempel på arv och miljö. C: förklarar samverkan. A: granskar påståenden om arv och miljö.",
  [("Arv och miljö", "Egenskaper formas av båda; tvillingar som exempel.", "NM2 F1"),
   ("Mutationer", "Vad de är och varför de skapar variation.", "NM2 NM1 S3 F1"),
   ("Elevlab: DNA ur frukt", "Utför och dokumentera.", "NM2 SU1 S8 F3")]),
]))

P.append((10, "Genteknik",
 "Metoder, användning och de etiska frågorna.", [
 ("10.1", "Metoder", 1,
  "Eleven kan beskriva några gentekniska metoder och skilja dem från traditionell förädling.",
  "E: beskriver en metod. C: jämför metoder. A: förklarar metodens principer.",
  [("Förädling och genteknik", "Urval över generationer jämfört med att ändra gener direkt.", "NM3 F1"),
   ("Gensax, GMO och kloning", "Principer i enkel form.", "NM3 F1")]),
 ("10.2", "Användning", 1,
  "Eleven kan ge exempel på hur genteknik används.",
  "E: ger exempel. C: förklarar nytta. A: analyserar nytta och risk.",
  [("Medicin", "Insulin, genterapi, vaccin.", "NM3 F1"),
   ("Jordbruk och livsmedel", "Förädlade och modifierade grödor.", "NM3 F1"),
   ("Släktskap och identifiering", "DNA-profil, genetiska tester.", "NM3 F1")]),
 ("10.3", "Möjligheter, risker och etik", 2,
  "Eleven kan argumentera om genteknik med naturvetenskaplig och etisk underbyggnad.",
  "E: framför och bemöter enkelt argument. C: bemöter med belägg. A: väger flera perspektiv mot varandra.",
  [("Möjligheter och risker", "Nytta, osäkerhet, regler.", "NM3 S5 F2"),
   ("Etiska frågor", "Vad vi bör göra – inte bara vad vi kan.", "NM3 S5 SU4 F2"),
   ("Elevlab: Strukturerad debatt", "Förbered argument med belägg och möt motargument.", "NM3 SU4 S4 F2")]),
]))

P.append((11, "Evolution och livets historia",
 "Hur livet uppstod och förändras, mekanismerna och bevisen. Evolutionen bär även övriga områden (S3).", [
 ("11.1", "Livets uppkomst och historia", 2,
  "Eleven kan beskriva livets historia och naturvetenskapliga förklaringar till livets uppkomst.",
  "E: återger en tidslinje. C: förklarar vad som är belagt och vad som är hypotes. A: resonerar om hur kunskapen om livets uppkomst prövas.",
  [("Jordens och livets tidslinje", "Jordens ålder, de första cellerna, flercelligt liv.", "NM1 F1"),
   ("Hur kan livet ha uppstått?", "Naturvetenskapliga hypoteser och vad som är osäkert.", "NM1 SU2 S3 F1"),
   ("Fossil och massutdöenden", "Hur fossil bildas och berättar.", "NM1 F1")]),
 ("11.2", "Evolutionens mekanismer", 2,
  "Eleven kan förklara naturligt urval, variation och artbildning.",
  "E: beskriver urval. C: förklarar med exempel. A: tillämpar mekanismerna på nya fall.",
  [("Variation och mutationer", "Källor till skillnader.", "NM1 NM2 F1"),
   ("Naturligt urval", "Överlevnad och fortplantning.", "NM1 F1"),
   ("Artbildning", "Isolering och särutveckling.", "NM1 F1")]),
 ("11.3", "Bevis för evolution", 1,
  "Eleven kan redogöra för bevis och värdera dem.",
  "E: ger bevis. C: förklarar vad beviset visar. A: väger bevis mot varandra.",
  [("Fossil och jämförande anatomi", "Släktskap som syns i byggnad.", "NM1 SU2 F1"),
   ("DNA och direkta observationer", "Släktskap i gener; evolution som sker nu.", "NM1 NM2 F1")]),
 ("11.4", "Människans evolution och synen på evolution", 1,
  "Eleven kan förklara människans evolution och skilja naturvetenskapliga från andra sätt att förklara.",
  "E: beskriver människans släktskap. C: skiljer ut vad som kan prövas. A: resonerar om hur olika sätt att förklara skiljer sig, respektfullt och sakligt.",
  [("Människans ursprung", "Primater och tidiga människor.", "NM1 F1"),
   ("Darwin och förklaringens historia", "Hur teorin växte fram och prövas.", "NM1 SU2 S3 F1"),
   ("Naturvetenskap och andra sätt att förklara", "Vad vetenskap kan och inte kan pröva.", "S3 S6 F2"),
   ("Elevlab: Modellförsök om urval", "Simulera urval och värdera modellens begränsningar.", "NM1 SU1 SU2 S8 F3")]),
]))

P.append((12, "Hälsa och levnadsvanor",
 "Kroppens styrning, stress, sömn, motion, beroende och hur hälsa kan främjas.", [
 ("12.1", "Nerver, hormoner och reglering", 1,
  "Eleven kan förklara hur nerver och hormoner styr kroppen.",
  "E: namnger system. C: jämför nerv- och hormonsignaler. A: förklarar reglering med exempel.",
  [("Nervsystemet och sinnena", "Hjärna, ryggmärg, nerver; reflex.", "KH1 F1"),
   ("Hormoner och balans", "Hur hormoner verkar; blodsockerreglering som exempel.", "KH1 F1")]),
 ("12.2", "Stress, sömn och psykisk hälsa", 2,
  "Eleven kan förklara stress och sömn och beskriva vad som främjar psykisk hälsa.",
  "E: beskriver stressreaktion. C: kopplar levnadsförhållanden till hälsa. A: analyserar åtgärder på individ- och samhällsnivå.",
  [("Stress i kroppen", "Reaktion, kort och lång stress.", "KH3 KH1 F1"),
   ("Sömn", "Vad sömn gör; råd.", "KH3 F1"),
   ("Psykisk ohälsa och stöd", "Sakligt om ohälsa och var man får hjälp.", "KH3 F1"),
   ("Levnadsförhållanden och hälsa", "Hur miljö, ekonomi och relationer påverkar.", "KH3 F2")]),
 ("12.3", "Motion och levnadsvanor", 1,
  "Eleven kan förklara motionens betydelse och sambandet mellan vanor och folksjukdomar.",
  "E: beskriver nytta. C: förklarar samband. A: granskar påståenden.",
  [("Fysisk aktivitet", "Effekter på kroppen.", "KH3 F1"),
   ("Levnadsvanor och sjukdom", "Hjärt-kärlsjukdom och typ 2-diabetes som exempel.", "KH3 F1")]),
 ("12.4", "Beroendeframkallande medel", 2,
  "Eleven kan förklara hur beroende uppstår och vad som kan begränsa problemen.",
  "E: beskriver risker. C: förklarar beroende. A: argumenterar om åtgärder på samhällsnivå.",
  [("Alkohol, tobak, nikotin", "Effekter och risker.", "KH3 F1"),
   ("Cannabis och andra droger", "Effekter, risker och lagar.", "KH3 F1"),
   ("Hjärnan och beroende", "Belöningssystemet.", "KH3 KH1 F1"),
   ("Förebyggande och stöd", "Individ och samhälle.", "KH3 SU4 S5 F2"),
   ("Elevlab: Enkät och diagram", "Planera en enkät, sammanställ och värdera.", "KH3 SU1 S8 F3")]),
]))

P.append((13, "Pubertet, sexualitet och relationer",
 "Kroppens förändringar, reproduktion, relationer och samtycke.", [
 ("13.1", "Pubertet", 1,
  "Eleven kan beskriva kroppens förändringar under puberteten.",
  "E: beskriver förändringar. C: förklarar hormoners roll. A: förklarar variation.",
  [("Förändringar i kroppen", "Hormoner och utveckling.", "KH4 KH1 F1"),
   ("Könsorgan och menscykel", "Byggnad och funktion.", "KH4 F1")]),
 ("13.2", "Reproduktion", 2,
  "Eleven kan förklara befruktning, graviditet och fosterutveckling.",
  "E: beskriver stegen. C: förklarar förloppet. A: kopplar till hormoner och hälsa.",
  [("Befruktning", "Från könsceller till zygot.", "KH4 F1"),
   ("Graviditet och fosterutveckling", "Skeden och hälsa under graviditet.", "KH4 F1"),
   ("Förlossning", "Förloppet i stora drag.", "KH4 F1")]),
 ("13.3", "Preventivmedel och sexuellt överförbara sjukdomar", 2,
  "Eleven kan förklara preventivmedel och STI samt hur man skyddar sig.",
  "E: ger exempel. C: jämför metoder. A: motiverar val med belägg.",
  [("Preventivmedel", "Metoder, skydd och nödpreventivmedel.", "KH4 F1"),
   ("STI", "Vanliga STI, skydd, test och behandling.", "KH4 KH2 F1"),
   ("Aborträtt och hjälp", "Faktabaserat om lagen och var man får hjälp.", "KH4 F1")]),
 ("13.4", "Sexualitet, identitet, relationer och samtycke", 2,
  "Eleven kan resonera om sexualitet, identitet, relationer och samtycke.",
  "E: förklarar samtycke. C: resonerar om ansvar och ömsesidighet. A: analyserar situationer med flera perspektiv.",
  [("Sexualitet och identitet", "Sakligt om variation.", "KH4 F1"),
   ("Relationer, kärlek och ansvar", "Vad som kännetecknar en god relation.", "KH4 S5 F2"),
   ("Samtycke och gränser", "Ömsesidighet, gränser, nätet, våld och var man får hjälp.", "KH4 S5 F2"),
   ("Granska information om sex och relationer", "Källkritik och mediebilder.", "KH4 SU3 S6 F2"),
   ("Elevlab: Faktaundersökning", "Sök, granska och sammanställ information.", "KH4 SU3 SU1 F3")]),
]))

P.append((14, "Repetition inför nationella proven",
 "Binder ihop begrepp, undersökningar och argumentation.", [
 ("14.1", "Begrepp och samband", 2,
  "Eleven kan förklara samband mellan områden.",
  "E: återger. C: förklarar samband. A: kopplar flera områden i ett resonemang.",
  [("Röda trådar", "Energi, kretslopp, evolution, samverkan.", "NM1 NM5 S3 F1"),
   ("Kroppen som helhet", "System som samverkar.", "KH1 KH2 KH3 F1")]),
 ("14.2", "Undersökning och argumentation", 1,
  "Eleven kan planera och värdera en undersökning och argumentera.",
  "E: planerar enkelt. C: värderar upplägg. A: förbättrar upplägg och argumenterar med belägg.",
  [("Planera och värdera en undersökning", "Träna på hela kedjan.", "SU1 S7 F3"),
   ("Argumentera i miljö- och hälsofrågor", "Övningar.", "SU4 S4 S5 F2")]),
 ("14.3", "Provträning", 1,
  "Eleven kan lösa provlika uppgifter.",
  "Prov som visar nivå på alla förmågor.",
  [("Provlik uppgiftsserie", "Blandade uppgifter.", "F1 F2 F3")]),
]))

# ---- Kontroll ------------------------------------------------------------
def check():
    seen = collections.Counter(); area_f = collections.defaultdict(set); s3 = set(); bad = []
    n_d = n_m = 0; weeks = 0
    for a in P:
        for d in a[3]:
            n_d += 1; weeks += d[2]
            for m in d[5]:
                n_m += 1
                for t in m[2].split():
                    if t not in CODES: bad.append((m[0], t))
                    seen[t] += 1
                    if t.startswith("F"): area_f[a[0]].add(t)
                    if t == "S3": s3.add(a[0])
    missing = sorted(CODES - set(seen))
    return seen, area_f, s3, bad, missing, n_d, n_m, weeks

def main():
    seen, area_f, s3, bad, missing, n_d, n_m, weeks = check()
    print("områden", len(P), "delområden", n_d, "moment", n_m, "veckor", weeks)
    print("okända koder:", bad, "ej täckta:", missing)
    print("S3 i områden:", sorted(s3))
    for a in P:
        print(a[0], sorted(area_f[a[0]]))
    if bad or missing: sys.exit(1)
    out = []
    w = out.append
    w("# Biologi åk 7–9 – planering (Lgr22)\n")
    w("Status: förslag, väntar på Vicks genomgång. Genereras av `planering/biologi_plan.py` – ändra där, inte här.\n")
    w("Källa: kursplanen i biologi (`kursplaner/Biologi-GRGRBIO01.pdf`): ämnets syfte, centralt innehåll för åk 7–9 och kunskapskraven för slutet av åk 9. Innehållet behandlas i sak och citeras inte.\n")
    w("## Hur planen är byggd\n")
    w("- **Område** – ett stort ämnesområde (t.ex. Ekologi). Blir ett kapitel i boken.")
    w("- **Delområde** – en snävare del som man kan arbeta med i 1–2 veckor (t.ex. Materiens kretslopp).")
    w("- **Moment** – en konkret lektion: vad som tas upp i texten. Varje moment är kodat mot kursplanen.")
    w("- Varje område (utom repetitionen) har minst en elevlab. Evolutionsperspektivet (S3) finns i åtta av fjorton områden, inte bara i kapitel 11.\n")
    w("Koder: **S1–S8** = ämnets syfte, **NM/KH/SU** = centralt innehåll, **F1–F3** = förmågorna i kunskapskraven. Nivåraden i varje delområde beskriver vad som skiljer E, C och A i just det innehållet (kriterierna används som riktning, inte som facit).\n")
    w("## Översikt\n")
    w("| Område | Delområden | Veckor (förslag) |"); w("|---|---|---|")
    for a in P:
        wk = sum(d[2] for d in a[3])
        w(f"| {a[0]}. {a[1]} | {len(a[3])} | {wk} |")
    w(f"| **Totalt** | **{n_d}** | **{weeks}** |\n")
    w(f"Antal moment: {n_m}. Veckorna är grova; ett delområde är tänkt att ta 1–2 veckor beroende på timplan.\n")
    w("## Täckning\n")
    w("### Syftet"); w("| Kod | Innehåll | Antal moment |"); w("|---|---|---|")
    for k, v in SYFTE.items(): w(f"| {k} | {v} | {seen[k]} |")
    w("\n### Centralt innehåll"); w("| Kod | Innehåll | Antal moment |"); w("|---|---|---|")
    for k, v in CI.items(): w(f"| {k} | {v} | {seen[k]} |")
    w("\n### Förmågor per område"); w("| Område | F1 | F2 | F3 |"); w("|---|---|---|---|")
    for a in P:
        f = area_f[a[0]]
        w(f"| {a[0]}. {a[1]} | {'x' if 'F1' in f else ''} | {'x' if 'F2' in f else ''} | {'x' if 'F3' in f else ''} |")
    w("\n" + "Evolution (S3) finns i områdena: " + ", ".join(str(x) for x in sorted(s3)) + ".\n")
    w("## Planen\n")
    for a in P:
        w(f"## {a[0]}. {a[1]}\n"); w(f"*{a[2]}*\n")
        for d in a[3]:
            w(f"### {d[0]} {d[1]} ({d[2]} v)\n")
            w(f"**Mål:** {d[3]}\n"); w(f"**Nivåer:** {d[4]}\n")
            for i, m in enumerate(d[5], 1):
                w(f"- **{d[0]}.{i} {m[0]}** – {m[1]} `{m[2]}`")
            w("")
    w("## Öppna frågor\n")
    w("1. Antal veckor och lektioner per vecka beror på din timplan; ska jag skala planen efter den?")
    w("2. Kapitel 11 (evolution) ligger sent. Vill du flytta det tidigare, eftersom det är grunden i syftet?")
    w("3. Genetik och genteknik (9 och 10) kan slås ihop om du vill ha färre kapitel.")
    w("4. Nerver och hormoner ligger i 12.1. Vill du ha dem tidigare, t.ex. före kapitel 7?")
    w("5. Sajten har idag två nivåer under ämnet (kapitel, moment). Tre nivåer kräver en ändring av ämnesträdet. Ska den göras efter att planen är godkänd?")
    open("planering/biologi.md", "w", encoding="utf-8").write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
