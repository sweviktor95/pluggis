# -*- coding: utf-8 -*-
"""Kapitel 4 Ekologi – lättläst version (innehåll)."""
FIG = '/tmp/bio/fig/'
NDEL = 8
UNDER = "Vem äter vem – och hur allt hänger ihop"
INTRO_L = ["I naturen påverkar alla varandra.",
           "I det här kapitlet lär du dig hur energi och näring går runt i naturen – och hur människan påverkar."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs en del i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje del.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Vad ekologi är", "Producenter, konsumenter och nedbrytare", "Näringskedjor och näringsvävar", "Hur energin och ämnena går runt", "Hur människan påverkar naturen", "Hur vi kan ta hand om naturen"]

ORD_FIG = FIG + "l_ord.png"
ORD_EXTRA = [("Invasiv art", "En art som människan har tagit med sig till en ny plats. Den skadar de arter som redan finns där."),
             ("Hållbart", "Att ta lagom, så att det finns kvar även i framtiden."),
             ("Naturbruk", "Att använda naturen för mat och virke."),
             ("Allemansrätten", "Alla får vara i naturen. Regeln är: inte störa, inte förstöra.")]

# Varje del: titel, före-figur-stycken, figur (filnamn eller None), efter-stycken, kom ihåg, öva
DELAR = [
 dict(titel="Vad är ekologi?",
  fore=["<strong>Ekologi</strong> handlar om hur allt i naturen påverkar varandra.", "I naturen finns det levande och icke-levande saker."],
  fig="l_levande.png",
  efter=["<strong>Levande:</strong> växter, djur, svampar och bakterier.", "<strong>Icke-levande:</strong> solljus, vatten, temperatur, luft och jord.",
         "Alla levande saker behöver de icke-levande.", "Växter behöver till exempel ljus och vatten för att växa.",
         "Allt tillsammans på en plats kallas ett <strong>ekosystem</strong>. En sjö och en skog är ekosystem."],
  kom="Ekologi handlar om hur levande och icke-levande saker påverkar varandra.",
  ova=[("sortera", "Är det levande eller icke-levande? Skriv L eller I i rutan.", ["Gran", "Solljus", "Hare", "Vatten", "Svamp", "Sten"]),
       ("ringa", "Vad behöver växter för att växa?", ["Ljus och vatten", "Bara mörker", "Sten"]),
       ("fyll", ["ekosystem", "ekologi", "icke-levande"], ["Läran om hur allt i naturen påverkar varandra kallas ______________.", "Temperatur är ______________.", "En sjö är ett ______________."]),
       ("skriv", "Vad behöver du själv från naturen för att leva? Skriv två saker.", "Jag behöver", 2)]),
 dict(titel="Vem gör vad i naturen?",
  fore=["Alla levande saker har ett jobb i ekosystemet.", "Det finns tre grupper:"],
  fig="l_tre.png",
  efter=["Djur som äter växter kallas <strong>växtätare</strong>. Haren är en växtätare.", "Djur som äter andra djur kallas <strong>rovdjur</strong>. Räven är ett rovdjur.", "Utan nedbrytare skulle döda löv och djur ligga kvar överallt!"],
  kom="Producenter gör mat. Konsumenter äter. Nedbrytare bryter ner det döda.",
  ova=[("streck", "Vilken grupp hör de till? Dra streck.", ["Blåbär", "Räv", "Svamp"], ["nedbrytare", "producent", "konsument"]),
       ("ringa", "Hur får producenter sin mat?", ["De gör den med solljus", "De äter djur", "De äter döda löv"]),
       ("sf", "Kryssa i rätt ruta.", ["Haren är ett rovdjur.", "Svampar kan vara nedbrytare.", "Alla djur är konsumenter."]),
       ("skriv", "Vad skulle hända om det inte fanns några nedbrytare?", "Om det inte fanns nedbrytare", 2)]),
 dict(titel="Vem äter vem?",
  fore=["En <strong>näringskedja</strong> visar vem som äter vem.", "Pilen pekar mot den som äter."],
  fig="l_kedja.png",
  efter=["I naturen äter de flesta djur flera olika saker.", "Då blir det många kedjor som hänger ihop. Det kallas en <strong>näringsväv</strong>."],
  fig2="l_vav.png",
  kom="En näringskedja visar vem som äter vem. Många kedjor tillsammans blir en näringsväv.",
  ova=[("siffror", "Sätt näringskedjan i rätt ordning. Skriv 1, 2, 3 och 4.", ["Gädda", "Växtplankton", "Djurplankton", "Abborre"]),
       ("ringa", "Titta på näringsväven. Vad äter räven?", ["Gräs och blåbär", "Hare och sork", "Örn"]),
       ("ringa", "Alla sorkar försvinner. Vad händer med räven?", ["Räven får mindre mat", "Räven får mer mat", "Inget händer"]),
       ("skriv3", "Gör en egen näringskedja med tre steg. Skriv namnen.")]),
 dict(titel="Energin minskar",
  fore=["Nästan allt liv får sin energi från <strong>solen</strong>.", "Växterna fångar solljuset. Sedan går energin vidare när någon äter."],
  fig="l_pyramid.png",
  efter=["Men det mesta av energin försvinner på vägen.", "Djuren använder energin till att röra sig och hålla sig varma. Den blir till värme.", "Bara en liten del går vidare till nästa djur.", "Därför finns det mest energi hos växterna och minst hos rovdjuren. Energin räcker bara till några få rovdjur."],
  kom="Energin kommer från solen. Den minskar för varje steg i näringskedjan.",
  ova=[("ringa", "Varifrån kommer energin från början?", ["Solen", "Jorden", "Rävarna"]),
       ("ringa", "Vilken grupp har mest energi?", ["Växterna", "Växtätarna", "Rovdjuren"]),
       ("fyll", ["värme", "solljuset", "mindre"], ["Växterna fångar ______________.", "Det mesta av energin blir till ______________.", "För varje steg i kedjan blir det ______________ energi kvar."]),
       ("skriv", "Varför finns det så få rovdjur i en skog?", "Det finns få rovdjur eftersom", 2)]),
 dict(titel="Allt går runt",
  fore=["Energin försvinner. Men <strong>ämnena</strong> försvinner inte.", "Samma ämnen används om och om igen. Det kallas ett <strong>kretslopp</strong>."],
  fig="l_kretslopp.png",
  efter=["Växterna tar upp näring från jorden.", "Djuren äter växterna. Sedan dör växter och djur.", "Nedbrytarna gör om det döda till ny näring i jorden.", "Kolet går också runt. Växter tar in koldioxid. Djur och växter släpper ut koldioxid när de gör cellandning."],
  kom="Ämnen går runt i ett kretslopp. Nedbrytarna gör det döda till ny näring.",
  ova=[("siffror", "Sätt kretsloppet i rätt ordning. Börja med växten. Skriv 1, 2, 3 och 4.", ["Djuret dör", "Växten tar upp näring", "Nedbrytare gör näring", "Ett djur äter växten"]),
       ("sf", "Kryssa i rätt ruta.", ["Ämnen kan användas igen.", "Nedbrytare gör ny näring.", "Växter släpper ut koldioxid när de gör cellandning."]),
       ("fyll", ["kretslopp", "koldioxid", "näring"], ["Växter tar in ______________ från luften.", "Nedbrytarna gör ny ______________ i jorden.", "Ämnen som går runt och runt är ett ______________."]),
       ("skriv", "Ett löv faller i skogen på hösten. Vad händer med lövet sedan?", "Lövet", 2)]),
 dict(titel="Människan påverkar",
  fore=["Människor påverkar ekosystemen. Här är två exempel."],
  sub1=("Miljögifter", ["Gifter kan hamna i vattnet. Djuren får i sig giftet när de äter.", "Giftet blir kvar i kroppen. Därför får djuren högst upp mest gift."], "l_gift.png"),
  sub2=("Övergödning", ["För mycket gödsel rinner ut i sjöar och hav. Då växer algerna för mycket.", "När algerna dör bryts de ner av nedbrytare. Nedbrytarna använder syret i vattnet. Då tar syret slut och fiskarna dör."], "l_overgodning.png"),
  kom="Gifter samlas högst upp i näringskedjan. För mycket gödsel ger syrebrist i vattnet.",
  ova=[("ringa", "Vem får mest gift i kroppen?", ["Havsörnen", "Fisken", "Planktonet"]),
       ("siffror", "Sätt övergödningen i rätt ordning. Skriv 1, 2 och 3.", ["Syret tar slut", "Alger växer för mycket", "Gödsel rinner ut"]),
       ("fyll", ["syre", "gödsel", "gift"], ["Fiskar dör när det inte finns ______________.", "Alger växer av ______________.", "Djur högst upp får mest ______________."]),
       ("skriv", "Vad kan vi människor göra för att sjöar och hav ska må bättre?", "Vi kan", 2)]),
 dict(titel="Fler hot mot naturen",
  fore=["Människan påverkar naturen på fler sätt."],
  fig="l_hot.png",
  efter=["<strong>Klimatet blir varmare.</strong> När vi bränner olja och kol släpps koldioxid ut. Då blir jorden varmare. Många djur och växter flyttar norrut eller upp på fjället. Isen smälter.",
         "<strong>Livsmiljöer försvinner.</strong> Djur och växter behöver en plats att bo på. När skog blir åker eller hus försvinner platsen.",
         "<strong>Nya arter kommer.</strong> Ibland tar människor med sig en art till en ny plats. Signalkräftan är ett exempel. Den bär på en sjukdom som dödar flodkräftan. En sådan art kallas <strong>invasiv art</strong>."],
  kom="Klimatet blir varmare, livsmiljöer försvinner och invasiva arter sprids.",
  ova=[("ringa", "Vad släpper vi ut när vi bränner olja och kol?", ["Koldioxid", "Syre", "Vatten"]),
       ("streck", "Dra streck till rätt förklaring.", ["Varmare klimat", "Livsmiljö försvinner", "Invasiv art"], ["en ny art som skadar de som redan finns", "arter flyttar norrut", "djur och växter får ingen plats att bo på"]),
       ("sf", "Kryssa i rätt ruta.", ["Alla nya arter är invasiva.", "Invasiva arter har ofta inga naturliga fiender.", "Jorden blir varmare när vi släpper ut mycket koldioxid."]),
       ("skriv", "Vad kan du göra för att inte sprida invasiva arter?", "Jag kan", 2)]),
 dict(titel="Ta hand om naturen",
  fore=["Vi använder naturen. Vi får virke från skogen, mat från åkern och fisk från havet. Det kallas <strong>naturbruk</strong>."],
  fig="l_lagom.png",
  efter=["Om vi tar för mycket tar det slut. Fiskarna kan bli för få. Det kallas <strong>överfiske</strong>.", "<strong>Hållbart</strong> betyder att vi tar lagom. Då finns det kvar även för dem som kommer efter oss.",
         "I Sverige har alla rätt att vara i naturen. Det kallas <strong>allemansrätten</strong>. Regeln är: <strong>inte störa, inte förstöra</strong>.",
         "Naturen hjälper oss också. Bin pollinerar blommor, och skogen renar vatten och luft. Det kallas <strong>ekosystemtjänster</strong>."],
  kom="Hållbart betyder att vi tar lagom. Allemansrätten: inte störa, inte förstöra.",
  ova=[("fyll", ["hållbart", "överfiske", "naturbruk"], ["Att använda naturen för mat och virke kallas ______________.", "När man fiskar för mycket kallas det ______________.", "Att ta lagom så att det finns kvar kallas ______________."]),
       ("sf", "Kryssa i rätt ruta.", ["Allemansrätten betyder att man får skräpa ner.", "Man får plocka bär i skogen.", "Bin hjälper till att pollinera blommor."]),
       ("ringa", "Vad är regeln i allemansrätten?", ["Inte störa, inte förstöra", "Ta så mycket du vill", "Bara på egen mark"]),
       ("skriv", "Vad kan du göra för att ta hand om naturen?", "Jag kan", 2)]),
]

VIKTIGAST = [("l_ic1.png", "Ekologi handlar om hur allt i naturen påverkar varandra."),
             ("l_ic2.png", "Producenter gör mat. Konsumenter äter. Nedbrytare bryter ner."),
             ("l_ic3.png", "En näringskedja visar vem som äter vem. Många kedjor blir en näringsväv."),
             ("l_ic4.png", "Energin kommer från solen och minskar för varje steg."),
             ("l_ic5.png", "Ämnen går runt i ett kretslopp."),
             ("l_ic6.png", "Människan påverkar: miljögifter, övergödning, klimat, nya arter och att livsmiljöer försvinner."),
             (None, "Vi ska ta hand om naturen: hållbart, lagom, inte störa – inte förstöra.")]

TEST = [("ringa", "Vilken är en producent?", ["Gran", "Räv", "Svamp"]),
        ("streck", "Dra streck till rätt förklaring.", ["Konsument", "Nedbrytare", "Näringsväv", "Kretslopp"], ["ämnen som går runt", "många kedjor som hänger ihop", "bryter ner det döda", "äter andra för att få energi"]),
        ("sf", "Kryssa i rätt ruta.", ["Nästan all energi kommer från början från solen.", "Det finns fler rovdjur än växter.", "Pilen i en näringskedja pekar mot den som äter.", "Övergödning ger mer syre i vattnet.", "Alla nya arter är invasiva.", "Allemansrätten betyder inte störa, inte förstöra."]),
        ("rita", "Rita en näringskedja från skogen med tre eller fyra steg. Skriv namnen och rita pilar."),
        ("skriv2", "Många harar blir sjuka och dör. Vad händer med gräset? Vad händer med räven?", ["Gräset", "Räven"]),
        ("skriv", "Varför är nedbrytarna viktiga för växterna?", "Nedbrytarna är viktiga eftersom", 2),
        ("ringa", "Vad betyder hållbart?", ["Vi tar lagom så att det finns kvar", "Vi tar allt vi kan", "Vi slutar använda naturen"])]

TILL_LARAREN = ("Den här versionen täcker samma centrala innehåll som kapitel 4 i grundboken – ekosystem, producenter, konsumenter och nedbrytare, näringskedjor och näringsvävar, energiflöde, kretslopp, "
                "människans påverkan (miljögifter, övergödning, klimat, förlorade livsmiljöer och invasiva arter) och hållbart naturbruk – men med anpassad text och bildstöd. Den passar elever med läs- och skrivsvårigheter, "
                "elever med annat modersmål och elever som lätt blir överväldigade av mycket text.")
TILL_PUNKTER = ["Korta meningar – oftast en tanke per rad.", "Bildstöd till nästan varje stycke, och viktiga ord med bild på sidan 2.",
                "8 korta delar med en förloppsindikator, så att eleven ser hur långt den har kommit.", "Kom ihåg-rutor med det viktigaste i en mening.",
                "Varierade övningar direkt efter varje del: ringa in, dra streck, fyll i med ordbank, sant/falskt och skriv med meningsstart."]
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt."
FACIT = [
 "<b>Del 1:</b> 1) Gran L, Solljus I, Hare L, Vatten I, Svamp L, Sten I. 2) Ljus och vatten. 3) ekologi, icke-levande, ekosystem. 4) T.ex. mat, vatten, luft/syre.",
 "<b>Del 2:</b> 1) Blåbär – producent; Räv – konsument; Svamp – nedbrytare. 2) De gör den med solljus. 3) Falskt, sant, sant. 4) Döda växter och djur skulle bli liggande och växterna skulle inte få ny näring.",
 "<b>Del 3:</b> 1) Gädda 4, Växtplankton 1, Abborre 3, Djurplankton 2. 2) Hare och sork. 3) Räven får mindre mat. 4) T.ex. gräs → hare → räv.",
 "<b>Del 4:</b> 1) Solen. 2) Växterna. 3) solljuset, värme, mindre. 4) Energin minskar i varje steg, så det räcker bara till några få rovdjur.",
 "<b>Del 5:</b> 1) Djuret dör 3, Växten tar upp näring 1, Nedbrytare gör näring 4, Ett djur äter växten 2. 2) Sant, sant, sant. 3) koldioxid, näring, kretslopp. 4) Det bryts ner av nedbrytare och blir ny näring i jorden.",
 "<b>Del 6:</b> 1) Havsörnen. 2) Syret tar slut 3, Gödsel rinner ut 1, Alger växer för mycket 2. 3) syre, gödsel, gift. 4) T.ex. gödsla mindre, rena avloppsvatten, inte släppa ut gifter.",
 "<b>Del 7:</b> 1) Koldioxid. 2) Varmare klimat – arter flyttar norrut; Livsmiljö försvinner – djur och växter får ingen plats att bo på; Invasiv art – en ny art som skadar de som redan finns. 3) Falskt, sant, sant. 4) T.ex. inte släppa ut akvariedjur eller husdjur i naturen, inte dumpa trädgårdsavfall i skogen.",
 "<b>Del 8:</b> 1) naturbruk, överfiske, hållbart. 2) Falskt, sant, sant. 3) Inte störa, inte förstöra. 4) T.ex. inte skräpa ner, slänga mindre mat, åka kollektivt.",
 "<b>Testa dig:</b> 1) Gran. 2) Konsument – äter andra för att få energi; Nedbrytare – bryter ner det döda; Näringsväv – många kedjor som hänger ihop; Kretslopp – ämnen som går runt. 3) Sant, falskt, sant, falskt, falskt, sant. 4) T.ex. gräs → hare → räv, gran → ekorre → mård eller blad → fjärilslarv → mes → sparvhök (pilar mot den som äter). 5) Gräset växer mer, räven får mindre mat och kan bli färre. 6) De gör döda växter och djur till ny näring som växterna tar upp. 7) Vi tar lagom så att det finns kvar.",
]
