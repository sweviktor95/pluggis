const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-4-0-introduktion-till-foreningar.pptx",
  title: "Introduktion till kemiska föreningar", kicker: "KEMI · KAPITEL 4 · KEMISKA FÖRENINGAR OCH REAKTIONER", sub: "Start: vad händer när atomer möts?",
  lessons: "Vad händer när atomer möts? · Vad ingår i kapitlet?",
  foot: "Kemi · Kapitel 4 · Start Vad händer när atomer möts?",
  titleNotes: "Presentationen följer grundtexten i kapitel 4. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Vad händer när atomer möts?";
    h.section(A, "Atomer som möts", "Fråga: varför blir en bit järn rostig men inte en guldring? Samla gissningar och spara dem till slutet av kapitlet.");
    await h.imgText(A, "Från atomer till föreningar", ["Atomer kan binda till varandra.", "Då bildas molekyler eller jonföreningar.", "Kemiska reaktioner gör att atomerna byter partner.", "Atomerna försvinner aldrig."], "v_oversikt.png", { iw: 7.6, imgLeft: false, fs: 22, notes: "Bilderna är schematiska. Koppla till skalmodellen från kapitel 3." });
    h.table(A, "Vad ingår i kapitlet?", ["Delområde", "Du lär dig"], [["4.1 Molekyler och joner", "Kovalent bindning, joner och jonbindning, egenskaper hos föreningar. Labb: leder lösningar elektrisk ström?"], ["4.2 Kemiska reaktioner", "Tecken på reaktion, reaktionsformler, massans bevarande, hastighet och energi. Labb: massan bevaras"]], { colW: [4, 8.2] });
    h.kolla(A, "Kolla dig själv", ["Vad händer med atomerna i en kemisk reaktion?", "Nämn en sak som du tror får järn att rosta.", "Vilka två sorters föreningar ska vi undersöka?"]);
  }
}).catch(e => { console.error(e); process.exit(1); });
