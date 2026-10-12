# -*- coding: utf-8 -*-
"""Kapitel 1 Biologi som vetenskap – lättläst version."""
FIG = '/tmp/bio/fig01/'
NR = 1
SLUG = "vetenskap"
TAB = "1"
NAMN = "Biologi som vetenskap"
NDEL = 6
UNDER = "Hur vet vi det vi vet om livet?"
INTRO_L = ["I det här kapitlet lär du dig hur forskare tar reda på saker.",
           "Du får också lära dig att göra egna undersökningar – och att inte tro på allt du läser."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs en del i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje del.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Vad biologi är", "Hur forskare arbetar", "Hur man gör en rättvis undersökning", "Hur man arbetar säkert i labbet", "Hur man vet om något är sant"]
ORD_FIG = FIG + "l_ord.png"
ORD_EXTRA = []

DELAR = [
 dict(titel="Vad är biologi?",
  fore=["Biologi är läran om allt som lever.", "Biologer forskar om djur, växter, svampar och mycket små organismer.", "De forskar också om människans kropp.", "Det finns många sorters biologer. Här är fyra:"],
  fig="l_yrken.png",
  efter=["Biologer arbetar ute i naturen eller inne i ett labb.", "Många biologer hjälper till att skydda naturen eller att göra nya mediciner."],
  kom="Biologi är läran om allt som lever. Det finns många olika sorters biologer.",
  ova=[("ringa", "Vad är biologi?", ["Läran om allt som lever", "Läran om stenar", "Läran om siffror"]),
       ("streck", "Vad forskar biologerna om? Dra streck.", ["Zoolog", "Botaniker", "Marinbiolog", "Mikrobiolog"], ["växter", "små organismer, som bakterier", "djur", "livet i havet"]),
       ("fyll", ["labb", "naturen", "kropp"], ["Biologer kan arbeta ute i ______________.", "Biologer kan också arbeta inne i ett ______________.", "Biologer forskar också om människans ______________."]),
       ("skriv", "Vilken sorts biolog skulle du vilja vara? Varför?", "Jag skulle vilja vara", 2)]),
 dict(titel="Så tar forskare reda på saker",
  fore=["Forskare arbetar i steg. Stegen går runt i en cirkel."],
  fig="l_cykel.png",
  efter=["<strong>1. Fråga.</strong> Forskaren undrar över något.", "<strong>2. Gissa.</strong> Forskaren gissar vad svaret är och förklarar varför. Det kallas en <strong>hypotes</strong>.",
         "<strong>3. Testa.</strong> Forskaren gör en undersökning.", "<strong>4. Svara.</strong> Forskaren drar en <strong>slutsats</strong>. Ofta får man en ny fråga.",
         "Andra forskare kontrollerar arbetet. Då blir kunskapen säkrare."],
  kom="Forskare frågar, gissar, testar och svarar. Andra forskare kontrollerar.",
  ova=[("siffror", "Sätt stegen i rätt ordning. Skriv 1, 2, 3 och 4.", ["Testa", "Fråga", "Svara", "Gissa"]),
       ("ringa", "Vad är en hypotes?", ["Det man tror blir svaret, och varför", "Ett djur", "Ett svar som alltid är rätt"]),
       ("sf", "Kryssa i rätt ruta.", ["Andra forskare kontrollerar arbetet.", "En slutsats är det man har lärt sig.", "Forskare gissar och testar aldrig."]),
       ("skriv", "Skriv en egen hypotes. Till exempel om växter eller djur.", "Jag tror att", 2)]),
 dict(titel="Ett rättvist test",
  fore=["Ella undrar: <em>Växer krasse bättre i ljus eller i mörker?</em>", "Hennes hypotes är: <em>Krassen blir högst i ljus, eftersom växter behöver ljus.</em>", "Hon gör ett test med två lådor krasse."],
  fig="l_krasse.png",
  efter=["Låda A står i ljus. Låda B står i mörker.", "Ella ändrar bara en sak: ljuset.", "Allt annat är lika: samma jord, samma vatten och lika många frön.", "Då blir testet <strong>rättvist</strong>."],
  kom="I ett rättvist test ändrar man bara en sak. Allt annat är lika.",
  ova=[("ringa", "Vilken sak ändrar Ella i testet?", ["Ljuset", "Jorden", "Vattnet"]),
       ("kryssa", "Vad ska vara lika i båda lådorna? Kryssa i rätt rutor.", ["Samma jord", "Lika mycket vatten", "Samma ljus", "Lika många frön"]),
       ("fyll", ["rättvist", "en", "mörker"], ["Låda B står i ______________.", "Man ska bara ändra ______________ sak.", "Då blir testet ______________."]),
       ("skriv", "Varför ska man bara ändra en sak i ett test?", "Man ska bara ändra en sak eftersom", 2)]),
 dict(titel="Resultat och slutsats",
  fore=["Ella mäter krassen varje dag i en vecka.", "Det hon mäter kallas <strong>resultat</strong>."],
  fig="l_stapel.png",
  efter=["Krassen i mörker blev högst!", "Men den var gul och tunn.", "Krassen i ljus var grön och stark.",
         "<strong>Ellas slutsats:</strong> Krassen blir högre i mörker. Den växer på höjden för att leta efter ljus. Men den mår bäst i ljus.",
         "Hypotesen var alltså fel. Det gör inget! Man lär sig ändå.", "Det är bra att göra testet flera gånger. Då blir resultatet säkrare."],
  kom="Resultatet är det man mäter. Slutsatsen är det man lär sig.",
  ova=[("ringa", "Titta på stapeldiagrammet. Vilken krasse blev högst?", ["Krassen i ljus", "Krassen i mörker"]),
       ("streck", "Dra streck till rätt förklaring.", ["Resultat", "Slutsats", "Hypotes"], ["det man lär sig", "det man tror blir svaret, och varför", "det man mäter eller ser"]),
       ("sf", "Kryssa i rätt ruta.", ["Krassen i ljus var grön och stark.", "Det är dåligt om hypotesen var fel.", "Det är bra att göra testet flera gånger."]),
       ("skriv", "Varför är det bra att göra ett test flera gånger?", "Det är bra eftersom", 2)]),
 dict(titel="I labbet",
  fore=["I labbet gör man undersökningar. Då måste man arbeta säkert."],
  fig="l_sakerhet.png",
  efter=["<h3>Mikroskopet</h3>", "Mikroskopet gör små saker mycket större. Då kan man se celler.",
         "Lägg glaset på objektbordet. Börja med minsta förstoringen. Titta i okularet och vrid på skruven tills bilden blir skarp."],
  fig2="l_mikroskop.png",
  kom="Arbeta säkert i labbet. Mikroskopet gör små saker större.",
  ova=[("kryssa", "Vad ska du göra i labbet? Kryssa i rätt rutor.", ["Ha skyddsglasögon", "Springa runt", "Äta godis", "Fråga om jag är osäker", "Sätta upp långt hår", "Smaka på saker"]),
       ("streck", "Vad gör delarna på mikroskopet?", ["Okular", "Objektbord", "Skruv"], ["gör bilden skarp", "här tittar du", "här ligger glaset"]),
       ("ringa", "Vad kan man se med ett mikroskop?", ["Celler", "Stjärnor", "Berg"]),
       ("skriv", "Varför ska man ha skyddsglasögon i labbet?", "Man ska ha skyddsglasögon eftersom", 2)]),
 dict(titel="Sant eller påhitt?",
  fore=["På nätet står det mycket om hälsa och natur.", "Allt är inte sant.", "Ibland låter något som vetenskap, men det finns inga bevis. Det kallas <strong>pseudovetenskap</strong>."],
  fig="l_telefon.png", figw="30%",
  efter=["Den här reklamen lovar för mycket. Den vill bara sälja.", "<h3>Fyra frågor att ställa</h3>"],
  fig2="l_fyra.png",
  kom="Tro inte på allt du läser. Kolla vem, varför, när – och om fler säger samma sak.",
  ova=[("ringa", "Reklamen säger: ”Superbär botar ALLT på en dag!” Vad tror du?", ["Det är sant", "Det är nog inte sant"]),
       ("streck", "Vilken fråga passar? Dra streck.", ["Vem?", "Varför?", "När?", "Fler källor?"], ["Står det på fler ställen?", "Vem har skrivit texten?", "Vill de sälja något?", "Är texten gammal?"]),
       ("fyll", ["bevis", "sälja", "källor"], ["Pseudovetenskap har inga ______________.", "Reklam vill ofta ______________ något.", "Kolla om fler ______________ säger samma sak."]),
       ("skriv2", "Var brukar du läsa om natur eller hälsa? Hur vet du att det är sant?", ["Jag läser på", "Jag vet att det är sant eftersom"])]),
]
VIKTIGAST = [("l_ic1.png", "Biologi är läran om allt som lever."), ("l_ic2.png", "Forskare frågar, gissar (hypotes), testar och svarar (slutsats)."),
             ("l_ic3.png", "I ett rättvist test ändrar man bara en sak."), ("l_ic4.png", "Resultatet är det man mäter. Slutsatsen är det man lär sig."),
             ("l_ic5.png", "Arbeta säkert i labbet. Använd skyddsglasögon."), ("l_ic6.png", "Tro inte på allt du läser. Kolla källan.")]
TEST = [("ringa", "Vem forskar om växter?", ["Botaniker", "Zoolog", "Marinbiolog"]),
        ("streck", "Dra streck till rätt förklaring.", ["Hypotes", "Resultat", "Slutsats", "Källa"], ["där informationen kommer ifrån", "det man har lärt sig", "det man tror blir svaret, och varför", "det man mäter i testet"]),
        ("sf", "Kryssa i rätt ruta.", ["I ett rättvist test ändrar man många saker.", "Man får äta i labbet.", "Ett mikroskop gör små saker större.", "Allt som står på nätet är sant."]),
        ("skriv2", "Du vill testa om bönor gror bäst i varmt eller kallt. Vad ska du ändra? Vad ska vara lika?", ["Jag ändrar", "Det här ska vara lika:"]),
        ("skriv", "Ali säger: ”Mina bönor i värmen grodde snabbast. Alltså gror alla bönor bäst i värme.” Vad borde Ali göra för att vara säkrare?", "Ali borde", 2),
        ("skriv", "En webbsida säger att ett te botar förkylning på en timme. Hur kan du ta reda på om det stämmer?", "Jag kan", 2)]
TILL_LARAREN = ("Den här versionen täcker samma centrala innehåll som kapitel 1 i grundboken – hur biologisk kunskap skapas, systematiska undersökningar, säkerhet i labbet, mikroskopet samt källkritik och pseudovetenskap – men med anpassad text och bildstöd. "
                "Den passar elever med läs- och skrivsvårigheter, elever med annat modersmål och elever som lätt blir överväldigade av mycket text.")
TILL_PUNKTER = ["Korta meningar – oftast en tanke per rad.", "Bildstöd till nästan varje stycke, och viktiga ord med bild på sidan 2.",
                "6 korta delar med en förloppsindikator, så att eleven ser hur långt den har kommit.", "Kom ihåg-rutor med det viktigaste i en mening.",
                "Varierade övningar direkt efter varje del: ringa in, dra streck, fyll i med ordbank, sant/falskt och skriv med meningsstart."]
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt."
FACIT = [
 "<b>Del 1:</b> 1) Läran om allt som lever. 2) Zoolog – djur; Botaniker – växter; Marinbiolog – livet i havet; Mikrobiolog – små organismer, som bakterier. 3) naturen, labb, kropp. 4) Egna svar.",
 "<b>Del 2:</b> 1) Testa 3, Fråga 1, Svara 4, Gissa 2. 2) Det man tror blir svaret, och varför. 3) Sant, sant, falskt. 4) Egna svar, t.ex. ”Jag tror att bönor växer snabbare i värme.”",
 "<b>Del 3:</b> 1) Ljuset. 2) Samma jord, lika mycket vatten, lika många frön. 3) mörker, en, rättvist. 4) Då vet man vad som orsakade skillnaden.",
 "<b>Del 4:</b> 1) Krassen i mörker. 2) Resultat – det man mäter eller ser; Slutsats – det man lär sig; Hypotes – det man tror blir svaret, och varför. 3) Sant, falskt, sant. 4) Då ser man att resultatet inte var en slump.",
 "<b>Del 5:</b> 1) Ha skyddsglasögon, sätta upp långt hår, fråga om jag är osäker. 2) Okular – här tittar du; Objektbord – här ligger glaset; Skruv – gör bilden skarp. 3) Celler. 4) T.ex. så att inget stänker i ögonen.",
 "<b>Del 6:</b> 1) Det är nog inte sant. 2) Vem? – vem har skrivit texten; Varför? – vill de sälja något; När? – är texten gammal; Fler källor? – står det på fler ställen. 3) bevis, sälja, källor. 4) Egna svar.",
 "<b>Testa dig:</b> 1) Botaniker. 2) Hypotes – det man tror blir svaret, och varför; Resultat – det man mäter i testet; Slutsats – det man har lärt sig; Källa – där informationen kommer ifrån. 3) Falskt, falskt, sant, falskt. 4) Ändra temperaturen. Lika: sorts bönor, antal, vatten, jord, ljus. 5) Göra om testet flera gånger, med fler bönor. 6) T.ex. kolla vem som står bakom, om de vill sälja, och om pålitliga källor (1177, forskare) säger samma sak.",
]
