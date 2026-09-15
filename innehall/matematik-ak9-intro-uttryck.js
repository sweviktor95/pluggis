var innehall = window.innehall || {};

innehall["matematik-ak9-intro-uttryck"] = {
  begrepp: [
    { term: "Uttryck", forklaring: "en kombination av tal, symboler och räknesätt - till skillnad från en ekvation har ett uttryck inget likhetstecken" },
    { term: "Term", forklaring: "en del av ett uttryck, t.ex. 3x eller −5, som hänger ihop med tecknet framför sig" },
    { term: "Koefficient", forklaring: "talet framför en variabel i en term, t.ex. är 3 koefficienten i termen 3x" },
    { term: "Konstant", forklaring: "en term som bara är ett tal, utan någon variabel, t.ex. 7" },
    { term: "Variabel", forklaring: "en bokstav (t.ex. x eller y) som representerar ett okänt eller varierande tal" }
  ],
  begreppExempel: '<p class="begrepp-exempel-titel">📝 Exempel på ett uttryck:</p>' +
    '<p class="begrepp-exempel-text">3<span class="variabel-x">x</span> − 5</p>' +
    '<p class="begrepp-exempel-forklaring"><strong>3x</strong> är en term - koefficienten 3 gånger variabeln x. <strong>−5</strong> är också en term, men eftersom den saknar variabel kallas den en konstant. Lägg märke till att minustecknet hör ihop med termen - det är därför den är negativ.</p>',
  text: "Ett uttryck är en kombination av tal, symboler och räknesätt - men till skillnad från en ekvation har det inget likhetstecken. Här bygger vi upp förståelsen i tre steg, från att räkna frukt till att förenkla uttryck helt på egen hand.",
  bild: "",
  simulering: "uttryck-dragspel"
};

window.innehall = innehall;
