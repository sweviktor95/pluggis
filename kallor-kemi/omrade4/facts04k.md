# Fakta kemi 4 – Kemiska föreningar och reaktioner (hämtade 2026-10-22)

Status: K2 = öppnad och kontrollerad 2026-10-22. E = ej kontrollerad mot källa (skrivs försiktigt).

## Källor (öppnade)
- cog_bond: https://cognito.org/cheat-sheets/gcse-chemistry/ionic-covalent-and-metallic-bonding (K2)
- tc_ionic: https://www.tutorchase.com/notes/cie-igcse/chemistry/2-4-3-ionic-compounds:-formation-and-properties (K2)
- aact_kitchen: https://teachchemistry.org/classroom-resources/kitchen-reaction (K2)
- pmt_rates: https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Notes/Edexcel/7-Rates-of-Reaction-and-Energy-Changes/Definitions%20-%20Topic%207%20Rates%20of%20Reaction%20and%20Energy%20Changes%20-%20Edexcel%20Chemistry%20GCSE.pdf (K2)
- tc_rust: https://tutorchase.com/answers/igcse/chemistry/what-are-effective-methods-to-prevent-rusting (K2)
- lt_polar: https://chem.libretexts.org/Courses/Harper_College/CHM_110%3A_Fundamentals_of_Chemistry/04%3A_Water/4.03%3A_Polarity_of_Bonds_and_Molecules (K2)
- Lavoisier: redan 'sh_lavoisier' i kallor_ref_k.py

## 4.1 Molekyler och joner
- Kovalent bindning: mellan icke-metaller, atomer delar elektronpar så att varje atom får fullt yttersta skal (cog_bond).
- HCl delar ett elektronpar; O2 delar två par (dubbelbindning); CH4: kol delar elektroner med fyra väte, fyra enkelbindningar (cog_bond).
- Enkla molekylföreningar: låga smält- och kokpunkter (svaga krafter mellan molekyler), ofta gas, vätska eller mjukt fast ämne; leder inte ström (inga fria laddade partiklar); oftast olösliga i vatten, men vissa polära, t.ex. socker, löser sig (cog_bond).
- Jonbindning: metall + icke-metall; metallen avger elektron(er), icke-metallen tar upp, motsatt laddade joner hålls ihop av stark elektrostatisk attraktion i ett jonkristallgitter (cog_bond).
- NaCl: Na avger 1 elektron -> Na+, Cl tar upp 1 -> Cl- (cog_bond, tc_ionic). Na har 1 elektron i yttersta skalet, Cl har 7 (tc_ionic).
- Gitter: varje positiv jon omges av negativa och tvärtom (tc_ionic).
- NaCl smälter vid 801 °C (tc_ionic). Jonföreningar: höga smält-/kokpunkter, hårda men spröda (om lager förskjuts stöter lika laddningar ihop), ofta lösliga i vatten (cog_bond).
- Ledningsförmåga: fast salt leder inte (jonerna sitter fast); smält och löst leder (jonerna kan röra sig) (cog_bond, tc_ionic).
- Vatten löser salt: polära vattenmolekyler skiljer jonerna åt (tc_ionic).
- Metaller: metallbindning, rörliga yttre elektroner; leder ström och värme; formbara; blanka; kvicksilver flytande (cog_bond).
- Egen kunskap (skalmodell 2/8/8 från kemi 3): Na 2,8,1; Cl 2,8,7; Na+ 2,8 (som neon); Cl- 2,8,8 (som argon). Ädelgasmodellen "fullt skal" är en förenkling. [allmänt kända fakta, ej webbkontrollerade]

## Fördjupning 4.1
- Elektronegativitet = relativ dragningskraft på bindningselektroner; Pauling skapade första skalan (lt_polar).
- Skillnad ΔEN: 0–0,4 opolär kovalent; 0,5–2,0 polär kovalent; >2,0 troligen jonbindning, gränsen är något godtycklig (lt_polar).
- Värden: O 3,5; Cl 3,0; C 2,5; H 2,1 (lt_polar). Na ej angivet i texten (E: ca 0,9, ej kontrollerat – använd inte som siffra).
- C–H ΔEN 0,4 opolär; O–H ΔEN 1,4 polär (lt_polar).
- Vatten polärt: vinklad form, dipolerna tar inte ut varandra; CO2 linjär, dipolerna tar ut varandra, opolär; polära ämnen har oftast högre smält-/kokpunkt och löser sig bättre i vatten (lt_polar).
- E: kemiska namn (natriumklorid, koldioxid, dikväveoxid-regler, prefix mono/di/tri) – allmän kunskap, ej källa.

## 4.2 Kemiska reaktioner
- Tecken på reaktion (aact_kitchen): bubblor = gasbildning; temperaturfall (endoterm); observera syn, lukt, ljud. E: färgförändring, fällning, ljus/värme – vanligt i läromedel, ej separat kontrollerat här.
- Ättika + bikarbonat: öppet system, gas lämnar, slutmassan blir mindre än startmassan; slutet system: massan ska vara oförändrad (bortsett från mätfel) (aact_kitchen). Reaktionen tar upp värme (temperaturfall) (aact_kitchen).
- Säkerhet (aact_kitchen): skyddsglasögon, vid syra på huden spola med vatten, tvätta händer, följ instruktion för uppstädning.
- E: ättiksyra + natriumvätekarbonat -> natriumacetat + vatten + koldioxid (allmän kemi, ej källa). Flaskor får inte vara hårt stängda om mycket gas bildas (tryck) – använd liten mängd och ballong/lock löst; skriv försiktigt.
- Massbevarande/Lavoisier: se 'sh_lavoisier'.
- Förbränning, rost (järn + syre + vatten), syra + metall: allmän kunskap (E för detaljer). Rostvillkor: syre och vatten behövs (tc_rust: nyckeln är att hålla syre och vatten borta från järnet).
- Korrosionsskydd (tc_rust): galvanisering (zink; skyddar även vid repa eftersom zink är mer reaktivt), målning/oljning (barriär, måste täcka och underhållas), offeranod (magnesium/zink på skrov, rörledningar), legering (rostfritt stål: järn, krom, nickel; kromoxidskikt).
- Reaktionshastighet (pmt_rates): mängd produkt/reaktant per tid; kollisionsteori – partiklar måste kollidera med rätt orientering och tillräcklig energi; temperatur (högre rörelseenergi, fler kollisioner, fler når aktiveringsenergi); koncentration (tätare partiklar, fler kollisioner); ytarea (fler exponerade partiklar); katalysator (annan väg med lägre aktiveringsenergi, förbrukas inte).
- Exoterm: avger energi till omgivningen, omgivningen blir varmare; endoterm: tar upp energi, omgivningen blir kallare (pmt_rates). Exempel (aact_kitchen): vätgasperoxid + kaliumjodid avger värme (lärardemo, ej elev); ättika+bikarbonat endoterm.
- E: exempel förbränning/värmedyna exoterm; kall-kompress/fotosyntes endoterm – allmänt kända.

## E-lista (skrivs försiktigt, flaggas i slutrapport)
1. Na elektronegativitet – ingen siffra.
2. Färgförändring/fällning som reaktionstecken – allmänt.
3. Exakt reaktionsformel ättika+bikarbonat – allmänt.
4. Namnregler för kemiska föreningar (fördjupning).
5. Exempel exoterma/endotermt utöver källorna.
6. Brandsäkerhet (brandtriangeln: bränsle, syre, värme) – allmän kunskap, ej källa.
