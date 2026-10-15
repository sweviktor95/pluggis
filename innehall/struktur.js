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
            id: "matematik-ak7-statistik",
            titel: "Statistik",
            barn: [
              { id: "matematik-ak7-statistik-tabeller", titel: "Tabeller" },
              { id: "matematik-ak7-statistik-diagram", titel: "Diagram" },
              { id: "matematik-ak7-statistik-lagesmatt", titel: "Lägesmått och spridningsmått" },
              { id: "matematik-ak7-statistik-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-tal",
            titel: "Tal",
            barn: [
              { id: "matematik-klockan", titel: "Klockan" },
              { id: "matematik-tallinjen", titel: "Tallinjen" },
              { id: "matematik-positionssystem", titel: "Positionssystemet" },
              { id: "matematik-positionssystem-decimaler", titel: "Positionssystemet - Inklusive decimaler" },
              { id: "matematik-ak7-tal-tiobas", titel: "Tiobas (multiplicera/dividera med 10, 100, 1000 osv)" },
              {
                id: "matematik-rakneattt",
                titel: "De fyra räknesätten",
                barn: [
                  { id: "matematik-addition", titel: "Addition" },
                  { id: "matematik-subtraktion", titel: "Subtraktion" },
                  { id: "matematik-multiplikation", titel: "Multiplikation" },
                  { id: "matematik-division", titel: "Division" }
                ]
              },
              { id: "matematik-ak7-tal-decimalberakningar", titel: "Decimalberäkningar (multiplicera/dividera med tal mellan 0 och 1)" },
              { id: "matematik-ak7-tal-primtal", titel: "Primtal" },
              { id: "matematik-ak7-tal-delbarhet", titel: "Delbarhet" },
              { id: "matematik-ak7-tal-avrundning", titel: "Avrundning" },
              { id: "matematik-ak7-tal-overslagsrakning", titel: "Överslagsräkning" },
              { id: "matematik-ak7-tal-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-brak",
            titel: "Bråk",
            barn: [
              { id: "matematik-ak7-brak-tallinjen", titel: "Bråkform" },
              { id: "matematik-ak7-brak-jamfora", titel: "Jämföra bråk" },
              { id: "matematik-ak7-brak-forlang-forkorta", titel: "Förlänga och förkorta bråk" },
              { id: "matematik-ak7-brak-add-sub", titel: "Addition och subtraktion av bråk" },
              { id: "matematik-ak7-brak-mult", titel: "Multiplikation av bråk" },
              { id: "matematik-ak7-brak-div", titel: "Division av bråk" },
              { id: "matematik-ak7-brak-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-procent",
            titel: "Procent",
            barn: [
              { id: "matematik-ak7-procent-andel", titel: "Andel" },
              { id: "matematik-ak7-procent-forandring", titel: "Förändring" },
              { id: "matematik-ak7-procent-huvudrakning", titel: "Huvudräkning" },
              { id: "matematik-ak7-procent-delen", titel: "Delen" },
              { id: "matematik-ak7-procent-det-hela", titel: "Det hela" },
              { id: "matematik-ak7-procent-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-algebra",
            titel: "Algebra",
            barn: [
              { id: "matematik-intro-uttryck", titel: "Algebraiska uttryck" },
              { id: "matematik-forenkla-uttryck", titel: "Förenkla uttryck" },
              { id: "matematik-ak7-algebra-formler", titel: "Formler" },
              { id: "matematik-ak7-algebra-monster", titel: "Mönster" },
              { id: "matematik-intro-ekvationer", titel: "Ekvationer intro" },
              { id: "matematik-ekvationer", titel: "Ekvationslösningar" },
              { id: "matematik-ak7-algebra-problemlosning", titel: "Problemlösning" },
              { id: "matematik-ak7-algebra-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-geometri",
            titel: "Geometri",
            barn: [
              { id: "matematik-ak7-geometri-enheter-prefix", titel: "Enheter och prefix" },
              { id: "matematik-ak7-geometri-vinklar", titel: "Vinklar" },
              { id: "matematik-ak7-geometri-vinkelsumma-manghorningar", titel: "Vinkelsumma och månghörningar" },
              { id: "matematik-ak7-geometri-omkrets", titel: "Omkrets" },
              { id: "matematik-ak7-geometri-area-intro", titel: "Area intro" },
              { id: "matematik-ak7-geometri-area-fyrhorningar", titel: "Area fyrhörningar" },
              { id: "matematik-ak7-geometri-area-trianglar", titel: "Area trianglar" },
              { id: "matematik-ak7-geometri-area-cirklar", titel: "Area cirklar" },
              { id: "matematik-ak7-geometri-repetition", titel: "Repetition" }
            ]
          }
        ]
      },
      { id: "matematik-ak8", titel: "Årskurs 8", barn: [] },
      {
        id: "matematik-ak9",
        titel: "Årskurs 9",
        barn: [
          {
            id: "matematik-ak9-brak",
            titel: "Bråk",
            barn: [
              { id: "matematik-ak9-tallinjen", titel: "Tallinjen" },
              { id: "matematik-ak9-brak-forlang-forkorta", titel: "Förlänga och förkorta bråk" },
              { id: "matematik-ak9-brak-add-sub", titel: "Addition och subtraktion av bråk" },
              { id: "matematik-ak9-brak-mult", titel: "Multiplikation av bråk" },
              { id: "matematik-ak9-brak-div", titel: "Division av bråk" },
              { id: "matematik-ak9-brak-repetition", titel: "Jeopardy bråk" },
              { id: "matematik-ak9-brak-repetition-knapp", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-algebra",
            titel: "Algebra",
            barn: [
              { id: "matematik-ak9-intro-uttryck", titel: "Uttryck intro" },
              { id: "matematik-ak9-forenkla-uttryck", titel: "Förenkla uttryck" },
              { id: "matematik-ak9-algebra-multiplicera-uttryck", titel: "Multiplicera uttryck" },
              { id: "matematik-ak9-algebra-faktorisera-uttryck", titel: "Faktorisera uttryck" },
              { id: "matematik-ak9-intro-ekvationer", titel: "Ekvationer intro" },
              { id: "matematik-ak9-ekvationer", titel: "Ekvationer" },
              { id: "matematik-ak9-algebra-problemlosning", titel: "Problemlösning" },
              { id: "matematik-ak9-algebra-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-samband",
            titel: "Samband och förändring",
            barn: [
              { id: "matematik-ak9-samband-funktioner-intro", titel: "Funktioner intro" },
              { id: "matematik-ak9-samband-linjara-funktioner", titel: "Linjära funktioner" },
              { id: "matematik-ak9-samband-rata-linjens-ekvation", titel: "Räta linjens ekvation" },
              { id: "matematik-ak9-samband-procentuell-forandring", titel: "Procentuell förändring" },
              { id: "matematik-ak9-samband-upprepad-procentuell-forandring", titel: "Upprepad procentuell förändring" },
              { id: "matematik-ak9-samband-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-geometri",
            titel: "Geometri",
            barn: [
              { id: "matematik-ak9-geometri-symmetri", titel: "Symmetri" },
              { id: "matematik-ak9-geometri-likformighet-kongruens", titel: "Likformighet och kongruens" },
              { id: "matematik-ak9-geometri-langdskala", titel: "Längdskala" },
              { id: "matematik-ak9-geometri-areaskala", titel: "Areaskala" },
              { id: "matematik-ak9-geometri-volymskala", titel: "Volymskala" },
              { id: "matematik-ak9-geometri-likformiga-trianglar-topptriangelsatsen", titel: "Likformiga trianglar och topptriangelsatsen" },
              { id: "matematik-ak9-geometri-pythagoras-sats", titel: "Pythagoras sats" },
              { id: "matematik-ak9-geometri-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-repetition-np",
            titel: "Repetition åk 7-9 inför NP",
            barn: [
              {
                id: "matematik-ak9-np-tal",
                titel: "Tal",
                barn: [
                  { id: "matematik-ak9-np-tal-decimalform", titel: "Decimalform" },
                  { id: "matematik-ak9-np-tal-mult-div", titel: "Multiplikation och division" },
                  { id: "matematik-ak9-np-tal-brak", titel: "Bråk" },
                  { id: "matematik-ak9-np-tal-negativa-tal", titel: "Negativa tal" },
                  { id: "matematik-ak9-np-tal-potenser-kvadratrotter", titel: "Potenser och kvadratrötter" },
                  { id: "matematik-ak9-np-tal-prioriteringsregler", titel: "Prioriteringsregler" },
                  { id: "matematik-ak9-np-tal-avrundning-overslag", titel: "Avrundning och överslagsräkning" },
                  { id: "matematik-ak9-np-tal-repetition", titel: "Repetition tal" }
                ]
              },
              {
                id: "matematik-ak9-np-algebra",
                titel: "Algebra",
                barn: [
                  { id: "matematik-ak9-np-algebra-uttryck", titel: "Uttryck" },
                  { id: "matematik-ak9-np-algebra-forenkla-uttryck", titel: "Förenkla uttryck" },
                  { id: "matematik-ak9-np-algebra-ekvationer", titel: "Ekvationer" },
                  { id: "matematik-ak9-np-algebra-monster", titel: "Mönster" },
                  { id: "matematik-ak9-np-algebra-formler", titel: "Formler" },
                  { id: "matematik-ak9-np-algebra-repetition", titel: "Repetition algebra" }
                ]
              },
              {
                id: "matematik-ak9-np-geometri",
                titel: "Geometri",
                barn: [
                  { id: "matematik-ak9-np-geometri-vinklar-manghorningar", titel: "Vinklar och månghörningar" },
                  { id: "matematik-ak9-np-geometri-omkrets-enheter", titel: "Omkrets och enheter" },
                  { id: "matematik-ak9-np-geometri-area-volym", titel: "Area och volym" },
                  { id: "matematik-ak9-np-geometri-symmetri", titel: "Symmetri" },
                  { id: "matematik-ak9-np-geometri-likformiga-figurer", titel: "Likformiga figurer" },
                  { id: "matematik-ak9-np-geometri-skala", titel: "Skala" },
                  { id: "matematik-ak9-np-geometri-pythagoras-sats", titel: "Pythagoras sats" },
                  { id: "matematik-ak9-np-geometri-repetition", titel: "Repetition geometri" }
                ]
              },
              {
                id: "matematik-ak9-np-statistik",
                titel: "Statistik och sannolikhetslära",
                barn: [
                  { id: "matematik-ak9-np-statistik-tolka-diagram", titel: "Tolka diagram" },
                  { id: "matematik-ak9-np-statistik-lagesmatt-spridningsmatt", titel: "Lägesmått och spridningsmått" },
                  { id: "matematik-ak9-np-statistik-kombinatorik", titel: "Kombinatorik" },
                  { id: "matematik-ak9-np-statistik-sannolikhet", titel: "Sannolikhet" },
                  { id: "matematik-ak9-np-statistik-repetition", titel: "Repetition statistik och sannolikhetslära" }
                ]
              },
              {
                id: "matematik-ak9-np-samband",
                titel: "Samband och förändring",
                barn: [
                  { id: "matematik-ak9-np-samband-andel-delen-hela", titel: "Andel, delen, det hela" },
                  { id: "matematik-ak9-np-samband-procentuell-forandring-forandringsfaktor", titel: "Procentuell förändring och förändringsfaktor" },
                  { id: "matematik-ak9-np-samband-procentenheter", titel: "Procentenheter" },
                  { id: "matematik-ak9-np-samband-koordinatsystem-grafer", titel: "Koordinatsystem och tolka grafer" },
                  { id: "matematik-ak9-np-samband-proportionalitet-linjara-samband", titel: "Proportionalitet och linjära samband" },
                  { id: "matematik-ak9-np-samband-rata-linjens-ekvation", titel: "Räta linjens ekvation" },
                  { id: "matematik-ak9-np-samband-repetition", titel: "Repetition samband och förändring" }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  // BIOLOGI START (genereras av planering/biologi_plan25.py)
  {
    id: "biologi",
    titel: "Biologi (beta)",
    ikon: "🌱",
    ramverk: true,
    barn: [
      {
        id: "biologi-vetenskap",
        titel: "1. Biologi som vetenskap",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-1-1",
            titel: "1.1 Undersöka systematiskt",
            ramverk: true,
            barn: [
              { id: "biologi-m-1-1-1", titel: "Från fråga till plan" },
              { id: "biologi-m-1-1-2", titel: "Dokumentera: tabell, diagram, rapport" },
              { id: "biologi-m-1-1-3", titel: "Värdera: slump, felkällor, slutsats" },
              { id: "biologi-m-1-1-l", titel: "Labb: Reaktionstid som rättvist försök" }
            ]
          },
          {
            id: "biologi-d-1-2",
            titel: "1.2 Modeller, källor och argument",
            ramverk: true,
            barn: [
              { id: "biologi-m-1-2-1", titel: "Vad kan vetenskap pröva?" },
              { id: "biologi-m-1-2-2", titel: "När forskare ändrat sig" },
              { id: "biologi-m-1-2-3", titel: "Söka information och bedöma källor" },
              { id: "biologi-m-1-2-l", titel: "Labb: Granska ett påstående" }
            ]
          },
          { id: "biologi-m-1-s", titel: "Sammanfattning och begrepp" },
          { id: "biologi-m-1-t", titel: "Testa dig själv" }
        ]
      },
      {
        id: "biologi-omrade-2",
        titel: "2. Cellen och livets processer",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-2-1",
            titel: "2.1 Cellen",
            ramverk: true,
            barn: [
              { id: "biologi-m-2-1-1", titel: "Vad är liv? Cellteorin och mikroskopet" },
              { id: "biologi-m-2-1-2", titel: "Djurcell och växtcell" },
              { id: "biologi-m-2-1-3", titel: "Bakterier och encelliga organismer" },
              { id: "biologi-m-2-1-l", titel: "Labb: Mikroskopera celler" }
            ]
          },
          {
            id: "biologi-d-2-2",
            titel: "2.2 Fotosyntes och cellandning",
            ramverk: true,
            barn: [
              { id: "biologi-m-2-2-1", titel: "Växten som producent" },
              { id: "biologi-m-2-2-2", titel: "Cellandning" },
              { id: "biologi-m-2-2-3", titel: "Processerna tillsammans" },
              { id: "biologi-m-2-2-l", titel: "Labb: Jäst och koldioxid" }
            ]
          },
          {
            id: "biologi-d-2-3",
            titel: "2.3 Organ och organsystem",
            ramverk: true,
            barn: [
              { id: "biologi-m-2-3-1", titel: "Specialiserade celler och vävnader" },
              { id: "biologi-m-2-3-2", titel: "Kroppens organsystem – översikt" }
            ]
          },
          { id: "biologi-m-2-s", titel: "Sammanfattning och begrepp" },
          { id: "biologi-m-2-t", titel: "Testa dig själv" }
        ]
      },
      {
        id: "biologi-omrade-3",
        titel: "3. Biologisk mångfald",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-3-1",
            titel: "3.1 Mångfald, hot och ekosystemtjänster",
            ramverk: true,
            barn: [
              { id: "biologi-m-3-1-1", titel: "Gener, arter och ekosystem" },
              { id: "biologi-m-3-1-2", titel: "Ekosystemtjänster" },
              { id: "biologi-m-3-1-3", titel: "Hoten mot mångfalden" },
              { id: "biologi-m-3-1-l", titel: "Labb: Artinventering i en provruta" }
            ]
          },
          {
            id: "biologi-d-3-2",
            titel: "3.2 Gruppera och organismvärlden",
            ramverk: true,
            barn: [
              { id: "biologi-m-3-2-1", titel: "Rikena" },
              { id: "biologi-m-3-2-2", titel: "Bestämningsnycklar" },
              { id: "biologi-m-3-2-3", titel: "Anpassningar" },
              { id: "biologi-m-3-2-l", titel: "Labb: Artbestämning med nyckel" }
            ]
          }
        ]
      },
      {
        id: "biologi-ekologi",
        titel: "4. Ekologi",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-4-1",
            titel: "4.1 Ekosystem och energi",
            ramverk: true,
            barn: [
              { id: "biologi-m-4-1-1", titel: "Vad är ett ekosystem?" },
              { id: "biologi-m-4-1-2", titel: "Producenter, konsumenter och näringsvävar" },
              { id: "biologi-m-4-1-3", titel: "Energiflöde och biomassa" },
              { id: "biologi-m-4-1-l", titel: "Labb: Energi i en näringskedja – modellspel" }
            ]
          },
          {
            id: "biologi-d-4-2",
            titel: "4.2 Materiens kretslopp",
            ramverk: true,
            barn: [
              { id: "biologi-m-4-2-1", titel: "Materia tillverkas inte och försvinner inte" },
              { id: "biologi-m-4-2-2", titel: "Kolets kretslopp" },
              { id: "biologi-m-4-2-3", titel: "Nedbrytning" },
              { id: "biologi-m-4-2-l", titel: "Labb: Nedbrytning i jord" }
            ]
          },
          {
            id: "biologi-d-4-3",
            titel: "4.3 Populationer och samspel",
            ramverk: true,
            barn: [
              { id: "biologi-m-4-3-1", titel: "Populationer och förändring" },
              { id: "biologi-m-4-3-2", titel: "Begränsande faktorer" },
              { id: "biologi-m-4-3-3", titel: "Konkurrens, jakt och samarbete" },
              { id: "biologi-m-4-3-l", titel: "Labb: Rovdjur–bytesmodell" }
            ]
          },
          { id: "biologi-m-4-s", titel: "Sammanfattning och begrepp" },
          { id: "biologi-m-4-t", titel: "Testa dig själv" }
        ]
      },
      {
        id: "biologi-omrade-5",
        titel: "5. Människan och miljön",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-5-1",
            titel: "5.1 Påverkan på naturen och klimat",
            ramverk: true,
            barn: [
              { id: "biologi-m-5-1-1", titel: "Övergödning" },
              { id: "biologi-m-5-1-2", titel: "Växthuseffekten" },
              { id: "biologi-m-5-1-3", titel: "Följder för arter och ekosystem" },
              { id: "biologi-m-5-1-l", titel: "Labb: Växthuseffekten – modell" }
            ]
          },
          {
            id: "biologi-d-5-2",
            titel: "5.2 Hållbar utveckling och ställningstagande",
            ramverk: true,
            barn: [
              { id: "biologi-m-5-2-1", titel: "Vad är hållbar utveckling?" },
              { id: "biologi-m-5-2-2", titel: "Naturresurser och ekosystemtjänster" },
              { id: "biologi-m-5-2-3", titel: "Vad kan jag och samhället göra?" },
              { id: "biologi-m-5-2-l", titel: "Labb: Argumentera i en miljöfråga" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-6",
        titel: "6. Kroppens system: mat, andning och blod",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-6-1",
            titel: "6.1 Mat och matspjälkning",
            ramverk: true,
            barn: [
              { id: "biologi-m-6-1-1", titel: "Kolhydrater, proteiner och fetter" },
              { id: "biologi-m-6-1-2", titel: "Matens väg och spjälkning" },
              { id: "biologi-m-6-1-3", titel: "Kostråd och energibalans" },
              { id: "biologi-m-6-1-l", titel: "Labb: Enzymförsök" }
            ]
          },
          {
            id: "biologi-d-6-2",
            titel: "6.2 Andning, blod och samverkan",
            ramverk: true,
            barn: [
              { id: "biologi-m-6-2-1", titel: "Luftvägar och lungor" },
              { id: "biologi-m-6-2-2", titel: "Hjärta och blodkärl" },
              { id: "biologi-m-6-2-3", titel: "Blodomloppet och syretransport" },
              { id: "biologi-m-6-2-l", titel: "Labb: Puls och andning vid belastning" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-7",
        titel: "7. Infektioner och immunförsvar",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-7-1",
            titel: "7.1 Bakterier, virus och smitta",
            ramverk: true,
            barn: [
              { id: "biologi-m-7-1-1", titel: "Bakterier och virus" },
              { id: "biologi-m-7-1-2", titel: "Smittvägar" },
              { id: "biologi-m-7-1-3", titel: "Förebygga smitta" },
              { id: "biologi-m-7-1-l", titel: "Labb: Smittspridningsmodell med handtvätt" }
            ]
          },
          {
            id: "biologi-d-7-2",
            titel: "7.2 Immunförsvar, vaccin och antibiotika",
            ramverk: true,
            barn: [
              { id: "biologi-m-7-2-1", titel: "Vita blodkroppar och antikroppar" },
              { id: "biologi-m-7-2-2", titel: "Vaccination" },
              { id: "biologi-m-7-2-3", titel: "Antibiotika och resistens" },
              { id: "biologi-m-7-2-l", titel: "Labb: Granska ett vaccinpåstående" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-8",
        titel: "8. Arv, genetik och genteknik",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-8-1",
            titel: "8.1 DNA och nedärvning",
            ramverk: true,
            barn: [
              { id: "biologi-m-8-1-1", titel: "DNA, gener och kromosomer" },
              { id: "biologi-m-8-1-2", titel: "Anlag och alleler" },
              { id: "biologi-m-8-1-3", titel: "Korsningsschema" },
              { id: "biologi-m-8-1-l", titel: "Labb: DNA ur frukt" }
            ]
          },
          {
            id: "biologi-d-8-2",
            titel: "8.2 Arv och miljö, mutationer och genteknik",
            ramverk: true,
            barn: [
              { id: "biologi-m-8-2-1", titel: "Arv och miljö" },
              { id: "biologi-m-8-2-2", titel: "Gensax, GMO och kloning" },
              { id: "biologi-m-8-2-3", titel: "Etiska frågor" },
              { id: "biologi-m-8-2-l", titel: "Labb: Etisk bedömning av genteknik" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-9",
        titel: "9. Evolution och livets historia",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-9-1",
            titel: "9.1 Livets historia och bevis",
            ramverk: true,
            barn: [
              { id: "biologi-m-9-1-1", titel: "Jordens och livets tidslinje" },
              { id: "biologi-m-9-1-2", titel: "Fossil och massutdöenden" },
              { id: "biologi-m-9-1-3", titel: "Fossil och jämförande anatomi" },
              { id: "biologi-m-9-1-l", titel: "Labb: Jämför skelett och bygg släktträd" }
            ]
          },
          {
            id: "biologi-d-9-2",
            titel: "9.2 Evolutionens mekanismer",
            ramverk: true,
            barn: [
              { id: "biologi-m-9-2-1", titel: "Variation och naturligt urval" },
              { id: "biologi-m-9-2-2", titel: "Artbildning" },
              { id: "biologi-m-9-2-3", titel: "Naturvetenskap och andra sätt att förklara" },
              { id: "biologi-m-9-2-l", titel: "Labb: Modellförsök om urval" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-10",
        titel: "10. Hälsa och levnadsvanor",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-10-1",
            titel: "10.1 Stress, sömn och psykisk hälsa",
            ramverk: true,
            barn: [
              { id: "biologi-m-10-1-1", titel: "Stress i kroppen" },
              { id: "biologi-m-10-1-2", titel: "Sömn och motion" },
              { id: "biologi-m-10-1-3", titel: "Psykisk ohälsa och stöd" },
              { id: "biologi-m-10-1-l", titel: "Labb: Sömn och vanor: statistik" }
            ]
          },
          {
            id: "biologi-d-10-2",
            titel: "10.2 Beroendeframkallande medel",
            ramverk: true,
            barn: [
              { id: "biologi-m-10-2-1", titel: "Alkohol, tobak, nikotin och droger" },
              { id: "biologi-m-10-2-2", titel: "Hjärnan och beroende" },
              { id: "biologi-m-10-2-3", titel: "Förebyggande och stöd" },
              { id: "biologi-m-10-2-l", titel: "Labb: Läs och tolka statistik om tobak och alkohol" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-11",
        titel: "11. Pubertet, sexualitet och relationer",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-11-1",
            titel: "11.1 Pubertet, reproduktion, preventivmedel och STI",
            ramverk: true,
            barn: [
              { id: "biologi-m-11-1-1", titel: "Pubertet och könsorgan" },
              { id: "biologi-m-11-1-2", titel: "Befruktning och graviditet" },
              { id: "biologi-m-11-1-3", titel: "Preventivmedel och STI" },
              { id: "biologi-m-11-1-l", titel: "Labb: Faktagranska information om skydd" }
            ]
          },
          {
            id: "biologi-d-11-2",
            titel: "11.2 Relationer, identitet och samtycke",
            ramverk: true,
            barn: [
              { id: "biologi-m-11-2-1", titel: "Sexualitet och identitet" },
              { id: "biologi-m-11-2-2", titel: "Relationer, kärlek och ansvar" },
              { id: "biologi-m-11-2-3", titel: "Samtycke och gränser" },
              { id: "biologi-m-11-2-l", titel: "Labb: Samtycke – fallövning" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-12",
        titel: "12. Repetition inför nationella proven",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-12-1",
            titel: "12.1 Repetition inför nationella proven",
            ramverk: true,
            barn: [
              { id: "biologi-m-12-1-1", titel: "Röda trådar" },
              { id: "biologi-m-12-1-2", titel: "Planera och värdera en undersökning" },
              { id: "biologi-m-12-1-3", titel: "Argumentera i miljö- och hälsofrågor" },
              { id: "biologi-m-12-1-l", titel: "Labb: Provlik mini-undersökning" }
            ]
          }
        ]
      }
    ]
  },
  // BIOLOGI END
  // KEMI START (genereras av planering/amne_plan.py)
  {
    id: "kemi",
    titel: "Kemi (beta)",
    ikon: "🧪",
    ramverk: true,
    barn: [
      {
        id: "kemi-omrade-1",
        titel: "1. Kemi som vetenskap",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-1-1",
            titel: "1.1 Arbeta som kemist",
            ramverk: true,
            barn: [
              { id: "kemi-m-1-1-1", titel: "Säkerhet och utrustning i kemilabbet" },
              { id: "kemi-m-1-1-2", titel: "Från fråga till plan" },
              { id: "kemi-m-1-1-3", titel: "Dokumentera och värdera" },
              { id: "kemi-m-1-1-l", titel: "Labb: Hur påverkar temperaturen hur fort en brustablett löser sig?" }
            ]
          },
          {
            id: "kemi-d-1-2",
            titel: "1.2 Modeller, källor och argument",
            ramverk: true,
            barn: [
              { id: "kemi-m-1-2-1", titel: "Vad är en modell i kemi?" },
              { id: "kemi-m-1-2-2", titel: "Hur kemin vuxit fram" },
              { id: "kemi-m-1-2-3", titel: "Granska kemipåståenden" },
              { id: "kemi-m-1-2-l", titel: "Labb: Granska ett påstående: fungerar fläckborttagaren bättre?" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-2",
        titel: "2. Materia och partiklar",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-2-1",
            titel: "2.1 Ämnen, blandningar och partikelmodellen",
            ramverk: true,
            barn: [
              { id: "kemi-m-2-1-1", titel: "Ämnen och material" },
              { id: "kemi-m-2-1-2", titel: "Partikelmodellen" },
              { id: "kemi-m-2-1-3", titel: "Rena ämnen och blandningar" },
              { id: "kemi-m-2-1-l", titel: "Labb: Densitet och flyta eller sjunka" }
            ]
          },
          {
            id: "kemi-d-2-2",
            titel: "2.2 Separations- och analysmetoder",
            ramverk: true,
            barn: [
              { id: "kemi-m-2-2-1", titel: "Filtrering, avdunstning och sedimentering" },
              { id: "kemi-m-2-2-2", titel: "Destillation och kromatografi" },
              { id: "kemi-m-2-2-3", titel: "Identifiera ämnen och fällning" },
              { id: "kemi-m-2-2-l", titel: "Labb: Separera en blandning av sand, salt och vatten" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-3",
        titel: "3. Atomer och grundämnen",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-3-1",
            titel: "3.1 Atomens byggnad",
            ramverk: true,
            barn: [
              { id: "kemi-m-3-1-1", titel: "Atomen och dess partiklar" },
              { id: "kemi-m-3-1-2", titel: "Atommodellernas historia" },
              { id: "kemi-m-3-1-3", titel: "Isotoper och radioaktivitet i korthet" },
              { id: "kemi-m-3-1-l", titel: "Labb: Svarta lådan: modellera det du inte kan se" }
            ]
          },
          {
            id: "kemi-d-3-2",
            titel: "3.2 Periodiska systemet",
            ramverk: true,
            barn: [
              { id: "kemi-m-3-2-1", titel: "Grundämnen och periodiska systemet" },
              { id: "kemi-m-3-2-2", titel: "Grupper med släktskap" },
              { id: "kemi-m-3-2-3", titel: "Grundämnen i naturen och kroppen" },
              { id: "kemi-m-3-2-l", titel: "Labb: Metaller och icke-metaller: egenskaper" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-4",
        titel: "4. Kemiska föreningar och reaktioner",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-4-1",
            titel: "4.1 Molekyler och joner",
            ramverk: true,
            barn: [
              { id: "kemi-m-4-1-1", titel: "Molekyler och kovalent bindning" },
              { id: "kemi-m-4-1-2", titel: "Joner och jonföreningar" },
              { id: "kemi-m-4-1-3", titel: "Egenskaper hos föreningar" },
              { id: "kemi-m-4-1-l", titel: "Labb: Leder lösningar elektrisk ström?" }
            ]
          },
          {
            id: "kemi-d-4-2",
            titel: "4.2 Kemiska reaktioner",
            ramverk: true,
            barn: [
              { id: "kemi-m-4-2-1", titel: "Vad är en kemisk reaktion?" },
              { id: "kemi-m-4-2-2", titel: "Reaktionsformler och oförstörbarhet" },
              { id: "kemi-m-4-2-3", titel: "Hastighet och energi" },
              { id: "kemi-m-4-2-l", titel: "Labb: Massan bevaras: väg före och efter" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-5",
        titel: "5. Vatten, syror och baser",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-5-1",
            titel: "5.1 Vatten som lösningsmedel",
            ramverk: true,
            barn: [
              { id: "kemi-m-5-1-1", titel: "Vatten och lösningar" },
              { id: "kemi-m-5-1-2", titel: "Koncentration och löslighet" },
              { id: "kemi-m-5-1-3", titel: "Vatten som transportör" },
              { id: "kemi-m-5-1-l", titel: "Labb: Hur mycket salt löser sig i vatten vid olika temperaturer?" }
            ]
          },
          {
            id: "kemi-d-5-2",
            titel: "5.2 Syror, baser och pH",
            ramverk: true,
            barn: [
              { id: "kemi-m-5-2-1", titel: "Syror, baser och indikatorer" },
              { id: "kemi-m-5-2-2", titel: "pH-skalan och pH-mätning" },
              { id: "kemi-m-5-2-3", titel: "Neutralisation i naturen och samhället" },
              { id: "kemi-m-5-2-l", titel: "Labb: pH med rödkålsindikator" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-6",
        titel: "6. Kemi i naturen och miljön",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-6-1",
            titel: "6.1 Luft, växthuseffekt och klimat",
            ramverk: true,
            barn: [
              { id: "kemi-m-6-1-1", titel: "Luftens sammansättning" },
              { id: "kemi-m-6-1-2", titel: "Växthuseffekten och klimatet" },
              { id: "kemi-m-6-1-3", titel: "Förbränning, bränslen och åtgärder" },
              { id: "kemi-m-6-1-l", titel: "Labb: Modell av växthuseffekten" }
            ]
          },
          {
            id: "kemi-d-6-2",
            titel: "6.2 Vatten, mark och miljögifter",
            ramverk: true,
            barn: [
              { id: "kemi-m-6-2-1", titel: "Vattenrening och dricksvatten" },
              { id: "kemi-m-6-2-2", titel: "Näringsämnen och övergödning" },
              { id: "kemi-m-6-2-3", titel: "Miljögifter och spridning" },
              { id: "kemi-m-6-2-l", titel: "Labb: Rena smutsigt vatten" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-7",
        titel: "7. Kolföreningar och livets kemi",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-7-1",
            titel: "7.1 Kolatomen och kolets kretslopp",
            ramverk: true,
            barn: [
              { id: "kemi-m-7-1-1", titel: "Kolatomens egenskaper" },
              { id: "kemi-m-7-1-2", titel: "Kolväten och bränslen" },
              { id: "kemi-m-7-1-3", titel: "Kolets kretslopp" },
              { id: "kemi-m-7-1-l", titel: "Labb: Påvisa koldioxid i utandningsluft" }
            ]
          },
          {
            id: "kemi-d-7-2",
            titel: "7.2 Kolhydrater, proteiner och fetter",
            ramverk: true,
            barn: [
              { id: "kemi-m-7-2-1", titel: "Kolhydrater" },
              { id: "kemi-m-7-2-2", titel: "Proteiner och fetter" },
              { id: "kemi-m-7-2-3", titel: "Näring, energi och kostråd" },
              { id: "kemi-m-7-2-l", titel: "Labb: Påvisa näringsämnen i mat" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-8",
        titel: "8. Material, produkter och hållbarhet",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-8-1",
            titel: "8.1 Material och produktutveckling",
            ramverk: true,
            barn: [
              { id: "kemi-m-8-1-1", titel: "Metaller, plast och andra material" },
              { id: "kemi-m-8-1-2", titel: "Batterier och elektrokemi" },
              { id: "kemi-m-8-1-3", titel: "Läkemedel och funktionskläder" },
              { id: "kemi-m-8-1-l", titel: "Labb: Bygg ett batteri" }
            ]
          },
          {
            id: "kemi-d-8-2",
            titel: "8.2 Livscykler och ställningstagande",
            ramverk: true,
            barn: [
              { id: "kemi-m-8-2-1", titel: "En produkts livscykel" },
              { id: "kemi-m-8-2-2", titel: "Återvinning och cirkulär ekonomi" },
              { id: "kemi-m-8-2-3", titel: "Jämföra produkter och argumentera" },
              { id: "kemi-m-8-2-l", titel: "Labb: Sortera plast efter densitet" }
            ]
          }
        ]
      },
      {
        id: "kemi-omrade-9",
        titel: "9. Repetition inför nationella proven",
        ramverk: true,
        barn: [
          {
            id: "kemi-d-9-1",
            titel: "9.1 Materia, atomer och föreningar",
            ramverk: true,
            barn: [
              { id: "kemi-m-9-1-1", titel: "Partikelmodellen och separation: repetition" },
              { id: "kemi-m-9-1-2", titel: "Atomer och periodiska systemet: repetition" },
              { id: "kemi-m-9-1-3", titel: "Föreningar och reaktioner: repetition" }
            ]
          },
          {
            id: "kemi-d-9-2",
            titel: "9.2 Vatten, miljö och livets kemi",
            ramverk: true,
            barn: [
              { id: "kemi-m-9-2-1", titel: "Vatten, syror och baser: repetition" },
              { id: "kemi-m-9-2-2", titel: "Miljö och kretslopp: repetition" },
              { id: "kemi-m-9-2-3", titel: "Livets kemi: repetition" }
            ]
          },
          {
            id: "kemi-d-9-3",
            titel: "9.3 Undersökningar, källor och argument",
            ramverk: true,
            barn: [
              { id: "kemi-m-9-3-1", titel: "Planera och värdera undersökningar" },
              { id: "kemi-m-9-3-2", titel: "Granska information" },
              { id: "kemi-m-9-3-3", titel: "Resonera om miljö och hälsa: repetition" }
            ]
          }
        ]
      }
    ]
  },
  // KEMI END
  // FYSIK START (genereras av planering/amne_plan.py)
  {
    id: "fysik",
    titel: "Fysik (beta)",
    ikon: "⚡",
    ramverk: true,
    barn: [
      {
        id: "fysik-omrade-1",
        titel: "1. Fysik som vetenskap",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-1-1",
            titel: "1.1 Mäta och undersöka som fysiker",
            ramverk: true,
            barn: [
              { id: "fysik-m-1-1-1", titel: "Storheter, enheter och instrument" },
              { id: "fysik-m-1-1-2", titel: "Från fråga till plan" },
              { id: "fysik-m-1-1-3", titel: "Mätvärden, tabeller och diagram" },
              { id: "fysik-m-1-1-l", titel: "Labb: Hur påverkar snörets längd en pendels svängningstid?" }
            ]
          },
          {
            id: "fysik-d-1-2",
            titel: "1.2 Modeller, källor och argument",
            ramverk: true,
            barn: [
              { id: "fysik-m-1-2-1", titel: "Vad är en modell i fysik?" },
              { id: "fysik-m-1-2-2", titel: "Hur fysiken vuxit fram" },
              { id: "fysik-m-1-2-3", titel: "Granska fysikpåståenden" },
              { id: "fysik-m-1-2-l", titel: "Labb: Granska ett påstående: isolerar jackan som reklamen säger?" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-2",
        titel: "2. Materia, tryck och temperatur",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-2-1",
            titel: "2.1 Partikelmodellen och fasövergångar",
            ramverk: true,
            barn: [
              { id: "fysik-m-2-1-1", titel: "Partikelmodellen" },
              { id: "fysik-m-2-1-2", titel: "Fasövergångar" },
              { id: "fysik-m-2-1-3", titel: "Värme och temperatur" },
              { id: "fysik-m-2-1-l", titel: "Labb: Hur ändras temperaturen när is smälter?" }
            ]
          },
          {
            id: "fysik-d-2-2",
            titel: "2.2 Tryck, volym och densitet",
            ramverk: true,
            barn: [
              { id: "fysik-m-2-2-1", titel: "Tryck" },
              { id: "fysik-m-2-2-2", titel: "Densitet" },
              { id: "fysik-m-2-2-3", titel: "Gaser: tryck, volym och temperatur" },
              { id: "fysik-m-2-2-l", titel: "Labb: Bestäm densiteten hos olika material" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-3",
        titel: "3. Krafter och rörelse",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-3-1",
            titel: "3.1 Krafter och Newtons lagar",
            ramverk: true,
            barn: [
              { id: "fysik-m-3-1-1", titel: "Krafter och kraftmätning" },
              { id: "fysik-m-3-1-2", titel: "Resulterande kraft och jämvikt" },
              { id: "fysik-m-3-1-3", titel: "Newtons andra och tredje lag" },
              { id: "fysik-m-3-1-l", titel: "Labb: Hur påverkar underlaget friktionen?" }
            ]
          },
          {
            id: "fysik-d-3-2",
            titel: "3.2 Rörelse, hastighet och trafiksäkerhet",
            ramverk: true,
            barn: [
              { id: "fysik-m-3-2-1", titel: "Hastighet och acceleration" },
              { id: "fysik-m-3-2-2", titel: "Rörelseenergi och bromssträcka" },
              { id: "fysik-m-3-2-3", titel: "Trafiksäkerhet" },
              { id: "fysik-m-3-2-l", titel: "Labb: Mät hastigheten hos en rullande kula" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-4",
        titel: "4. Energi",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-4-1",
            titel: "4.1 Energiformer, flöde och oförstörbarhet",
            ramverk: true,
            barn: [
              { id: "fysik-m-4-1-1", titel: "Energiformer och energiomvandlingar" },
              { id: "fysik-m-4-1-2", titel: "Energins oförstörbarhet och verkningsgrad" },
              { id: "fysik-m-4-1-3", titel: "Energins kvalitet" },
              { id: "fysik-m-4-1-l", titel: "Labb: Studsbollen: vart tar energin vägen?" }
            ]
          },
          {
            id: "fysik-d-4-2",
            titel: "4.2 Energikällor, för- och nackdelar",
            ramverk: true,
            barn: [
              { id: "fysik-m-4-2-1", titel: "Energikällor i Sverige och världen" },
              { id: "fysik-m-4-2-2", titel: "För- och nackdelar för samhälle och miljö" },
              { id: "fysik-m-4-2-3", titel: "Energi, klimat och ställningstagande" },
              { id: "fysik-m-4-2-l", titel: "Labb: Hur påverkar solcellens vinkel elproduktionen?" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-5",
        titel: "5. Elektricitet och magnetism",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-5-1",
            titel: "5.1 Elektriska kretsar",
            ramverk: true,
            barn: [
              { id: "fysik-m-5-1-1", titel: "Strömkrets, ström och spänning" },
              { id: "fysik-m-5-1-2", titel: "Resistans och Ohms lag" },
              { id: "fysik-m-5-1-3", titel: "Seriekoppling och parallellkoppling" },
              { id: "fysik-m-5-1-l", titel: "Labb: Ström och spänning i serie och parallellt" }
            ]
          },
          {
            id: "fysik-d-5-2",
            titel: "5.2 Magnetism och elektromagnetism",
            ramverk: true,
            barn: [
              { id: "fysik-m-5-2-1", titel: "Magneter och magnetfält" },
              { id: "fysik-m-5-2-2", titel: "Elektromagnetism" },
              { id: "fysik-m-5-2-3", titel: "Elektricitet i samhället" },
              { id: "fysik-m-5-2-l", titel: "Labb: Bygg en elektromagnet" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-6",
        titel: "6. Ljud",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-6-1",
            titel: "6.1 Hur ljud uppstår och breder ut sig",
            ramverk: true,
            barn: [
              { id: "fysik-m-6-1-1", titel: "Vibrationer och ljudkällor" },
              { id: "fysik-m-6-1-2", titel: "Ljudets utbredning" },
              { id: "fysik-m-6-1-3", titel: "Eko och ljudisolering" },
              { id: "fysik-m-6-1-l", titel: "Labb: Hur snabbt går ljudet?" }
            ]
          },
          {
            id: "fysik-d-6-2",
            titel: "6.2 Tonhöjd, ljudstyrka och hörsel",
            ramverk: true,
            barn: [
              { id: "fysik-m-6-2-1", titel: "Frekvens och amplitud" },
              { id: "fysik-m-6-2-2", titel: "Hörsel och hörselskydd" },
              { id: "fysik-m-6-2-3", titel: "Registrera ljud" },
              { id: "fysik-m-6-2-l", titel: "Labb: Hur påverkar längden tonhöjden?" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-7",
        titel: "7. Ljus",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-7-1",
            titel: "7.1 Ljusets utbredning och reflektion",
            ramverk: true,
            barn: [
              { id: "fysik-m-7-1-1", titel: "Ljuskällor och ljusets utbredning" },
              { id: "fysik-m-7-1-2", titel: "Reflektion" },
              { id: "fysik-m-7-1-3", titel: "Färg och ytor" },
              { id: "fysik-m-7-1-l", titel: "Labb: Reflektion med ljuslåda" }
            ]
          },
          {
            id: "fysik-d-7-2",
            titel: "7.2 Brytning, linser och färger",
            ramverk: true,
            barn: [
              { id: "fysik-m-7-2-1", titel: "Brytning" },
              { id: "fysik-m-7-2-2", titel: "Linser och optiska instrument" },
              { id: "fysik-m-7-2-3", titel: "Färgspridning och spektrum" },
              { id: "fysik-m-7-2-l", titel: "Labb: Brytning i vatten" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-8",
        titel: "8. Strålning, väder och klimat",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-8-1",
            titel: "8.1 Strålning: användning och risker",
            ramverk: true,
            barn: [
              { id: "fysik-m-8-1-1", titel: "Elektromagnetisk strålning" },
              { id: "fysik-m-8-1-2", titel: "Partikelstrålning och radioaktivitet" },
              { id: "fysik-m-8-1-3", titel: "Användning och risker" },
              { id: "fysik-m-8-1-l", titel: "Labb: Vad stoppar UV-strålning?" }
            ]
          },
          {
            id: "fysik-d-8-2",
            titel: "8.2 Strålningsbalans, växthuseffekt och klimat",
            ramverk: true,
            barn: [
              { id: "fysik-m-8-2-1", titel: "Jordens strålningsbalans" },
              { id: "fysik-m-8-2-2", titel: "Växthuseffekten" },
              { id: "fysik-m-8-2-3", titel: "Klimatförändringar och ställningstagande" },
              { id: "fysik-m-8-2-l", titel: "Labb: Hur påverkar ytans färg uppvärmningen?" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-9",
        titel: "9. Universum",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-9-1",
            titel: "9.1 Universums uppkomst och uppbyggnad",
            ramverk: true,
            barn: [
              { id: "fysik-m-9-1-1", titel: "Solsystemet och gravitation" },
              { id: "fysik-m-9-1-2", titel: "Stjärnor och galaxer" },
              { id: "fysik-m-9-1-3", titel: "Big bang och universums utveckling" },
              { id: "fysik-m-9-1-l", titel: "Labb: Solsystemet i skala" }
            ]
          },
          {
            id: "fysik-d-9-2",
            titel: "9.2 Planeter och liv i andra solsystem",
            ramverk: true,
            barn: [
              { id: "fysik-m-9-2-1", titel: "Exoplaneter och hur vi hittar dem" },
              { id: "fysik-m-9-2-2", titel: "Livets villkor och beboeliga zonen" },
              { id: "fysik-m-9-2-3", titel: "Granska rymdnyheter" },
              { id: "fysik-m-9-2-l", titel: "Labb: Transitmetoden: hur upptäcks planeter?" }
            ]
          }
        ]
      },
      {
        id: "fysik-omrade-10",
        titel: "10. Repetition inför nationella proven",
        ramverk: true,
        barn: [
          {
            id: "fysik-d-10-1",
            titel: "10.1 Materia, energi och krafter",
            ramverk: true,
            barn: [
              { id: "fysik-m-10-1-1", titel: "Partikelmodell, tryck och densitet: repetition" },
              { id: "fysik-m-10-1-2", titel: "Energi och energikällor: repetition" },
              { id: "fysik-m-10-1-3", titel: "Krafter och rörelse: repetition" }
            ]
          },
          {
            id: "fysik-d-10-2",
            titel: "10.2 Elektricitet, ljus, ljud, strålning och universum",
            ramverk: true,
            barn: [
              { id: "fysik-m-10-2-1", titel: "Elektricitet och magnetism: repetition" },
              { id: "fysik-m-10-2-2", titel: "Ljus och ljud: repetition" },
              { id: "fysik-m-10-2-3", titel: "Strålning, klimat och universum: repetition" }
            ]
          },
          {
            id: "fysik-d-10-3",
            titel: "10.3 Undersökningar, källor och argument",
            ramverk: true,
            barn: [
              { id: "fysik-m-10-3-1", titel: "Planera och värdera undersökningar" },
              { id: "fysik-m-10-3-2", titel: "Granska källor" },
              { id: "fysik-m-10-3-3", titel: "Argumentera om energi, teknik och miljö" }
            ]
          }
        ]
      }
    ]
  },
  // FYSIK END
  // TEKNIK START (genereras av planering/amne_plan.py)
  {
    id: "teknik",
    titel: "Teknik (beta)",
    ikon: "⚙️",
    ramverk: true,
    barn: [
      {
        id: "teknik-omrade-1",
        titel: "1. Teknik och teknikutveckling",
        ramverk: true,
        barn: [
          {
            id: "teknik-d-1-1",
            titel: "1.1 Teknikutvecklingens faser",
            ramverk: true,
            barn: [
              { id: "teknik-m-1-1-1", titel: "Behov och problem" },
              { id: "teknik-m-1-1-2", titel: "Undersöka och föreslå lösningar" },
              { id: "teknik-m-1-1-3", titel: "Konstruera och pröva" },
              { id: "teknik-m-1-1-l", titel: "Praktiskt arbete: Prototyp: en lösning på ett vardagsproblem" }
            ]
          },
          {
            id: "teknik-d-1-2",
            titel: "1.2 Digitala verktyg och dokumentation",
            ramverk: true,
            barn: [
              { id: "teknik-m-1-2-1", titel: "Skisser och ritningar" },
              { id: "teknik-m-1-2-2", titel: "Digitala modeller och simulering" },
              { id: "teknik-m-1-2-3", titel: "Rapporten" },
              { id: "teknik-m-1-2-l", titel: "Praktiskt arbete: Rita och simulera en lösning i CAD" }
            ]
          }
        ]
      },
      {
        id: "teknik-omrade-2",
        titel: "2. Tekniska system och delsystem",
        ramverk: true,
        barn: [
          {
            id: "teknik-d-2-1",
            titel: "2.1 System, komponenter och delsystem",
            ramverk: true,
            barn: [
              { id: "teknik-m-2-1-1", titel: "Från komponent till system" },
              { id: "teknik-m-2-1-2", titel: "IKT-system" },
              { id: "teknik-m-2-1-3", titel: "Hur delarna samverkar" },
              { id: "teknik-m-2-1-l", titel: "Praktiskt arbete: Kartlägg ett system och rita en systemskiss" }
            ]
          },
          {
            id: "teknik-d-2-2",
            titel: "2.2 Transportsystem och samhällets system",
            ramverk: true,
            barn: [
              { id: "teknik-m-2-2-1", titel: "Transportsystem" },
              { id: "teknik-m-2-2-2", titel: "Kollektivtrafik och arkitektur" },
              { id: "teknik-m-2-2-3", titel: "Transport genom tiden" },
              { id: "teknik-m-2-2-l", titel: "Praktiskt arbete: Planera en ny busslinje eller hållplats" }
            ]
          }
        ]
      },
      {
        id: "teknik-omrade-3",
        titel: "3. Elektronik, styrning och reglering",
        ramverk: true,
        barn: [
          {
            id: "teknik-d-3-1",
            titel: "3.1 Elektronik och sensorer",
            ramverk: true,
            barn: [
              { id: "teknik-m-3-1-1", titel: "Elektronikkomponenter" },
              { id: "teknik-m-3-1-2", titel: "Sensorer" },
              { id: "teknik-m-3-1-3", titel: "Styrning och reglering" },
              { id: "teknik-m-3-1-l", titel: "Praktiskt arbete: Koppla en krets med sensor: nattlampa" }
            ]
          },
          {
            id: "teknik-d-3-2",
            titel: "3.2 Programmering och styrning",
            ramverk: true,
            barn: [
              { id: "teknik-m-3-2-1", titel: "Algoritmer och program" },
              { id: "teknik-m-3-2-2", titel: "Programmera en styrning" },
              { id: "teknik-m-3-2-3", titel: "Felsökning och förbättring" },
              { id: "teknik-m-3-2-l", titel: "Praktiskt arbete: Bygg en automatisk fläkt eller ett trafikljus" }
            ]
          }
        ]
      },
      {
        id: "teknik-omrade-4",
        titel: "4. Konstruktioner och material",
        ramverk: true,
        barn: [
          {
            id: "teknik-d-4-1",
            titel: "4.1 Hållfasta och stabila konstruktioner",
            ramverk: true,
            barn: [
              { id: "teknik-m-4-1-1", titel: "Krafter i konstruktioner" },
              { id: "teknik-m-4-1-2", titel: "Stabilitet och form" },
              { id: "teknik-m-4-1-3", titel: "Konstruktioner i samhället" },
              { id: "teknik-m-4-1-l", titel: "Praktiskt arbete: Bygg och belasta en bro av papper eller spagetti" }
            ]
          },
          {
            id: "teknik-d-4-2",
            titel: "4.2 Material och deras egenskaper",
            ramverk: true,
            barn: [
              { id: "teknik-m-4-2-1", titel: "Materialegenskaper" },
              { id: "teknik-m-4-2-2", titel: "Trä, metall, plast och kompositer" },
              { id: "teknik-m-4-2-3", titel: "Materialval och hållbarhet" },
              { id: "teknik-m-4-2-l", titel: "Praktiskt arbete: Testa materialets styrka" }
            ]
          }
        ]
      },
      {
        id: "teknik-omrade-5",
        titel: "5. Från råvara till produkt",
        ramverk: true,
        barn: [
          {
            id: "teknik-d-5-1",
            titel: "5.1 Tillverkning och industriella processer",
            ramverk: true,
            barn: [
              { id: "teknik-m-5-1-1", titel: "Processkedjan" },
              { id: "teknik-m-5-1-2", titel: "Förpackningar" },
              { id: "teknik-m-5-1-3", titel: "Automation och kvalitetskontroll" },
              { id: "teknik-m-5-1-l", titel: "Praktiskt arbete: Följ en produkt från råvara till färdig vara" }
            ]
          },
          {
            id: "teknik-d-5-2",
            titel: "5.2 Avfall, återvinning och hållbarhet",
            ramverk: true,
            barn: [
              { id: "teknik-m-5-2-1", titel: "Avfall i processen" },
              { id: "teknik-m-5-2-2", titel: "Återvinning och cirkulär ekonomi" },
              { id: "teknik-m-5-2-3", titel: "Livscykel" },
              { id: "teknik-m-5-2-l", titel: "Praktiskt arbete: Sortera och väg: hur mycket avfall skapar vi?" }
            ]
          }
        ]
      },
      {
        id: "teknik-omrade-6",
        titel: "6. Internet och globala tekniska system",
        ramverk: true,
        barn: [
          {
            id: "teknik-d-6-1",
            titel: "6.1 Internet och globala system",
            ramverk: true,
            barn: [
              { id: "teknik-m-6-1-1", titel: "Hur Internet fungerar" },
              { id: "teknik-m-6-1-2", titel: "Fördelar och begränsningar" },
              { id: "teknik-m-6-1-3", titel: "Andra globala system" },
              { id: "teknik-m-6-1-l", titel: "Praktiskt arbete: Kartlägg vägen från din mobil till en server" }
            ]
          },
          {
            id: "teknik-d-6-2",
            titel: "6.2 Säkerhet, data och risker",
            ramverk: true,
            barn: [
              { id: "teknik-m-6-2-1", titel: "Lösenord och kontosäkerhet" },
              { id: "teknik-m-6-2-2", titel: "Lagring av data och integritet" },
              { id: "teknik-m-6-2-3", titel: "Risker och ansvar" },
              { id: "teknik-m-6-2-l", titel: "Praktiskt arbete: Granska en apps behörigheter och datainsamling" }
            ]
          }
        ]
      },
      {
        id: "teknik-omrade-7",
        titel: "7. Teknik, samhälle och framtid",
        ramverk: true,
        barn: [
          {
            id: "teknik-d-7-1",
            titel: "7.1 Teknik och vetenskap",
            ramverk: true,
            barn: [
              { id: "teknik-m-7-1-1", titel: "Teknik möjliggör vetenskap" },
              { id: "teknik-m-7-1-2", titel: "Vetenskap möjliggör teknik" },
              { id: "teknik-m-7-1-3", titel: "Teknikhistoria i vändpunkter" },
              { id: "teknik-m-7-1-l", titel: "Praktiskt arbete: Bygg ett vattendroppsmikroskop" }
            ]
          },
          {
            id: "teknik-d-7-2",
            titel: "7.2 Teknikval, hållbar utveckling och yrken",
            ramverk: true,
            barn: [
              { id: "teknik-m-7-2-1", titel: "Hållbar utveckling i teknikval" },
              { id: "teknik-m-7-2-2", titel: "Teknikval i praktiken" },
              { id: "teknik-m-7-2-3", titel: "Föreställningar om teknik och yrkesval" },
              { id: "teknik-m-7-2-l", titel: "Praktiskt arbete: Konsekvensanalys: vilket teknikval är mest hållbart?" }
            ]
          }
        ]
      }
    ]
  },
  // TEKNIK END
  {
    id: "historia",
    titel: "Historia (beta)",
    ikon: "🏛️",
    barn: [
      {
        id: "historia-hogkulturer",
        titel: "Kapitel 2 – Högkulturer",
        barn: [
          { id: "historia-hogkulturer-vad-ar-hogkultur", titel: "Vad är en högkultur?" },
          { id: "historia-hogkulturer-mesopotamien-egypten", titel: "Mesopotamien och Egypten" },
          { id: "historia-hogkulturer-indus-kina", titel: "Indusdalen och Kina" },
          { id: "historia-hogkulturer-amerika", titel: "Högkulturer i Amerika" },
          { id: "historia-hogkulturer-tidsresa", titel: "Tidsresa (spel)" }
        ]
      }
    ]
  },
  {
    id: "bild",
    titel: "Bild",
    ikon: "🎨",
    barn: []
  },
  {
    id: "engelska",
    titel: "Engelska",
    ikon: "🇬🇧",
    barn: []
  },
  {
    id: "geografi",
    titel: "Geografi",
    ikon: "🌍",
    barn: []
  },
  {
    id: "hem-konsumentkunskap",
    titel: "Hem- och konsumentkunskap",
    ikon: "🍳",
    barn: []
  },
  {
    id: "idrott-halsa",
    titel: "Idrott och hälsa",
    ikon: "🏃",
    barn: []
  },
  {
    id: "moderna-sprak",
    titel: "Moderna språk",
    ikon: "🗣️",
    barn: []
  },
  {
    id: "musik",
    titel: "Musik",
    ikon: "🎵",
    barn: []
  },
  {
    id: "religionskunskap",
    titel: "Religionskunskap",
    ikon: "🕊️",
    barn: []
  },
  {
    id: "samhallskunskap",
    titel: "Samhällskunskap",
    ikon: "🗳️",
    barn: []
  },
  {
    id: "slojd",
    titel: "Slöjd",
    ikon: "🧵",
    barn: [
      { id: "slojd-textil", titel: "Textilslöjd" },
      { id: "slojd-tra-metall", titel: "Trä- och metallslöjd" }
    ]
  },
  {
    id: "svenska",
    titel: "Svenska",
    ikon: "📖",
    barn: []
  }
];

