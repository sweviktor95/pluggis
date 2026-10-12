# -*- coding: utf-8 -*-
"""Område 4 Ekologi – grundtext (nya ramverket, per moment). Samma format som område 1."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
FIG = '/tmp/bio/fig04n/'
NR = 4
SLUG = "ekologi"
TAB = "4"
NAMN = "Ekologi"
UNDER = "Vem äter vem – och vart tar energin vägen?"
INTRO = ("En havsörn dyker ner mot en vik i Bottenviken och fångar en gädda. Gäddan har ätit abborrar, abborrarna har ätit djurplankton och djurplanktonen har ätit små alger som har fångat solljus. "
         "Allt levande hänger ihop i ett nät av beroenden. Läran om hur organismer samspelar med varandra och med sin miljö kallas <strong>ekologi</strong>. "
         "Namn och mätvärden i uppgifterna är påhittade, om inget annat står. Undersökningarna av van Helmont, Paine och Gause samt exemplen Yellowstone och St Matthew är verkliga.")
MAL = ["vad ekologi är och hur population, samhälle och ekosystem skiljer sig åt", "hur biotiska och abiotiska faktorer påverkar organismer",
       "vad producenter, konsumenter och nedbrytare gör och hur man tolkar näringskedjor och näringsvävar", "hur energin flödar genom ett ekosystem och varför den minskar i varje led",
       "att materien och kolet går i kretslopp och hur nedbrytning går till", "hur populationer förändras, vad som begränsar dem och hur arter samspelar"]
FUNDERA = "Vad åt du till lunch i dag? Försök följa maten bakåt ända till solen. Hur många steg blev det?"
DELOMR = {"4.1": "Ekosystem och energi", "4.2": "Materiens kretslopp", "4.3": "Populationer och samspel"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)
def cards4(items):
    return '<div class="cards" style="grid-template-columns:repeat(%d,1fr)">' % len(items) + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in items) + '</div>'

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Vad är ekologi?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p><strong class='green'>Ekologi</strong> kommer från grekiskans <em>oikos</em>, som betyder hus eller hem. Ekologer undersöker hur organismer lever i sitt ”hem”: vad de äter, vem som äter dem, vilka de konkurrerar med och hur de påverkas av till exempel temperatur, ljus och vatten. Ekologer studerar naturen på olika nivåer.</p>"
     "<p>En ekolog kan följa en enda individ, till exempel en skogshare, men också räkna alla harar i en skog eller undersöka hur skogen som helhet fungerar.</p>",
   [begrepp([("Ekologi", "Läran om samspelet mellan organismer och deras miljö."), ("Population", "Alla individer av en art inom ett område."),
             ("Samhälle", "Alla populationer av olika arter i samma område."), ("Ekosystem", "Samhället tillsammans med den livlösa miljön."),
             ("Biosfär", "Alla ekosystem på jorden tillsammans.")])])
 + fig(FIG+"ekologi-nivaer.png", "<b>Bild 4.1</b> Ekologins nivåer, från en enda individ till allt liv på jorden.")
 + bullets(["En <strong class='green'>population</strong> är alla individer av samma art som lever inom ett visst område, till exempel alla skogsharar i en skog.",
            "Ett <strong class='green'>samhälle</strong> är alla populationer av olika arter i samma område.",
            "Ett <strong class='green'>ekosystem</strong> är samhället tillsammans med den livlösa miljön: ljus, vatten, jord, luft och temperatur.",
            "<strong class='green'>Biosfären</strong> är alla ekosystem på jorden tillsammans – allt liv och alla platser där det finns liv."])
 + kolla("Start", ["Vad betyder ordet ekologi?", "Vad är skillnaden mellan en population och ett samhälle?", "Ge ett exempel på ett litet och ett stort ekosystem."]))

# ------------------------------------------------------------------ 4.1.1
add("4.1.1", "Vad är ett ekosystem?", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Vad är ett ekosystem?",
 "<p>Allt som påverkar en organism kallas <strong class='green'>faktorer</strong>. De delas in i två grupper:</p>"
 + cards4([("Biotiska faktorer", "Påverkan från andra levande organismer (bios = liv): föda, rovdjur, konkurrenter, sjukdomar och parasiter."),
           ("Abiotiska faktorer", "Påverkan från den livlösa miljön: temperatur, ljus, vatten, näringsämnen och vind.")])
 + row("<p>Varje art har en <strong class='green'>livsmiljö</strong>, platsen där den kan leva. En abborre behöver sjö- eller havsvatten med tillräckligt med syre. En fjällräv behöver kalla fjäll med lämlar och gamla lyor. En viss typ av livsmiljö, som barrskog, myr, sjö eller strandäng, kallas en <strong class='green'>biotop</strong>.</p>"
       "<p>Ett ekosystem kan vara stort, som en hel skog eller ett hav, eller litet, som en vattenpöl eller en murken stubbe. Det som gör något till ett ekosystem är att organismerna och den livlösa miljön hänger ihop.</p>",
       [begrepp([("Biotisk faktor", "Påverkan från andra levande organismer."), ("Abiotisk faktor", "Påverkan från den livlösa miljön."),
                 ("Livsmiljö", "Platsen där en art lever."), ("Biotop", "En typ av livsmiljö, till exempel barrskog, myr eller sjö.")]),
        box("tank", "Tänk efter", "<p>Är ett ekosystem alltid stort? Kan en vattenpöl, en murken stubbe eller din tarm vara ett ekosystem?</p>")])
 + "<h3>Ekosystem ser olika ut – men fungerar likadant</h3>"
 + fig(FIG+"ekologi-ekosystem.png", "<b>Bild 4.2</b> Två ekosystem i Norrbotten och två i andra delar av världen.")
 + table(["", "Barrskog i Norrbotten", "Bottenviken", "Tropisk regnskog", "Savann"],
         [["Klimat", "Kalla vintrar, kort sommar med ljusa nätter", "Kallt bräckt vatten, is på vintern", "Varmt och regnigt hela året", "Varmt, regnperiod och torrperiod"],
          ["Producenter", "Tall, gran, björk, bärris, mossor, lavar", "Växtplankton, alger, vass", "Höga lövträd, lianer", "Gräs, spridda träd som akacior"],
          ["Konsumenter", "Älg, skogshare, tjäder, lodjur, björn", "Djurplankton, sik, abborre, gädda, säl, havsörn", "Insekter, apor, fåglar, ormar, jaguar", "Zebror, gnuer, giraffer, lejon"],
          ["Artrikedom", "Måttlig", "Låg – få arter klarar bräckt vatten", "Mycket hög", "Hög, särskilt stora däggdjur"]])
 + "<p>Ekosystemen ser olika ut beroende på klimat, ljus, vatten och jord. Men de fungerar efter samma principer: producenter fångar solenergi, konsumenter äter, nedbrytare tar hand om det döda och materien går i kretslopp. Ekosystemen hänger också ihop över hela jorden. Flyttfåglar som häckar i Norrbotten övervintrar i Afrika, och laxen vandrar mellan älvarna och havet.</p>"
 + kolla("4.1.1", ["Ge två biotiska och två abiotiska faktorer som påverkar en gädda.", "Varför räknas vattnet och solljuset till ekosystemet?", "Välj två ekosystem i tabellen. Beskriv en skillnad och en likhet mellan dem."]))

# ------------------------------------------------------------------ 4.1.2
add("4.1.2", "Producenter, konsumenter och näringsvävar", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Producenter, konsumenter och näringsvävar",
 "<p>I kapitel 2 lärde du dig att växter gör fotosyntes och att alla celler behöver energi från cellandning. Nu ska vi se vad det betyder för ett helt ekosystem. Organismerna kan delas in i tre grupper efter hur de får sin energi och näring.</p>"
 + cards4([("Producenter", "Gröna växter, alger och växtplankton. De bygger sin egen näring med fotosyntes och är grunden i alla näringskedjor."),
           ("Konsumenter", "Djur som äter andra organismer. Växtätare äter producenter, rovdjur äter andra djur och allätare äter både och."),
           ("Nedbrytare", "Svampar och bakterier som bryter ner döda växter och djur, avföring och nedfallna löv. De frigör näringsämnen som växterna kan använda igen.")])
 + "<h3>Näringskedjor</h3>"
 + "<p>En <strong class='green'>näringskedja</strong> visar vem som äter vem. Varje steg i kedjan kallas ett led. Pilarna ritas från den som blir uppäten till den som äter, alltså åt samma håll som energin går. Den som står först i kedjan är alltid en producent.</p>"
 + fig(FIG+"ekologi-kedja.png", "<b>Bild 4.3</b> En näringskedja i Bottenviken. Konsumenterna numreras efter hur många steg de står från producenterna.")
 + row("<p>Djurplankton äter växtplankton och är därför <em>första ordningens konsument</em>, en växtätare. Abborren äter djurplankton och är <em>andra ordningens konsument</em>. Havsörnen har inga naturliga fiender och kallas <strong class='green'>toppkonsument</strong>.</p>"
       "<p>Många djur kan stå på flera led. En björn äter både blåbär och älgkalvar. En människa som äter en sallad är första ordningens konsument, men när hon äter en köttbit är hon andra eller tredje ordningens konsument.</p>",
       [box("visste", "Visste du?", "<p>Detritusätare som daggmaskar, gråsuggor och hoppstjärtar äter döda växtdelar. De hackar sönder materialet så att svampar och bakterier kan bryta ner det snabbare.</p>")])
 + "<h3>Näringsvävar</h3>"
 + "<p>I verkligheten äter de flesta djur flera olika saker och blir uppätna av flera olika rovdjur. Näringskedjorna korsar varandra och bildar en <strong class='green'>näringsväv</strong>. En näringsväv visar bättre hur ett ekosystem verkligen fungerar.</p>"
 + fig(FIG+"ekologi-vav.png", "<b>Bild 4.4</b> En förenklad näringsväv i en sjö eller vik. Pilarna visar åt vilket håll energin går.")
 + roww("<p>Om en art försvinner påverkas alla som hänger ihop med den. Om abborrarna fiskas bort får gäddan mindre mat. Samtidigt blir det fler djurplankton och insektslarver, eftersom färre äter dem. Ju fler kopplingar det finns i väven, desto lättare kan ekosystemet klara en förändring.</p>"
        "<p>I nationalparken Yellowstone i USA utrotades vargarna under 1920-talet. Hjortarna blev många och betade hårt på unga träd och buskar längs vattendragen. År 1995 släpptes vargar ut igen, och forskare såg att träd och buskar kunde växa upp på vissa platser. När en förändring högst upp i en näringskedja sprider sig nedåt genom flera nivåer kallas det en <strong class='green'>kaskadeffekt</strong>. Forskarna diskuterar fortfarande hur stor vargarnas betydelse var jämfört med andra orsaker, till exempel klimat och jakt.</p>",
        [begrepp([("Näringskedja", "Visar vem som äter vem."), ("Näringsväv", "Flera näringskedjor som hänger ihop."), ("Toppkonsument", "Djur högst upp i näringskedjan, utan naturliga fiender."),
                  ("Kaskadeffekt", "En förändring som sprider sig genom flera nivåer i en näringsväv.")]),
         box("tank", "Tänk efter", "<p>Använd bild 4.4. Vad händer med insektslarverna om knipan försvinner? Vad händer då med vattenväxterna?</p>")])
 + kolla("4.1.2", ["Varför står alltid en producent först i en näringskedja?", "Rita en näringskedja med fyra led från en skog. Skriv vilka som är producent och konsumenter.",
                   "Vad skulle hända i en skog om alla nedbrytare försvann?", "Förklara varför en näringsväv visar mer än en näringskedja."]))

# ------------------------------------------------------------------ 4.1.3
add("4.1.3", "Energiflöde och biomassa", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Energiflöde och biomassa",
 "<p>Nästan all energi i ett ekosystem kommer från solen. Producenterna fångar en liten del av solljuset med fotosyntesen och lagrar energin i glukos och andra ämnen. När en växtätare äter växten förs en del av energin vidare. Men det mesta av energin förs inte vidare.</p>"
 + roww("<h3 style='margin-top:0'>Varför försvinner energi i varje led?</h3>"
        + bullets(["Organismen använder energi för att leva: röra sig, hålla värmen och laga celler. Det mesta blir till slut värme.", "Allt äts inte upp: rötter, ben, päls och fjädrar blir kvar.", "Allt som äts tas inte upp i kroppen, utan lämnar den som avföring."])
        + "<p>Som en tumregel förs bara omkring <strong class='green'>10 procent</strong> av energin vidare till nästa led. Resten går förlorad som värme eller hamnar hos nedbrytarna. Man brukar rita det som en <strong class='green'>energipyramid</strong>.</p>"
        "<p>Energi går alltså inte i kretslopp, den <strong class='green'>flödar</strong> genom ekosystemet: in som solljus och ut som värme. Därför behövs ett ständigt tillskott av solenergi.</p>",
        [fig(FIG+"ekologi-pyramid.png", "<b>Bild 4.5</b> En energipyramid. Bara ungefär en tiondel av energin förs vidare till nästa nivå.")])
 + "<h3>Biomassa</h3>"
 + row("<p><strong class='green'>Biomassa</strong> är den sammanlagda vikten av levande organismer, till exempel alla växter på en kvadratmeter. Ofta mäter man torrvikten, alltså vikten när vattnet är borta. Eftersom energin minskar uppåt i kedjan minskar också biomassan: en skog har mycket mer växtmaterial än växtätare, och mer växtätare än rovdjur. Man kan därför rita pyramider både för energi och för biomassa.</p>"
       "<h3>Vad betyder det?</h3><p><strong>Därför är näringskedjor korta.</strong> Efter fyra eller fem led finns det för lite energi kvar för ytterligare ett led. Därför finns det många fler harar än lodjur och många fler växtplankton än havsörnar. Toppkonsumenter behöver stora områden för att hitta tillräckligt med mat.</p>"
       "<p><strong>Mat och hållbarhet.</strong> Om vi äter växtmat direkt tar vi vara på mer av den energi växterna har fångat. När djur föds upp på foder går en stor del av energin förlorad på vägen. Därför kan samma åkermark föda fler människor om en större del av maten är växtbaserad.</p>",
       [begrepp([("Energiflöde", "Energin går in som solljus och ut som värme. Den går inte i kretslopp."), ("Energipyramid", "Bild som visar hur energin minskar för varje nivå."), ("Biomassa", "Vikten av levande organismer, ofta mätt som torrvikt.")]),
        box("visste", "Bra att veta", "<p>10 procent är ett grovt genomsnitt. I verkligheten varierar värdet mellan olika ekosystem och organismer, ofta mellan 5 och 20 procent.</p>")])
 + kolla("4.1.3", ["Varifrån kommer nästan all energi i ett ekosystem?", "Ge två förklaringar till varför energi försvinner mellan leden.", "Varför finns det färre rovdjur än växtätare i en skog?", "Vad menas med biomassa, och hur ändras den uppåt i en näringskedja?"]))

# ------------------------------------------------------------------ Labb 4.1
add("Labb", "4.1 Energi i en näringskedja – modellspel", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Labb 4.1 Energi i en näringskedja",
 "<p>Du ska bygga en modell av hur energin minskar i en näringskedja. Riset i skålarna föreställer energi, och varje skål föreställer ett led i kedjan. Modellen är en förenkling: verkliga ekosystem är mer komplicerade, men modellen visar principen.</p>"
 + roww("<p><strong class='green'>Frågeställning:</strong> Hur mycket energi når toppkonsumenten i en näringskedja med fyra led?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror och motivera.</p>"
        "<p><strong class='green'>Material:</strong> 1 000 g ris eller torkade ärtor (energin), våg som mäter i gram, fem skålar märkta Producent, Växtätare, Rovdjur, Toppkonsument och Värme, papper och penna.</p><h3>Gör så här</h3>"
        + steps(["Väg upp 1 000 g ris i skålen Producent. Det är all energi som växterna har fångat från solen.", "Växtätaren äter producenterna. Flytta 10 procent av riset (100 g) till skålen Växtätare. Resten (900 g) hälls i skålen Värme.",
                 "Rovdjuret äter växtätaren. Flytta 10 procent av växtätarens ris (10 g) till skålen Rovdjur och resten till Värme.", "Toppkonsumenten äter rovdjuret. Flytta 10 procent av rovdjurets ris (1 g) till skålen Toppkonsument och resten till Värme.",
                 "Fyll i tabellen. Gör sedan om försöket med 20 procent i stället för 10 procent."]),
        [table(["Led", "Ris (g) vid 10 %", "Ris (g) vid 20 %"], [["Producent", "1 000", "1 000"], ["Växtätare", "", ""], ["Rovdjur", "", ""], ["Toppkonsument", "", ""]], "tbl num"),
         box("begrepp", "Modellen", "<b class='t'>Ris</b><p>Energi.</p><b class='t'>Skål</b><p>Ett led i kedjan.</p><b class='t'>Värmeskålen</b><p>Energi som använts och blivit värme.</p>"),
         box("tank", "Utvärdera", "<p>Hur många procent av producenternas energi når toppkonsumenten? Varför kan en näringskedja sällan ha tio led? Vad förenklar modellen?</p>")])
 + '<p class="note">Säkerhet: låg risk. Ät inte riset och torka upp spill så att ingen halkar.</p>')

# ------------------------------------------------------------------ 4.2.1
add("4.2.1", "Materia tillverkas inte och försvinner inte", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Materia tillverkas inte och försvinner inte",
 "<p>Energin flödar igenom ekosystemet och försvinner som värme. Men <strong class='green'>materien</strong> – alla atomer som organismer är byggda av – försvinner aldrig. Samma kolatomer, kväveatomer och vattenmolekyler används om och om igen. Atomerna i din kropp har en gång funnits i växter, djur, luft och hav. Materien går i <strong class='green'>kretslopp</strong>.</p>"
 + table(["", "Energi", "Materia"], [["Vägen", "Flödar genom ekosystemet: in som solljus, ut som värme.", "Går runt i ett kretslopp: används om och om igen."], ["Behövs det nytt?", "Ja, hela tiden. Solen ger ny energi.", "Nej. Atomerna finns redan, de byter bara plats."], ["Exempel", "Solljus → växt → hare → värme", "Kol: luft → växt → hare → nedbrytare → luft"]], "tbl")
 + "<h3>Varifrån kommer växtens vikt?</h3>"
 + row("<p>Många tror att växter blir stora av att ta upp jord. Det stämmer inte. På 1600-talet planterade den belgiske läkaren Jan Baptist van Helmont en pilgren som vägde 5 pund i en kruka med 200 pund torkad jord. Han vattnade den i fem år. Då vägde trädet drygt 169 pund, men jorden hade bara blivit ungefär 2 uns lättare.</p>"
       "<p>Van Helmont drog slutsatsen att trädets vikt kom från vattnet. Vi vet i dag att den största delen kommer från <strong>koldioxid i luften</strong>. Genom fotosyntesen bygger växten in kolet från koldioxid och väte och syre från vatten i glukos. Växten är alltså till största delen byggd av luft och vatten, och bara lite av jorden.</p>",
       [box("visste", "Bra att veta", "<p>Van Helmonts försök är ett bra exempel på en undersökning med kontroll: han vägde både trädet och jorden. Ändå kom han delvis fel, eftersom ingen då visste att luften innehåller koldioxid.</p>")])
 + "<h3>Vattnets kretslopp</h3>"
 + row("<p>Även vattnet går runt. Solen värmer havet och vattnet <strong>avdunstar</strong>. Högre upp svalnar ångan och bildar moln (<strong>kondensation</strong>). Vattnet faller som <strong>nederbörd</strong> och rinner tillbaka till sjöar och hav. Växter tar upp vatten med rötterna och avger en del som vattenånga genom bladen.</p>",
       [begrepp([("Materia", "Det atomerna och molekylerna är gjorda av. Den försvinner inte och tillverkas inte i ekosystemet."), ("Kretslopp", "När ämnen används om och om igen i naturen.")])])
 + kolla("4.2.1", ["Vad är skillnaden mellan hur energi och materia rör sig i ett ekosystem?", "Van Helmonts pilträd växte från 5 till drygt 169 pund medan jorden bara förlorade ungefär 2 uns. Varifrån kom nästan all vikt?", "Beskriv vattnets kretslopp i tre steg."]))

# ------------------------------------------------------------------ 4.2.2
add("4.2.2", "Kolets kretslopp", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Kolets kretslopp",
 "<p>Kol finns i allt levande: i proteiner, fett, kolhydrater och DNA. Kolet rör sig mellan luften, levande organismer och marken i ett kretslopp.</p>"
 + fig(FIG+"ekologi-kol.png", "<b>Bild 4.6</b> Kolets kretslopp, förenklat. Pilarna visar hur kol rör sig mellan luften, levande organismer och marken.")
 + row("<h3>Så går kolet runt</h3>"
       + steps(["<strong>Fotosyntes:</strong> Växter tar upp koldioxid från luften och bygger in kolet i glukos.", "<strong>Näringskedjan:</strong> Kolet förs vidare till djur som äter växterna.",
                "<strong>Cellandning:</strong> Växter och djur släpper ut koldioxid när de använder glukosen.", "<strong>Nedbrytning:</strong> När organismer dör bryter nedbrytarna ner dem. Då frigörs koldioxid och näringsämnen.",
                "<strong>Förbränning:</strong> Kol som har legat lagrat i miljontals år som olja, kol och naturgas släpps ut när människan bränner det."]),
       [box("klimat", "Klimatet", "<p>När vi bränner fossila bränslen släpper vi ut mer koldioxid än växterna och haven hinner ta upp. Halten i luften ökar och förstärker växthuseffekten. Mer om det i område 5.</p>"),
        box("kvave", "Även kväve", "<p>Växter behöver kväve för att bygga proteiner. Nedbrytarna frigör kväve ur döda organismer, och vissa bakterier kan ta kväve direkt från luften.</p>")])
 + kolla("4.2.2", ["Beskriv två processer som tar kol från luften och två som släpper ut kol till luften.", "Vad händer med kolet i ett träd som dör i skogen?", "Varför kallas det ett kretslopp och inte ett flöde?"]))

# ------------------------------------------------------------------ 4.2.3
add("4.2.3", "Nedbrytning", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Nedbrytning",
 "<p>Utan nedbrytning skulle döda löv, träd och djur bli liggande för alltid, och växterna skulle ta slut på näring. <strong class='green'>Nedbrytning</strong> betyder att dött material bryts ner till enklare ämnen som kan användas igen.</p>"
 + roww("<p>Jobbet görs av flera grupper tillsammans. <strong class='green'>Detritusätare</strong> som daggmaskar, gråsuggor och hoppstjärtar äter döda växtdelar och hackar sönder dem. <strong class='green'>Nedbrytare</strong>, alltså svampar och bakterier, tar sedan hand om resten. De gör cellandning på det döda materialet och frigör koldioxid, vatten och näringsämnen som kväve och fosfor. Dessa ämnen tar växterna upp igen.</p>"
        "<p>Döda löv och barr som ligger på marken kallas <strong class='green'>förna</strong>. I förnan lever tusentals små djur och mikroorganismer.</p>",
        [begrepp([("Nedbrytare", "Svampar och bakterier som bryter ner dött material."), ("Detritusätare", "Djur som äter döda växtdelar och hackar sönder dem."), ("Förna", "Döda löv och barr som ligger på marken.")]),
         box("visste", "Visste du?", "<p>En kompost kan bli varm, ofta över 50 °C. Värmen kommer från nedbrytarnas cellandning.</p>")])
 + "<h3>Vad påverkar hur snabbt det går?</h3>"
 + table(["Faktor", "Effekt", "Exempel"],
         [["Temperatur", "Varmt ger snabbare nedbrytning, kallt ger långsammare.", "Löv bryts ner snabbare i södra Sverige än i Norrbotten."], ["Fukt", "Nedbrytare behöver vatten. Det kan vara för torrt.", "Torr förna ligger kvar länge."],
          ["Syre", "De flesta nedbrytare behöver syre. Utan syre går det mycket långsamt.", "Dött material på en syrefri havsbotten bryts ner långsamt."], ["Materialet", "Mjuka löv bryts ner fortare än trä, barr och ben.", "Björklöv försvinner snabbare än ett grenvirke."]])
 + roww("<p>I barrskogen i Norrbotten bryts löv och barr ner långsamt eftersom det är kallt. Därför bildas tjocka lager av förna och torv. I den tropiska regnskogen går nedbrytningen så fort att näringen nästan direkt tas upp av växterna igen. Jorden i sig är därför ofta näringsfattig, trots att skogen är så rik.</p>",
        [box("tank", "Tänk efter", "<p>Varför är det bra att en kompost luftas och hålls lagom fuktig?</p>")])
 + kolla("4.2.3", ["Varför är nedbrytare viktiga för kretsloppet?", "Ge två faktorer som gör nedbrytningen snabbare eller långsammare. Förklara hur de påverkar.", "Varför är jorden i en regnskog ofta näringsfattig, trots att det växer så mycket där?"]))

# ------------------------------------------------------------------ Labb 4.2
add("Labb", "4.2 Nedbrytning i jord", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Labb 4.2 Nedbrytning i jord",
 "<p>Nedbrytarna arbetar i det tysta, men deras arbete går att mäta. Du gräver ner tepåsar och väger hur mycket som har brutits ner. Metoden används även av riktiga forskare för att jämföra nedbrytning i olika jordar.</p>"
 + fig(FIG+"ekologi-tepasar.png", "<b>Bild 4.7</b> Tepåsar nedgrävda i tre olika jordar.", "62%")
 + roww("<p><strong class='green'>Frågeställning:</strong> I vilken jord bryts organiskt material ner snabbast?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror och motivera med det du vet om nedbrytare.</p>"
        "<p><strong class='green'>Material:</strong> tepåsar med grönt te eller rooibos (utan snöre av plast), våg, spritpenna, glasspinnar som markörer, spade, tre olika platser eller krukor med olika jord.</p><h3>Gör så här</h3>"
        + steps(["Märk och väg varje tepåse. Skriv upp vikten.", "Gräv ner tre påsar på varje plats, 8 cm djupt. Märk platsen.", "Låt påsarna ligga kvar tills läraren säger till. (I kruka inomhus: håll jorden fuktig.)", "Gräv upp påsarna, borsta av jorden och låt dem torka.", "Väg igen och räkna ut hur många procent som har försvunnit."]),
        [table(["Plats", "Före (g)", "Efter (g)", "Förlust (%)"], [["Skogsjord", "", "", ""], ["Gräsmatta", "", "", ""], ["Sand", "", "", ""]], "tbl num"),
         box("begrepp", "Variabler", "<b class='t'>Oberoende</b><p>Typ av jord.</p><b class='t'>Beroende</b><p>Hur mycket av teet som har brutits ner.</p><b class='t'>Kontrollerade</b><p>Samma sorts te, samma djup, lika länge i jorden.</p>"),
         box("tank", "Utvärdera", "<p>Var gick nedbrytningen snabbast? Vilka abiotiska faktorer kan förklara skillnaden – fukt, temperatur, syre? Varför ska man ha tre påsar på varje plats?</p>")])
 + '<p class="note">Säkerhet: tvätta händerna efter jordarbete. Samla in alla påsar och markörer så att inget blir kvar i naturen.</p>')

# ------------------------------------------------------------------ 4.3.1
add("4.3.1", "Populationer och förändring", f"Kapitel {NR} · Delområde 4.3 {DELOMR['4.3']} · Populationer och förändring",
 "<p>En <strong class='green'>population</strong> är alla individer av en art inom ett område. Antalet individer ändras hela tiden. Fyra saker avgör hur:</p>"
 + cards4([("Födda", "Nya individer föds eller kläcks."), ("Döda", "Individer dör av ålder, sjukdom, svält eller rovdjur."), ("Inflyttning", "Individer flyttar in från andra områden."), ("Utflyttning", "Individer flyttar ut.")])
 + "<p>Om det föds och flyttar in fler än det dör och flyttar ut, växer populationen. Annars minskar den.</p>"
 + "<h3>Lämmelår</h3>"
 + roww("<p>I fjällen varierar antalet lämlar kraftigt. Vissa år blir de enormt många, ett lämmelår, och sedan kraschar populationen. Fjällräven, som lever mest av lämlar, får många valpar under lämmelår och nästan inga under år med lite mat. Därför ökar antalet fjällrävar efter ett lämmelår. Rovdjurens antal följer alltså bytesdjurens, med en liten fördröjning.</p>",
        [fig(FIG+"ekologi-lamlar.png", "<b>Bild 4.8</b> Antalet lämlar och fjällrävar varierar i cykler. Kurvorna är förenklade.")])
 + row("<p>Om en population har gott om mat, plats och inga fiender kan den växa snabbt. Men ingen population kan växa hur länge som helst.</p>",
       [begrepp([("Population", "Alla individer av en art inom ett område."), ("Lämmelår", "Ett år då lämlarna blir ovanligt många, följt av en kraftig minskning.")])])
 + kolla("4.3.1", ["Vilka fyra saker avgör hur en populations storlek ändras?", "Titta på bild 4.8. Varför kommer topparna för fjällrävarna lite efter topparna för lämlarna?",
                   "I början av året finns det 200 harar i en skog. Under året föds 150, 120 dör, 20 flyttar in och 30 flyttar ut. Hur många harar finns det i slutet av året?"]))

# ------------------------------------------------------------------ 4.3.2
add("4.3.2", "Begränsande faktorer", f"Kapitel {NR} · Delområde 4.3 {DELOMR['4.3']} · Begränsande faktorer",
 "<p>Förr eller senare tar någon <strong class='green'>resurs</strong> slut – mat, vatten, boplatser eller ljus. Det finns alltid något som begränsar hur stor en population kan bli. Det kallas en <strong class='green'>begränsande faktor</strong>. Det största antal individer som miljön kan försörja under lång tid kallas miljöns <strong class='green'>bärkraft</strong>.</p>"
 + table(["Faktor", "Typ", "Så begränsar den"],
         [["Tillgång på föda och vatten", "Biotisk (maten är levande) eller abiotisk (vattnet)", "Mer mat ger fler ungar som överlever. Brist ger svält."], ["Rovdjur", "Biotisk", "Många rovdjur håller nere antalet bytesdjur."],
          ["Konkurrens", "Biotisk", "Arter som behöver samma resurs tävlar om den."], ["Sjukdomar och parasiter", "Biotisk", "Sprids lättare när det är trångt."], ["Väder", "Abiotisk", "En kall vår eller en torr sommar kan slå ut många individer."]], "tbl")
 + row("<p>Faktorerna samverkar. En ovanligt snörik vinter (abiotisk) kan göra att rådjuren har svårt att nå föda. Då blir konkurrensen om maten hårdare (biotisk), och många djur svälter. Bärkraften är inte konstant: den ändras med väder, årstid och miljö.</p>"
       "<p>Om en population växer långt över bärkraften kan den förstöra sin egen föda. Då kan den krascha, och bärkraften kan bli lägre än förut.</p>",
       [begrepp([("Resurs", "Något en organism behöver, till exempel mat, vatten, boplats eller ljus."), ("Begränsande faktor", "Något som sätter en gräns för hur stor en population kan bli."), ("Bärkraft", "Det största antal individer som miljön kan försörja under lång tid.")]),
        box("tank", "Tänk efter", "<p>Du släpper ut 10 kaniner på en liten ö utan rovdjur. Vad kommer att begränsa populationen efter några år?</p>")])
 + kolla("4.3.2", ["Ge tre faktorer som kan begränsa hur stor en population blir.", "Vad menas med bärkraft?", "Förklara hur en snörik vinter kan påverka en population av rådjur."]))

# ------------------------------------------------------------------ 4.3.3
add("4.3.3", "Konkurrens, jakt och samarbete", f"Kapitel {NR} · Delområde 4.3 {DELOMR['4.3']} · Konkurrens, jakt och samarbete",
 "<p>Arter påverkar varandra på olika sätt. Man brukar skilja på fyra sorters samspel.</p>"
 + cards4([("Jakt", "Rovdjuret tjänar, bytet förlorar. Lodjur och skogshare är ett exempel."), ("Konkurrens", "Båda förlorar lite. Rödräv och fjällräv konkurrerar om både mat och lyor."),
           ("Parasitism", "Parasiten tjänar, värden förlorar. En fästing suger blod från sin värd."), ("Symbios", "Båda tjänar på samarbetet. En lav är en svamp och en alg som lever tillsammans: algen gör fotosyntes, svampen skyddar och håller kvar vatten.")])
 + "<h3>Livsmiljö och nisch</h3>"
 + row("<p>Alla arter har en livsmiljö, platsen där de kan leva. Men varje art har också en egen roll i ekosystemet. Det kallas artens <strong class='green'>nisch</strong>: vad den äter, var och när den söker mat, var den bor och vilka den påverkar. Nischen är ungefär artens ”yrke”, medan livsmiljön är dess ”adress”.</p>"
       "<p>Två arter som har exakt samma nisch konkurrerar hårt, och ofta blir det bara en av dem som klarar sig. Därför har arter som lever på samma plats ofta olika nischer. Ju fler olika nischer det finns, desto fler arter får plats.</p>",
       [begrepp([("Nisch", "Artens roll i ekosystemet: vad den äter, var och när den söker mat och hur den påverkar andra."), ("Konkurrens", "När organismer tävlar om samma resurs."), ("Symbios", "Samarbete där båda arterna tjänar på det.")]),
        box("tank", "Tänk efter", "<p>Du och din granne bor på samma gata men har olika yrken. Vad motsvarar gatan, och vad motsvarar yrket, i ekologins ord?</p>")])
 + fig(FIG+"ekologi-nisch.png", "<b>Bild 4.9</b> Två småfåglar i samma gran. De söker föda på olika ställen och har därför olika nischer.", "78%")
 + kolla("4.3.3", ["Vad är skillnaden mellan konkurrens och symbios?", "Vad är skillnaden mellan en arts livsmiljö och dess nisch?", "Varför kan flera fågelarter leva i samma gran utan att konkurrera ut varandra?"]))

# ------------------------------------------------------------------ Labb 4.3
add("Labb", "4.3 Rovdjur–bytesmodell", f"Kapitel {NR} · Delområde 4.3 {DELOMR['4.3']} · Labb 4.3 Rovdjur–bytesmodell",
 "<p>Du ska bygga en modell av hur en rovdjurspopulation och en bytespopulation påverkar varandra. Pappersbitar föreställer bytesdjur, och några av er är rovdjur. Modellen förenklar verkligheten, men den visar samma mönster som lämlar och fjällrävar.</p>"
 + roww("<p><strong class='green'>Frågeställning:</strong> Hur förändras antalet rovdjur och bytesdjur från omgång till omgång?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror och motivera.</p>"
        "<p><strong class='green'>Material:</strong> 40 pappersbitar eller bönor (byten), ett bord eller en markerad yta, stoppur, papper och penna.</p><h3>Gör så här</h3>"
        + steps(["Börja med 20 bytesdjur utspridda på ytan och 2 rovdjur (elever).", "Varje rovdjur plockar bytesdjur med pekfinger och tumme i 10 sekunder. Räkna hur många varje rovdjur fångade.",
                 "Ett rovdjur som fångat färre än 3 svälter och lämnar spelet. Ett rovdjur som fångat 6 eller fler får en unge: en ny elev blir rovdjur i nästa omgång.", "De bytesdjur som finns kvar förökar sig. Lägg dit lika många nya som det finns kvar, men aldrig fler än 40 totalt (så mycket föda finns).",
                 "Skriv in siffrorna i tabellen. Gör åtta omgångar. Rita sedan ett linjediagram med omgång på x-axeln och antal på y-axeln, med en linje för rovdjur och en för byten."]),
        [table(["Omgång", "Rovdjur", "Byten före", "Fångade", "Byten efter"], [["1", "2", "20", "", ""], ["2", "", "", "", ""], ["3", "", "", "", ""], ["4", "", "", "", ""]], "tbl num"),
         box("begrepp", "Variabler", "<b class='t'>Oberoende</b><p>Antal rovdjur och byten i början av en omgång.</p><b class='t'>Beroende</b><p>Antal fångade och antal i nästa omgång.</p><b class='t'>Lika</b><p>Tid, yta, sättet att plocka.</p>"),
         box("tank", "Utvärdera", "<p>Jämför ert diagram med bild 4.8. Vad är lika och vad skiljer? Hur kan du ändra modellen så att den liknar verkligheten mer, till exempel med gömställen (lägg papper över några byten)? Vad förenklar modellen?</p>")])
 + '<p class="note">Säkerhet: låg risk. Ingen får springa. Plocka upp alla pappersbitar efteråt.</p>')

SAMMAN = ["<strong>Ekologi</strong> handlar om hur organismer samspelar med varandra och med sin miljö, från individ och population till ekosystem och biosfär.",
          "Organismer påverkas av <strong>biotiska faktorer</strong> (andra organismer) och <strong>abiotiska faktorer</strong> (ljus, temperatur, vatten). Ekosystem ser olika ut men fungerar efter samma principer.",
          "<strong>Producenter</strong> gör fotosyntes, <strong>konsumenter</strong> äter andra organismer och <strong>nedbrytare</strong> bryter ner det döda.",
          "<strong>Näringskedjor</strong> visar vem som äter vem. Flera kedjor tillsammans bildar en <strong>näringsväv</strong>. En förändring kan sprida sig som en <strong>kaskadeffekt</strong>.",
          "<strong>Energin flödar</strong> genom ekosystemet. Bara cirka 10 % förs vidare till nästa led, resten blir värme. Biomassan minskar också uppåt i kedjan.",
          "<strong>Materien går i kretslopp.</strong> Växtens vikt kommer mest från koldioxid i luften och vatten. Kol rör sig mellan luften, organismer och marken genom fotosyntes, cellandning, nedbrytning och förbränning.",
          "<strong>Nedbrytare</strong> och detritusätare gör döda organismer till näring. Hastigheten beror på temperatur, fukt, syre och material.",
          "Populationers storlek avgörs av födda, döda, inflyttning och utflyttning, och <strong>begränsas</strong> av resurser, rovdjur, konkurrens och sjukdomar. Miljön har en <strong>bärkraft</strong>.",
          "Arter samspelar genom jakt, konkurrens, parasitism och <strong>symbios</strong>. Varje art har en egen <strong>nisch</strong>."]

BEGR = [("Abiotisk faktor", "Påverkan från den livlösa miljön, t.ex. ljus och temperatur."), ("Begränsande faktor", "Något som sätter en gräns för en populations storlek."), ("Biomassa", "Vikten av levande organismer, ofta mätt som torrvikt."),
        ("Biosfär", "Alla ekosystem på jorden tillsammans."), ("Biotisk faktor", "Påverkan från andra organismer."), ("Biotop", "En typ av livsmiljö, t.ex. barrskog eller sjö."), ("Bärkraft", "Det största antal individer som miljön kan försörja under lång tid."),
        ("Detritusätare", "Djur som äter döda växtdelar och hackar sönder dem."), ("Ekologi", "Läran om samspelet mellan organismer och deras miljö."), ("Ekosystem", "Organismerna och den livlösa miljön i ett område."),
        ("Energiflöde", "Energin går in som solljus och ut som värme."), ("Energipyramid", "Bild som visar hur energin minskar för varje nivå."), ("Förna", "Döda löv och barr på marken."), ("Kaskadeffekt", "En förändring som sprider sig genom flera nivåer."),
        ("Konkurrens", "När organismer tävlar om samma resurs."), ("Konsument", "Organism som äter andra organismer."), ("Kretslopp", "När ämnen används om och om igen i naturen."), ("Livsmiljö", "Platsen där en art lever."),
        ("Materia", "Det som atomer och molekyler bygger upp. Den försvinner inte."), ("Nedbrytare", "Svampar och bakterier som bryter ner dött material."), ("Nisch", "Artens roll i ekosystemet."), ("Näringskedja", "Visar vem som äter vem."),
        ("Näringsväv", "Flera näringskedjor som hänger ihop."), ("Population", "Alla individer av en art inom ett område."), ("Producent", "Organism som gör sin egen näring genom fotosyntes."), ("Symbios", "Samarbete där båda arterna tjänar på det."),
        ("Toppkonsument", "Djur högst upp i näringskedjan.")]

TEST = [
 ("A", "Vilken organism är en producent?", ["A Flugsvamp", "B Växtplankton", "C Daggmask", "D Abborre"], 1, 0),
 ("A", "Vad händer med det mesta av energin när en hare äter gräs?", ["A Den lagras i harens kropp och förs vidare till räven.", "B Den används av haren för att leva och blir till slut värme.", "C Den går tillbaka till gräset som näring.", "D Den förvandlas till syre."], 1, 0),
 ("A", "Vilket påstående om kretslopp stämmer?", ["A Både energi och materia går i kretslopp.", "B Energi går i kretslopp, men materia flödar igenom.", "C Materia går i kretslopp, men energi flödar igenom.", "D Varken energi eller materia går i kretslopp."], 1, 0),
 ("A", "Vilken är en abiotisk faktor som påverkar en björkskog?", ["A Älgar som äter bark", "B Svampar som angriper stammen", "C Antalet soltimmar på sommaren", "D Fåglar som bygger bon"], 1, 0),
 ("B", "Rita en näringskedja med fyra led från en sjö. Skriv under varje led om det är producent eller konsument.", None, 1, 4),
 ("B", "Ge två abiotiska faktorer och en biotisk faktor som påverkar hur många blåbär det blir i en skog.", None, 1, 3),
 ("C", "I ett skogsområde sköts nästan alla lodjur under några år. Forskare upptäckte efter en tid att det fanns färre unga aspar och rönnar. Använd dina kunskaper om näringskedjor för att förklara varför.", None, 2, 4),
 ("C", "Ett björkträd växer från ett litet frö till ett träd som väger 200 kg. Nästan hela vikten är kol, väte och syre. Var kommer de flesta av dessa atomer ifrån, och hur kom de in i trädet?", None, 2, 4),
 ("D", "TABELL", None, 2, 5),
 ("E", "Ella säger: ”Om fler människor äter mer vegetarisk mat kan samma åkermark föda fler människor.” Använd energipyramiden för att resonera om Ella har rätt. Ge också ett argument som talar för att djurhållning kan vara bra i Norrbotten.", None, 3, 5),
 ("E", "Antalet rådjur i ett skogsområde ökade i flera år och föll sedan kraftigt efter en lång, snörik vinter. Använd begreppen bärkraft och begränsande faktor för att förklara varför. Ge också ett exempel på hur en biotisk faktor kan ha bidragit.", None, 3, 5),
 ("E", "Ett löv faller från en björk och ligger kvar på marken. Beskriv vad som händer med kolet i lövet, och hur ett kolatom från lövet så småningom kan hamna i en växt igen.", None, 3, 5),
]
TEST_TABELL = (["Plats", "Prov 1", "Prov 2", "Prov 3", "Prov 4", "Prov 5"],
               [["Lövskog, fuktig", "46", "52", "39", "58", "45"], ["Granplantering, torr", "21", "18", "25", "64", "22"]])
TEST_D_TEXT = "En klass räknade småkryp i förna från två platser. De tog fem prover på varje plats."
TEST_D_SUB = ["a) Räkna ut medelvärdet för lövskogen.", "b) Ett värde i granplanteringen skiljer sig från de andra. Vilket? Ge en möjlig förklaring.",
              "c) Vilken slutsats kan klassen dra? Vad betyder det för nedbrytningen på platserna? ●●●"]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Förklara", "D": "Tolka resultat", "E": "Resonera"}
FACIT = [
 "B", "B", "C", "C",
 "T.ex. växtplankton (producent) → djurplankton → mört → gädda (konsumenter).",
 "Abiotiska: ljus, temperatur, nederbörd, frost, jordens näring. Biotisk: pollinerare (humlor), betande djur, konkurrerande växter, svampangrepp.",
 "Lodjuret äter rådjur och harar. När lodjuren försvinner ökar antalet rådjur och harar, och de äter mer av unga aspar och rönnar. Färre unga träd växer upp – en kaskadeffekt i flera led.",
 "Nästan allt kommer från koldioxid i luften och vatten. Trädet tar upp koldioxid genom bladens klyvöppningar och bygger in kolet i glukos i fotosyntesen. Väte och syre kommer från vattnet som rötterna tar upp. Från jorden kommer bara små mängder mineraler.",
 "a) (46 + 52 + 39 + 58 + 45) / 5 = 48. b) 64 – t.ex. ett prov från en fuktigare plats, mer förna, eller räknefel. c) Det fanns fler småkryp i den fuktiga lövskogen. Fler detritusätare och nedbrytare ger troligen snabbare nedbrytning där. Ett välutvecklat svar diskuterar att 64 påverkar medelvärdet och att fler prover behövs.",
 "Ella har i stort sett rätt: varje led i näringskedjan förlorar cirka 90 % av energin, så att äta växter direkt ger mer mat per yta. Argument för djurhållning: renar och kor kan beta mark där man inte kan odla grödor (t.ex. fjäll, skog, naturbetesmarker), och betet gynnar biologisk mångfald i odlingslandskapet.",
 "Bärkraften är det största antal rådjur som skogen kan försörja. Populationen växte så att den närmade sig eller översteg bärkraften. Snön (abiotisk faktor) gjorde det svårt att nå föda, så maten blev den begränsande faktorn och många svalt. Biotisk faktor: konkurrens om föda, sjukdomar som sprids lättare i en tät population eller rovdjur som lättare fångar försvagade djur.",
 "Lövet bryts ner av detritusätare, svampar och bakterier. Deras cellandning släpper ut en del av kolet som koldioxid i luften, och en del blir kvar i marken. Växter tar upp koldioxid genom fotosyntesen och bygger in kolet i glukos. Då har kolatomen kommit tillbaka in i en växt.",
]

LGR = ("Området täcker det centrala innehållet om lokala och globala ekosystem, sambanden mellan populationer och tillgängliga resurser samt fotosyntes, cellandning, materiens kretslopp och energins flöden i årskurs 7–9. "
       "Delområde 4.1 behandlar ekosystem och energi, delområde 4.2 materiens kretslopp och nedbrytning och delområde 4.3 populationer och samspel. Labbarna tränar systematiska undersökningar och modeller. "
       "Människans påverkan på ekosystemen, naturbruk och hållbar utveckling hör till nästa område (5), där begreppen från detta område används. "
       "Uppgifterna följer betygskriteriernas progression: från att beskriva och ge exempel till att förklara samband och resonera i flera led, och är inspirerade av frisläppta nationella prov i biologi.")
FAKTA = ("Lämmel- och fjällrävskurvorna i bild 4.8 är förenklade och visar ett mönster, inte verkliga data. Tumregeln om 10 % energiöverföring är ett genomsnitt (ofta 5–20 %). "
         "Van Helmonts pilträdsförsök: trädet vägde 5 pund från början och drygt 169 pund efter fem år, jorden förlorade ca 2 uns av 200 pund (uppgifter enligt hans egen skildring, återgiven på bl.a. Univ. of St. John's/College of St. Benedict). "
         "Vattnets kretslopp och nedbrytningens faktorer är läroboksfakta. Komposttemperaturer över 50 °C är vanliga. Yellowstone-exemplet är förenklat: forskare debatterar vargarnas betydelse jämfört med andra orsaker. "
         "Källor: Skolverket, Lgr22 kursplan i biologi. · Frisläppta nationella prov i biologi åk 9. · Illustrationer: egenritade för detta kapitel.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start.</b> Mål: eleven skiljer individ, population, samhälle, ekosystem och biosfär. Låt eleverna placera skolgården på nivåerna.</p>
<p><b>Vad är ett ekosystem?</b> C-mål: skilja biotiska och abiotiska faktorer och jämföra ekosystem. Vanligt fel: eleverna räknar bara djur som ekosystemet. Betona den livlösa miljön.</p>
<p><b>Producenter, konsumenter och näringsvävar.</b> C-mål: rita och tolka näringskedjor och förutsäga följder av en förändring i en väv. Vanligt fel: pilen ritas åt fel håll (från ätaren till den uppätna). Pilen visar energins väg.</p>
<p><b>Energiflöde och biomassa.</b> C-mål: förklara varför energi minskar och varför kedjorna är korta. Tumregeln 10 % är ett genomsnitt. Biomassa är torrvikt, inte antal individer.</p>
<p><b>Labb 4.1 Energi i en näringskedja – modellspel.</b> Material: 1 000 g ris, våg, skålar. Förväntat: 1 000 → 100 → 10 → 1 g (10 %) respektive 1 000 → 200 → 40 → 8 g (20 %). Vanliga fel: eleverna blandar ihop procent och gram. Diskutera vad modellen förenklar.</p>
<p><b>Materia tillverkas inte och försvinner inte.</b> C-mål: skilja energins flöde från materiens kretslopp. Van Helmont är en bra start på resonemanget om att växten mest är byggd av luft och vatten. Vanligt fel: ”växter blir stora av jorden”.</p>
<p><b>Kolets kretslopp.</b> C-mål: beskriva kretsloppet med fotosyntes, cellandning, nedbrytning och förbränning. Kopplas till område 5 (klimat).</p>
<p><b>Nedbrytning.</b> C-mål: förklara nedbrytarnas roll och vad som påverkar hastigheten. Vanligt fel: ”ruttnande” ses som att materien försvinner.</p>
<p><b>Labb 4.2 Nedbrytning i jord.</b> Förväntat: skogsjord och fuktig jord ger störst viktförlust, sand minst. Avvikande värden är utgångspunkt för diskussion om felkällor (fukt, påsens placering). Bonuslabb: Småkryp i förnan.</p>
<p><b>Populationer och förändring.</b> C-mål: tolka diagram över populationsförändring. Facit till hararna: 200 + 150 − 120 + 20 − 30 = 220.</p>
<p><b>Begränsande faktorer.</b> C-mål: förklara hur flera faktorer samverkar. Skilj biotiska från abiotiska faktorer och begreppet bärkraft från ”max antal som någonsin funnits”.</p>
<p><b>Konkurrens, jakt och samarbete.</b> C-mål: ge exempel på samspel och förklara nisch. Vanligt fel: nisch och livsmiljö blandas ihop.</p>
<p><b>Labb 4.3 Rovdjur–bytesmodell.</b> Resultaten varierar. Ofta dör bytena ut eller rovdjuren svälter i början. Justera reglerna (tid, krav på fångst) så att kurvorna svänger. Jämför med lämmelåren i bild 4.8.</p>"""

