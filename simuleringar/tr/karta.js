/* Karta-tidsresa: världskarta, flygning till varje plats (nedslag) med fakta, scen och fråga. Specifikation i window.SCEN (etapper med kart:[lon,lat,bredd], valfritt zon:[[lon,lat,rx,ry],...]). */
(function(){
var S=window.SCEN, ET=S.etapper, N=ET.length, QUIZ=N-1;
var NS="http://www.w3.org/2000/svg";
var R=Math.PI/180, SC=170;
function proj(lon,lat){var l=lon*R,p=lat*R,p2=p*p,p4=p2*p2;var x=l*(0.8707-0.131979*p2+p4*(-0.013791+p4*(0.003971*p2-0.001529*p4)));var y=p*(1.007226+p2*(0.015085+p4*(-0.044475+0.028874*p2-0.005916*p4)));return [x*SC,-y*SC];}
var svg=document.getElementById("svg"),landG=document.getElementById("land"),gratG=document.getElementById("grat"),zonG=document.getElementById("zon"),marksG=document.getElementById("marks"),labG=document.getElementById("labels");
var dock=document.getElementById("dock"),stepsEl=document.getElementById("steps"),clock=document.getElementById("clock");
function pathOf(pts){return "M"+pts.map(function(q){var p=proj(q[0],q[1]);return p[0].toFixed(1)+" "+p[1].toFixed(1)}).join("L")+"Z"}
function ringPath(pts){var out=[pts[0].slice()],mn=pts[0][0],mx=pts[0][0];for(var i=1;i<pts.length;i++){var lon=pts[i][0],prev=out[i-1][0];while(lon-prev>180)lon-=360;while(lon-prev<-180)lon+=360;out.push([lon,pts[i][1]]);mn=Math.min(mn,lon);mx=Math.max(mx,lon);}
  var d=pathOf(out);if(mx>180)d+=pathOf(out.map(function(q){return [q[0]-360,q[1]]}));if(mn<-180)d+=pathOf(out.map(function(q){return [q[0]+360,q[1]]}));return d;}
function drawGrat(){var d="",lon,lat,pts;for(lon=-180;lon<=180;lon+=20){pts=[];for(lat=-80;lat<=80;lat+=4)pts.push(proj(lon,lat));d+="M"+pts.map(function(p){return p[0].toFixed(1)+" "+p[1].toFixed(1)}).join("L");}
  for(lat=-60;lat<=80;lat+=20){pts=[];for(lon=-180;lon<=180;lon+=4)pts.push(proj(lon,lat));d+="M"+pts.map(function(p){return p[0].toFixed(1)+" "+p[1].toFixed(1)}).join("L");}
  gratG.innerHTML='<path class="grat" d="'+d+'"/>';}
function drawLand(){var topo=window.Datamap&&Datamap.prototype.worldTopo;if(!topo||!topo.objects){landG.innerHTML="";return false}
  var tf=topo.transform;var arcs=topo.arcs.map(function(a){var x=0,y=0;return a.map(function(p){if(tf){x+=p[0];y+=p[1];return [x*tf.scale[0]+tf.translate[0],y*tf.scale[1]+tf.translate[1]]}return p})});
  function ring(idx){var out=[];idx.forEach(function(i,j){var a=i<0?arcs[~i].slice().reverse():arcs[i];if(j>0)a=a.slice(1);out.push.apply(out,a)});return out}
  var obj=topo.objects.world||topo.objects[Object.keys(topo.objects)[0]],html="";
  obj.geometries.forEach(function(g){if(g.id==="ATA"||!g.arcs)return;var polys=g.type==="Polygon"?[g.arcs]:g.type==="MultiPolygon"?g.arcs:[];
    html+='<path class="country" d="'+polys.map(function(poly){return poly.map(function(r){return ringPath(ring(r))}).join("")}).join("")+'" fill-rule="evenodd"/>'});
  landG.innerHTML=html;return true}
drawGrat();drawLand();
/* zoner (mjuka områden) */
function zonPath(z){var pts=[];for(var a=0;a<=360;a+=15){pts.push(proj(z[0]+z[2]*Math.cos(a*R),z[1]+z[3]*Math.sin(a*R)))}return "M"+pts.map(function(p){return p[0].toFixed(1)+" "+p[1].toFixed(1)}).join("L")+"Z"}
ET.forEach(function(e,i){var p=proj(e.kart[0],e.kart[1]);e.px=p[0];e.py=p[1];e.w=e.kart[2]||260;
  var g=document.createElementNS(NS,"g");g.setAttribute("class","mk");g.dataset.i=i;g.innerHTML='<circle class="pulse" r="13"/><circle class="ring" r="13"/><text text-anchor="middle" y="5">'+(i+1)+'</text>';marksG.appendChild(g);
  (e.zon||[]).forEach(function(z){var pa=document.createElementNS(NS,"path");pa.setAttribute("d",zonPath(z));pa.setAttribute("class","zon z"+i);zonG.appendChild(pa)});
  var t=document.createElementNS(NS,"g");t.dataset.x=p[0];t.dataset.y=p[1];t.dataset.i=i;t.setAttribute("class","lb");t.innerHTML='<text class="place" x="18" y="-14">'+e.plats+'</text>';labG.appendChild(t);});
var FULL={x:0,y:-10,w:2*Math.PI*0.8707*SC*1.02},cam={x:FULL.x,y:FULL.y,w:FULL.w},raf=null;
function box(){var r=svg.getBoundingClientRect();return {W:Math.max(r.width,1),H:Math.max(r.height,1)}}
function apply(){var b=box(),w=cam.w,h=w*b.H/b.W;svg.setAttribute("viewBox",(cam.x-w/2)+" "+(cam.y-h*0.55)+" "+w+" "+h);var k=w/b.W;
  marksG.childNodes.forEach(function(g){var e=ET[g.dataset.i];g.setAttribute("transform","translate("+e.px+" "+e.py+") scale("+k+")")});
  labG.childNodes.forEach(function(g){g.setAttribute("transform","translate("+g.dataset.x+" "+g.dataset.y+") scale("+k+")")});}
function fly(to,done){var from={x:cam.x,y:cam.y,w:cam.w},dx=to.x-from.x,dy=to.y-from.y,dist=Math.hypot(dx,dy),reduce=matchMedia("(prefers-reduced-motion: reduce)").matches,dur=reduce?1:Math.min(3400,1300+dist*2.2),t0=performance.now(),lift=Math.max(0,dist*1.15-(from.w+to.w)/2);
  cancelAnimationFrame(raf);var step=function(now){var t=Math.min(1,(now-t0)/dur),e=t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;cam={x:from.x+dx*e,y:from.y+dy*e,w:from.w+(to.w-from.w)*e+lift*Math.sin(Math.PI*e)};apply();if(t<1)raf=requestAnimationFrame(step);else done&&done();};raf=requestAnimationFrame(step);}
addEventListener("resize",apply);
function target(e){return {x:e.px,y:e.py,w:e.w}}
var cur=-1,moving=false,done=ET.map(function(){return false}),firstTry=ET.map(function(){return null});
var KEY="pluggis-sim-"+S.id+"-v1";
function save(){try{localStorage.setItem(KEY,JSON.stringify({cur:cur,done:done,firstTry:firstTry}))}catch(e){}}
function load(){try{var d=JSON.parse(localStorage.getItem(KEY)||"null");if(!d||!(d.cur>=0)||d.cur>=QUIZ||!Array.isArray(d.done)||d.done.length!==N)return null;return d}catch(e){return null}}
function clear(){try{localStorage.removeItem(KEY)}catch(e){}}
function steps(){stepsEl.innerHTML=ET.map(function(e,i){return '<span class="dot '+(done[i]?"done":"")+' '+(i===cur?"now":"")+'" title="'+e.x_etikett+'">'+(i+1)+'</span>'}).join("");
  marksG.childNodes.forEach(function(g){var i=+g.dataset.i;g.classList.toggle("done",!!done[i]);g.classList.toggle("now",i===cur);g.style.display=(cur>=0&&i!==cur&&!done[i])?"none":""});
  zonG.childNodes.forEach(function(p){var i=+p.getAttribute("class").split(" z")[1];p.classList.toggle("on",!!done[i]||i===cur)});
  labG.childNodes.forEach(function(g){g.style.display=(+g.dataset.i===cur)?"":"none"});}
function nedslag(e){if(!window.PLA)return "";var o='<svg class="ned" xmlns="'+NS+'" viewBox="0 0 640 260" role="img" aria-label="Illustration: '+e.plats+'"><defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+S.sky[0]+'"/><stop offset="1" stop-color="'+S.sky[1]+'"/></linearGradient></defs><rect width="640" height="260" fill="url(#sk)"/><rect y="210" width="640" height="50" fill="'+S.mark+'"/>';
  (e.deko||[]).forEach(function(d){o+='<g transform="translate('+(320+d[1])+' '+(214+(PLA.FLY[d[0]]||0))+') scale('+d[2]+')">'+PLA.draw(d[0])+'</g>'});return o+'</svg>';}
function intro(){clock.innerHTML='<small>'+S.plats+'</small>'+S.tid;cam={x:FULL.x,y:FULL.y,w:FULL.w};apply();
  dock.innerHTML='<article class="card"><div class="stamp"><span>Tidsresa med karta</span><b>'+S.tid+'</b></div><h2>'+S.titel+'</h2><p>'+(S.intro||"Följ med på en resa över världskartan. Vi flyger till varje plats, läser om vad som hände där och svarar på en fråga. Platsen blir grön när du svarat rätt, och då kan du flyga vidare.")+'</p><div class="foot"><span>'+N+' platser · ca 10 minuter</span><button class="go ready" id="start">Starta resan →</button></div></article>';
  var sv=load();if(sv){var r=document.createElement("p");r.innerHTML='<button class="go ready" type="button" id="resume">Fortsätt där du var (plats '+(sv.cur+1)+') →</button>';dock.querySelector(".foot").before(r);
    document.getElementById("resume").onclick=function(){sv.done.forEach(function(v,i){done[i]=!!v});(sv.firstTry||[]).forEach(function(v,i){firstTry[i]=v});goTo(sv.cur)};document.getElementById("start").textContent="Börja om →";}
  document.getElementById("start").onclick=function(){clear();goTo(0)};steps();}
function goTo(t){if(moving)return;moving=true;cur=-1;steps();dock.innerHTML='<article class="card"><div class="stamp"><span>På väg…</span><b>'+ET[t].x_etikett+'</b></div><h2>Vi flyger vidare</h2><p>Kartan följer med dig till nästa plats.</p></article>';
  fly(target(ET[t]),function(){moving=false;arrive(t)});}
function arrive(i){cur=i;save();var e=ET[i];clock.innerHTML='<small>'+e.plats+'</small>'+e.tid;steps();render();}
function render(){var i=cur,e=ET[i];if(i===QUIZ){done[i]=true;clear();steps();}
  var quiz="";if(i<QUIZ){var solved=done[i];quiz='<div class="quiz"><p class="q">'+e.fraga+'</p><div class="opts">'+e.alt.map(function(o,k){return '<button class="opt '+(solved&&k===e.ratt?"right":"")+'" data-k="'+k+'" '+(solved?"disabled":"")+'>'+o+'</button>'}).join("")+'</div><p class="fb '+(solved?"ok":"")+'" id="fb">'+(solved?'<b>Rätt!</b> '+e.forklaring:"")+'</p></div>';}
  else{var sc=firstTry.slice(0,QUIZ).filter(Boolean).length;quiz='<p class="discuss">'+S.diskutera+'</p><div class="foot"><span class="score">'+sc+' av '+QUIZ+' rätt på första försöket</span><button class="go" id="again">Spela igen</button></div>';}
  var next=i<QUIZ?'<div class="foot"><span>Plats '+(i+1)+' av '+N+'</span><button class="go '+(done[i]?"ready":"")+'" id="next" '+(done[i]?"":"disabled")+'>Flyg vidare →</button></div>':"";
  dock.innerHTML='<article class="card"><div class="stamp"><span>'+e.tid+' · '+e.plats+'</span><b>Plats '+(i+1)+'</b></div>'+nedslag(e)+'<h2>'+e.rubrik+'</h2>'+e.fakta.map(function(f){return '<p>'+f+'</p>'}).join("")+ord(e)+quiz+next+'</article>';
  dock.scrollTop=0;dock.querySelectorAll(".opt").forEach(function(b){b.onclick=function(){answer(+b.dataset.k,b)}});var n=document.getElementById("next");if(n)n.onclick=goNext;var a=document.getElementById("again");if(a)a.onclick=restart;}
function ord(e){return (e.ord&&e.ord.length)?'<div class="ord"><b>Ord att kunna</b><ul>'+e.ord.map(function(o){return '<li><strong>'+o[0]+'</strong> – '+o[1]+'</li>'}).join('')+'</ul></div>':''}
function answer(k,btn){var e=ET[cur],fb=document.getElementById("fb");if(firstTry[cur]===null)firstTry[cur]=(k===e.ratt);
  if(k===e.ratt){done[cur]=true;save();steps();dock.querySelectorAll(".opt").forEach(function(b){b.disabled=true});btn.classList.add("right");fb.className="fb ok";fb.innerHTML="<b>Rätt!</b> "+e.forklaring;var n=document.getElementById("next");n.disabled=false;n.classList.add("ready");}
  else{btn.classList.add("wrong");btn.disabled=true;fb.className="fb no";fb.innerHTML="<b>Inte riktigt.</b> Läs texten igen och försök på nytt.";}}
function goNext(){if(moving||cur>=QUIZ||!done[cur])return;goTo(cur+1)}
function restart(){done.fill(false);firstTry.fill(null);cur=-1;moving=true;steps();fly({x:FULL.x,y:FULL.y,w:FULL.w},function(){moving=false;intro()})}
marksG.addEventListener("click",function(ev){var g=ev.target.closest&&ev.target.closest(".mk");if(!g||moving)return;var i=+g.dataset.i;if(i===cur){dock.scrollTop=0;return}if(done[i]||(i>0&&done[i-1])){goTo(i)}});
addEventListener("keydown",function(e){if(e.key==="ArrowRight")goNext()});
apply();intro();
})();
