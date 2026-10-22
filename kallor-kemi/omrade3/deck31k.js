const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-3-1-atomens-byggnad.pptx",
  title: "Atomens byggnad", kicker: "KEMI · KAPITEL 3 · ATOMER OCH GRUNDÄMNEN", sub: "Delområde 3.1: partiklar, atommodeller, isotoper och radioaktivitet, labb: svarta lådan",
  lessons: "Atomen och dess partiklar · Atommodellernas historia · Isotoper och radioaktivitet · Labb 3.1",
  foot: "Kemi · Kapitel 3 · Delområde 3.1 Atomens byggnad",
  titleNotes: "Presentationen följer grundtexten i kapitel 3, delområde 3.1. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Atomen och dess partiklar", B = "Atommodellernas historia", Cc = "Isotoper och radioaktivitet", D = "Labb 3.1 Svarta lådan";
    h.section(A, "Atomen och dess partiklar", "Fråga: vilka delar tror ni att en atom har? Samla förslag på tavlan.");
    h.table(A, "Tre partiklar", ["Partikel", "Laddning", "Plats"], [["Proton", "+1", "Atomkärnan"], ["Neutron", "0", "Atomkärnan"], ["Elektron", "−1", "Elektronskalen"]], { colW: [3.6, 3, 5.6], note: "Elektronens massa är ungefär en tvåtusendel av protonens och räknas oftast som noll." });
    await h.imgText(A, "Kolatomen", ["6 protoner och 6 neutroner i kärnan.", "6 elektroner i skal: 2 i första och 4 i andra.", "Lika många elektroner som protoner: atomen är neutral."], "v_atom.png", { iw: 6.6, imgLeft: false, fs: 22, notes: "Låt eleverna räkna partiklarna i bilden." });
    h.cards(A, "Atomnummer och masstal", [["Atomnummer", "Antalet protoner. Avgör vilket grundämne det är."], ["Masstal", "Protoner + neutroner."], ["Neutroner", "masstal − atomnummer. Exempel: fosfor 31 − 15 = 16."]], { h: 3.2, note: "Låt eleverna räkna natrium (23 − 11 = 12) i par." });
    h.kolla(A, "Kolla dig själv", ["Var finns protoner, neutroner och elektroner?", "Varför är en atom neutral?", "Atomnummer 8 och masstal 16: hur många neutroner?"]);

    h.section(B, "Atommodellernas historia", "Fråga: hur kan man veta hur något osynligt ser ut? Låt eleverna fundera innan ni går vidare.");
    await h.imgText(B, "Fyra modeller", ["Dalton (1808): atomen är en liten kula.", "Thomson: positiv laddning med elektroner i, som russin i en kaka.", "Rutherford (1911): liten tung kärna.", "Bohr (1913): elektroner i skal med bestämd energi."], "v_modeller.png", { iw: 8.6, imgLeft: false, fs: 20, notes: "Poängtera att varje modell byggde på vad man kunde mäta då." });
    await h.imgText(B, "Rutherfords försök", ["Alfapartiklar sköts mot tunn guldfolie.", "De flesta gick rakt igenom, några få avlänkades.", "Slutsats: liten, tung, positiv kärna och mestadels tom atom."], "v_rutherford.png", { iw: 7.4, imgLeft: false, fs: 22, notes: "Fråga vad Thomsons modell skulle förutsagt. Koppla till labben." });
    h.cards(B, "Modellernas gränser", [["Bohr", "Fungerar bra för väte men inte för atomer med flera elektroner. Ersattes av kvantmekaniken på 1920-talet."], ["Skolan", "Skalmodellen används eftersom den är enkel och förklarar mycket."], ["Lärdom", "Nya experiment ger nya modeller."]], { h: 3.4 });
    h.kolla(B, "Kolla dig själv", ["Vad såg man i Rutherfords försök?", "Vilken slutsats drog han?", "Nämn en begränsning hos Bohrs modell."]);

    h.section(Cc, "Isotoper och radioaktivitet", "Fråga: kan två atomer av samma grundämne vara olika? På vilket sätt?");
    await h.imgText(Cc, "Isotoper av kol", ["Alla har 6 protoner.", "Kol-12: 6 neutroner. Kol-13: 7. Kol-14: 8.", "Kol-14 är radioaktivt."], "v_isotoper.png", { iw: 8.6, imgLeft: false, fs: 22, notes: "Isotoper har samma kemiska egenskaper men olika masstal." });
    await h.imgText(Cc, "Tre sorters strålning", ["Alfa stoppas av papper eller hud.", "Beta stoppas av aluminium.", "Gamma stoppas av bly.", "All sådan strålning är joniserande och kan skada celler."], "v_stralning.png", { iw: 7.6, imgLeft: false, fs: 21, notes: "Visa att olika strålning kräver olika skydd." });
    h.table(Cc, "Halveringstid", ["Tid", "Halveringstider", "Kvar av 80 g"], [["0 år", "0", "80 g"], ["10 år", "1", "40 g"], ["20 år", "2", "20 g"], ["30 år", "3", "10 g"]], { colW: [3, 4, 5.2], note: "Påhittat ämne med halveringstid 10 år. Kol-14 har halveringstiden 5 730 år." });
    h.cards(Cc, "Användning och risker", [["Användning", "Strålbehandling, bilddiagnostik (PET), åldersbestämning med kol-14, kärnkraft."], ["Risk", "Strålningen kan skada celler. Tjernobyl och Fukushima är exempel på olyckor."], ["Skydd", "Korta tiden, öka avståndet, skärma av."]], { h: 3.4 });
    h.kolla(Cc, "Kolla dig själv", ["Vad är isotoper?", "Vad menas med halveringstid?", "Nämn en användning och en risk."]);

    h.section(D, "Labb 3.1: svarta lådan", "Material: lådor med gömda former, kulor. Förväntat: kulan avlänkas där formen sitter. Låt eleverna rulla från minst tre håll.");
    await h.imgText(D, "Gör så här", ["Du får en låda utan att se in i den.", "Rulla kulor från olika håll och anteckna.", "Rita en gissning på formen.", "Kontrollera. Stämde det?"], "v_labb1.png", { iw: 5.4, imgLeft: false, fs: 21, notes: "Koppla till Rutherford: dra slutsatser om något dolt." });
    h.table(D, "Frågor att svara på", ["Fråga", "Tips"], [["Hur gjorde du din gissning?", "Vilka banor var viktigast?"], ["Hur liknar försöket Rutherfords?", "Lika och olika."], ["Hur säker är din slutsats?", "Fler försök från fler håll."]], { colW: [6, 6.2] });
  }
}).catch(e => { console.error(e); process.exit(1); });