BONUS = dict(
 titel="Småkryp i förnan",
 ingress="Med en tratt, ett nät och en lampa kan eleverna få fram hundratals småkryp ur en handfull löv. En enkel men spektakulär labb om livet i marken.",
 syfte="Eleverna samlar in och artbestämmer småkryp från förna med en egen Berlesetratt. De ser med egna ögon de detritusätare och rovdjur som håller igång nedbrytningen. Labben kopplar till näringsvävar, nedbrytare och fältstudier, och kan bli en jämförande undersökning mellan två platser.",
 tid="Grupper om tre till fyra.",
 material=["Stor tratt (eller avklippt PET-flaska)", "Nät eller trådnät med 2–3 mm maskor", "Skrivbordslampa (glödlampa eller halogen ger värme)", "Burk med fuktigt papper eller lite vatten", "Påse förna och översta jordlagret, ca 1 liter", "Lupp eller stereolupp, petriskål, pensel", "Enkel nyckel över småkryp"],
 genomf=["Samla förna från en tydligt avgränsad yta, t.ex. 25 × 25 cm, så att proverna blir jämförbara.", "Lägg förnan löst på nätet i tratten. Lampan ska vara 10–15 cm ovanför.", "Djuren flyr ljus, värme och uttorkning – nedåt – och faller ner i burken. Låt tratten stå tills djuren har fallit ner.", "Töm burken i en petriskål och sortera djuren i grupper med lupp.", "Jämför gärna två platser, t.ex. lövskog och granskog, fuktigt och torrt."],
 resultat="Hoppstjärtar och kvalster är nästan alltid flest. Man brukar också hitta spindlar, gråsuggor, tusenfotingar, små skalbaggar och fluglarver. Fuktig lövförna innehåller oftast fler djur än torr barrförna. Hoppstjärtar, kvalster och gråsuggor äter dött material och svamptrådar. Spindlar, enfotingar och rovkvalster äter dem – en egen liten näringsväv i marken.",
 sakerhet=["Lampan blir varm: inget papper nära, stäng av när den inte behövs.", "Tvätta händerna efter jordarbete.", "Använd vatten i burken om djuren ska släppas tillbaka; använd bara etanol om de ska bevaras och efter samråd."],
 problem=["Få djur: förnan var för torr, för lite material eller tratten stod för kort tid.", "Jord rinner ner: lägg ett lager förna överst och använd finare nät."],
 bedom=[("Grundläggande", "Sorterar och räknar djuren och redovisar i tabell."), ("Utvecklat", "Delar in djuren i nedbrytare/detritusätare och rovdjur och ritar en näringsväv."), ("Välutvecklat", "Jämför platser, förklarar skillnader med abiotiska faktorer och värderar metoden.")],
)
