# -*- coding: utf-8 -*-
"""Biologi kapitel 4 – Ekologi. Källa för alla sex PDF:er (vanlig, lättläst, fördjupning, med/utan lärarversion)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *

NR = 4
SLUG = "ekologi"
TAB = "4"
FIG = '/tmp/bio/fig/'
NR = 4
NAMN = "Ekologi"
UNDER = "Vem äter vem – och vart tar energin vägen?"
INTRO = ("En havsörn dyker ner mot en vik i Bottenviken och fångar en gädda. Gäddan har ätit abborrar, abborrarna har ätit "
         "djurplankton och djurplanktonen har ätit små alger som har fångat solljus. Allt levande hänger ihop i ett nät av "
         "beroenden. Läran om hur organismer samspelar med varandra och med sin miljö kallas <strong>ekologi</strong>.")

MAL = ["vad ekologi är och vad som menas med population, samhälle och ekosystem",
       "vad producenter, konsumenter och nedbrytare gör",
       "att rita och tolka näringskedjor och näringsvävar",
       "hur energin flödar och varför den minskar i varje led",
       "hur kolet och andra ämnen går i kretslopp",
       "vad som styr hur stor en population blir, och hur arter samspelar",
       "hur människan påverkar ekosystem, lokalt och globalt",
       "hur vi kan använda naturen hållbart"]
FUNDERA = "Vad åt du till lunch i dag? Försök följa maten bakåt ända till solen. Hur många steg blev det?"

# Sektioner: (nr, titel, html). Sidnummer till innehållsförteckningen räknas fram vid bygget.
S = []

# ---------------------------------------------------------------- 4.1
S.append(("4.1", "Vad är ekologi?",
 row("<p><strong class='green'>Ekologi</strong> kommer från grekiskans <em>oikos</em>, som betyder hus eller hem. Ekologer undersöker hur organismer lever i sitt ”hem”: vad de äter, vem som äter dem, vilka de konkurrerar med och hur de påverkas av till exempel temperatur, ljus och vatten. Ekologer studerar naturen på olika nivåer.</p>")

 + fig(FIG+"ekologi-nivaer.png", "<b>Bild 4.1</b> Ekologins nivåer, från en enda individ till allt liv på jorden.")
 + row(bullets([
     "En <strong class='green'>population</strong> är alla individer av samma art som lever inom ett visst område, till exempel alla skogsharar i en skog.",
     "Ett <strong class='green'>samhälle</strong> är alla populationer av olika arter i samma område.",
     "Ett <strong class='green'>ekosystem</strong> är samhället tillsammans med den livlösa miljön: ljus, vatten, jord, luft och temperatur.",
     "<strong class='green'>Biosfären</strong> är alla ekosystem på jorden tillsammans – allt liv och alla platser där det finns liv."])
   + "<h3>Levande och icke-levande faktorer</h3>"
   + "<p>Allt som påverkar en organism kallas faktorer. Faktorer från andra organismer, som föda, rovdjur, konkurrenter och sjukdomar, kallas <strong class='green'>biotiska</strong> (bios = liv). Faktorer från den livlösa miljön, som temperatur, ljus, vatten, näringsämnen och vind, kallas <strong class='green'>abiotiska</strong>.</p>"
   + "<p>Varje art har en <strong class='green'>livsmiljö</strong> där den kan leva. En abborre behöver sjö- eller havsvatten med tillräckligt med syre. En fjällräv behöver kalla fjäll med lämlar och gamla lyor.</p>",
   [begrepp([("Population", "Alla individer av en art inom ett område."),
             ("Ekosystem", "Organismerna och den livlösa miljön i ett område."),
             ("Biotisk faktor", "Påverkan från andra levande organismer."),
             ("Abiotisk faktor", "Påverkan från den livlösa miljön.")]),
    box("tank", "Tänk efter", "<p>Är ett ekosystem alltid stort? Kan en vattenpöl, en murken stubbe eller din tarm vara ett ekosystem?</p>")])
 + kolla("4.1", ["Vad är skillnaden mellan en population och ett samhälle?",
                 "Ge två biotiska och två abiotiska faktorer som påverkar en gädda.",
                 "Varför räknas vattnet och solljuset till ekosystemet?"])))

# ---------------------------------------------------------------- 4.2
S.append(("4.2", "Producenter, konsumenter och nedbrytare",
 "<p>I kapitel 2 lärde du dig att växter gör fotosyntes och att alla celler behöver energi från cellandning. Nu ska vi se vad det betyder för ett helt ekosystem. Organismerna kan delas in i tre grupper efter hur de får sin energi och näring.</p>"
 + cards([("Producenter", "Gröna växter, alger och växtplankton. De bygger sin egen näring med fotosyntes och är grunden i alla näringskedjor."),
          ("Konsumenter", "Djur som äter andra organismer. Växtätare äter producenter, rovdjur äter andra djur och allätare äter både och."),
          ("Nedbrytare", "Svampar och bakterier som bryter ner döda växter och djur, avföring och nedfallna löv. De frigör näringsämnen som växterna kan använda igen.")])
 + "<h3>Näringskedjor</h3>"
 + "<p>En <strong class='green'>näringskedja</strong> visar vem som äter vem. Varje steg i kedjan kallas ett led. Pilarna ritas från den som blir uppäten till den som äter, alltså åt samma håll som energin går. Den som står först i kedjan är alltid en producent.</p>"
 + fig(FIG+"ekologi-kedja.png", "<b>Bild 4.2</b> En näringskedja i Bottenviken. Konsumenterna numreras efter hur många steg de står från producenterna.")
 + row("<p>Djurplankton äter växtplankton och är därför <em>första ordningens konsument</em> eller växtätare. Abborren äter djurplankton och är <em>andra ordningens konsument</em>. Havsörnen har inga naturliga fiender och kallas <strong class='green'>toppkonsument</strong>.</p>"
       "<p>Många djur kan stå på flera led. En björn äter både blåbär och älgkalvar. En människa som äter en sallad är första ordningens konsument, men när hon äter en köttbit är hon andra eller tredje ordningens konsument.</p>",
       [box("visste", "Visste du?", "<p>Detritusätare som daggmaskar, gråsuggor och hoppstjärtar äter döda växtdelar. De hackar sönder materialet så att svampar och bakterier kan bryta ner det snabbare.</p>")])
 + kolla("4.2", ["Varför står alltid en producent först i en näringskedja?",
                 "Rita en näringskedja med fyra led från en skog. Skriv vilka som är producent och konsumenter.",
                 "Vad skulle hända i en skog om alla nedbrytare försvann?"])))

# ---------------------------------------------------------------- 4.3
S.append(("4.3", "Näringsvävar",
 "<p>I verkligheten äter de flesta djur flera olika saker och blir uppätna av flera olika rovdjur. Näringskedjorna korsar varandra och bildar en <strong class='green'>näringsväv</strong>. En näringsväv visar bättre hur ett ekosystem verkligen fungerar.</p>"
 + fig(FIG+"ekologi-vav.png", "<b>Bild 4.3</b> En förenklad näringsväv i en sjö eller vik. Pilarna visar åt vilket håll energin går.")
 + row("<h3>När en art försvinner</h3>"
       "<p>Om en art försvinner påverkas alla som hänger ihop med den. Om abborrarna fiskas bort får gäddan mindre mat. Samtidigt blir det fler djurplankton och insektslarver, eftersom färre äter dem. Ju fler kopplingar det finns i väven, desto lättare kan ekosystemet klara en förändring.</p>"
       "<h3>Exempel: vargarna i Yellowstone</h3>"
       "<p>I nationalparken Yellowstone i USA utrotades vargarna under 1920-talet. Hjortarna blev då många och betade hårt på unga träd och buskar längs vattendragen. År 1995 släpptes vargar ut igen. Forskare såg att hjortarna betade mindre på vissa platser och att träd och buskar kunde växa upp. Där blev det fler småfåglar och bävrar.</p>"
       "<p>När en förändring högst upp i en näringskedja sprider sig nedåt genom flera nivåer kallas det en <strong class='green'>kaskadeffekt</strong>. Forskarna diskuterar fortfarande hur stor vargarnas betydelse var jämfört med andra orsaker, till exempel klimat och jakt.</p>",
       [begrepp([("Näringsväv", "Flera näringskedjor som hänger ihop."),
                 ("Toppkonsument", "Ett djur högst upp i näringskedjan, utan naturliga fiender."),
                 ("Kaskadeffekt", "En förändring som sprider sig genom flera nivåer i en näringsväv.")]),
        box("tank", "Tänk efter", "<p>Använd bild 4.3. Vad händer med insektslarverna om knipan försvinner? Vad händer då med vattenväxterna?</p>")])))

# ---------------------------------------------------------------- 4.4
S.append(("4.4", "Energin flödar genom ekosystemet",
 "<p>Nästan all energi i ett ekosystem kommer från solen. Producenterna fångar en liten del av solljuset med fotosyntesen och lagrar energin i glukos och andra ämnen. När en växtätare äter växten förs en del av energin vidare. Men det mesta av energin förs inte vidare.</p>"
 + '<div class="row w"><div class="main"><h3>Varför försvinner energi i varje led?</h3>'
 + bullets(["Organismen använder energi för att leva: röra sig, hålla värmen och laga celler. Det mesta blir till slut värme.",
            "Allt äts inte upp: rötter, ben, päls och fjädrar blir kvar.",
            "Allt som äts tas inte upp i kroppen, utan lämnar den som avföring."])
 + "<p>Som en tumregel förs bara omkring <strong class='green'>10 procent</strong> av energin vidare till nästa led. Resten går förlorad som värme eller hamnar hos nedbrytarna. Man brukar rita det som en <strong class='green'>energipyramid</strong>.</p>"
 + "<p>Energi går alltså inte i kretslopp, den <strong class='green'>flödar</strong> genom ekosystemet: in som solljus och ut som värme. Därför behövs ett ständigt tillskott av solenergi.</p></div>"
 + '<div class="side">' + fig(FIG+"ekologi-pyramid.png", "<b>Bild 4.4</b> En energipyramid. Bara ungefär en tiondel av energin förs vidare till nästa nivå.") + '</div></div>'
 + "<h3>Vad betyder det?</h3>"
 + '<div class="cols2" style="column-gap:18pt"><p><strong>Därför är näringskedjor korta</strong><br>Efter fyra eller fem led finns det för lite energi kvar för ytterligare ett led. Därför finns det många fler harar än lodjur och många fler växtplankton än havsörnar. Toppkonsumenter behöver stora områden för att hitta tillräckligt med mat.</p>'
   "<p><strong>Mat och hållbarhet</strong><br>Om vi äter växtmat direkt tar vi vara på mer av den energi växterna har fångat. När djur föds upp på foder går en stor del av energin förlorad på vägen. Därför kan samma åkermark föda fler människor om en större del av maten är växtbaserad.</p></div>"
 + kolla("4.4", ["Varifrån kommer nästan all energi i ett ekosystem?",
                 "Ge två förklaringar till varför energi försvinner mellan leden.",
                 "Varför finns det färre rovdjur än växtätare i en skog?"])))

# ---------------------------------------------------------------- 4.5
S.append(("4.5", "Materien går i kretslopp",
 "<p>Energin flödar igenom och försvinner som värme, men <strong class='green'>materien</strong> – alla atomer som organismer är byggda av – försvinner aldrig. Samma kolatomer, kväveatomer och vattenmolekyler används om och om igen. Atomerna i din kropp har en gång funnits i växter, djur, luft och hav.</p>"
 + fig(FIG+"ekologi-kol.png", "<b>Bild 4.5</b> Kolets kretslopp, förenklat. Pilarna visar hur kol rör sig mellan luften, levande organismer och marken.")
 + row("<h3>Kolets kretslopp</h3>"
       + steps(["<strong>Fotosyntes:</strong> Växter tar upp koldioxid från luften och bygger in kolet i glukos.",
                "<strong>Näringskedjan:</strong> Kolet förs vidare till djur som äter växterna.",
                "<strong>Cellandning:</strong> Växter och djur släpper ut koldioxid när de använder glukosen.",
                "<strong>Nedbrytning:</strong> När organismer dör bryter nedbrytarna ner dem. Då frigörs koldioxid och näringsämnen.",
                "<strong>Förbränning:</strong> Kol som har legat lagrat i miljontals år som olja, kol och naturgas släpps ut när människan bränner det."]),
       [box("klimat", "Klimatet", "<p>När vi bränner fossila bränslen släpper vi ut mer koldioxid än växterna och haven hinner ta upp. Halten i luften ökar och förstärker växthuseffekten. Därför blir jorden varmare.</p>"),
        box("kvave", "Även kväve", "<p>Växter behöver kväve för att bygga proteiner. Nedbrytarna frigör kväve ur döda organismer, och vissa bakterier kan ta kväve direkt från luften.</p>")])
 + kolla("4.5", ["Vad är skillnaden mellan hur energi och materia rör sig i ett ekosystem?",
                 "Beskriv två processer som tar kol från luften och två som släpper ut kol till luften.",
                 "Varför är nedbrytarna så viktiga för växterna?"])))

# ---------------------------------------------------------------- 4.6 (två sidor: population + samspel + nisch)
S.append(("4.6", "Populationer och resurser",
 "<p>Om en population har gott om mat, plats och inga fiender kan den växa snabbt. Men ingen population kan växa hur länge som helst. Förr eller senare tar någon <strong class='green'>resurs</strong> slut – mat, vatten, boplatser eller ljus. Det finns alltid något som begränsar hur stor en population kan bli.</p>"
 + '<div class="row w"><div class="main"><h3>Vad påverkar populationens storlek?</h3>'
 + bullets(["<strong>Tillgång på föda och vatten</strong> – mer mat ger fler ungar som överlever.",
            "<strong>Rovdjur</strong> – många rovdjur håller nere antalet bytesdjur.",
            "<strong>Konkurrens</strong> – arter som behöver samma resurs tävlar om den.",
            "<strong>Sjukdomar och parasiter</strong> sprids lättare när det är trångt.",
            "<strong>Abiotiska faktorer</strong> – en kall vår eller en torr sommar kan slå ut många individer."])
 + "<h3>Lämmelår</h3><p>I fjällen varierar antalet lämlar kraftigt. Vissa år blir de enormt många, ett lämmelår, och sedan kraschar populationen. Fjällräven, som lever mest av lämlar, får många valpar under lämmelår och nästan inga under år med lite mat. Därför ökar antalet fjällrävar efter ett lämmelår. Rovdjurens antal följer alltså bytesdjurens, med en liten fördröjning.</p></div>"
 + '<div class="side">' + fig(FIG+"ekologi-lamlar.png", "<b>Bild 4.6</b> Antalet lämlar och fjällrävar varierar i cykler. Kurvorna är förenklade.") + '</div></div>'
 + "<h3>Samspel mellan arter</h3>"
 + cards([("Rovdjur och byte", "Rovdjuret tjänar, bytet förlorar. Lodjur och skogshare är ett exempel."),
          ("Konkurrens", "Båda förlorar lite. Rödräv och fjällräv konkurrerar om både mat och lyor."),
          ("Symbios", "Båda tjänar på samarbetet. En lav är en svamp och en alg som lever tillsammans: algen gör fotosyntes, svampen skyddar och håller kvar vatten.")])
 + row("<h3>Livsmiljö och nisch</h3>"
       "<p>Alla arter har en <strong class='green'>livsmiljö</strong>, platsen där de kan leva. Kungsfågeln lever i granskog, gäddan i grunda vikar med vass och lodjuret i stora skogsområden. En viss typ av miljö, som barrskog, myr, sjö eller strandäng, kallas en <strong class='green'>biotop</strong>.</p>"
       "<p>Men varje art har också en egen roll i ekosystemet. Det kallas artens <strong class='green'>nisch</strong>: vad den äter, var och när den söker mat, var den bor och vilka den påverkar. Nischen är ungefär artens ”yrke”, medan livsmiljön är dess ”adress”.</p>"
       "<p>Två arter som har exakt samma nisch konkurrerar hårt, och ofta blir det bara en av dem som klarar sig. Därför har arter som lever på samma plats ofta olika nischer. Ju fler olika nischer det finns, desto fler arter får plats.</p>",
       [begrepp([("Livsmiljö", "Platsen där en art lever."),
                 ("Biotop", "En typ av livsmiljö, till exempel barrskog, myr eller sjö."),
                 ("Nisch", "Artens roll i ekosystemet: vad den äter, var och när den söker mat och hur den påverkar andra."),
                 ("Symbios", "Samarbete där båda arterna tjänar på det.")]),
        box("tank", "Tänk efter", "<p>Du och din granne bor på samma gata men har olika yrken. Vad motsvarar gatan, och vad motsvarar yrket, i ekologins ord?</p>")])
 + fig(FIG+"ekologi-nisch.png", "<b>Bild 4.7</b> Två småfåglar i samma gran. De söker föda på olika ställen och har därför olika nischer.")
 + kolla("4.6", ["Ge tre faktorer som kan begränsa hur stor en population blir.",
                 "Titta på bild 4.6. Varför kommer topparna för fjällrävarna lite efter topparna för lämlarna?",
                 "Vad är skillnaden mellan en arts livsmiljö och dess nisch?"])))

# ---------------------------------------------------------------- 4.7 (två sidor)
S.append(("4.7", "Människan påverkar ekosystemen",
 "<p>Människan är en del av ekosystemen och påverkar dem mer än någon annan art. Först två tydliga exempel från Östersjön, sedan tre stora hot mot naturen: klimatförändringar, förlorade livsmiljöer och invasiva arter. Kunskap om näringskedjor och kretslopp hjälper oss att förstå dem alla.</p>"
 + "<h3>Miljögifter anrikas i näringskedjan</h3>"
 + fig(FIG+"ekologi-anrikning.png", "<b>Bild 4.8</b> Hur ett miljögift anrikas. Varje mört äter många plankton, och varje gädda äter många mörtar.")
 + row("<p>Vissa gifter, till exempel DDT och PCB, bryts ner mycket långsamt och lagras i djurens fett. När en mört äter tusentals plankton samlas giftet från alla planktonen i mörtens kropp. När gäddan äter många mörtar blir halten ännu högre. Det kallas <strong class='green'>anrikning</strong>. Toppkonsumenterna drabbas därför hårdast.</p>"
       "<p>På 1960- och 70-talen var havsörnen nära att försvinna från Östersjön. Gifterna gjorde att äggskalen blev tunna och att ungarna dog. I början av 1970-talet lyckades bara ungefär var femte häckning längs östkusten. Gifterna förbjöds, och Naturskyddsföreningen lade ut giftfri mat. I dag finns det flera tusen havsörnar i Sverige, och arten är inte längre rödlistad.</p>",
       [begrepp([("Anrikning", "När ett gift samlas i allt högre halter högre upp i näringskedjan."),
                 ("Övergödning", "När för mycket näringsämnen hamnar i sjöar och hav.")])])
 + "<h3>Övergödning</h3>"
 + fig(FIG+"ekologi-overgodning.png", "<b>Bild 4.9</b> Övergödning steg för steg. Kväve och fosfor fungerar som gödning för alger.")
 + "<p>Kväve och fosfor från jordbruk, avlopp och trafik rinner ut i sjöar och hav. Där fungerar de som gödning. Algerna växer explosionsartat, och när de dör sjunker de till botten. Nedbrytarna som bryter ner dem förbrukar syret. I delar av Östersjön har bottnarna blivit så syrefattiga att nästan inget kan leva där.</p>"
 + '<div class="pg"></div>'
 + row("<h3>Klimatförändringar</h3>"
       "<p>När vi bränner olja, kol och naturgas släpps koldioxid ut (se kolets kretslopp i 4.5). Mer koldioxid i luften förstärker växthuseffekten, och jordens medeltemperatur har hittills stigit med mer än en grad sedan 1800-talet. Det kan låta lite, men ekosystemen är byggda för vissa temperaturer.</p>"
       + bullets(["<strong>Arter flyttar.</strong> Många arter förskjuts norrut eller uppåt i fjällen, där det är kallare. Rödräven går högre upp i fjällen och konkurrerar där med fjällräven.",
                  "<strong>Säsongerna ändras.</strong> Om våren kommer tidigt kan insekterna komma före flyttfåglarna, som då missar maten till sina ungar.",
                  "<strong>Isar smälter.</strong> Djur som lever på isen, som isbjörn och ringsäl, förlorar sin livsmiljö.",
                  "<strong>Haven blir surare.</strong> Haven tar upp en del av koldioxiden, och då blir vattnet surare. Det gör det svårare för bland annat musslor, snäckor och koraller att bygga sina skal."])
      
       ,
       [box("klimat", "Fjällen", "<p>Fjällräven är en art som både drabbas av värmen och av nya konkurrenter. Mer om det i fördjupningen.</p>")])
 + row("<h3>Förlorade livsmiljöer</h3>"
       "<p>Det största hotet mot arter i Sverige och i världen är att deras livsmiljöer försvinner eller förändras. När skog avverkas, våtmarker dikas ut, mark bebyggs eller blir åker tappar arter sin ”adress”.</p>"
       "<p>Många rödlistade arter, till exempel vitryggig hackspett, flera lavar och skalbaggar, lever i gammal skog eller på död ved. I ett skogsbruk där alla träd avverkas i ung ålder finns det därför lite plats för dem.</p>"
       "<p>Även när en del av livsmiljön blir kvar kan den delas upp i små öar av vägar, åkrar och bebyggelse. Det kallas <strong class='green'>fragmentering</strong>. Små populationer på små öar har svårt att möta varandra, och de blir lättare utrotade.</p>",
       [begrepp([("Fragmentering", "När en livsmiljö delas upp i små delar, till exempel av vägar och åkrar."),
                 ("Invasiv art", "En art som människan fört till en ny plats och som sprider sig och skadar andra arter där.")])])
 + "<h3>Invasiva arter</h3>"
 + "<p>Ibland för människan med sig arter till nya platser, med flit eller av misstag. De flesta klarar sig inte, men en del trivs och sprider sig så mycket att de skadar de arter som redan finns där. De kallas <strong class='green'>invasiva arter</strong>. De har ofta inga naturliga fiender på den nya platsen.</p>"
 + cards([("Signalkräfta", "Sattes ut i svenska vatten från 1960-talet. Den bär på kräftpest, som slår ut den inhemska flodkräftan."),
          ("Mink", "Kom från pälsfarmer. Den jagar bland annat sjöfåglar."),
          ("Jättebjörnklo", "Planterades som trädgårdsväxt och tränger undan andra växter. Saften kan ge brännskador på huden.")])
 + "<p>Inte alla införda arter är ett problem. Det är de som sprider sig kraftigt och hotar andra arter som kallas invasiva. Därför ska man aldrig släppa ut akvariedjur eller dumpa trädgårdsavfall i naturen.</p>"
 + kolla("4.7", ["Varför drabbas toppkonsumenter hårdast av miljögifter?",
                 "Förklara kort hur övergödning kan leda till syrebrist.",
                 "Ge två sätt som klimatförändringar kan påverka arter och ekosystem.",
                 "Varför kan en invasiv art få stor skada på ett ekosystem?"])))

# ---------------------------------------------------------------- 4.8
S.append(("4.8", "Lokala och globala ekosystem",
 "<p>Ekosystemen ser olika ut beroende på klimat, ljus, vatten och jord. Men de fungerar efter samma principer: producenter fångar solenergi, konsumenter äter, nedbrytare tar hand om det döda och materien går i kretslopp.</p>"
 + fig(FIG+"ekologi-ekosystem.png", "<b>Bild 4.10</b> Två ekosystem i Norrbotten och två i andra delar av världen.")
 + table(["", "Barrskog i Norrbotten", "Bottenviken", "Tropisk regnskog", "Savann"],
         [["Klimat", "Kalla vintrar, kort sommar med ljusa nätter", "Kallt bräckt vatten, is på vintern", "Varmt och regnigt hela året", "Varmt, regnperiod och torrperiod"],
          ["Producenter", "Tall, gran, björk, bärris, mossor, lavar", "Växtplankton, alger, vass", "Höga lövträd, lianer, epifyter", "Gräs, spridda träd som akacior"],
          ["Konsumenter", "Älg, skogshare, tjäder, lodjur, björn", "Djurplankton, sik, abborre, gädda, säl, havsörn", "Insekter, apor, fåglar, ormar, jaguar", "Zebror, gnuer, giraffer, lejon"],
          ["Nedbrytning", "Långsam – kallt och surt", "Långsam i kallt vatten", "Mycket snabb", "Snabb under regnperioden"],
          ["Artrikedom", "Måttlig", "Låg – få arter klarar bräckt vatten", "Mycket hög", "Hög, särskilt stora däggdjur"]])
 + row("<p>I barrskogen bryts löv och barr ner långsamt eftersom det är kallt. Därför bildas tjocka lager av förna och torv. I regnskogen går nedbrytningen så fort att näringen nästan direkt tas upp av växterna igen – jorden i sig är ofta näringsfattig.</p>"
       "<p>Ekosystemen hänger också ihop globalt. Flyttfåglar som häckar i Norrbotten övervintrar i Afrika, och laxen vandrar mellan älvarna och havet. Koldioxid från ett land påverkar klimatet i hela världen.</p>",
       [begrepp([("Förna", "Döda löv och barr som ligger på marken.")])])
 + kolla("4.8", ["Varför bryts löv ner långsammare i Norrbotten än i en regnskog?",
                 "Ge ett exempel på hur ekosystem hänger ihop över hela jorden.",
                 "Varför har Bottenviken låg artrikedom?"])))

# ---------------------------------------------------------------- 4.9 Naturbruk
S.append(("4.9", "Naturbruk: skog, jordbruk och fiske",
 "<p><strong class='green'>Naturbruk</strong> betyder att vi använder naturen för att få mat och material. I Sverige är de tre stora områdena skogsbruk, jordbruk och fiske. Alla tre bygger på ekosystem, och alla kan skada dem om de sköts fel.</p>"
 + cards([("Skogsbruk", "Ungefär två tredjedelar av Sveriges yta är skog. Den ger virke, papper och jobb, lagrar kol och är livsmiljö för många arter."),
          ("Jordbruk", "Åkrar och betesmarker ger oss mat. Gödsel och bekämpningsmedel kan läcka till vattnet och skada insekter."),
          ("Fiske", "Fisk är mat och inkomst. Om man fiskar mer än bestånden hinner ersätta kallas det <strong>överfiske</strong>.")])
 + table(["", "Vad kan gå fel?", "Hållbart sätt"],
         [["Skogsbruk", "Gammal skog och död ved försvinner, så arter som lever där förlorar sin livsmiljö.", "Spara nyckelbiotoper, lämna döda träd och några levande träd på hygget och skydda vissa områden helt."],
          ["Jordbruk", "Kväve och fosfor läcker ut och ger övergödning (se 4.7). Insekter drabbas av bekämpningsmedel.", "Gödsla lagom, ha kantzoner mot vattendrag och låt djur beta gräsmarker. Betesmarker har ofta många arter."],
          ["Fiske", "Överfiske gör att bestånden minskar. Torsken i östra Östersjön är ett exempel där fisket har begränsats kraftigt.", "Fiskekvoter, minimimått och fredade områden så att fiskarna hinner växa upp och föröka sig."]])
 + row("<h3>Att väga mot varandra</h3>"
       "<p>Naturbruk ger jobb, mat och pengar, men kan också påverka natur och klimat. Det är därför sällan helt enkelt att veta vad som är rätt. Man får väga olika intressen mot varandra: Hur mycket får vi ta ut? Vilka områden ska skyddas? Vem betalar kostnaden?</p>"
       "<p>Grundregeln för ett hållbart naturbruk är att ta ut mindre än naturen hinner växa till igen, och att spara tillräckligt med livsmiljöer så att arterna klarar sig.</p>",
       [begrepp([("Naturbruk", "Att använda naturen för att få mat och material, till exempel genom skogsbruk, jordbruk och fiske."),
                 ("Överfiske", "När man fiskar mer än fiskbeståndet hinner ersätta.")]),
        box("tank", "Tänk efter", "<p>Skogsbruk ger jobb och virke, men kalhyggen påverkar många arter. Vem borde få vara med och bestämma hur skogen används?</p>")])
 + kolla("4.9", ["Vad betyder naturbruk? Nämn tre exempel.",
                 "Ge ett exempel på hur skogsbruk, jordbruk eller fiske kan skada ett ekosystem, och ett sätt att göra det mer hållbart.",
                 "Varför är det ofta svårt att avgöra vad som är bäst för naturen och för människorna samtidigt?"])))

# ---------------------------------------------------------------- 4.10 Hållbar utveckling
S.append(("4.10", "Hållbar utveckling och ekosystemtjänster",
 "<p>Vi lever av naturen: mat, vatten, virke och luft att andas. Men om vi använder naturen för hårt kan den inte ge oss lika mycket i framtiden. <strong class='green'>Hållbar utveckling</strong> betyder att vi tillgodoser dagens behov utan att ta ifrån kommande generationer möjligheten att tillgodose sina. Så beskrevs det i en rapport från FN år 1987. År 2015 enades världens länder om 17 globala mål, <strong class='green'>Agenda 2030</strong>. Hållbar utveckling har tre delar som hänger ihop: miljön (naturen och klimatet), samhället (till exempel hälsa och rättvisa) och ekonomin (jobb och pengar). I biologin tittar vi mest på miljön.</p>"

 + row("<h3>Ekosystemtjänster – naturens gratis hjälp</h3>"
       "<p><strong class='green'>Ekosystemtjänster</strong> är det naturen gör för oss. Friska ekosystem med stor biologisk mångfald ger oss många tjänster:</p>"
       + bullets(["<strong>Mat och material:</strong> fisk, bär, virke.",
                  "<strong>Pollinering:</strong> humlor och bin gör att många grödor ger skörd.",
                  "<strong>Rent vatten och ren luft:</strong> skogar och våtmarker renar vatten, och växter tar upp koldioxid.",
                  "<strong>Jordens näring:</strong> nedbrytare ger växterna näring.",
                  "<strong>Hälsa och naturupplevelser:</strong> många mår bra av att vara ute i naturen."])
       + "<p>Om mångfalden minskar kan tjänsterna bli sämre. Därför hänger biologisk mångfald och hållbar utveckling ihop.</p>",
       [begrepp([("Hållbar utveckling", "Att tillgodose dagens behov utan att ta ifrån framtida generationer möjligheten att tillgodose sina."),
                 ("Ekosystemtjänst", "Något naturen gör för oss, till exempel pollinering, rent vatten eller mat."),
                 ("Allemansrätten", "Rätten att vistas i naturen, med regeln inte störa, inte förstöra.")])])
 + row("<h3>Allemansrätten – frihet med ansvar</h3>"
       "<p>I Sverige har alla rätt att vara i naturen, även på mark som någon annan äger. Det kallas <strong class='green'>allemansrätten</strong>. Du får till exempel gå, cykla, åka skidor, bada, plocka bär, svamp och vanliga blommor och sova en natt i tält en bit från hus.</p>"
       "<p>Rätten har två enkla regler: <strong>inte störa, inte förstöra</strong>. Du får inte vara nära någons hem, skräpa ner, bryta kvistar eller skada djur och fåglar. Du får inte plocka fridlysta växter eller störa häckande fåglar, och hunden ska hållas kopplad under våren och sommaren.</p>",
       [box("tank", "Tänk efter", "<p>Varför fungerar allemansrätten bara när många tar ansvar?</p>")])
 + '<div class="cols2"><div><h3>Vad kan jag göra?</h3>'
 + "<p><strong>Mat:</strong> släng mindre mat och ät mer växtbaserat (se 4.4).<br><strong>Prylar:</strong> laga, byt och köp begagnat.<br><strong>Resor:</strong> gå, cykla eller åk kollektivt. Det minskar utsläppen av koldioxid.<br><strong>Natur:</strong> släng aldrig skräp i naturen och plantera aldrig ut trädgårdsväxter där. Låt en bit gräsmatta bli äng.</p></div>"
 + "<div><h3>Vad kan samhället göra?</h3><p><strong>Lagar och regler:</strong> till exempel förbudet mot DDT (se 4.7) och regler för fiske.<br><strong>Skyddad natur:</strong> nationalparker och naturreservat.<br><strong>Energi:</strong> ersätta olja, kol och naturgas med vind, sol och vatten.<br><strong>Kretslopp:</strong> återvinning, och produkter som håller längre.</p></div></div>"
 + kolla("4.10", ["Förklara med egna ord vad hållbar utveckling betyder.",
                  "Ge två exempel på ekosystemtjänster och förklara hur de hjälper oss.",
                  "Ge två saker du själv kan göra och en sak som bara samhället kan göra för en mer hållbar framtid."])))

# ---------------------------------------------------------------- Undersök (elevlabb)
LAB_HTML = (
 '<div class="sh small"><h2>Undersök: Var bryts det ner snabbast?</h2></div>'
 "<p>Nedbrytarna arbetar i det tysta, men deras arbete går att mäta. I den här undersökningen gräver du ner tepåsar och väger hur mycket som har brutits ner efter några veckor. Metoden används även av riktiga forskare runt om i världen för att jämföra nedbrytning i olika jordar.</p>"
 + fig(FIG+"ekologi-tepasar.png", "<b>Bild 4.11</b> Tepåsar nedgrävda i tre olika jordar.")
 + row("<p><strong class='green'>Frågeställning:</strong> I vilken jord bryts organiskt material ner snabbast?</p>"
       "<p><strong class='green'>Hypotes:</strong> Skriv vad du tror och motivera med det du vet om nedbrytare.</p>"
       "<p><strong class='green'>Material:</strong> tepåsar med grönt te eller rooibos (utan snöre av plast), våg, spritpenna, glasspinnar som markörer, spade, tre olika platser eller krukor med olika jord.</p>"
       "<h3>Gör så här</h3>"
       + steps(["Märk och väg varje tepåse. Skriv upp vikten.",
                "Gräv ner tre påsar på varje plats, 8 cm djupt. Märk platsen.",
                "Vänta 4–8 veckor. (I kruka inomhus: håll jorden fuktig.)",
                "Gräv upp påsarna, borsta av jorden och låt dem torka ett dygn.",
                "Väg igen och räkna ut hur många procent som har försvunnit."]),
       [table(["Plats", "Före (g)", "Efter (g)", "Förlust (%)"], [["Skogsjord", "", "", ""], ["Gräsmatta", "", "", ""], ["Sand", "", "", ""]], "tbl num"),
        box("begrepp", "Variabler", "<b class='t'>Oberoende</b><p>Typ av jord.</p><b class='t'>Beroende</b><p>Hur mycket av teet som har brutits ner.</p><b class='t'>Kontrollerade</b><p>Samma sorts te, samma djup, samma tid.</p>"),
        box("tank", "Utvärdera", "<p>Var gick nedbrytningen snabbast? Vilka abiotiska faktorer kan förklara skillnaden – fukt, temperatur, syre? Varför ska man ha tre påsar på varje plats?</p>")]))

# ---------------------------------------------------------------- Sammanfattning
SAMMAN = [
 "<strong>Ekologi</strong> handlar om hur organismer samspelar med varandra och med sin miljö, från individ och population till ekosystem och biosfär.",
 "Organismer påverkas av <strong>biotiska faktorer</strong> (andra organismer) och <strong>abiotiska faktorer</strong> (ljus, temperatur, vatten).",
 "<strong>Producenter</strong> gör fotosyntes, <strong>konsumenter</strong> äter andra organismer och <strong>nedbrytare</strong> bryter ner det döda.",
 "<strong>Näringskedjor</strong> visar vem som äter vem. Flera kedjor tillsammans bildar en <strong>näringsväv</strong>.",
 "<strong>Energin flödar</strong> genom ekosystemet. Bara cirka 10 % förs vidare till nästa led, resten blir värme.",
 "<strong>Materien går i kretslopp.</strong> Kol rör sig mellan luften, organismer och marken genom fotosyntes, cellandning, nedbrytning och förbränning.",
 "Populationers storlek begränsas av <strong>resurser</strong>, rovdjur, konkurrens och sjukdomar. Arter har olika <strong>nischer</strong>.",
 "Människan påverkar ekosystemen genom <strong>miljögifter</strong>, <strong>övergödning</strong>, <strong>klimatförändringar</strong>, förlorade livsmiljöer och <strong>invasiva arter</strong>.",
 "<strong>Naturbruk</strong> som skogsbruk, jordbruk och fiske måste vara <strong>hållbart</strong>. Naturen ger oss <strong>ekosystemtjänster</strong>, och <strong>allemansrätten</strong> ger frihet med ansvar."]

BEGR = [("Abiotisk faktor", "Påverkan från den livlösa miljön, t.ex. ljus och temperatur."),
 ("Allemansrätten", "Rätten att vistas i naturen: inte störa, inte förstöra."),
 ("Anrikning", "När ett gift samlas i allt högre halter uppåt i näringskedjan."),
 ("Biosfär", "Alla ekosystem på jorden tillsammans."),
 ("Biotisk faktor", "Påverkan från andra organismer."),
 ("Biotop", "En typ av livsmiljö, t.ex. barrskog eller sjö."),
 ("Ekologi", "Läran om samspelet mellan organismer och deras miljö."),
 ("Ekosystem", "Organismerna och den livlösa miljön i ett område."),
 ("Ekosystemtjänst", "Något naturen gör för oss, t.ex. pollinering eller rent vatten."),
 ("Energipyramid", "Bild som visar hur energin minskar för varje nivå."),
 ("Fragmentering", "När en livsmiljö delas upp i små delar."),
 ("Hållbar utveckling", "Att klara dagens behov utan att ta ifrån framtiden."),
 ("Invasiv art", "Art som människan fört till en ny plats och som skadar andra arter där."),
 ("Kaskadeffekt", "En förändring som sprider sig genom flera nivåer."),
 ("Konkurrens", "När organismer tävlar om samma resurs."),
 ("Konsument", "Organism som äter andra organismer."),
 ("Kretslopp", "När ämnen används om och om igen i naturen."),
 ("Livsmiljö", "Platsen där en art lever."),
 ("Naturbruk", "Att använda naturen för mat och material."),
 ("Nedbrytare", "Svampar och bakterier som bryter ner dött material."),
 ("Nisch", "Artens roll i ekosystemet."),
 ("Näringskedja", "Visar vem som äter vem."),
 ("Näringsväv", "Flera näringskedjor som hänger ihop."),
 ("Population", "Alla individer av en art inom ett område."),
 ("Producent", "Organism som gör sin egen näring genom fotosyntes."),
 ("Symbios", "Samarbete där båda arterna tjänar på det."),
 ("Toppkonsument", "Djur högst upp i näringskedjan."),
 ("Överfiske", "När man fiskar mer än beståndet hinner ersätta."),
 ("Övergödning", "För mycket näringsämnen i sjöar och hav.")]

# ---------------------------------------------------------------- Testa dig själv
# (del, fråga, [alt], poäng/nivåsymbol, antal rader)
TEST = [
 ("A", "Vilken organism är en producent?", ["A Flugsvamp", "B Växtplankton", "C Daggmask", "D Abborre"], 1, 0),
 ("A", "Vad händer med det mesta av energin när en hare äter gräs?", ["A Den lagras i harens kropp och förs vidare till räven.", "B Den används av haren för att leva och blir till slut värme.", "C Den går tillbaka till gräset som näring.", "D Den förvandlas till syre."], 1, 0),
 ("A", "Vilket påstående om kretslopp stämmer?", ["A Både energi och materia går i kretslopp.", "B Energi går i kretslopp, men materia flödar igenom.", "C Materia går i kretslopp, men energi flödar igenom.", "D Varken energi eller materia går i kretslopp."], 2, 0),
 ("A", "Vilket påstående om invasiva arter stämmer?", ["A De är alla arter som har flyttat till en ny plats.", "B De är arter som människan fört till en ny plats och som sprider sig och skadar andra arter.", "C De finns bara i vatten.", "D De hjälper alltid ekosystemet."], 2, 0),
 ("B", "Rita en näringskedja med fyra led från en sjö. Skriv under varje led om det är producent eller konsument.", None, 1, 4),
 ("B", "Ge två abiotiska faktorer och en biotisk faktor som påverkar hur många blåbär det blir i en skog.", None, 1, 3),
 ("C", "I ett skogsområde sköts nästan alla lodjur under några år. Forskare upptäckte efter en tid att det fanns färre unga aspar och rönnar. Använd dina kunskaper om näringskedjor för att förklara varför.", None, 2, 4),
 ("C", "Havsörnen var nära att dö ut i Sverige på 1970-talet på grund av miljögifter, trots att giftet fanns i mycket låga halter i vattnet. Använd dina kunskaper om näringskedjor och förklara varför just havsörnen drabbades så hårt.", None, 3, 5),
 ("D", "TABELL", None, 2, 5),
 ("E", "Övergödning är ett av Östersjöns största miljöproblem. Förklara i flera steg hur utsläpp av näringsämnen från jordbruket kan leda till att fiskar dör på havsbottnen.", None, 3, 5),
 ("E", "Ella säger: ”Om fler människor äter mer vegetarisk mat kan samma åkermark föda fler människor.” Använd energipyramiden för att resonera om Ella har rätt. Ge också ett argument som talar för att djurhållning kan vara bra i Norrbotten.", None, 3, 5),
 ("E", "Signalkräfta och mink är två arter som människan har fört till Sverige. Förklara vad en invasiv art är och varför de kan vara ett hot mot ekosystem. Ge också ett råd som kan hjälpa till att förhindra att fler invasiva arter sprids.", None, 2, 5),
 ("E", "Ett fiskebestånd i ett hav minskar kraftigt. Förklara vad överfiske är och föreslå två åtgärder som kan hjälpa beståndet att återhämta sig. Ge också en anledning till att det kan vara svårt att genomföra åtgärderna.", None, 3, 6),
]
TEST_TABELL = (["Plats", "Prov 1", "Prov 2", "Prov 3", "Prov 4", "Prov 5"],
               [["Lövskog, fuktig", "46", "52", "39", "58", "45"], ["Granplantering, torr", "21", "18", "25", "64", "22"]])
TEST_D_TEXT = "En klass räknade småkryp i förna från två platser. De tog fem prover på varje plats."
TEST_D_SUB = ["a) Räkna ut medelvärdet för lövskogen.",
              "b) Ett värde i granplanteringen skiljer sig från de andra. Vilket? Ge en möjlig förklaring.",
              "c) Vilken slutsats kan klassen dra? Vad betyder det för nedbrytningen på platserna? ●●●"]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Förklara", "D": "Tolka resultat", "E": "Resonera"}
FACIT = [
 "B", "B", "C", "B",
 "T.ex. växtplankton (producent) → djurplankton → mört → gädda (konsumenter).",
 "Abiotiska: ljus, temperatur, nederbörd, frost, jordens näring. Biotisk: pollinerare (humlor), betande djur, konkurrerande växter, svampangrepp.",
 "Lodjuret äter rådjur och harar. När lodjuren försvinner ökar antalet rådjur och harar, och de äter mer av unga aspar och rönnar. Färre unga träd växer upp – en kaskadeffekt i flera led.",
 "Giftet bryts inte ner och lagras i fett. Varje led äter många individer från ledet under, så giftet anrikas och halten blir högst hos toppkonsumenten. Havsörnen äter fisk och sjöfåglar högt upp i kedjan. Giftet gav tunna äggskal och döda ungar, så populationen minskade kraftigt.",
 "a) (46 + 52 + 39 + 58 + 45) / 5 = 48. b) 64 – t.ex. ett prov från en fuktigare plats, mer förna, eller räknefel. c) Det fanns fler småkryp i den fuktiga lövskogen. Fler detritusätare och nedbrytare ger troligen snabbare nedbrytning där. Ett välutvecklat svar diskuterar att 64 påverkar medelvärdet och att fler prover behövs.",
 "Gödning (kväve, fosfor) rinner ut i havet → alger växer mycket → algerna dör och sjunker → nedbrytare bryter ner dem och förbrukar syre → syrebrist vid botten → fiskar och bottendjur dör eller flyr.",
 "Ella har i stort sett rätt: varje led i näringskedjan förlorar cirka 90 % av energin, så att äta växter direkt ger mer mat per yta. Argument för djurhållning: renar och kor kan beta mark där man inte kan odla grödor (t.ex. fjäll, skog, naturbetesmarker), och betet gynnar biologisk mångfald i odlingslandskapet.",
 "En invasiv art är en art som människan fört till en ny plats och som sprider sig och skadar andra arter där. De har ofta inga naturliga fiender, så de kan öka kraftigt och konkurrera ut, äta upp eller smitta arter som redan finns. Signalkräftan bär på kräftpest som slår ut flodkräftan. Råd: släpp aldrig ut akvariedjur eller husdjur och dumpa inte trädgårdsavfall i naturen.",
 "Överfiske är när man fiskar mer än fiskbeståndet hinner ersätta genom att föröka sig och växa. Åtgärder: fiskekvoter, minimimått, fredade områden eller fiskestopp tills beståndet har återhämtat sig. Det kan vara svårt eftersom fiskare förlorar inkomster, och eftersom flera länder fiskar i samma hav och måste komma överens. Ett välutvecklat svar väger ihop miljö, ekonomi och rättvisa.",
]

LGR = ("Kapitlet täcker det centrala innehållet ”Lokala och globala ekosystem. Sambanden mellan populationer och tillgängliga resurser. "
       "Fotosyntes, cellandning, materiens kretslopp och energins flöden” samt ”Människans påverkan på naturen lokalt och globalt samt hur man på individ- och "
       "samhällsnivå kan främja hållbar utveckling. Betydelsen av biologisk mångfald och ekosystemtjänster”, och delar av ”Människans beroende av och påverkan på naturen med koppling till naturbruk, "
       "hållbar utveckling och ekosystemtjänster. Naturen som resurs och vårt ansvar när vi nyttjar den”. Undersökningen tränar fältstudier och experiment. "
       "Uppgifterna följer betygskriteriernas progression: från att beskriva och ge exempel till att förklara samband och resonera i flera led. "
       "De är inspirerade av frisläppta nationella prov: vargarna i Yellowstone (vt 2019, A1 uppg. 4), övergödning (vt 2019, A1 uppg. 3 och vt 2017, A1 uppg. 1) "
       "samt havsörnen och miljögifter (vt 2017, A1 uppg. 6).")
FAKTA = ("Lämmel- och fjällrävskurvorna i bild 4.6 är förenklade och visar ett mönster, inte verkliga data. Tumregeln om 10 % energiöverföring är ett genomsnitt; "
         "verkliga värden varierar. Signalkräftan fördes till Sverige 1960 som försök och sattes ut i större skala från 1969. Uppgiften att ungefär två tredjedelar av Sverige är skogsmark "
         "bygger på Naturvårdsverkets och SCB:s statistik (ca 27 miljoner hektar skogsmark av ca 41 miljoner hektar landareal). Temperaturökningen ”mer än en grad” avser långtidstrenden sedan förindustriell tid; enskilda år kan ligga högre. "
         "Torskfisket i östra Östersjön är kraftigt begränsat sedan 2019 enligt EU:s fiskeregler. Texten om allemansrätten är förenklad; se Naturvårdsverkets information för detaljer. "
         "Källor: Skolverket, Lgr22 kursplan i biologi. · Umeå universitet: tidigare givna nationella prov i biologi åk 9 (vt 2017, vt 2019). · Rädda en art: Havsörnen – ett projekt med stor framgång. · "
         "SLU Artdatabanken: Rödlista 2025. · Havs- och vattenmyndigheten: faktablad om signalkräfta och flodkräfta. · Naturvårdsverket: skogsmark i statistik, allemansrätten. · "
         "SMHI och WMO om global uppvärmning. · Illustrationer: egenritade för detta kapitel.")

BONUS = dict(
 titel="Småkryp i förnan",
 ingress="Med en tratt, ett nät och en lampa kan eleverna få fram hundratals småkryp ur en handfull löv. En enkel men spektakulär labb om livet i marken.",
 syfte="Eleverna samlar in och artbestämmer småkryp från förna med en egen Berlesetratt. De ser med egna ögon de detritusätare och rovdjur som håller igång nedbrytningen. Labben kopplar till näringsvävar, nedbrytare och fältstudier, och kan bli en jämförande undersökning mellan två platser.",
 tid="Insamling 15 min ute. Tratten står 1–3 dygn. Artbestämning och redovisning 1 lektion. Grupper om 3–4.",
 material=["Stor tratt (eller avklippt PET-flaska)", "Nät eller trådnät med 2–3 mm maskor", "Skrivbordslampa (glödlampa eller halogen ger värme)", "Burk med fuktigt papper eller lite vatten", "Påse förna och översta jordlagret, ca 1 liter", "Lupp eller stereolupp, petriskål, pensel", "Enkel nyckel över småkryp"],
 genomf=["Samla förna från en tydligt avgränsad yta, t.ex. 25 × 25 cm, så att proverna blir jämförbara.", "Lägg förnan löst på nätet i tratten. Lampan ska vara 10–15 cm ovanför.", "Djuren flyr ljus, värme och uttorkning – nedåt – och faller ner i burken.", "Töm burken i en petriskål och sortera djuren i grupper med lupp.", "Jämför gärna två platser, t.ex. lövskog och granskog, fuktigt och torrt."],
 resultat="Hoppstjärtar och kvalster är nästan alltid flest. Man brukar också hitta spindlar, gråsuggor, tusenfotingar, små skalbaggar och fluglarver. Fuktig lövförna innehåller oftast fler djur än torr barrförna. Hoppstjärtar, kvalster och gråsuggor äter dött material och svamptrådar. Spindlar, enfotingar och rovkvalster äter dem – en egen liten näringsväv i marken.",
 sakerhet=["Lampan blir varm: inget papper nära, stäng av över natten om det behövs.", "Tvätta händerna efter jordarbete.", "Använd vatten i burken om djuren ska släppas tillbaka; använd bara etanol om de ska bevaras och efter samråd."],
 problem=["Få djur: förnan var för torr, för lite material eller för kort tid.", "Jord rinner ner: lägg ett lager förna överst och använd finare nät."],
 bedom=[("Grundläggande", "Sorterar och räknar djuren och redovisar i tabell."), ("Utvecklat", "Delar in djuren i nedbrytare/detritusätare och rovdjur och ritar en näringsväv."), ("Välutvecklat", "Jämför platser, förklarar skillnader med abiotiska faktorer och värderar metoden.")],
)
