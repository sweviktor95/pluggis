# -*- coding: utf-8 -*-
"""Område 2 Cellen och livets processer – grundtext (nya ramverket, per moment). Samma format som område 1 och 4."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
FIG = '/tmp/bio/fig02n/'
NR = 2
SLUG = "cellen"
TAB = "2"
NAMN = "Cellen och livets processer"
UNDER = "Små byggstenar – stora processer"
INTRO = ("Du består av ungefär trettio tusen miljarder celler. Varje cell är så liten att du behöver ett mikroskop för att se den, men den kan ändå ta emot ämnen, få energi, bygga nytt och ibland dela sig. "
         "En växtcell fångar ljus och gör socker. En muskelcell drar ihop sig. En bakterie klarar sig helt själv. I det här kapitlet lär du dig hur celler är byggda, hur de får energi och hur miljarder celler tillsammans kan bli en växt, ett djur eller en människa. "
         "Namn och mätvärden i uppgifterna är påhittade, om inget annat står.")
MAL = ["vad som kännetecknar liv och vad cellteorin säger", "hur djurceller, växtceller och bakterier är byggda och vad cellens delar gör",
       "hur ett mikroskop används och hur man räknar ut förstoring", "vad fotosyntes och cellandning är och hur processerna hänger ihop",
       "varför celler specialiserar sig och hur celler bildar vävnader, organ och organsystem", "hur man planerar och genomför egna undersökningar med mikroskop och jäst"]
FUNDERA = "Är en bakterie levande? Och ett virus? Skriv ner vad du tycker att allt levande måste kunna, och kom tillbaka till listan när du har läst klart momentet."
DELOMR = {"2.1": "Cellen", "2.2": "Fotosyntes och cellandning", "2.3": "Organ och organsystem"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)
def cards4(items):
    return '<div class="cards" style="grid-template-columns:repeat(%d,1fr)">' % len(items) + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in items) + '</div>'

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Vad är liv?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p>Hur vet vi att något lever? En kråka, en gran och en jästsvamp ser olika ut, men de har mycket gemensamt. Biologer brukar beskriva liv med några <strong class='green'>kännetecken</strong>. Alla levande organismer:</p>"
     + bullets(["är uppbyggda av <strong class='green'>celler</strong>,",
                "tar upp <strong class='green'>energi</strong> och ämnen och omvandlar dem,",
                "<strong class='green'>växer</strong> och utvecklas,",
                "kan <strong class='green'>föröka</strong> sig och för då vidare sitt ärftliga material (DNA),",
                "<strong class='green'>reagerar</strong> på sin omgivning, till exempel på ljus, värme eller beröring."])
     + "<p>Alla kännetecknen utgår från en enda sak: <strong class='green'>cellen</strong>. Cellen är den minsta enhet som är levande. En bakterie är en enda cell. En människa är miljarder celler som samarbetar.</p>",
   [begrepp([("Organism", "En levande varelse, till exempel en växt, ett djur, en svamp eller en bakterie."), ("Cell", "Den minsta levande enheten."),
             ("Encellig", "Består av en enda cell."), ("Flercellig", "Består av många celler.")]),
    box("tank", "Tänk efter", "<p>Är en bil levande? Den tar upp energi (bensin) och rör sig. Vilka av kännetecknen saknas?</p>")])
 + "<h3>Gränsfallet virus</h3>"
 + "<p>Virus är inte byggda av celler och kan inte föröka sig på egen hand. De måste ta sig in i en levande cell och använda cellens utrustning för att göra nya virus. Därför räknas virus oftast <em>inte</em> som levande, men de har arvsmassa och kan förändras över tid. Biologer diskuterar var gränsen går, och det är ett bra exempel på att definitioner i naturvetenskap kan ändras när vi lär oss mer.</p>"
 + fig(FIG+"cellen-nivaer.png", "<b>Bild 2.1</b> Från en liten cell till en hel organism. Varje nivå består av många enheter från nivån före. Vi återvänder till bilden i delområde 2.3.", "92%")
 + kolla("Start", ["Nämn tre kännetecken på liv.", "Vilken är den minsta enhet som är levande?", "Varför räknas virus oftast inte som levande?"]))

# ------------------------------------------------------------------ 2.1.1
add("2.1.1", "Cellteorin och mikroskopet", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Cellteorin och mikroskopet",
 row("<p>Celler är för små för att synas med blotta ögat. De upptäcktes först när man kunde förstora saker. År 1665 tittade den engelske forskaren <strong class='green'>Robert Hooke</strong> på en tunn skiva kork i ett mikroskop som han hade konstruerat själv. Han såg tusentals små kammare som liknade vaxkakorna i en bikupa. Han kallade dem <em>cells</em>, ”celler”. Det var döda korkceller, så Hooke såg bara de tomma väggarna.</p>"
     "<p>Under 1800-talet undersökte många forskare växter och djur. Matthias Schleiden såg att växter är uppbyggda av celler (1838), och Theodor Schwann kom fram till samma sak för djur (1839). År 1855 sammanfattade Rudolf Virchow att nya celler alltid bildas av redan levande celler, och inte uppstår av sig själva. Av detta växte <strong class='green'>cellteorin</strong> fram.</p>",
   [begrepp([("Cellteorin", "Alla organismer består av en eller flera celler, och nya celler bildas bara från andra celler."), ("Mikroskop", "Instrument som förstorar små föremål."), ("Förstoring", "Hur många gånger större något ser ut.")]),
    box("visste", "Visste du?", "<p>En människokropp har ungefär lika många bakterier som egna celler. De flesta bakterierna finns i tjocktarmen och är en del av din normala tarmflora.</p>")])
 + fig(FIG+"kork.png", "<b>Bild 2.2</b> Hooke såg kork som ett rutnät av små kammare. Bilden är en förenklad återgivning.", "86%")
 + cards4([("Alla organismer består av celler", "Från bakterier till blåvalar: allt liv är uppbyggt av en eller flera celler."),
           ("Cellen är minsta levande enheten", "Delar av en cell, som en cellkärna eller en mitokondrie, kan inte leva på egen hand."),
           ("Celler kommer från celler", "Nya celler bildas genom att en cell delar sig. Så växer vi och ersätter gamla celler.")])
 + "<h3>Hur stor är en cell?</h3>"
 + "<p>De flesta celler är mellan några tusendelar och några tiondels millimeter. Bakterier är bland de minsta: runt två tusendelar av en millimeter (2 µm). En röd blodkropp är ungefär 0,007 mm. Ett människoägg är runt 0,1 mm och kan med lite tur skymtas som en prick. Några celler är mycket större: en nervcell kan vara över en meter lång, och gulan i ett strutsägg är en enda cell.</p>"
 + fig(FIG+"cellen-storlek.png", "<b>Bild 2.3</b> Storleken på några celler och virus. Varje steg åt höger är tio gånger mindre. Bilderna är inte skalenliga.", "82%")
 + roww("<h3 style='margin-top:0'>Så räknar du ut förstoringen</h3><p>Ett ljusmikroskop har två linser som förstorar: <strong class='green'>okularet</strong> där du tittar och <strong class='green'>objektivet</strong> nära preparatet. Den totala förstoringen är okularets förstoring gånger objektivets.</p>"
        "<p class='ex'><b>Exempel:</b> okular 10× och objektiv 40× ger 10 · 40 = <b>400</b> gånger förstoring.</p>"
        "<p>Ljusmikroskop förstorar upp till ungefär tusen gånger. För att se virus och cellens minsta delar behövs ett <strong class='green'>elektronmikroskop</strong>, som förstorar många tusen gånger mer.</p>",
        [box("tank", "Tänk efter", "<p>Du tittar i ett mikroskop med okular 10× och objektiv 10×. Du byter till objektiv 40×. Hur många gånger ökar förstoringen?</p>")])
 + kolla("2.1.1", ["Vad såg Hooke i korken, och vad kallade han det?", "Vad säger cellteorin?", "Beräkna förstoringen med okular 10× och objektiv 40×.", "Varför ser man inte virus i ett vanligt ljusmikroskop?"]))

# ------------------------------------------------------------------ 2.1.2
add("2.1.2", "Djurcell och växtcell", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Djurcell och växtcell",
 "<p>Djur, växter och svampar har <strong class='green'>celler med cellkärna</strong>. Inuti cellen finns små delar med olika uppgifter, som kallas <strong class='green'>organeller</strong>. De fungerar lite som organen i en kropp. Här är de viktigaste:</p>"
 + table(["Del", "Vad den gör", "Djurcell", "Växtcell"],
         [["<b>Cellmembran</b>", "Tunt skal runt cellen som bestämmer vad som får komma in och ut.", "✔", "✔"],
          ["<b>Cytoplasma</b>", "Geléartad massa som fyller cellen. Många av cellens kemiska reaktioner sker här.", "✔", "✔"],
          ["<b>Cellkärna</b>", "Innehåller DNA, cellens arvsmassa. Styr vad cellen gör.", "✔", "✔"],
          ["<b>Ribosomer</b>", "Bygger proteiner efter ritningar från DNA.", "✔", "✔"],
          ["<b>Mitokondrie</b>", "Gör cellandning: frigör energi ur glukos och syre.", "✔", "✔"],
          ["<b>Kloroplast</b>", "Gör fotosyntes med hjälp av grönt klorofyll.", "–", "✔ (i gröna delar)"],
          ["<b>Cellvägg</b>", "Stadig vägg utanför cellmembranet som ger stöd och form.", "–", "✔"],
          ["<b>Vakuol</b>", "Stor blåsa med vatten och lösta ämnen. Håller cellen spänd.", "små", "✔ stor"]])
 + fig(FIG+"cellen-djurcell.png", "<b>Bild 2.4</b> En djurcell. Färgerna är påhittade för att man ska kunna skilja delarna åt.", "88%")
 + fig(FIG+"cellen-vaxtcell.png", "<b>Bild 2.5</b> En växtcell med cellvägg, kloroplaster och en stor vakuol.", "88%")
 + roww("<h3 style='margin-top:0'>Vad är skillnaden?</h3>" + bullets(["Växtceller har <strong class='green'>cellvägg</strong>, <strong class='green'>kloroplaster</strong> och en stor <strong class='green'>vakuol</strong>. Djurceller saknar dessa.",
         "Växtceller har <em>också</em> mitokondrier. Alla celler behöver energi, även de som gör fotosyntes.",
         "Alla celler har cellmembran, cytoplasma, DNA och ribosomer.",
         "Inte alla växtceller har kloroplaster. Rötter och löken du undersöker i labben ligger under jord och saknar dem."]),
        [begrepp([("Organell", "Del av en cell med en särskild uppgift."), ("Cellkärna", "Organell som innehåller DNA."), ("Mitokondrie", "Organell där cellandning sker."), ("Kloroplast", "Organell där fotosyntes sker."),
                  ("Cellvägg", "Fast vägg utanför membranet hos växtceller."), ("Vakuol", "Blåsa med vatten och lösta ämnen.")])])
 + kolla("2.1.2", ["Vilka tre delar har växtceller men inte djurceller?", "Vad gör mitokondrien, och varför har även växtceller sådana?", "Vad är skillnaden mellan cellvägg och cellmembran?", "Förklara varför en cell i en rot saknar kloroplaster."]))

# ------------------------------------------------------------------ 2.1.3
add("2.1.3", "Bakterier och encelliga organismer", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Bakterier och encelliga organismer",
 "<p>Alla organismer består inte av många celler. Många klarar sig som en enda cell. Det finns två huvudtyper av celler:</p>"
 + cards4([("Cell utan cellkärna", "<b>Bakterier.</b> DNA ligger fritt i cytoplasman. Saknar kärna och andra organeller med membran. Mycket små, ungefär 0,001–0,005 mm."),
           ("Cell med cellkärna", "<b>Växter, djur, svampar och många encelliga organismer.</b> DNA ligger i en cellkärna. Har organeller. Oftast 0,01–0,1 mm.")])
 + fig(FIG+"cellen-bakterie.png", "<b>Bild 2.6</b> En bakteriecell. DNA ligger fritt i cytoplasman, och många bakterier har en cellvägg och ett eller flera spröt (flageller) för att röra sig.", "88%")
 + roww("<p>Bakterier finns överallt: i jord, vatten, på huden och i tarmen. De flesta är ofarliga eller till och med nyttiga. Bakterier i tarmen hjälper till att bryta ner maten, och bakterier i jorden bryter ner döda växter. Några få orsakar sjukdomar, till exempel halsfluss (streptokocker) eller magsjuka (salmonella). Bakterier som orsakar sjukdom kan ofta behandlas med <strong class='green'>antibiotika</strong>.</p>"
        "<p>Virus är inte celler och kan inte behandlas med antibiotika. Antibiotika angriper delar som bakterier har men våra celler saknar, till exempel bakteriens cellvägg. Virus har inga sådana delar. De lever i våra egna celler och förökar sig där.</p>",
        [begrepp([("Bakterie", "Encellig organism utan cellkärna."), ("Encellig organism", "Organism som består av en enda cell."), ("Antibiotika", "Läkemedel som dödar eller hämmar bakterier. Verkar inte mot virus.")]),
         box("visste", "Visste du?", "<p>Virus är mycket mindre än bakterier. Ett typiskt virus är runt 0,0001 mm, alltså ungefär tjugo gånger mindre än en bakterie.</p>")])
 + "<h3>Encelliga organismer med cellkärna</h3>"
 + "<p>Alla encelliga organismer är inte bakterier. <strong class='green'>Amöbor</strong> är encelliga djur som rör sig och slukar mindre organismer. Många <strong class='green'>alger</strong> är encelliga och gör fotosyntes. <strong class='green'>Jäst</strong> är en encellig svamp, och du möter den i nästa delområde. Alla dessa har cellkärna och organeller, alltså en mer komplicerad cell än bakteriens, men hela organismen är bara en enda cell. Hela livet sker i den.</p>"
 + kolla("2.1.3", ["Vad är den viktigaste skillnaden mellan en bakteriecell och en djurcell?", "Varför hjälper antibiotika mot en halsfluss orsakad av bakterier men inte mot en förkylning?", "Ge två exempel på encelliga organismer som inte är bakterier."]))

# ------------------------------------------------------------------ Labb 2.1
add("Labb", "2.1 Mikroskopera celler", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Labb 2.1 Mikroskopera celler",
 "<p>Du ska göra ett eget preparat av växtceller, titta på det i mikroskop och rita vad du ser. Sedan jämför du med bild 2.4 av en djurcell.</p>"
 + roww("<p><strong class='green'>Frågeställning:</strong> Hur ser en växtcell ut i ett mikroskop, och vilka delar går att se?</p><p><strong class='green'>Hypotes:</strong> Skriv vilka delar du tror att du kommer att se, och vilka du tror inte syns. Motivera.</p>"
        "<p><strong class='green'>Material:</strong> mikroskop, objektglas och täckglas, pincett, pipett, vatten, jodlösning (utspädd), bit av lök som läraren har skurit ut, papper, penna.</p><h3>Gör så här</h3>"
        + steps(["Läraren skär en lökbit. Använd pincetten och dra loss ett tunt, genomskinligt skinn från insidan av ett lökblad.",
                 "Lägg skinnet plant på ett objektglas. Se till att det inte veckar sig. Droppa på en droppe jodlösning.",
                 "Sänk långsamt ned ett täckglas över preparatet från ena sidan, så att inga luftbubblor fastnar.",
                 "Börja med lägsta förstoring. Vrid på ratten tills du ser skarpt. Byt sedan till högre förstoring.",
                 "Rita en cell eller två och märk ut det du ser. Skriv förstoringen under teckningen. Räkna ut den totala förstoringen."]),
        [box("begrepp", "Begrepp", "<b class='t'>Preparat</b><p>Det du lägger under mikroskopet.</p><b class='t'>Objektglas</b><p>Glasskiva som preparatet ligger på.</p><b class='t'>Täckglas</b><p>Tunt glas som skyddar preparatet.</p>"),
         box("tank", "Bra att veta", "<p>Joden färgar cellkärnan brun så att den syns bättre. Löken växer under jord och saknar därför kloroplaster.</p>")])
 + "<h3>Frågor</h3>"
 + steps(["Vilka delar kunde du se? Vilka syntes inte, och varför tror du det?", "Hur ser cellernas form och storlek ut? Jämför med bild 2.5.", "Vilka skillnader finns mellan dina lökceller och djurcellen på bild 2.4?", "Vad var svårt i undersökningen, och hur skulle du göra annorlunda nästa gång?"], True)
 + '<p class="note">Säkerhet: Mikroskop och glas hanteras varsamt. Skärverktyg används bara av läraren. Jodlösning kan färga kläder och hud: tvätta händerna efteråt.</p>')

# ------------------------------------------------------------------ 2.2.1
add("2.2.1", "Växten som producent", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Växten som producent",
 "<p>Växter behöver ingen mat från andra. De gör sin egen näring av sådant som finns i luft och vatten, med hjälp av solljus. Processen kallas <strong class='green'>fotosyntes</strong>, och växten kallas därför en <strong class='green'>producent</strong>. Fotosyntesen är grunden för nästan allt liv på jorden, eftersom den både ger mat och frigör syre.</p>"
 + cards4([("In i växten", "<b>Koldioxid</b> från luften, som tas upp genom små öppningar i bladet. <b>Vatten</b> från jorden, som tas upp av rötterna. <b>Ljusenergi</b> från solen."),
           ("Ut ur växten", "<b>Glukos</b> (druvsocker) som växten använder som energi och byggmaterial. <b>Syre</b> som släpps ut i luften.")])
 + roww("<h3 style='margin-top:0'>Fotosyntesen i ord</h3><p style='font-size:1.1em;text-align:center'><b>koldioxid + vatten + ljusenergi → glukos + syre</b></p>"
        "<p>Fotosyntesen sker i <strong class='green'>kloroplasterna</strong>. De innehåller det gröna ämnet <strong class='green'>klorofyll</strong>, som fångar ljus. Ljusenergin lagras som kemisk energi i glukosen.</p>"
        "<p>Glukosen används på tre sätt. En del går till cellandningen för att ge växten energi. En del bygger nya delar, till exempel cellulosa i cellväggarna. Resten lagras, ofta som stärkelse i rötter, frön och knölar. Därför är potatis och spannmål så näringsrika för oss.</p>",
        [begrepp([("Fotosyntes", "Process där växter, alger och vissa bakterier använder ljus, koldioxid och vatten för att bilda glukos och syre."), ("Producent", "Organism som själv bygger sin näring."), ("Klorofyll", "Grönt ämne i kloroplasterna som fångar ljus."), ("Glukos", "Druvsocker, ett enkelt socker.")]),
         box("visste", "Visste du?", "<p>Det kemiska uttrycket är 6 CO₂ + 6 H₂O + ljus → C₆H₁₂O₆ + 6 O₂. Siffrorna visar att atomerna inte försvinner utan bara byter plats.</p>")])
 + fig(FIG+"cellen-fotosyntes.png", "<b>Bild 2.7</b> Fotosyntes och cellandning, två processer som är varandras motsatser. Vi återvänder till bilden i 2.2.3.", "54%")
 + box("tank", "Tänk efter", "<p>En frukostflinga innehåller stärkelse som en gång gjordes i en veteplanta. Följ stärkelsen bakåt. Var kommer energin från ursprungligen?</p>")
 + kolla("2.2.1", ["Vilka ämnen behöver en växt för fotosyntes, och vad bildas?", "Var i cellen sker fotosyntesen, och vilket ämne fångar ljuset?", "Varför kallas växter för producenter?", "Vad kan växten göra med glukosen?"]))

# ------------------------------------------------------------------ 2.2.2
add("2.2.2", "Cellandning", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Cellandning",
 "<p>Alla celler behöver energi hela tiden: för att bygga nytt, ta upp ämnen, röra sig och hålla värmen. Energin finns lagrad i glukos. I <strong class='green'>cellandningen</strong> frigörs energin så att cellen kan använda den. Det sker i <strong class='green'>mitokondrierna</strong>.</p>"
 + roww("<h3 style='margin-top:0'>Cellandning i ord</h3><p style='font-size:1.1em;text-align:center'><b>glukos + syre → koldioxid + vatten + energi</b></p>"
        "<p>Cellandning sker i nästan alla levande celler hos djur, växter och svampar, <em>dag och natt</em>. Energin används till cellens arbete, och en del blir värme. Därför blir du varm när du rör dig mycket.</p>"
        "<p>Cellandning är inte samma sak som att andas med lungorna. Lungorna tar in syre och släpper ut koldioxid, men det är i cellerna som syret används och koldioxiden bildas. Lungorna och blodet transporterar bara ämnena dit.</p>",
        [begrepp([("Cellandning", "Process där glukos och syre ger energi, koldioxid och vatten."), ("Mitokondrie", "Organell där cellandningen sker."), ("Energi", "Förmåga att utföra arbete. Kan inte skapas eller förstöras, bara omvandlas.")]),
         box("visste", "Visste du?", "<p>Röda blodkroppar har inga mitokondrier. Muskelceller och leverceller kan ha hundratals eller tusentals. De arbetar hårt och behöver mycket energi.</p>")])
 + "<h3>Utan syre: jäsning</h3>"
 + "<p>Vissa celler kan få energi även utan syre. Jäst, som är en encellig svamp, kan göra <strong class='green'>jäsning</strong>. Då bryts sockret ner utan syre, och det bildas koldioxid och alkohol (etanol). Jäsningen ger mycket mindre energi än cellandning med syre. Det är jästens koldioxid som får bröddegen att jäsa och bli luftig. I labben i nästa avsnitt mäter du hur mycket koldioxid jäst bildar.</p>"
 + box("tank", "Tänk efter", "<p>Vilka celler i din kropp tror du har extra många mitokondrier? Motivera: vad gör de, och vad behöver de?</p>")
 + kolla("2.2.2", ["Skriv cellandningen i ord.", "Var i cellen sker cellandningen?", "Vad är skillnaden mellan cellandning och att andas med lungorna?", "Vad händer med energin när cellen använder den? Vart tar den vägen?"]))

# ------------------------------------------------------------------ 2.2.3
add("2.2.3", "Processerna tillsammans", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Processerna tillsammans",
 "<p>Jämför de två formlerna. Ämnena som bildas i den ena processen är ämnena som används i den andra. De är varandras motsatser, och tillsammans bildar de ett <strong class='green'>kretslopp</strong> för kol och syre.</p>"
 + table(["", "Fotosyntes", "Cellandning"],
         [["Ämnen in", "koldioxid, vatten, ljus", "glukos, syre"], ["Ämnen ut", "glukos, syre", "koldioxid, vatten"], ["Energi", "ljusenergi lagras i glukos", "energi frigörs från glukos"],
          ["Var i cellen", "kloroplaster", "mitokondrier"], ["Vilka celler", "växter, alger, vissa bakterier", "nästan alla levande celler"], ["När", "bara i ljus", "dag och natt"]])
 + "<h3>Gör växter båda sakerna?</h3>"
 + "<p>Ja. En grön växt gör fotosyntes i ljus, men den gör <em>också</em> cellandning hela tiden. Det är ett vanligt fel att tro att växter andas bara på natten, eller att de är motsatsen till djur. Under dagen gör en växt i ljus oftast mer fotosyntes än cellandning, så nettot blir att syre släpps ut. På natten, utan ljus, sker bara cellandning, och växten tar upp syre och släpper ut koldioxid.</p>"
 + fig(FIG+"dagnatt.png", "<b>Bild 2.8</b> Gasutbyte hos ett blad. I ljus pågår både fotosyntes och cellandning. På natten pågår bara cellandning.", "76%")
 + roww("<h3 style='margin-top:0'>Kol och energi</h3><p>Kolatomerna går i <strong class='green'>kretslopp</strong>. Fotosyntesen tar koldioxid från luften och bygger in kolet i glukos. När växten, ett djur som äter den eller en nedbrytare använder glukosen i cellandningen, hamnar kolet i koldioxid igen. I kapitel 4 följer vi kolets kretslopp genom hela ekosystem.</p>"
        "<p>Energin däremot går <em>inte</em> i kretslopp. Den kommer in som ljus från solen, omvandlas till kemisk energi i glukos och blir till slut värme som lämnar systemet. Därför behöver livet ständigt ny energi från solen.</p>",
        [begrepp([("Kretslopp", "När ett ämne används om och om igen."), ("Energiflöde", "Energin går in som ljus och ut som värme, och återanvänds inte.")]),
         box("tank", "Tänk efter", "<p>Ett barr på en gran i Norrbotten gör mindre fotosyntes i december än i juni. Gör det någon cellandning i december? Motivera.</p>")])
 + kolla("2.2.3", ["Beskriv hur fotosyntes och cellandning är varandras motsatser.", "Gör växter cellandning? När?", "Varför säger man att kol går i kretslopp men energi inte?", "Förklara varför en växt som står i mörker en hel dag inte kan växa till sig."]))

# ------------------------------------------------------------------ Labb 2.2
add("Labb", "2.2 Jäst och koldioxid", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Labb 2.2 Jäst och koldioxid",
 "<p>Jäst får energi ur socker och bildar koldioxid. Du ska undersöka hur temperaturen påverkar hur mycket koldioxid jästen bildar. Koldioxiden fångas i en ballong, så att du kan mäta hur mycket gas som bildats.</p>"
 + roww("<p><strong class='green'>Frågeställning:</strong> Hur påverkar temperaturen hur mycket koldioxid jäst bildar?</p><p><strong class='green'>Hypotes:</strong> Vid vilken temperatur tror du att jästen bildar mest koldioxid? Motivera.</p>"
        "<p><strong class='green'>Material:</strong> 4 små plastflaskor (0,5 l) med ballonger, jäst, socker, mätcylinder, termometer, vattenbad med olika temperaturer, måttband eller sytråd, stoppur, penna.</p><h3>Gör så här</h3>"
        + steps(["Förbered fyra vattenbad: kallt (isvatten, ca 5 °C), rumstemperatur (ca 20 °C), ljummet (ca 35 °C) och varmt (ca 50 °C). Mät med termometer.",
                 "Rör ihop jästblandning: 1 tsk torrjäst, 1 tsk socker och 1 dl ljummet vatten i varje flaska. Alla flaskor ska ha exakt samma mängd.",
                 "Sätt en ballong på varje flaska direkt och ställ flaskorna i varsitt vattenbad. Starta stoppuret.",
                 "Efter 5, 10 och 15 minuter mäter du ballongens omkrets med måttband eller sytråd. Skriv i tabellen.",
                 "Rita ett diagram med temperaturen på x-axeln och ballongens omkrets efter 15 minuter på y-axeln."]),
        [table(["Temperatur", "5 min", "10 min", "15 min"], [["ca 5 °C", "", "", ""], ["ca 20 °C", "", "", ""], ["ca 35 °C", "", "", ""], ["ca 50 °C", "", "", ""]], "tbl num"),
         box("begrepp", "Variabler", "<b class='t'>Oberoende</b><p>Temperaturen.</p><b class='t'>Beroende</b><p>Ballongens omkrets.</p><b class='t'>Lika</b><p>Mängd jäst, socker och vatten, flaskans storlek, tid.</p>")])
 + "<h3>Frågor</h3>"
 + steps(["Vid vilken temperatur bildades mest koldioxid? Hur såg diagrammet ut?", "Vad tror du hände med jästen vid den varmaste temperaturen? Motivera.", "Hur vet du att det är jästen som bildar gasen? Hur kunde ni ha kontrollerat det (kontrollförsök utan jäst)?", "Vilka felkällor finns? Hur kan ni minska dem?"], True)
 + '<p class="note">Säkerhet: Använd ljummet, inte hett vatten (högst ca 50 °C). Torka upp spill så ingen halkar. Jästen är ofarlig men ska inte ätas. Tvätta händerna efteråt.</p>')

# ------------------------------------------------------------------ 2.3.1
add("2.3.1", "Specialiserade celler och vävnader", f"Kapitel {NR} · Delområde 2.3 {DELOMR['2.3']} · Specialiserade celler och vävnader",
 "<p>Hos encelliga organismer får en enda cell göra allt. Hos flercelliga organismer arbetar cellerna ihop, och då kan de bli bra på olika saker. Celler som har fått en särskild uppgift kallas <strong class='green'>specialiserade celler</strong>. En specialiserad cell har fått en form och innehåll som passar uppgiften.</p>"
 + fig(FIG+"spec-celler.png", "<b>Bild 2.9</b> Fem specialiserade celler. Bilderna är förenklade och inte skalenliga.", "82%")
 + roww("<p>Exempel: Muskelceller kan dra ihop sig och ger rörelse. Nervceller skickar signaler över långa avstånd och är därför långa och grenade. Röda blodkroppar transporterar syre. De har ingen cellkärna, vilket ger mer plats åt hemoglobin, som binder syre. Rothårsceller har en lång utväxt som ger stor yta för att ta upp vatten. Palisadceller i bladet har många kloroplaster för fotosyntes.</p>"
        "<p>Nästan alla celler i en människa innehåller samma arvsmassa. De blir olika eftersom olika delar av DNA används i olika celltyper.</p>"
        "<h3>Vävnader</h3><p>En grupp lika celler som arbetar tillsammans med samma uppgift kallas en <strong class='green'>vävnad</strong>. I kroppen finns fyra grundtyper:</p>"
        + bullets(["<b>Epitelvävnad</b> täcker ytor och kläder insidan av kroppens hålrum, till exempel huden och tarmens insida.",
                   "<b>Bindväv</b> binder ihop och stödjer, till exempel senor, fett och brosk. Blodet räknas också hit.",
                   "<b>Muskelvävnad</b> drar ihop sig och ger rörelse.",
                   "<b>Nervvävnad</b> leder nervsignaler mellan kroppens delar."]),
        [begrepp([("Specialiserad cell", "Cell med en särskild uppgift och en byggnad som passar den."), ("Vävnad", "Grupp lika celler som arbetar tillsammans."), ("Organ", "Del av kroppen som består av flera vävnader.")]),
         box("tank", "Tänk efter", "<p>Varför är det bra att en nervcell är lång och grenad, medan en röd blodkropp är liten och rund?</p>")])
 + "<h3>Organ</h3>"
 + "<p>Flera olika vävnader som samarbetar bildar ett <strong class='green'>organ</strong>. Hjärtat består till största delen av muskelvävnad, men också av bindväv, nervvävnad och epitel. Magsäcken har muskelvävnad som knådar maten, epitel som bildar magsaft och nervvävnad som styr. Växter har också organ: rot, stam och blad.</p>"
 + kolla("2.3.1", ["Vad menas med en specialiserad cell? Ge två exempel.", "Skilj på cell, vävnad och organ.", "Nämn de fyra vävnadstyperna i kroppen.", "Varför kan inte hjärtat bestå av bara muskelvävnad? Vilka andra vävnader behövs?"]))

# ------------------------------------------------------------------ 2.3.2
add("2.3.2", "Kroppens organsystem – översikt", f"Kapitel {NR} · Delområde 2.3 {DELOMR['2.3']} · Kroppens organsystem – översikt",
 "<p>Organ som arbetar tillsammans för en gemensam uppgift bildar ett <strong class='green'>organsystem</strong>. Munnen, matstrupen, magsäcken och tarmarna hör till exempel till matsmältningssystemet. Alla organsystem tillsammans bildar en hel <strong class='green'>organism</strong>.</p>"
 + fig(FIG+"cellen-organ.png", "<b>Bild 2.10</b> Några av kroppens organ.", "62%")
 + table(["Organsystem", "Viktigaste uppgift", "Exempel på organ"],
         [["Matsmältningssystemet", "Bryter ner maten och tar upp näring", "magsäck, tunntarm, lever"], ["Andningssystemet", "Tar in syre, släpper ut koldioxid", "lungor, luftrör"],
          ["Cirkulationssystemet", "Transporterar ämnen med blodet", "hjärta, blodkärl"], ["Nervsystemet", "Tar emot och skickar signaler", "hjärna, ryggmärg, nerver"],
          ["Skelettet och musklerna", "Stöd, skydd och rörelse", "skelett, muskler"], ["Utsöndringssystemet", "Renar blodet och för bort avfall", "njurar, urinblåsa"],
          ["Immunförsvaret", "Skyddar mot sjukdom", "vita blodkroppar, lymfkörtlar"], ["Hormonsystemet", "Styr kroppen med hormoner", "sköldkörtel, bukspottkörtel"],
          ["Fortplantningssystemet", "Gör nya individer möjliga", "könsorgan"], ["Huden", "Skyddar och reglerar temperaturen", "hud, hår, naglar"]])
 + roww("<h3 style='margin-top:0'>Alla system hjälper cellerna</h3><p>Varje cell i kroppen behöver glukos och syre för cellandning, och måste bli av med koldioxid och avfall. Organsystemen samarbetar för att det ska fungera. Matsmältningssystemet tar upp glukos. Andningssystemet tar in syre och släpper ut koldioxid. Cirkulationssystemet transporterar ämnena till och från alla celler. Utsöndringssystemet renar blodet. Det här är kapitlets viktiga sammanhang: <em>allt kroppen gör hjälper till att försörja cellerna</em>.</p>"
        "<p>I kapitel 6 tittar vi närmare på matsmältning, andning och blod, och i kapitel 7 på immunförsvaret.</p>",
        [begrepp([("Organsystem", "Organ som samarbetar för en gemensam uppgift."), ("Organism", "En hel levande varelse.")])])
 + fig(FIG+"cellen-samarbete.png", "<b>Bild 2.11</b> Så samarbetar kroppens system för att försörja cellerna.", "86%")
 + kolla("2.3.2", ["Vad är ett organsystem? Ge ett exempel.", "Vilka tre organsystem hjälps åt att förse cellerna med glukos och syre?", "Välj ett organsystem och förklara hur det hjälper kroppens celler.", "Vad skulle hända med kroppens celler om cirkulationssystemet slutade fungera? Förklara."]))

SAMMAN = ["<strong>Liv</strong> kännetecknas av celler, energiomsättning, tillväxt, förökning och reaktion på omgivningen. Virus räknas oftast inte som levande.",
          "<strong>Cellteorin:</strong> alla organismer består av celler, cellen är den minsta levande enheten och nya celler bildas från andra celler. Hooke såg celler i kork 1665.",
          "Förstoring i ljusmikroskop = okularets förstoring · objektivets förstoring.",
          "<strong>Djur- och växtceller</strong> har cellkärna, cellmembran, cytoplasma, ribosomer och mitokondrier. Växtceller har dessutom cellvägg, kloroplaster och stor vakuol.",
          "<strong>Bakterier</strong> är encelliga och saknar cellkärna. Antibiotika hjälper mot bakterier men inte mot virus.",
          "<strong>Fotosyntes:</strong> koldioxid + vatten + ljusenergi → glukos + syre. Sker i kloroplasterna.",
          "<strong>Cellandning:</strong> glukos + syre → koldioxid + vatten + energi. Sker i mitokondrierna i nästan alla levande celler, dag och natt. Jäst kan också få energi utan syre (jäsning).",
          "Fotosyntes och cellandning är varandras motsatser. <strong>Kol går i kretslopp</strong>, men <strong>energi flödar</strong> genom systemet och blir värme.",
          "<strong>Specialiserade celler</strong> bildar <strong>vävnader</strong>, som bildar <strong>organ</strong>, som bildar <strong>organsystem</strong>, som tillsammans bildar en <strong>organism</strong>."]

BEGR = [("Antibiotika", "Läkemedel som dödar eller hämmar bakterier. Verkar inte mot virus."), ("Bakterie", "Encellig organism utan cellkärna."), ("Cell", "Den minsta levande enheten."), ("Cellandning", "Process där glukos och syre ger energi, koldioxid och vatten."),
        ("Cellkärna", "Organell som innehåller DNA."), ("Cellmembran", "Tunt skal som styr vad som passerar in och ut ur cellen."), ("Cellteorin", "Alla organismer består av celler, och celler bildas från celler."), ("Cellvägg", "Fast vägg utanför cellmembranet hos växter."),
        ("Cytoplasma", "Geléartad massa som fyller cellen."), ("Encellig, flercellig", "Består av en cell respektive av många celler."), ("Fotosyntes", "Process där ljus, koldioxid och vatten blir glukos och syre."),
        ("Glukos", "Druvsocker, cellens bränsle."), ("Jäsning", "Nedbrytning av socker utan syre, ger koldioxid och alkohol."), ("Klorofyll", "Grönt ämne som fångar ljus."), ("Kloroplast", "Organell där fotosyntes sker."),
        ("Kretslopp", "När ett ämne används om och om igen."), ("Mikroskop", "Instrument som förstorar små föremål."), ("Mitokondrie", "Organell där cellandning sker."), ("Organ", "Del av kroppen som består av flera vävnader."),
        ("Organell", "Del av en cell med en särskild uppgift."), ("Organism", "En hel levande varelse."), ("Organsystem", "Organ som samarbetar för en gemensam uppgift."), ("Producent", "Organism som själv bygger sin näring."),
        ("Ribosom", "Organell som bygger proteiner."), ("Specialiserad cell", "Cell med en särskild uppgift."), ("Vakuol", "Blåsa med vatten och lösta ämnen."), ("Vävnad", "Grupp lika celler som arbetar tillsammans.")]

TEST = [
 ("A", "Vilket påstående ingår i cellteorin?", ["A Alla celler har en cellkärna.", "B Nya celler bildas från andra celler.", "C Bara växter består av celler.", "D Celler kan uppstå av död materia."], 1, 0),
 ("A", "Vilken del finns i växtceller men inte i djurceller?", ["A Cellmembran", "B Mitokondrie", "C Cellvägg", "D Cellkärna"], 2, 0),
 ("A", "Ett mikroskop har okular 10× och objektiv 40×. Hur stor är förstoringen?", ["A 50 gånger", "B 400 gånger", "C 4 gånger", "D 4 000 gånger"], 1, 0),
 ("A", "Vad bildas vid fotosyntes?", ["A Koldioxid och vatten", "B Glukos och syre", "C Glukos och koldioxid", "D Syre och vatten"], 1, 0),
 ("B", "Skriv cellandningen i ord. Skriv också i vilken del av cellen den sker.", None, 1, 3),
 ("B", "Ge tre skillnader mellan en bakteriecell och en växtcell.", None, 1, 3),
 ("C", "Förklara varför växter behöver både kloroplaster och mitokondrier.", None, 2, 4),
 ("C", "Elin hävdar att växter inte gör cellandning eftersom de gör fotosyntes. Förklara varför hon har fel och när växter gör vad.", None, 2, 4),
 ("D", "TABELL", None, 2, 5),
 ("E", "Kalle har en förkylning och vill ha antibiotika. Förklara med hjälp av vad du vet om bakterier, virus och antibiotika varför läkaren troligen säger nej.", None, 3, 5),
 ("E", "En muskelcell i benet och en hudcell i ansiktet har samma DNA men gör helt olika saker. Förklara hur det kan vara så, och varför muskelceller behöver fler mitokondrier än hudceller.", None, 3, 5),
 ("E", "En elev stänger in en grön växt i en tät, mörk låda i ett dygn. Beskriv vad som händer med gaserna i lådan och med växtens glukos. Förklara med fotosyntes och cellandning.", None, 3, 5),
]
TEST_TABELL = (["Temperatur (°C)", "Ballongens omkrets efter 15 min (cm)"],
               [["5", "2"], ["20", "5"], ["35", "14"], ["50", "6"]])
TEST_D_TEXT = "En klass undersökte hur temperaturen påverkar jäst. De mätte omkretsen på en ballong efter 15 minuter. Resultaten är påhittade."
TEST_D_SUB = ["a) Vid vilken temperatur bildades mest koldioxid?", "b) Förklara varför det bildades mindre koldioxid vid 5 °C än vid 35 °C.",
              "c) Vid 50 °C bildades mindre än vid 35 °C. Ge en möjlig förklaring och föreslå hur klassen kan ta reda på vilken temperatur som är bäst, till exempel mellan 35 och 50 °C. ●●●"]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Förklara", "D": "Tolka resultat", "E": "Resonera"}
FACIT = [
 "B", "C", "B", "B",
 "glukos + syre → koldioxid + vatten + energi. Sker i mitokondrierna.",
 "T.ex. bakterien saknar cellkärna (DNA ligger fritt), saknar mitokondrier och kloroplaster, och är mycket mindre.",
 "Kloroplasterna gör fotosyntes och bildar glukos. Mitokondrierna gör cellandning och frigör energi ur glukosen så att cellen kan leva och växa. Växten behöver båda: fotosyntesen gör bränslet, cellandningen använder det.",
 "Växter gör cellandning hela tiden, dag och natt, eftersom alla levande celler behöver energi. Fotosyntes sker bara när det finns ljus. Under dagen gör växten både fotosyntes och cellandning. På natten bara cellandning.",
 "a) 35 °C. b) T.ex. jästen är kall och reaktionerna går långsamt vid 5 °C, så mindre socker bryts ner. c) Vid 50 °C kan värmen skada jästcellernas proteiner (enzymer), så att de fungerar sämre. Klassen kan upprepa försöket med fler temperaturer, t.ex. 35, 40, 45 och 50 °C, och göra flera mätningar vid varje temperatur.",
 "Förkylning orsakas av virus. Antibiotika verkar mot bakterier genom att angripa delar som bakterier har men våra celler saknar, till exempel cellväggen. Virus har inga sådana delar och förökar sig i våra egna celler. Antibiotika skulle därför inte hjälpa, men kan ge biverkningar och bidra till resistenta bakterier.",
 "Nästan alla celler har samma DNA, men olika gener används i olika celltyper, så cellerna bygger olika proteiner och får olika form och uppgift. Muskelceller arbetar hårt och behöver mycket energi, vilket de får genom cellandning i mitokondrierna. Fler mitokondrier ger mer energi.",
 "Utan ljus sker ingen fotosyntes, men cellandningen fortsätter. Växten tar upp syre och släpper ut koldioxid, så syrehalten minskar och koldioxidhalten ökar i lådan. Glukosen används i cellandningen och bildas inte på nytt, så växtens glukosförråd minskar.",
]

LGR = ("Området täcker det centrala innehållet om celler och organsystem, fotosyntes och cellandning samt kunskapens och undersökningarnas karaktär i årskurs 7–9. "
       "Delområde 2.1 behandlar cellens byggnad och celltyper, delområde 2.2 fotosyntes och cellandning och delområde 2.3 hur celler bildar vävnader, organ och organsystem. "
       "Labbarna tränar att använda mikroskop och att planera systematiska undersökningar med variabler. "
       "Uppgifterna följer betygskriteriernas progression: från att namnge och beskriva till att förklara samband och resonera i flera led, och är inspirerade av frisläppta nationella prov i biologi.")
FAKTA = ("Uppgifter i kapitlet kommer från läroböcker och undervisningsmaterial, i huvudsak sekundärkällor. Cellantalet (cirka 3·10¹³ egna celler, ungefär lika många bakterier) bygger på Sender, Fuchs & Milo (2016) och är en uppskattning med osäkerhet. "
         "Storleksangivelserna är avrundade medelvärden. Hookes årtal (1665) och Schleiden/Schwann/Virchow (1838/1839/1855) är återgivna efter OpenStax Microbiology; vem som ska få äran för cellteorins tredje led (Virchow eller Remak) diskuteras av historiker. "
         "Jästlabbens förväntade resultat (mest koldioxid vid ljummen temperatur, mindre vid hög) är ett vanligt utfall men beror på jästsort och försöksuppställning. Enkla förklaringar som ”energi skapas inte” är förenklingar på nivå med läroplanen. "
         "Källor: Skolverket, Lgr22 kursplan i biologi. · Frisläppta nationella prov i biologi åk 9. · Illustrationer: egenritade för detta kapitel.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start.</b> Mål: eleven kan lista kännetecken på liv och motivera varför virus är ett gränsfall. Låt eleverna först skriva sin egen lista (Fundera) och jämföra efteråt.</p>
<p><b>Cellteorin och mikroskopet.</b> C-mål: återge cellteorin och använda mikroskop med rätt förstoring. Vanligt fel: att glömma att multiplicera okular och objektiv. Hooke såg döda korkceller (cellväggar). Skalan på bild 2.3 är i tiopotenser, inte linjär.</p>
<p><b>Djurcell och växtcell.</b> C-mål: jämföra celltyper och koppla organellernas byggnad till funktion. Vanligt fel: att växtceller saknar mitokondrier. Vanligt fel: kloroplaster finns i alla växtceller (inte i rötter eller lök).</p>
<p><b>Bakterier och encelliga organismer.</b> C-mål: beskriva skillnader mellan celler med och utan cellkärna och förklara varför antibiotika inte verkar mot virus. Vanligt fel: att alla bakterier är farliga, och att virus är en sorts bakterier.</p>
<p><b>Labb 2.1 Mikroskopera celler.</b> Material: mikroskop, objektglas, täckglas, pincett, jodlösning, lök. Förväntat: rektangulära celler med tydlig cellvägg och en eller flera kärnor färgade bruna av jod. Inga kloroplaster i lök. Vanliga fel: veckat skinn, luftbubblor, för tjockt preparat. Använd gärna vattenpest (Elodea) som bonus för att se kloroplaster. Cellvägg och cellmembran skiljs inte åt i ljusmikroskop.</p>
<p><b>Växten som producent.</b> C-mål: ange ämnen in och ut och förklara samband med ljus och koldioxid. Vanligt fel: ”växter får mat från jorden”. Växtens vikt kommer mest från koldioxid och vatten (van Helmont, kapitel 4).</p>
<p><b>Cellandning.</b> C-mål: ange ämnen in och ut och skilja cellandning från lungandning. Vanligt fel: ”energi skapas” eller ”förbrukas”. Energi omvandlas.</p>
<p><b>Processerna tillsammans.</b> C-mål: jämföra processerna. Vanligt fel: att växter bara gör cellandning på natten. Koppla till kolets kretslopp i kapitel 4.</p>
<p><b>Labb 2.2 Jäst och koldioxid.</b> Förväntat: mest gas vid ljummet (35–40 °C), lite i kyla, ofta mindre vid 50 °C. Resultaten varierar med jästsort och färskhet. I tät flaska finns lite syre, så processen är mest jäsning. Kontrollförsök: flaska utan jäst, eller utan socker. Vanliga fel: olika mängd jäst, ballongen sätts på för sent, termometern flyttas mellan baden.</p>
<p><b>Specialiserade celler och vävnader.</b> C-mål: förklara hur byggnad passar funktion. Vanligt fel: att specialiserade celler har olika DNA. De har samma DNA men använder olika gener. Röda blodkroppar saknar cellkärna.</p>
<p><b>Kroppens organsystem – översikt.</b> C-mål: förklara samverkan mellan två organsystem. Använd cellen som utgångspunkt: vad behöver cellen, vilka system levererar det? Tabellen är en karta över kapitel 6–7 och 10–11.</p>"""

