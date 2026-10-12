const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-4-3-populationer-och-samspel.pptx",
  title: "Populationer och samspel", kicker: "BIOLOGI · KAPITEL 4 · EKOLOGI", sub: "Delområde 4.3: populationer, begränsande faktorer och samspel mellan arter",
  lessons: "Populationer och förändring · Begränsande faktorer · Konkurrens, jakt och samarbete · Labb 4.3 Rovdjur–bytesmodell",
  foot: "Biologi · Kapitel 4 · Delområde 4.3 Populationer och samspel",
  titleNotes: "Presentationen följer grundtexten i kapitel 4, delområde 4.3. Några bilder per moment. Anteckningarna innehåller handledning.",
  async slides(h) {
    const A = "Populationer och förändring";
    h.section(A, "Födda, döda, inflyttning och utflyttning", "Räkna harexemplet tillsammans: 200 + 150 − 120 + 20 − 30 = 220.");
    h.cards(A, "Fyra saker avgör populationens storlek", [["Födda", "Nya individer."], ["Döda", "Ålder, sjukdom, svält, rovdjur."], ["Inflyttning", "Individer flyttar in."], ["Utflyttning", "Individer flyttar ut."]], { h: 3.0, note: "Fler in än ut: populationen växer.", notes: "Be eleverna hitta på ett eget exempel med siffror." });
    await h.imgText(A, "Lämmelår och fjällrävar", ["Lämlarna varierar kraftigt i antal.", "Fjällräven lever av lämlar.", "Rovdjurens antal följer bytesdjurens, med fördröjning.", "Kurvorna är förenklade."], "ekologi-lamlar.png", { iw: 6.6, imgLeft: false, fs: 22, notes: "Fråga: varför kommer topparna för fjällrävarna lite efter topparna för lämlarna?" });
    h.kolla(A, "Kolla dig själv", ["Vilka fyra saker avgör en populations storlek?", "Varför kommer fjällrävarnas toppar efter lämlarnas?", "200 harar, 150 föds, 120 dör, 20 in, 30 ut. Hur många blir det?"]);

    const B = "Begränsande faktorer";
    h.section(B, "Ingen population växer för alltid", "Bärkraft är det största antal individer som miljön kan försörja under lång tid.");
    h.table(B, "Vad begränsar en population?", ["Faktor", "Typ", "Så begränsar den"], [["Föda och vatten", "Biotisk/abiotisk", "Brist ger svält"], ["Rovdjur", "Biotisk", "Håller nere bytesdjuren"], ["Konkurrens", "Biotisk", "Tävlan om samma resurs"], ["Väder", "Abiotisk", "Kall vår eller torr sommar"]], { colW: [3.2, 3.4, 5.53], fs: 20, rowH: 0.8, note: "Faktorerna samverkar: snörik vinter och hård konkurrens om maten.", notes: "Bärkraften är inte konstant. Den ändras med väder och mat." });
    await h.imgText(B, "J-kurva och S-kurva", ["Utan begränsning växer populationen exponentiellt.", "Tillväxten bromsas när resurser tar slut.", "Populationen planar ut kring bärkraften.", "Växer den över bärkraften kan den krascha."], "f_jkurva.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Fördjupning: renarna på St Matthew, 29 renar 1944, omkring 6 000 år 1963 och 42 år 1966." });
    h.kolla(B, "Kolla dig själv", ["Ge tre faktorer som kan begränsa en population.", "Vad menas med bärkraft?", "Hur kan en snörik vinter påverka rådjur?"]);

    const C = "Konkurrens, jakt och samarbete";
    h.section(C, "Hur arter påverkar varandra", "Vanligt fel: nisch och livsmiljö blandas ihop. Livsmiljö är adressen, nisch är yrket.");
    h.cards(C, "Fyra sorters samspel", [["Jakt", "Rovdjuret tjänar, bytet förlorar."], ["Konkurrens", "Båda förlorar lite."], ["Parasitism", "Parasiten tjänar, värden förlorar."], ["Symbios", "Båda tjänar. Exempel: lav (svamp och alg)."]], { h: 3.4, note: "Nisch = artens roll: vad den äter, var och när.", notes: "Be eleverna sortera egna exempel under de fyra rubrikerna." });
    await h.imgText(C, "Olika nischer i samma gran", ["Två småfåglar i samma träd.", "De söker föda på olika ställen.", "Då konkurrerar de mindre.", "Ju fler nischer, desto fler arter."], "ekologi-nisch.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Fördjupning: Gauses tofsdjur visar konkurrensutslagning när två arter har samma nisch." });
    h.kolla(C, "Kolla dig själv", ["Vad är skillnaden mellan konkurrens och symbios?", "Vad är skillnaden mellan livsmiljö och nisch?", "Varför kan flera fågelarter leva i samma gran?"]);

    const D = "Labb 4.3 Rovdjur–bytesmodell";
    h.section(D, "Pappersbitar och rovdjur", "Material: 40 pappersbitar eller bönor, stoppur. Resultaten varierar. Justera reglerna så att kurvorna svänger.");
    h.steps(D, "Så gör ni", ["Börja med 20 byten och 2 rovdjur.", "Plocka i 10 sekunder och räkna fångsten.", "Under 3 fångade: rovdjuret svälter. 6 eller fler: en unge.", "Bytena förökar sig, högst 40 totalt.", "Åtta omgångar. Rita linjediagram."], { notes: "Jämför med lämmelåren. Diskutera vad modellen förenklar, till exempel gömställen. Ingen får springa." });
  }
}).catch(e => { console.error(e); process.exit(1); });
