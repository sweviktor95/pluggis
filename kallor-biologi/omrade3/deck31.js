const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-3-1-mangfald-hot-och-ekosystemtjanster.pptx",
  title: "Mångfald, hot och ekosystemtjänster", kicker: "BIOLOGI · KAPITEL 3 · BIOLOGISK MÅNGFALD", sub: "Delområde 3.1: tre nivåer, ekosystemtjänster, hot och en artinventering",
  lessons: "Gener, arter och ekosystem · Ekosystemtjänster · Hoten mot mångfalden · Labb 3.1",
  foot: "Biologi · Kapitel 3 · Delområde 3.1 Mångfald, hot och ekosystemtjänster",
  titleNotes: "Presentationen följer grundtexten i kapitel 3, delområde 3.1. Några bilder per moment. Anteckningarna innehåller handledning.",
  async slides(h) {
    const A = "Gener, arter och ekosystem";
    h.section(A, "Tre nivåer av mångfald", "Fråga: är alla tallar i en skog likadana? Vad skulle det betyda om miljön ändras?");
    await h.imgText(A, "Tre nivåer", ["Gener: variation inom en art.", "Arter: variation mellan arter.", "Ekosystem: variation mellan livsmiljöer.", "Alla tre är viktiga och påverkar varandra."], "mangfald-tre-nivaer.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Artrikedom är antalet arter i ett område. En population är alla individer av en art i området." });
    await h.imgText(A, "Näringsväv i en barrskog", ["Producenter, konsumenter och nedbrytare.", "Pilarna visar åt vilket håll energin går.", "Många arter ger fler reservdelar.", "Om sorken blir färre kan räven äta annat."], "mangfald-naringsvav.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Irländska potatismöglet: nästan bara en sorts potatis, genetiskt lika plantor. Delvis kontrollerat historiskt faktum." });
    h.kolla(A, "Kolla dig själv", ["Nämn de tre nivåerna och ett exempel på varje.", "Förklara vad en art är.", "Varför hjälper stor genetisk variation vid ett varmare klimat?", "Varför klarar ett artrikt ekosystem störningar bättre?"]);

    const B = "Ekosystemtjänster";
    h.section(B, "Det naturen gör för oss", "Låt eleverna sortera egna exempel (vandring, bär, bin, jord) i de fyra typerna.");
    await h.imgText(B, "Fyra typer", ["Försörjande: bär, fisk, virke.", "Reglerande: pollinering, vattenrening.", "Stödjande: bördig jord, fotosyntes.", "Kulturella: friluftsliv, fiske."], "ekotjanster.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Vanligt fel: att ekosystemtjänster bara är sådant man kan sälja." });
    h.stat(B, "Pollinering", "≈ 75 %", "av grödtyperna är beroende av pollinatörer i någon grad", ["Cirka 35 % av produktionen i ton kommer från sådana grödor.", "Utan pollinatörer minskar totalen med några procent, men frukt och bär drabbas hårdast.", "Myrar renar vatten och minskar översvämningar."], { notes: "Källa: Our World in Data (kontrollerad). Handpollinering i vissa kinesiska fruktodlingar är ett ofta citerat exempel som inte är källkontrollerat." });
    h.kolla(B, "Kolla dig själv", ["Ge ett exempel på varje typ av ekosystemtjänst.", "Hur kan en myr minska risken för översvämning?", "Varför är många pollinerare säkrare än en enda art?"]);

    const C = "Hoten mot mångfalden";
    h.section(C, "Fem hot och en rödlista", "Diskutera: vad är skillnaden mellan hotad och rödlistad? Hotad = VU, EN eller CR.");
    h.table(C, "De fem hoten", ["Hot", "Exempel"], [["Ändrad markanvändning", "skog avverkas, myrar dikas"], ["Överuttag", "överfiske"], ["Klimatförändringar", "arter måste flytta"], ["Föroreningar", "plast, övergödning"], ["Invasiva arter", "blomsterlupin"]], { colW: [5.4, 6.7], fs: 22, rowH: 0.7, note: "Ordningen följer IPBES 2019: cirka en miljon arter är hotade.", noteY: 6.0 });
    await h.imgText(C, "Rödlistan", ["Antal rödlistade arter i Sverige.", "Rödlistan 2025: 23 103 bedömda, 5 217 rödlistade och 2 373 hotade.", "Granska kritiskt: fler bedömda arter ger fler rödlistade."], "mangfald-rodlista-diagram.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Antalet bedömda arter ökade från cirka 19 000 till drygt 23 000. Jämför andelar, inte bara antal." });
    await h.imgText(C, "Fjällräv och gammal skog", ["Fjällräven fridlystes 1928.", "Runt år 2000 fanns cirka 35–50 vuxna.", "Rödräven konkurrerar om mat och lyor.", "Garnlav är en signalart för gammal skog."], "mangfald-fjallrav-rodrav.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Källa: SVT. Samhällsfrågan om skogen har konstruerade citat som visar olika perspektiv." });
    h.kolla(C, "Kolla dig själv", ["Nämn tre hot och ge exempel.", "Vad är en rödlista?", "Vad är en signalart?", "Ge ett argument för och ett emot att avverka gammal skog."]);

    const D = "Labb 3.1 Artinventering i en provruta";
    h.section(D, "Äng mot gräsmatta", "Material: fyra pinnar, snöre, tumstock, mobil. Planera på sommarhalvåret. Vanligt fel: rutorna läggs olika, arter räknas dubbelt.");
    await h.imgText(D, "Provruta på 1 m²", ["Märk ut en ruta på 1 × 1 meter.", "Räkna växtarter. Ta bilder och numrera.", "Gör tre rutor på varje plats.", "Räkna medelvärde för äng och gräsmatta."], "mangfald-provruta.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Förväntat: ofta fler arter på ängen, men det beror på plats och årstid. Fler rutor ger säkrare resultat." });
  }
}).catch(e => { console.error(e); process.exit(1); });
