# -*- coding: utf-8 -*-
import json
KAT = [
 ("Undersökningar", [
   ("Biologi är läran om …?", "allt som lever / livet"),
   ("I ett rättvist test ändrar man hur många saker?", "en"),
   ("Vad kallas variabeln du mäter?", "beroende variabel"),
   ("Varför har man en kontrollgrupp?", "för att ha något att jämföra med"),
   ("Vad kallas det när slumpen bestämmer vem som hamnar i vilken grupp?", "randomisering")]),
 ("Tabeller och diagram", [
   ("Vad ska stå efter siffran i en tabell, till exempel mm?", "enhet"),
   ("Vad ska ett diagram ha överst?", "rubrik"),
   ("Vilket diagram passar bäst för att jämföra två grupper?", "stapeldiagram"),
   ("Vilket diagram passar när något förändras över tid?", "linjediagram"),
   ("Ett värde avviker mycket från de andra. Vad gör du först?", "undersöker om det finns en förklaring (t.ex. ett misstag) och redovisar det")]),
 ("Värdera", [
   ("Vad kallas något som kan göra att resultatet blir fel?", "felkälla"),
   ("Varför gör man om ett försök flera gånger?", "slumpen påverkar mindre / resultatet blir säkrare"),
   ("Vad kallas det att man får samma resultat när man upprepar försöket?", "tillförlitlighet"),
   ("Ge ett exempel på ett systematiskt fel.", "t.ex. en låda som alltid är varmare / ett instrument som visar fel"),
   ("Fiskätare lever längre, men de äter också mer grönsaker. Vad kallas grönsakerna i sambandet?", "störfaktor")]),
 ("Forskare som ändrat sig", [
   ("Vilka visade att magsår orsakas av en bakterie?", "Marshall och Warren"),
   ("Vad kräver Semmelweis av läkarna 1847?", "att de tvättar händerna (i klorkalk)"),
   ("Vad visade Pasteurs svanhalskolv?", "att mikroorganismer kommer utifrån"),
   ("Vad heter bakterien i magsäcken?", "Helicobacter pylori"),
   ("Ge ett skäl till att många inte trodde på Semmelweis.", "han kunde inte förklara hur / man kände inte till bakterier / läkarna ville inte skylla på sig själva")]),
 ("Källor och påståenden", [
   ("Mätningar som visar något kallas …?", "belägg"),
   ("Något som låter som vetenskap men saknar belägg?", "pseudovetenskap"),
   ("Vad kallas en källa som passar din fråga?", "relevant"),
   ("Nämn ett av de fyra källkritiska kriterierna.", "äkthet, tid, beroende eller tendens"),
   ("Studien är betald av företaget som säljer produkten. Vilket kriterium handlar det om?", "tendens (och beroende)")]),
]
NIV = {100: "Lättläst", 200: "Lättläst", 300: "Grundtext", 400: "Grundtext", 500: "Fördjupning"}
data = [{"kat": k, "fr": [{"p": 100*(i+1), "q": q, "a": a} for i, (q, a) in enumerate(fr)]} for k, fr in KAT]
HTML = r"""<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jeopardy: Biologi som vetenskap</title>
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
.board{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;padding:8px 16px 24px}
.cat{background:var(--g2);color:#fff;font-weight:700;text-align:center;padding:12px 6px;border-radius:8px;display:flex;align-items:center;justify-content:center;min-height:56px}
.tile{background:var(--g1);color:#fff;border:0;border-radius:8px;font-size:clamp(1.2rem,3vw,2rem);font-weight:800;padding:22px 4px;cursor:pointer}
.tile[disabled]{background:var(--line);color:transparent;cursor:default}
.ov{position:fixed;inset:0;background:rgba(10,20,15,.82);display:none;align-items:center;justify-content:center;padding:16px;z-index:10}
.ov.vis{display:flex}
.box{background:var(--card);border-radius:16px;max-width:900px;width:100%;padding:24px;text-align:center}
.box .lv{color:var(--g2);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.85rem}
.box .q{font-size:clamp(1.4rem,3.4vw,2.4rem);font-weight:700;margin:14px 0}
.box .a{font-size:clamp(1.2rem,3vw,2rem);color:var(--g1);font-weight:800;margin:10px 0;min-height:2.6rem}
.row{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:8px}
.ok{background:#2f8a4f}.no{background:#b3402f}
#lar{display:none;padding:0 16px 40px}
#lar.vis{display:block}
#lar table{width:100%;border-collapse:collapse;margin-bottom:16px;background:var(--card)}
#lar th,#lar td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
#lar th{background:var(--g2);color:#fff}
.note{padding:0 16px 24px;color:var(--ink);opacity:.8;font-size:.9rem}
@media print{header .btn,.teams,.board,.note{display:none}#lar{display:block}}
</style></head><body>
<header><h1>Jeopardy: Biologi som vetenskap</h1>
<div class="row"><button class="btn alt" id="lagBtn">+ Lag</button><button class="btn alt" id="larBtn">Lärarvy: alla svar</button><button class="btn" id="nytt">Nytt spel</button></div></header>
<div class="teams" id="teams"></div>
<div class="board" id="board" role="grid" aria-label="Spelplan"></div>
<p class="note">Poängen visar nivån: 100–200 går att klara med lättläst, 300–400 med grundtexten och 500 med fördjupningen. Svaren är korta, ett ord eller en kort mening. Personer och exempel i frågorna är påhittade.</p>
<div id="lar"></div>
<div class="ov" id="ov" role="dialog" aria-modal="true" aria-live="polite"><div class="box">
<div class="lv" id="lv"></div><div class="q" id="q"></div><div class="a" id="a"></div>
<div class="row"><button class="btn alt" id="vis">Visa svar</button></div>
<div class="row" id="bed" style="display:none"><button class="btn ok" id="ratt">Rätt</button><button class="btn no" id="fel">Fel</button><button class="btn alt" id="hopp">Ingen poäng</button></div>
</div></div>
<script>
var DATA=__DATA__;
var NIV={100:"Lättläst",200:"Lättläst",300:"Grundtext",400:"Grundtext",500:"Fördjupning"};
var lag=[{n:"Lag 1",p:0},{n:"Lag 2",p:0}],tur=0,aktuell=null,anv={};
function rita(){
  var b=document.getElementById("board");b.innerHTML="";
  DATA.forEach(function(c){var d=document.createElement("div");d.className="cat";d.textContent=c.kat;b.appendChild(d);});
  for(let r=0;r<5;r++){DATA.forEach(function(c,ci){var f=c.fr[r];var t=document.createElement("button");t.className="tile";t.textContent=f.p;
    var k=ci+"-"+r;if(anv[k]){t.disabled=true;}t.setAttribute("aria-label",c.kat+" "+f.p+" poäng");t.onclick=function(){oppna(ci,r,k);};b.appendChild(t);});}
  var tm=document.getElementById("teams");tm.innerHTML="";
  lag.forEach(function(l,i){var d=document.createElement("div");d.className="team"+(i===tur?" on":"");
    var inp=document.createElement("input");inp.value=l.n;inp.setAttribute("aria-label","Lagnamn");inp.oninput=function(){l.n=inp.value;};
    var p=document.createElement("div");p.className="pts";p.textContent=l.p;d.appendChild(inp);d.appendChild(p);d.onclick=function(e){if(e.target.tagName!=="INPUT"){tur=i;rita();}};tm.appendChild(d);});
}
function oppna(ci,r,k){var f=DATA[ci].fr[r];aktuell={k:k,p:f.p};
  document.getElementById("lv").textContent=DATA[ci].kat+" · "+f.p+" · "+NIV[f.p];
  document.getElementById("q").textContent=f.q;document.getElementById("a").textContent="";
  document.getElementById("vis").style.display="";document.getElementById("bed").style.display="none";
  document.getElementById("ov").classList.add("vis");document.getElementById("vis").focus();
  document.getElementById("vis").onclick=function(){document.getElementById("a").textContent=f.a;this.style.display="none";document.getElementById("bed").style.display="flex";};}
function stang(ratt){anv[aktuell.k]=1;if(ratt===1){lag[tur].p+=aktuell.p;}else if(ratt===-1){lag[tur].p-=aktuell.p;}
  tur=(tur+1)%lag.length;document.getElementById("ov").classList.remove("vis");rita();}
document.getElementById("ratt").onclick=function(){stang(1);};
document.getElementById("fel").onclick=function(){stang(-1);};
document.getElementById("hopp").onclick=function(){stang(0);};
document.getElementById("lagBtn").onclick=function(){if(lag.length<6){lag.push({n:"Lag "+(lag.length+1),p:0});rita();}};
document.getElementById("nytt").onclick=function(){lag.forEach(function(l){l.p=0;});anv={};tur=0;rita();};
document.getElementById("larBtn").onclick=function(){document.getElementById("lar").classList.toggle("vis");};
document.addEventListener("keydown",function(e){if(e.key==="Escape"){document.getElementById("ov").classList.remove("vis");}});
var h="";DATA.forEach(function(c){h+="<h2>"+c.kat+"</h2><table><tr><th>Poäng</th><th>Nivå</th><th>Fråga</th><th>Svar</th></tr>";
  c.fr.forEach(function(f){h+="<tr><td>"+f.p+"</td><td>"+NIV[f.p]+"</td><td>"+f.q+"</td><td>"+f.a+"</td></tr>";});h+="</table>";});
document.getElementById("lar").innerHTML=h;
rita();
</script></body></html>"""
open('/home/claude/pluggis/simuleringar/jeopardy-bio-1.html', 'w', encoding='utf8').write(HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False)))
print("ok", sum(len(c["fr"]) for c in data))
