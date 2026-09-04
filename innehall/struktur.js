// Hela Pluggis ämnesträd. Varje nod kan ha "barn" (undernivåer) - hur
// många nivåer djupt som helst. En nod UTAN barn (eller med tom barn-lista)
// blir en innehållssida - då letar mallen efter en matchande post i
// "innehall"-objektet (se t.ex. matematik-tallinjen.js) för text/bild/simulering.
//
// Så här lägger du till mer:
// - Nytt ämne: lägg till ett objekt i toppnivå-listan (med ikon!)
// - Ny nivå/delmoment: lägg till i rätt "barn"-lista
// - Idéer på ikoner: 🧮 📐 🧬 🌱 🧪 ⚗️ ⚡ 🔭 ⚙️ 🔧

var struktur = [
  {
    id: "matematik",
    titel: "Matematik",
    ikon: "🧮",
    barn: [
      {
        id: "matematik-ak7",
        titel: "Årskurs 7",
        barn: [
          {
            id: "matematik-ak7-tal",
            titel: "Tal",
            barn: [
              { id: "matematik-tallinjen", titel: "Tallinjen" }
            ]
          },
          { id: "matematik-ak7-brak", titel: "Bråk" },
          { id: "matematik-ak7-procent", titel: "Procent" },
          { id: "matematik-ak7-algebra", titel: "Algebra" },
          { id: "matematik-ak7-geometri", titel: "Geometri" }
        ]
      },
      { id: "matematik-ak8", titel: "Årskurs 8", barn: [] },
      { id: "matematik-ak9", titel: "Årskurs 9", barn: [] }
    ]
  },
  {
    id: "biologi",
    titel: "Biologi",
    ikon: "🌱",
    barn: [
      { id: "biologi-vetenskap", titel: "Vetenskap" },
      { id: "biologi-liv", titel: "Liv" },
      { id: "biologi-mangfald", titel: "Biologisk mångfald" },
      { id: "biologi-ekologi", titel: "Ekologi" }
    ]
  },
  {
    id: "kemi",
    titel: "Kemi",
    ikon: "🧪",
    barn: []
  },
  {
    id: "fysik",
    titel: "Fysik",
    ikon: "⚡",
    barn: []
  },
  {
    id: "teknik",
    titel: "Teknik",
    ikon: "⚙️",
    barn: []
  }
];
