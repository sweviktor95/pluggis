// Lista över färdiga häften per kapitel (nyckel = kapitlets id i struktur.js).
// Fyll i filnamn när PDF:erna lagts i mappen hafte/. Tomt = inga knappar visas.
// Exempel:
// "biologi-vetenskap-metod": {
//   titel: "Biologi som vetenskap",
//   vanlig: "hafte/bio1-vanlig.pdf",
//   lattlast: "hafte/bio1-lattlast.pdf",
//   fordjupning: "hafte/bio1-fordjupning.pdf",
//   paket: "hafte/bio1-paket.pdf",            // alla tre i en fil, för utskrift
//   sidor: "Vanlig s. 1–8, Lättläst s. 9–14, Fördjupning s. 15–18",
//   zip: "hafte/bio1.zip",                    // alla tre som separata filer
//   handledning: "hafte/bio1-lararhandledning.pdf",   // visas bara på lärarsidan
//   facit: "hafte/bio1-facit.pdf"                     // visas bara på lärarsidan
// },
window.hafte = window.hafte || {};
