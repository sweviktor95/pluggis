const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-1-0-introduktion-till-biologi.pptx",
  title: "Introduktion till biologi", kicker: "BIOLOGI · KAPITEL 1 · BIOLOGI SOM VETENSKAP", sub: "Start: vad är biologi och vad gör biologer?",
  lessons: "Startlektion före delområde 1.1 · Vad är biologi? · Organismer · Naturvetenskap · Biologer",
  foot: "Biologi · Kapitel 1 · Introduktion till biologi",
  titleNotes: "Kort startlektion som följer avsnittet Start i grundtexten, före delområde 1.1. Anteckningarna innehåller handledning.",
  async slides(h) {
    const S = "Introduktion till biologi";
    h.section(S, "Start: biologi, organismer och biologer", "Börja med att fråga: vad tror ni att biologi handlar om? Samla svaren på tavlan.");
    h.cards(S, "Vad betyder biologi?", [["bios", "Grekiska för liv."], ["logos", "Grekiska för lära."], ["Biologi", "Läran om livet och levande organismer."]], { h: 3.0, note: "Biologi handlar om allt som lever.", notes: "Låt eleverna gissa vad bios och logos betyder innan ni visar svaret. Fråga efter andra ord med -logi." });
    h.cards(S, "Allt levande kallas organismer", [["Bakterier", "Mycket små organismer."], ["Svampar", "Till exempel kantareller och jäst."], ["Växter", "Gräs, buskar och träd."], ["Djur", "Även människor."]], { h: 3.2, note: "En organism är en levande varelse.", notes: "Gränsfall för den som frågar: virus har arvsmassa men kan inte föröka sig utan en värdcell, så många forskare räknar dem inte som levande organismer." });
    h.steps(S, "Vad undersöker biologer?", ["Hur organismer är uppbyggda.", "Hur de fungerar.", "Hur de samspelar med varandra.", "Hur livet har utvecklats."], { notes: "Koppla till kapitlen längre fram: cellen, mångfald, ekologi och människokroppen." });
    h.cards(S, "Biologi är en naturvetenskap", [["Biologi", "Livet och organismerna."], ["Kemi", "Ämnen och hur de reagerar."], ["Fysik", "Krafter, energi och rörelse."]], { h: 3.0, note: "Gemensamt: systematiska undersökningar som andra kan kontrollera och upprepa.", notes: "Systematisk = noggrant och planerat. Det är temat i resten av kapitel 1." });
    await h.imgText(S, "Biologer arbetar på många sätt", ["Zoolog: forskar om djur.", "Botaniker: forskar om växter.", "Mikrobiolog: forskar om bakterier och andra små organismer.", "Marinbiolog: forskar om livet i havet."], "l_yrken.png", { iw: 6.8, imgLeft: false, fs: 22, notes: "Vissa biologer arbetar ute i naturen, andra i laboratorier, på sjukhus eller vid en dator där de analyserar stora mängder data. Låt eleverna berätta vilken sorts biolog de själva skulle vilja vara." });
    h.kolla(S, "Kolla dig själv: Start", ["Vad betyder ordet biologi?", "Vad menas med att en undersökning är systematisk?", "Välj två av biologerna. Ge ett exempel på en fråga som var och en kan undersöka."]);
  }
}).catch(e => { console.error(e); process.exit(1); });
