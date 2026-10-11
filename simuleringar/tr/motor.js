/* Generisk "tidsresa": en person vandrar genom 7 etapper med fakta och frågor. Specifikation i window.SCEN. */
(function(){
var S=window.SCEN, ET=S.etapper, N=ET.length, QUIZ=N-1, GY=470, STEP=620;
var NS="http://www.w3.org/2000/svg";
var clamp=function(v,a,b){return Math.max(a,Math.min(b,v))};
ET.forEach(function(e,i){e.x=330+i*STEP;});
var svg=document.getElementById("svg"),far=document.getElementById("far"),world=document.getElementById("world");
var dock=document.getElementById("dock"),stepsEl=document.getElementById("steps"),clock=document.getElementById("clock");
svg.style.background="linear-gradient(#"+S.sky[0].replace("#","")+",#"+S.sky[1].replace("#","")+")";
function farSVG(){var s='<rect x="-600" y="'+(GY-120)+'" width="'+(N*STEP+1600)+'" height="400" fill="'+shade(S.mark,-.25)+'"/>';
  var p="M-600 "+(GY-100);for(var x=-600;x<=N*STEP+900;x+=60)p+=" L"+x+" "+(GY-110-26*Math.sin(x/130)-12*Math.sin(x/47));
  s+='<path d="'+p+" L"+(N*STEP+900)+" "+(GY+20)+' L-600 '+(GY+20)+'Z" fill="'+shade(S.mark,-.12)+'"/>';
  for(var i=0;i<14;i++)s+='<g transform="translate('+(-200+i*300)+' '+(60+(i*53)%90)+')">'+PLA.A.moln()+'</g>';
  s+='<circle cx="'+(200+STEP*1.6)+'" cy="90" r="34" fill="#fff6cf" opacity=".85"/>';
  return s;}
function shade(hex,k){var n=parseInt(hex.slice(1),16),r=n>>16,g=(n>>8)&255,b=n&255,f=function(v){return clamp(Math.round(v+(k<0?v*k:(255-v)*k)),0,255)};return "#"+((1<<24)+(f(r)<<16)+(f(g)<<8)+f(b)).toString(16).slice(1)}
function worldSVG(){var s='<rect x="-1200" y="'+GY+'" width="'+(N*STEP+3000)+'" height="400" fill="'+S.mark+'"/>';
  s+='<rect x="-1200" y="'+GY+'" width="'+(N*STEP+3000)+'" height="8" fill="'+shade(S.mark,.25)+'"/>';
  s+='<g fill="'+shade(S.mark,-.15)+'">';for(var x=-1000;x<N*STEP+1500;x+=140)s+='<ellipse cx="'+x+'" cy="'+(GY+26+(x%3)*12)+'" rx="30" ry="4"/>';s+='</g>';
  ET.forEach(function(e,i){
    (e.deko||[]).forEach(function(d){var y=GY+(PLA.FLY[d[0]]||0);
      s+='<g transform="translate('+(e.x+d[1])+' '+y+') scale('+d[2]+')">'+PLA.draw(d[0])+'</g>';});
    var mx=e.x+70,my=GY-200;
    s+='<g class="marker" id="m'+i+'" data-i="'+i+'" tabindex="0" role="button" aria-label="Etapp '+(i+1)+'"><circle class="pulse" cx="'+mx+'" cy="'+my+'" r="14"/><circle class="ring" cx="'+mx+'" cy="'+my+'" r="14"/><text x="'+mx+'" y="'+(my+5)+'" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">'+(i+1)+'</text></g>';
  });
  s+='<g id="sol" transform="translate('+ET[0].x+' '+GY+')">'+PLA.W(S.walker.typ)+'</g>';
  return s;}
far.innerHTML=farSVG(); world.innerHTML=worldSVG();
var sol=document.getElementById("sol"),camX=ET[0].x,anim=null;
function centerX(){return innerWidth>=860?330:400}
function place(){var cx=centerX();world.setAttribute("transform","translate("+(cx-camX)+" "+(350-GY)+")");far.setAttribute("transform","translate("+(cx-camX*.35)+" "+((350-GY)*.3)+")");sol.setAttribute("transform","translate("+camX+" "+GY+")");}
function walkTo(x,done){var from=camX,dist=Math.abs(x-from),reduce=matchMedia("(prefers-reduced-motion: reduce)").matches,dur=reduce?1:clamp(dist*2.4,1400,3200),t0=performance.now();
  sol.classList.add("walking");cancelAnimationFrame(anim);
  var step=function(now){var t=clamp((now-t0)/dur,0,1),e=t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;camX=from+(x-from)*e;place();if(t<1)anim=requestAnimationFrame(step);else{sol.classList.remove("walking");done&&done();}};
  anim=requestAnimationFrame(step);}
addEventListener("resize",place);
var cur=-1,moving=false,done=ET.map(function(){return false}),firstTry=ET.map(function(){return null});
var KEY="pluggis-sim-"+S.id+"-v1";
function save(){try{localStorage.setItem(KEY,JSON.stringify({cur:cur,done:done,firstTry:firstTry}))}catch(e){}}
function load(){try{var d=JSON.parse(localStorage.getItem(KEY)||"null");if(!d||!(d.cur>=0)||d.cur>=QUIZ||!Array.isArray(d.done)||d.done.length!==N)return null;return d}catch(e){return null}}
function clear(){try{localStorage.removeItem(KEY)}catch(e){}}
function esc(t){return t}
function steps(){stepsEl.innerHTML=ET.map(function(e,i){return '<span class="dot '+(done[i]?"done":"")+' '+(i===cur?"now":"")+'" title="'+e.x_etikett+'">'+(i+1)+'</span>'}).join("");ET.forEach(function(e,i){document.getElementById("m"+i).classList.toggle("done",done[i])})}
function intro(){
  dock.innerHTML='<article class="card"><div class="stamp"><span>Tidsresa</span><b>'+S.tid+'</b></div><h2>'+S.titel+'</h2><p>'+(S.intro||("Följ med på en resa genom tiden: "+S.plats+". Vid varje röd cirkel läser du om vad som händer och svarar på en fråga. Cirkeln blir grön när du svarat rätt, och då kan du gå vidare."))+'</p><div class="foot"><span>'+N+' etapper · ca 10 minuter</span><button class="go ready" id="start">Starta resan →</button></div></article>';
  var sv=load();
  if(sv){var r=document.createElement("p");r.innerHTML='<button class="go ready" type="button" id="resume">Fortsätt där du var (etapp '+(sv.cur+1)+') →</button>';dock.querySelector(".foot").before(r);
    document.getElementById("resume").onclick=function(){sv.done.forEach(function(v,i){done[i]=!!v});(sv.firstTry||[]).forEach(function(v,i){firstTry[i]=v});camX=ET[sv.cur].x;place();arrive(sv.cur)};
    document.getElementById("start").textContent="Börja om →";}
  document.getElementById("start").onclick=function(){clear();arrive(0)};}
function arrive(i){cur=i;save();var e=ET[i];clock.innerHTML='<small>'+e.plats+'</small>'+e.tid;steps();render();}
function render(){var i=cur,e=ET[i];
  if(i===QUIZ){done[i]=true;clear();steps();}
  var quiz="";
  if(i<QUIZ){var solved=done[i];
    quiz='<div class="quiz"><p class="q">'+e.fraga+'</p><div class="opts">'+e.alt.map(function(o,k){return '<button class="opt '+(solved&&k===e.ratt?"right":"")+'" data-k="'+k+'" '+(solved?"disabled":"")+'>'+o+'</button>'}).join("")+'</div><p class="fb '+(solved?"ok":"")+'" id="fb">'+(solved?'<b>Rätt!</b> '+e.forklaring:"")+'</p></div>';}
  else{var sc=firstTry.slice(0,QUIZ).filter(Boolean).length;
    quiz='<p class="discuss">'+S.diskutera+'</p><div class="foot"><span class="score">'+sc+' av '+QUIZ+' rätt på första försöket</span><button class="go" id="again">Spela igen</button></div>';}
  var next=i<QUIZ?'<div class="foot"><span>Etapp '+(i+1)+' av '+N+'</span><button class="go '+(done[i]?"ready":"")+'" id="next" '+(done[i]?"":"disabled")+'>Gå vidare →</button></div>':"";
  dock.innerHTML='<article class="card"><div class="stamp"><span>'+e.tid+' · '+e.plats+'</span><b>Etapp '+(i+1)+'</b></div><h2>'+e.rubrik+'</h2>'+e.fakta.map(function(f){return '<p>'+f+'</p>'}).join("")+ord(e)+quiz+next+'</article>';
  dock.scrollTop=0;
  dock.querySelectorAll(".opt").forEach(function(b){b.onclick=function(){answer(+b.dataset.k,b)}});
  var n=document.getElementById("next");if(n)n.onclick=goNext;var a=document.getElementById("again");if(a)a.onclick=restart;}
function ord(e){return (e.ord&&e.ord.length)?'<div class="ord"><b>Ord att kunna</b><ul>'+e.ord.map(function(o){return '<li><strong>'+o[0]+'</strong> – '+o[1]+'</li>'}).join('')+'</ul></div>':''}
function answer(k,btn){var e=ET[cur],fb=document.getElementById("fb");if(firstTry[cur]===null)firstTry[cur]=(k===e.ratt);
  if(k===e.ratt){done[cur]=true;save();steps();dock.querySelectorAll(".opt").forEach(function(b){b.disabled=true});btn.classList.add("right");fb.className="fb ok";fb.innerHTML="<b>Rätt!</b> "+e.forklaring;var n=document.getElementById("next");n.disabled=false;n.classList.add("ready");}
  else{btn.classList.add("wrong");btn.disabled=true;fb.className="fb no";fb.innerHTML="<b>Inte riktigt.</b> Läs texten igen och försök på nytt.";}}
function goNext(){if(moving||cur>=QUIZ||!done[cur])return;moving=true;dock.innerHTML='<article class="card"><div class="stamp"><span>På väg…</span><b>'+ET[cur+1].x_etikett+'</b></div><h2>Framåt!</h2><p>Du fortsätter resan genom tiden.</p></article>';var t=cur+1;walkTo(ET[t].x,function(){moving=false;arrive(t)});}
function restart(){done.fill(false);firstTry.fill(null);cur=-1;moving=true;walkTo(ET[0].x,function(){moving=false;steps();intro()});}
document.querySelectorAll(".marker").forEach(function(m){var open=function(){if(+m.dataset.i===cur){dock.scrollTop=0}};m.addEventListener("click",open);m.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();open()}})});
addEventListener("keydown",function(e){if(e.key==="ArrowRight")goNext()});
place();steps();intro();
})();
