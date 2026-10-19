var innehall = window.innehall || {};

innehall["matematik-ak9-samband-funktioner-intro"] = {
  begrepp: [
    { term: "Funktion", forklaring: "en regel som gör om ett tal (x) till precis ett annat tal (y). Samma x ger alltid samma y" },
    { term: "Indata (x)", forklaring: "det tal som du stoppar in i funktionen, ofta kallat x" },
    { term: "Utdata (y)", forklaring: "det tal som kommer ut ur funktionen, ofta kallat y" },
    { term: "Formel", forklaring: "ett uttryck som beskriver hur man räknar ut y när man vet x, t.ex. y = 2x + 1" },
    { term: "Funktionsvärde", forklaring: "det y-värde som en viss x ger. Skrivs ibland f(x), så f(3) är y-värdet när x = 3" }
  ],
  begreppExempel: '<p class="begrepp-exempel-titel">📝 Exempel på en funktion:</p>' +
    '<p class="begrepp-exempel-text">y = 2<span class="variabel-x">x</span> + 1</p>' +
    '<p class="begrepp-exempel-forklaring">Funktionen dubblar x och lägger sedan till 1. Stoppar du in x = 3 får du y = 2 · 3 + 1 = 7. Stoppar du in x = 0 får du y = 1. Varje x ger precis ett y. Man kan också skriva f(x) = 2x + 1, och då betyder f(3) = 7.</p>',
  text: "En funktion är som en maskin: du stoppar in ett tal x, maskinen räknar med en formel, och ut kommer ett nytt tal y. I fyra steg får du först se maskinen arbeta, sedan räkna ut y, sedan ta reda på vilket x som gav ett visst y, och till sist lista ut vilken formel maskinen har.",
  bild: "",
  simulering: "funktioner-intro"
};

window.innehall = innehall;
