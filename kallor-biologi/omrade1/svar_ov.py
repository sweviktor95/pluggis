# -*- coding: utf-8 -*-
"""Facit till frågorna på sajten (grundtext och fördjupning). Visas när eleven klickar 'Visa facit'."""
KOLLA = {
 "Vad betyder ordet biologi?": "Läran om livet.",
 "Vad menas med att en undersökning är systematisk?": "Att den görs noggrant och planerat, så att andra kan kontrollera och upprepa den.",
 "Välj två av biologerna i bild 1.1. Ge ett exempel på en fråga som var och en kan undersöka.": "Till exempel: en zoolog kan undersöka hur långt en fågel flyger på en dag. En botaniker kan undersöka om en växt växer bättre i sol än i skugga.",
 "Gör frågan ”Är hundar snälla?” om till en undersökningsbar fråga.": "Till exempel: Hur många gånger skäller hundarna på en främling under tio minuter? (En fråga som går att besvara med mätning.)",
 "Vad är skillnaden mellan oberoende och beroende variabel?": "Den oberoende variabeln är det du ändrar. Den beroende variabeln är det du mäter för att se vad ändringen gav.",
 "Varför behövs en kontrollgrupp?": "Den ger något att jämföra med, så att man kan se om det man ändrade verkligen gjorde skillnad.",
 "Varför får man bara ändra en variabel åt gången?": "Annars vet man inte vilken ändring som orsakade resultatet.",
 "Vad ska en tabell innehålla?": "Rubriker, och enhet efter varje mått (till exempel mm eller s). Värdena skrivs ner direkt när man mäter.",
 "När passar ett stapeldiagram och när ett linjediagram?": "Stapeldiagram när man jämför grupper. Linjediagram när något förändras över tid (tiden på x-axeln).",
 "Räkna ut medelvärdet av 12, 14 och 13 mm.": "(12 + 14 + 13) ÷ 3 = 39 ÷ 3 = 13 mm.",
 "Vilka delar ingår i en rapport?": "Syfte och frågeställning, hypotes, material och metod, resultat (tabeller och diagram) samt diskussion och slutsats.",
 "Vad är skillnaden mellan slump och systematiskt fel? Ge ett exempel på vardera.": "Slump ger små, olika fel åt olika håll, till exempel att man läser av linjalen lite olika varje gång. Systematiskt fel ger samma fel åt samma håll varje gång, till exempel en linjal som är felgraderad.",
 "Varför minskar slumpens betydelse när man upprepar ett försök?": "Slumpens små fel jämnar ut sig när man räknar medelvärde av flera försök, och avvikande värden syns lättare.",
 "Vad menas med giltighet?": "Att man har mätt det man ville undersöka.",
 "Varför ska en slutsats också säga vad man inte vet?": "För att resultatet nästan alltid har osäkerheter. Man ska inte påstå mer än vad belägg och undersökning visar.",
 "Vad är skillnaden mellan belägg och åsikt?": "Belägg är mätningar och observationer som andra kan kontrollera. En åsikt är vad någon tycker eller tror.",
 "Varför kan man inte pröva ”Det är fel att jaga varg” med bara mätningar?": "Det är ett värderingspåstående. Mätningar kan visa hur vargen påverkar andra djur, men inte om något är rätt eller fel, eftersom det beror på värderingar.",
 "Ge två kännetecken på pseudovetenskap.": "Till exempel: den låter vetenskaplig men saknar belägg, den går inte att pröva eller visa sig vara fel, den bygger på enstaka berättelser, eller den ändras inte när nya belägg kommer.",
 "Vad visade Pasteurs svanhalskolv?": "Att mikroorganismer kommer utifrån, från luften. De uppstår inte av sig själva i buljongen.",
 "Vad var beläggen för Semmelweis idé?": "Dödligheten på hans avdelning sjönk kraftigt efter att läkarna började tvätta händerna (från 11,4 % till 1,3 %).",
 "Varför trodde många inte på honom?": "Han kunde inte förklara hur handtvätt hjälpte (bakterier var inte kända), och idén innebar att läkarna själva hade smittat patienterna.",
 "Vad menas med att en modell är en förenkling? Ge ett exempel.": "En modell visar bara det viktigaste och lämnar annat utanför. Till exempel visar en bild av en cell bara några delar, inte alla.",
 "Vad är skillnaden mellan trovärdig och relevant?": "Trovärdig betyder att man kan lita på källan. Relevant betyder att den passar min fråga. En studie på möss kan vara trovärdig men inte relevant för en fråga om människor.",
 "Varför är reklam en källa man ska vara försiktig med?": "Avsändaren vill sälja något (tendens) och visar sällan baksidor eller belägg.",
 "Granska ett påstående med hjälp av de fyra kriterierna.": "Äkthet: är källan äkta? Tid: är den aktuell? Beroende: har avsändaren själv undersökt eller bara hört det? Tendens: vill avsändaren sälja eller övertyga?",
 "Skriv ett kort argument om ett eget påstående, med belägg och motargument.": "Eget svar. Ett bra svar har ett påstående, ett belägg, ett motargument och ett bemötande. Exempel: ”Skolor bör ha rutiner för handtvätt. Handtvätt minskar smitta, som Semmelweis visade. Någon kan säga att det tar tid, men det är litet jämfört med dagar som sjuk.”",
}
def kolla_objekt(q):
    return {"f": q, "svar": KOLLA[q]} if q in KOLLA else q