BONUS = dict(
 titel="Potatis och osmos",
 ingress="Vad händer med en potatisbit i saltvatten respektive sötvatten? En enkel labb som visar att vatten rör sig över cellmembranet.",
 syfte="Eleverna undersöker hur potatisbitar förändras i vatten med olika mycket salt och kopplar resultatet till cellmembranet och vatten som rör sig in och ut ur cellerna. Labben är en förberedelse för fördjupningsavsnittet om transport över cellmembranet.",
 tid="Grupper om tre till fyra. Förberedelse 10 minuter, mätning efter 30–60 minuter (eller över natten).",
 material=["Potatis och potatisskalare eller korkborr", "Våg som visar 0,1 g", "Tre glas eller bägare", "Kranvatten", "Saltlösning (ca 1 tsk salt per dl) och mer koncentrerad saltlösning (ca 4 tsk per dl)", "Pappershandduk", "Klocka"],
 genomf=["Skär fyra lika stora potatisbitar (t.ex. 1 × 1 × 4 cm). Väg varje bit och skriv upp vikten.", "Lägg bitarna i var sitt glas: kranvatten, svag saltlösning och stark saltlösning. Märk glasen.", "Låt stå 30–60 minuter (eller över natten i kylskåp).", "Torka bitarna lätt med pappershandduk, väg dem och beräkna viktförändringen i procent.", "Känn på bitarna: hur är de, hårda eller mjuka? Skriv ner."],
 resultat="Bitar i kranvatten ökar i vikt och blir hårda. Bitar i stark saltlösning minskar i vikt och blir mjuka. Förklaring: vatten rör sig genom cellmembranet mot den sida där det finns mer lösta ämnen (osmos). Celler i kranvatten fylls på och blir spända. Celler i saltlösning förlorar vatten. Detaljerna ligger över grundnivån men räcker som förklaring till vad som händer.",
 sakerhet=["Salt är ofarligt men ska inte ätas under laborationen.", "Använd inte vassa knivar utan lärare.", "Torka upp spill."],
 problem=["Bitarna är olika stora: mät och väg varje bit före och efter.", "Inga skillnader: för kort tid eller för svag saltlösning."],
 bedom=[("Grundläggande", "Redovisar vikterna och beskriver vilka bitar som blev tyngre och lättare."), ("Utvecklat", "Räknar ut procentuell förändring och förklarar med att vatten rör sig in och ut ur cellerna."), ("Välutvecklat", "Förklarar med osmos, värderar felkällor och föreslår hur metoden kan förbättras.")],
)
