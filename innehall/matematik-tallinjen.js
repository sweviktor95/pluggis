// Exempel på en innehållsfil - så här ser mönstret ut för varje lövnod
// (moment utan egna "barn" i struktur.js). Kopiera den här filen och
// byt ut id och innehåll när ni skriver fler moment.

var innehall = window.innehall || {};

innehall["matematik-tallinjen"] = {
  text: "Här skriver ni texten om tallinjen. Förklara vad tallinjen är, hur man läser av tal på den, och gör gärna kopplingen till negativa tal och decimaltal.",
  bild: "",           // t.ex. "bilder/tallinjen.png"
  simulering: "tallinjen-heltal-0-10"
};

window.innehall = innehall;
