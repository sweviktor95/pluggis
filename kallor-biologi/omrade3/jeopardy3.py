# -*- coding: utf-8 -*-
import json
KAT = [
 ("Mångfald", [
   ("Vilka tre nivåer har biologisk mångfald?", "gener (genetisk mångfald), arter och ekosystem"),
   ("Vad kallas alla individer av en art i ett område?", "population"),
   ("Vad menas med artrikedom?", "antalet olika arter i ett område"),
   ("Varför klarar ett artrikt ekosystem störningar bättre?", "det finns fler arter som kan ta över en uppgift (reservdelar) och arterna reagerar olika"),
   ("Varför slog potatisbladmögel så hårt mot potatisen på Irland på 1840-talet?", "nästan alla plantor var genetiskt mycket lika, så ingen tålde sjukdomen")]),
 ("Naturens tjänster", [
   ("Vilka fyra typer av ekosystemtjänster finns det?", "försörjande, reglerande, stödjande och kulturella"),
   ("Vad kallas det när pollen flyttas mellan blommor?", "pollinering"),
   ("Ge ett exempel på en reglerande ekosystemtjänst.", "t.ex. pollinering, vattenrening i våtmark, koldioxidupptag i skog"),
   ("Hur kan en myr minska risken för översvämning?", "den suger upp vatten som en svamp och släpper ut det långsamt"),
   ("Varför är många pollinerande arter säkrare än en enda?", "om en art får ett dåligt år kan de andra fortfarande pollinera")]),
 ("Hot och skydd", [
   ("Nämn ett av de fem största hoten mot mångfalden.", "ändrad markanvändning, överuttag, klimatförändringar, föroreningar eller invasiva arter"),
   ("Vad är en rödlista?", "en förteckning över arter och hur stor risken är att de försvinner"),
   ("Vad är en signalart? Ge ett exempel.", "art som visar att miljön har höga naturvärden, t.ex. garnlav i gammal skog"),
   ("Nämn två orsaker till att fjällräven haft svårt att öka.", "jakt förr, brist på lämlar, rödräven konkurrerar"),
   ("Varför kan en ökning av antalet rödlistade arter bero på något annat än att naturen mår sämre?", "forskarna kan ha bedömt fler arter än förut")]),
 ("Riken och nycklar", [
   ("Nämn de fem rikena.", "djur, växter, svampar, bakterier och encelliga organismer med cellkärna"),
   ("Vad är en lav?", "en samlevnad mellan en svamp och en alg eller bakterie som gör fotosyntes"),
   ("Hur skrivs en arts vetenskapliga namn?", "två latinska ord: släkte och art, t.ex. Pinus sylvestris"),
   ("Vad är en bestämningsnyckel?", "en serie val med två alternativ som leder till artens namn"),
   ("Delfin och haj ser lika ut men är inte nära släkt. Vad kallas det när olika arter utvecklar liknande drag?", "konvergent evolution")]),
 ("Anpassning", [
   ("Vad är en anpassning?", "ett drag som gör att en art klarar sin miljö"),
   ("Nämn en anpassning hos fjällräven.", "t.ex. tjock päls, små öron, vit vinterpäls"),
   ("Vad kallas skillnader mellan individer av samma art?", "variation"),
   ("Beskriv naturligt urval med tre ord.", "variation, urval, ärftlighet"),
   ("Hur blir bakterier resistenta mot antibiotika?", "några bakterier är redan resistenta av en slump, de överlever behandlingen och förökar sig (naturligt urval)")]),
]
NIV = {100: "Lättläst", 200: "Lättläst", 300: "Grundtext", 400: "Grundtext", 500: "Fördjupning"}
data = [{"kat": k, "fr": [{"p": 100*(i+1), "q": q, "a": a} for i, (q, a) in enumerate(fr)]} for k, fr in KAT]
HTML = r"""<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jeopardy: Biologisk mångfald</title>
<style>
:root{--g1:#245040;--g2:#2f6b4f;--g3:#4f8a63;--ink:#1f2a24;--bg:#f4f7f3;--card:#fff;--line:#cfd9d2;--acc:#e0782f}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--ink:#e8efe9;--bg:#16201b;--card:#1f2c25;--line:#34473d;--g1:#9fd0b3;--g2:#3f8a62}}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,Segoe UI,Arial,sans-serif;background:var(--bg);color:var(--ink)}
header{padding:12px 16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between}
h1{font-size:1.25rem;margin:0;color:var(--g1)}
.btn{background:var(--g2);color:#fff;border:0;border-radius:8px;padding:8px 14px;font-size:.95rem;cursor:pointer}
.btn.alt{background:transparent;color:var(--g2);border:1.5px solid var(--g2)}
.btn:focus-visible,.tile:focus-visible{outline:3px solid var(--acc);outline-offset:2px}
.teams{display:flex;flex-wrap:wrap;gap:8px;padding:0 16px 8px}
.team{background:var(--card);border:2px solid var(--line);border-radius:10px;padding:6px 12px;min-width:130px}
.team.on{border-color:var(--acc);box-shadow:0 0 0 2px var(--acc) inset}
.team input{width:100%;border:0;background:transparent;font:inherit;font-weight:700;color:var(--ink)}
.team .pts{font-size:1.5rem;font-weight:800;color:var(--g1)}
.board{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));grid-auto-rows:minmax(72px,auto);gap:8px;padding:8px 16px 24px}
.cat{background:var(--g2);color:#fff;font-weight:700;text-align:center;padding:8px 6px;border-radius:8px;display:flex;align-items:center;justify-content:center;min-height:72px;width:100%;overflow-wrap:anywhere;hyphens:auto;font-size:clamp(.8rem,1.8vw,1.1rem)}
.tile{background:var(--g1);color:#fff;border:0;border-radius:8px;font-size:clamp(1.2rem,3vw,2rem);font-weight:800;padding:0;width:100%;height:100%;min-height:72px;cursor:pointer}
.tile[disabled]{background:var(--line);color:transparent;cursor:default}
.ov{position:fixed;inset:0;background:rgba(10,20,15,.82);display:none;align-items:center;justify-content:center;padding:16px;z-index:10}
.ov.vis{display:flex}
.box{background:var(--card);border-radius:16px;max-width:900px;width:100%;padding:24px;text-align:center}
.box .lv{color:var(--g2);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.85rem}
.box .q{font-size:clamp(1.4rem,3.4vw,2.4rem);font-weight:700;margin:14px 0}
.box .a{font-size:clamp(1.2rem,3vw,2rem);color:var(--g1);font-weight:800;margin:10px 0;min-height:2.6rem}
.row{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:8px}

#lar{display:none;padding:0 16px 40px}
#lar.vis{display:block}
#lar table{width:100%;border-collapse:collapse;margin-bottom:16px;background:var(--card)}
#lar th,#lar td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
#lar th{background:var(--g2);color:#fff}
.note{padding:0 16px 24px;color:var(--ink);opacity:.8;font-size:.9rem}
.start{max-width:520px;margin:24px auto;background:var(--card);border:2px solid var(--line);border-radius:14px;padding:20px}
.start h2{margin:0 0 10px;color:var(--g1);font-size:1.15rem}
.antal{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.antal .btn{min-width:48px}.antal .btn.val{background:var(--g2);color:#fff}
.namn{display:flex;flex-direction:column;gap:8px;margin-bottom:14px}
.namn input{padding:9px 10px;border:1.5px solid var(--line);border-radius:8px;font:inherit;background:var(--bg);color:var(--ink)}
.lagrad{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:8px 4px;border-top:1px solid var(--line)}
.lagrad .ln{font-weight:700;text-align:left;flex:1}
.lagrad .vb{display:flex;gap:6px}
.vb .btn{min-width:84px;background:transparent;color:var(--ink);border:2px solid var(--line)}
.vb .btn.ok.pa{background:#2f8a4f;color:#fff;border-color:#2f8a4f}
.vb .btn.no.pa{background:#b3402f;color:#fff;border-color:#b3402f}
@media print{header .btn,.teams,.board,.note{display:none}#lar{display:block}}
@media(max-width:520px){.cat{font-size:.62rem!important;padding:4px 2px;hyphens:none!important;overflow-wrap:normal!important;word-break:normal!important}}
</style></head><body>
<header><h1>Jeopardy: Biologisk mångfald</h1>
<div class="row"><button class="btn alt" id="larBtn">Lärarvy: alla svar</button><button class="btn" id="nytt">Nytt spel</button></div></header>
<div class="start" id="start"></div>
<div class="teams" id="teams"></div>
<div class="board" id="board" role="grid" aria-label="Spelplan"></div>
<p class="note">Poängen visar nivån: 100–200 går att klara med lättläst, 300–400 med grundtexten och 500 med fördjupningen. Svaren är korta, ett ord eller en kort mening. Personer och exempel i frågorna är påhittade.</p>
<div id="lar"></div>
<div class="ov" id="ov" role="dialog" aria-modal="true" aria-live="polite"><div class="box">
<div class="lv" id="lv"></div><div class="q" id="q"></div><div class="a" id="a"></div>
<div class="row"><button class="btn alt" id="vis">Visa svar</button></div>
<div id="bed" style="display:none"><div id="lagrader"></div><div class="row"><button class="btn" id="klar">Klar</button></div></div>
</div></div>
<script>
var DATA=__DATA__;
var NIV={100:"Lättläst",200:"Lättläst",300:"Grundtext",400:"Grundtext",500:"Fördjupning"};
var lag=[],aktuell=null,anv={},val={},antal=2;
function startskarm(){
  document.getElementById("board").style.display="none";document.getElementById("teams").style.display="none";
  var st=document.getElementById("start");st.style.display="";
  var h='<h2>Hur många lag?</h2><div class="antal">';
  for(var n=1;n<=6;n++){h+='<button class="btn alt'+(n===antal?' val':'')+'" data-n="'+n+'">'+n+'</button>';}
  h+='</div><h2>Lagnamn</h2><div class="namn">';
  for(var i=0;i<antal;i++){h+='<input type="text" maxlength="24" aria-label="Lag '+(i+1)+'" placeholder="Lag '+(i+1)+'" value="'+(window.__namn&&window.__namn[i]||"")+'">';}
  h+='</div><button class="btn" id="spela">Starta spelet</button>';
  st.innerHTML=h;
  Array.prototype.forEach.call(st.querySelectorAll("[data-n]"),function(bt){bt.onclick=function(){sparaNamn();antal=+bt.getAttribute("data-n");startskarm();};});
  document.getElementById("spela").onclick=function(){sparaNamn();
    lag=[];for(var i=0;i<antal;i++){lag.push({n:(window.__namn[i]||"").trim()||("Lag "+(i+1)),p:0});}
    anv={};st.style.display="none";document.getElementById("board").style.display="";document.getElementById("teams").style.display="";rita();};
}
function sparaNamn(){window.__namn=Array.prototype.map.call(document.querySelectorAll(".namn input"),function(x){return x.value;});}
function rita(){
  var b=document.getElementById("board");b.innerHTML="";
  DATA.forEach(function(c){var d=document.createElement("div");d.className="cat";d.textContent=c.kat;b.appendChild(d);});
  for(let r=0;r<5;r++){DATA.forEach(function(c,ci){var f=c.fr[r];var t=document.createElement("button");t.className="tile";t.textContent=f.p;
    var k=ci+"-"+r;if(anv[k]){t.disabled=true;}t.setAttribute("aria-label",c.kat+" "+f.p+" poäng");t.onclick=function(){oppna(ci,r,k);};b.appendChild(t);});}
  var tm=document.getElementById("teams");tm.innerHTML="";
  lag.forEach(function(l){var d=document.createElement("div");d.className="team";
    var nm=document.createElement("div");nm.style.fontWeight="700";nm.textContent=l.n;
    var p=document.createElement("div");p.className="pts";p.textContent=l.p;d.appendChild(nm);d.appendChild(p);tm.appendChild(d);});
}
function oppna(ci,r,k){var f=DATA[ci].fr[r];aktuell={k:k,p:f.p};val={};
  document.getElementById("lv").textContent=DATA[ci].kat+" · "+f.p+" · "+NIV[f.p];
  document.getElementById("q").textContent=f.q;document.getElementById("a").textContent="";
  document.getElementById("vis").style.display="";document.getElementById("bed").style.display="none";
  document.getElementById("ov").classList.add("vis");document.getElementById("vis").focus();
  document.getElementById("vis").onclick=function(){document.getElementById("a").textContent=f.a;this.style.display="none";
    visaLag();document.getElementById("bed").style.display="";};}
function visaLag(){var h="";
  lag.forEach(function(l,i){h+='<div class="lagrad"><span class="ln"></span><span class="vb"><button class="btn ok" data-i="'+i+'" data-v="1">Rätt</button><button class="btn no" data-i="'+i+'" data-v="-1">Fel</button></span></div>';});
  var c=document.getElementById("lagrader");c.innerHTML=h;
  Array.prototype.forEach.call(c.querySelectorAll(".ln"),function(e,i){e.textContent=lag[i].n;});
  Array.prototype.forEach.call(c.querySelectorAll("button"),function(bt){bt.onclick=function(){
    var i=bt.getAttribute("data-i"),v=+bt.getAttribute("data-v");val[i]=(val[i]===v)?0:v;
    Array.prototype.forEach.call(c.querySelectorAll('button[data-i="'+i+'"]'),function(x){x.classList.toggle("pa",+x.getAttribute("data-v")===val[i]);x.setAttribute("aria-pressed",+x.getAttribute("data-v")===val[i]);});};});}
document.getElementById("klar").onclick=function(){anv[aktuell.k]=1;
  lag.forEach(function(l,i){if(val[i]===1){l.p+=aktuell.p;}else if(val[i]===-1){l.p-=aktuell.p;}});
  document.getElementById("ov").classList.remove("vis");rita();};
document.getElementById("nytt").onclick=function(){startskarm();};
document.getElementById("larBtn").onclick=function(){document.getElementById("lar").classList.toggle("vis");};
document.addEventListener("keydown",function(e){if(e.key==="Escape"){document.getElementById("ov").classList.remove("vis");}});
var h="";DATA.forEach(function(c){h+="<h2>"+c.kat+"</h2><table><tr><th>Poäng</th><th>Nivå</th><th>Fråga</th><th>Svar</th></tr>";
  c.fr.forEach(function(f){h+="<tr><td>"+f.p+"</td><td>"+NIV[f.p]+"</td><td>"+f.q+"</td><td>"+f.a+"</td></tr>";});h+="</table>";});
document.getElementById("lar").innerHTML=h;
startskarm();
</script></body></html>"""
open('/home/claude/pluggis/simuleringar/jeopardy-bio-3.html', 'w', encoding='utf8').write(HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False)))
print("ok", sum(len(c["fr"]) for c in data))
