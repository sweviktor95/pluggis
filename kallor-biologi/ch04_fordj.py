# -*- coding: utf-8 -*-
"""Biologi kapitel 4 – Fördjupning (källa för fördjupning och fördjupning-komplett)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
FIG = '/tmp/bio/fig/'
NAMN = "Ekologi"
UNDER = "Kretslopp, kurvor och klimat i norr"
INTRO = ("Varför växer klöver bra i mager jord? Hur kunde 29 renar bli 6 000 – och sedan nästan inga? Hur mycket fisk behöver en säl? "
         "Och vad händer med fjällen när klimatet blir varmare? I den här fördjupningen räknar, tolkar och resonerar du om ekosystem som en ekolog.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa – ”eftersom … därför … vilket leder till …”.",
       "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Väg för- och nackdelar och se frågan från flera perspektiv, till exempel miljö, hälsa, ekonomi och etik.",
       "Var nyanserad: visa vad som är osäkert och vad mer man skulle behöva veta.",
       "Ta ställning och motivera med naturvetenskapliga argument."]
FUNDERA = ("Läs först kapitel 4 i grundboken. Fördjupningen bygger på begreppen producent, konsument, nedbrytare, kretslopp, "
           "energiflöde, population och övergödning.")
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"

def roww(m, side):
    return row(m, side).replace('class="row"','class="row w"',1)

S = []
S.append(("F4.1", "Kvävets kretslopp",
 "<p>Alla organismer behöver kväve för att bygga proteiner och DNA. Luften består till 78 procent av kvävgas – men varken växter eller djur kan använda den direkt. Kvävgasmolekylen är för stabil. Det är därför kväve ofta är det ämne som begränsar hur mycket växter kan växa.</p>"
 + fig(FIG+"f_kvave.png", "<b>Bild F4.1</b> Kvävets kretslopp, förenklat.")
 + row(
   "<p><strong>Kvävefixering.</strong> Vissa bakterier kan omvandla kvävgas till ämnen som växter kan ta upp. En del lever i knölar på rötterna hos baljväxter som klöver, ärter och bönor. Växten ger bakterierna socker och får kväve tillbaka – en symbios.</p>"
   "<p><strong>Näringskedjan.</strong> Djur får kväve genom att äta växter eller andra djur.</p>"
   "<p><strong>Nedbrytning.</strong> Nedbrytare frigör kväveföreningar ur döda organismer och avföring. Växterna kan ta upp dem igen.</p>"
   "<p><strong>Tillbaka till luften.</strong> Andra bakterier, särskilt i syrefattig och blöt mark, omvandlar kväveföreningar till kvävgas igen.</p>"
   "<p>Människan har förändrat kretsloppet kraftigt. Med konstgödsel tillför vi stora mängder kväve till åkrarna. Det som växterna inte tar upp kan rinna ut i sjöar och hav och orsaka övergödning.</p>",
   [box("klimat", "Östersjön", "<p>På sommaren kan man se stora gröna mattor av blågröna bakterier, cyanobakterier, i Östersjön. De kan fixera kväve från luften själva och gynnas därför när det finns mycket fosfor i vattnet.</p>"),
    box("begrepp", "Begrepp", "<b class='t'>Kvävefixering</b><p>När bakterier gör om kvävgas till ämnen som växter kan använda.</p>")])))

S.append(("F4.2", "Populationer som växer – och kraschar",
 roww("<p>Om varje hare får fyra ungar som överlever och förökar sig blir det snabbt väldigt många harar. När en population kan växa fritt ökar den inte med samma antal varje år, utan med en viss andel. Ju fler individer, desto fler nya – kurvan böjer uppåt som ett J. Det kallas <strong class='green'>exponentiell tillväxt</strong>.</p>"
     "<p>I verkligheten tar resurserna slut förr eller senare. Tillväxten bromsas och populationen planar ut kring det antal som miljön kan försörja långsiktigt. Det kallas miljöns <strong class='green'>bärförmåga</strong>. Kurvan får formen av ett S.</p>"
     "<p>Bärförmågan är inte konstant. Den beror på födotillgång, väder, rovdjur och konkurrenter – och kan förändras om miljön förändras. Om en population växer långt över bärförmågan kan den förstöra sin egen födobas. Då kan den krascha och bärförmågan bli lägre än förut.</p>",
   [fig(FIG+"f_jkurva.png", "<b>Bild F4.2</b> J-kurva och S-kurva.")])
 + "<h3>Renarna på St Matthew</h3>"
 + roww("<p>År 1944 släpptes 29 renar ut på den obebodda ön St Matthew i Berings hav. Där fanns tjocka mattor av lavar men inga rovdjur och ingen jakt. Renarna förökade sig snabbt. År 1963 räknade forskare till omkring 6 000 renar. Men lavarna, som växer mycket långsamt, var nästan helt uppätna.</p>"
       "<p>Vintern 1963–64 var ovanligt sträng med mycket snö. Renarna svalt ihjäl i stort antal. År 1966 fanns bara 42 renar kvar, och på 1980-talet var de helt borta. Lavmattorna har fortfarande inte återhämtat sig helt.</p>",
   [fig(FIG+"f_ren.png", "<b>Bild F4.3</b> Renpopulationen på St Matthew.")])
 + box("fundera", "Tänk efter", "<p>Varför räckte det inte att renarna hade gott om mat år 1950 för att populationen skulle förbli stabil?</p>")))

S.append(("F4.3", "Räkna med energi",
 "<p>I grundboken lärde du dig tumregeln att bara omkring 10 procent av energin förs vidare från en nivå i näringskedjan till nästa. Med den kan man göra uppskattningar som visar varför ekosystem ser ut som de gör. Tumregeln kan användas för både energi och biomassa (vikten av levande material).</p>"
 + fig(FIG+"f_tumregel.png", "<b>Bild F4.4</b> En näringskedja i Östersjön med tumregeln om 10 procent.")
 + row("<h3>Exempel</h3><p>En säl äter strömming och torsk. Om sälen växer 1 kg, hur mycket växtplankton har det krävt längre ner i kedjan?</p>"
   "<p class='green'><strong>1 kg säl ← 10 kg torsk ← 100 kg strömming ← 1 000 kg djurplankton ← 10 000 kg växtplankton</strong></p>"
   "<p>Varje steg uppåt i kedjan gör alltså att det krävs tio gånger mer föda längst ner. Det förklarar varför toppkonsumenter är få, behöver stora områden och är så känsliga för förändringar.</p>"
   "<h3>Anrikning i siffror</h3><p>Om ett miljögift inte bryts ner och stannar i kroppen gäller det omvända: halten kan bli ungefär tio gånger högre i varje steg. Ett gift som finns i mycket låg halt i växtplankton kan alltså finnas i tusen eller tiotusen gånger högre halt i en säl eller havsörn.</p>",
   [box("tank", "Räkna själv", "<p>Kedjan är växtplankton → djurplankton → strömming → gädda → havsörn. Ungefär hur mycket djurplankton behövs för att havsörnen ska öka 1 kg? Hur mycket växtplankton?</p>"),
    box("varning", "Varning", "<p>10 procent är ett grovt genomsnitt. Hos växtätande insekter kan det vara mer, hos varmblodiga däggdjur ofta mindre, eftersom de använder mycket energi för att hålla värmen.</p>")])))

S.append(("F4.4", "Ett varmare norr",
 "<p>Arktis och de nordligaste delarna av Sverige blir varmare betydligt snabbare än jorden i genomsnitt. Det påverkar ekosystemen på många sätt, och förändringarna hänger ihop i långa kedjor.</p>"
 + fig(FIG+"f_tradgrans.png", "<b>Bild F4.5</b> När det blir varmare kan träd och buskar växa högre upp på fjällen.")
 + row("<h3>Trädgränsen kryper uppåt</h3><p>När somrarna blir varmare och längre kan fjällbjörk, tall och buskar växa högre upp. Kalfjället krymper, och arter som är anpassade till öppna fjällmiljöer – som fjällräv, fjällripa och många fjällväxter – får mindre plats. Fjällen är den landskapstyp i Sverige där andelen rödlistade arter har ökat mest.</p>"
   "<h3>Tajmingen går fel</h3><p>Många organismer styrs av olika signaler. Växter och insekter påverkas mycket av temperaturen, medan flyttfåglar ofta startar flytten efter dagslängden. När våren kommer tidigare kan insekterna ha sin topp innan fåglarnas ungar har kläckts. Då får ungarna för lite mat. Forskare kallar det en <strong class='green'>felmatchning i tid</strong>.</p>"
   "<h3>Nya arter flyttar in</h3><p>Arter som tidigare inte klarade de kalla vintrarna kan sprida sig norrut, till exempel rödräven upp på fjället. De kan konkurrera med arter som redan finns där.</p>",
   [box("klimat", "Positiv återkoppling", "<p>Snö och is reflekterar solljus. När snösäsongen blir kortare och mörk skog ersätter vitt fjäll tar marken upp mer värme. Då blir det ännu varmare – uppvärmningen förstärker sig själv.</p>"),
    box("fundera", "Fundera", "<p>Lämlarna behöver ett stabilt snötäcke på vintern. Vad kan hända med fjällräven om vintrarna får fler perioder med töväder och skare?</p>")])))

UPG = [
 ("Använd bild F4.3 om renarna på St Matthew. a) Beskriv populationens utveckling och förklara den med begreppen exponentiell tillväxt och bärförmåga. b) Förklara varför populationen inte planade ut som i en S-kurva. c) Hur hade utvecklingen troligen sett ut om det funnits vargar på ön?", 3),
 ("En ekologisk bonde gödslar inte med konstgödsel. I stället odlar hon klöver vartannat år på åkern och plöjer ner den. Förklara i flera steg hur det kan ge mer kväve till grödan nästa år. Diskutera också för- och nackdelar jämfört med konstgödsel för miljön.", 3),
 ("En gråsäl äter ungefär 5 kg fisk per dag. Använd tumregeln om 10 procent och gör en uppskattning av hur mycket djurplankton som krävs för en säls mat under ett år, om fisken den äter är strömming som äter djurplankton. Redovisa dina beräkningar och kommentera hur säker uppskattningen är.", 2),
 ("Förklara i minst tre led hur ett varmare klimat kan påverka fjällrävens möjligheter att överleva i Sverige. Använd begrepp från ekologin, till exempel livsmiljö, konkurrens, näringskedja och population.", 3),
 ("För att minska övergödningen i Östersjön föreslås två åtgärder: A) anlägga våtmarker där åkrarnas vatten rinner ut, eller B) förbjuda konstgödsel helt. Jämför åtgärderna utifrån effekt på övergödningen, konsekvenser för livsmedelsproduktionen och hur realistiska de är. Ta ställning.", 3),
 ("Kvicksilver har hittats i gädda från en skogssjö, trots att det knappt går att mäta i sjövattnet. Förklara varför och vad det kan betyda för människor som äter mycket insjöfisk.", 2),
]
def uppg_html():
    out = ['<section class="sec"><div class="sh"><h2>Resonera och ta ställning</h2></div>'
           '<p class="note">Uppgifterna motsvarar de svåraste uppgifterna på nationella prov. Svara utförligt och resonera i flera led. ● grundläggande &nbsp;●● utvecklat &nbsp;●●● välutvecklat</p>']
    for i, (q, p) in enumerate(UPG, 1):
        if i == 4:
            out.append('</section><section class="sec"><div class="sh"><h2>Resonera och ta ställning, forts.</h2></div>')
        out.append(f'<div class="q" style="break-inside:avoid;grid-template-columns:16pt minmax(0,1fr) 34pt"><span class="n">{i}</span><div>{q}{lines(7)}</div><span class="pts">{"●"*p}</span></div>')
    out.append('</section>')
    return "".join(out)

SVAR = [
 "a) Mycket föda och inga rovdjur gav exponentiell tillväxt från 29 till ca 6 000. Populationen växte långt över öns bärförmåga och åt upp de långsamt växande lavarna. b) Ingen broms (rovdjur, jakt) när populationen närmade sig bärförmågan, och fördröjningen mellan att lavarna tog slut och att renarna dog gjorde att de överskred den. En sträng vinter gav kraschen. Bärförmågan sjönk eftersom lavmattorna förstördes. c) Vargar hade ätit renar, så populationen hade vuxit långsammare och troligen pendlat kring en lägre nivå utan att förstöra lavarna.",
 "Klöverns rotknölar har kvävefixerande bakterier som tar kväve från luften. Kvävet byggs in i klöverns proteiner. När klövern plöjs ner bryter nedbrytare ner den och frigör kväveföreningar som nästa gröda tar upp. Fördelar: ingen energikrävande tillverkning av konstgödsel, bättre jordstruktur. Nackdelar: åkern ger ingen säljbar gröda det året, kväve kan läcka även här vid fel tidpunkt.",
 "5 kg/dag · 365 ≈ 1 800 kg strömming per år. Strömmingen behöver ca 10 gånger så mycket djurplankton: ca 18 000 kg (18 ton). Osäkert: 10 % är ett grovt genomsnitt, sälen äter flera fiskarter, och fisken äter också annat. Välutvecklat svar resonerar om vad osäkerheterna gör med svaret.",
 "T.ex.: varmare → trädgränsen flyttar upp → kalfjällets livsmiljö krymper. Varmare → rödräven sprider sig upp → konkurrens om lyor och föda, rödräven kan också döda fjällrävar. Fler töperioder → skare → lämlarna får svårt under snön → färre lämmelår → fjällrävarna får färre valpar → populationen minskar. Välutvecklat: kedjor i flera led och koppling till liten population/inavel.",
 "A: våtmarker fångar näringsämnen och partiklar och bakterier omvandlar kväve till kvävgas; påverkar inte livsmedelsproduktionen mycket; realistiskt men tar tid och mark, och löser inte allt. B: kraftig minskning av kväveläckage, men skördarna skulle sjunka mycket och maten kanske produceras någon annanstans med större påverkan; svårt att genomföra. Välutvecklat: kombination av åtgärder, och att fosfor från avlopp också spelar roll.",
 "Kvicksilver anrikas i näringskedjan: det stannar i kroppen och halten ökar i varje led. Gäddan står högt upp i näringskedjan och får därför hög halt. Människor som äter mycket rovfisk kan få i sig skadliga mängder, därför finns kostråd om att begränsa rovfisk som gädda, abborre och gös, särskilt för gravida.",
]
def teacher_html():
    sv = '<div class="cols2">' + "".join(f"<p><b>{i}.</b> {x}</p>" for i, x in enumerate(SVAR, 1)) + '</div>'
    bed = table(["", "Grundläggande", "Utvecklat", "Välutvecklat"], [
        ["Resonemang", "Enkla påståenden, ett led. Orsak eller verkan nämns.", "Orsak och verkan kopplas ihop i två led.", "Flera led i en sammanhängande kedja. Visar hur stegen hänger ihop."],
        ["Begrepp", "Några begrepp används, ibland oprecist.", "Relevanta begrepp används korrekt.", "Begreppen används korrekt och förklaras i sammanhanget."],
        ["Värdering", "Ger ett argument eller en åsikt.", "Ger argument för och emot.", "Väger argument mot varandra, visar osäkerheter och tar motiverat ställning."],
        ["Undersökningar", "Föreslår en enkel undersökning.", "Planerar med variabler och upprepningar.", "Värderar metoden, felkällor och hur säker slutsatsen kan bli."]])
    return ('<section class="sec teacher"><h2>Till läraren: facit och bedömningsstöd</h2>'
      '<p>Fördjupningen riktar sig till elever som är klara tidigt eller behöver mer utmaning. Den fördjupar det centrala innehållet om sambanden mellan populationer och tillgängliga resurser, materiens kretslopp och energins flöden samt människans påverkan på naturen, och tränar den typ av resonemang som krävs på högsta nivå i de nationella proven.</p>'
      '<h3>Svarsexempel</h3>' + sv + '</section>'
      '<section class="sec teacher"><h2>Till läraren: bedömning och svar på rutorna</h2><h3>Bedömningsstöd för resonemangsuppgifter</h3>' + bed +
      '<h3>Svar på rutorna i texten</h3><p><b>Tänk efter (F4.2):</b> Mat i överflöd ger tillväxt men säger inget om hur länge den räcker. Lavarna växer långsamt och förbrukades snabbare än de hann växa tillbaka, så bärförmågan sjönk.</p>'
      '<p><b>Räkna själv (F4.3):</b> Från djurplankton till havsörn är det tre steg: 1 kg · 10³ = 1 000 kg djurplankton. Ett steg till ger 10 000 kg växtplankton.</p>'
      '<p><b>Fundera (F4.4):</b> Skare och töväder gör att lämlarna får svårt att hitta mat och skydd under snön. Lämmelåren blir färre, fjällrävarna får färre valpar, och populationen kan minska. Det förstärks av konkurrensen från rödräven.</p>'
      '<h3>Faktakontroll och källor</h3><p class="note">Uppgifterna om St Matthew bygger på D. R. Klein (1968), The introduction, increase and crash of reindeer on St. Matthew Island; värdet för 1957 är ungefärligt. Siffran 78 % kväve i luften avser volymprocent. Uppgiften om 5 kg fisk per dag är en ungefärlig siffra för en vuxen gråsäl. Källor: Skolverket, Lgr22 kursplan i biologi. · SLU Artdatabanken, Rödlista 2025. · Livsmedelsverket, råd om fisk. · Illustrationer: egenritade.</p></section>')
