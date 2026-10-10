/* Bildbibliotek för Pluggis historia: enkla tecknade SVG-figurer. Varje figur ritas med marken vid y=0, centrerad vid x=0, ca 120 px hög vid skala 1. */
(function(){
var A={};
function R(x,y,w,h,f,x2){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+f+'"'+(x2||'')+'/>';}
function P(d,f,x2){return '<path d="'+d+'" fill="'+f+'"'+(x2||'')+'/>';}
function C(x,y,r,f){return '<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="'+f+'"/>';}
function L(a,b,c,d,s,w){return '<line x1="'+a+'" y1="'+b+'" x2="'+c+'" y2="'+d+'" stroke="'+s+'" stroke-width="'+(w||2)+'" stroke-linecap="round"/>';}
function E(x,y,rx,ry,f){return '<ellipse cx="'+x+'" cy="'+y+'" rx="'+rx+'" ry="'+ry+'" fill="'+f+'"/>';}
function water(w){return '<g class="vag">'+P('M'+(-w/2)+' 6 Q'+(-w/4)+' -2 0 6 T'+(w/2)+' 6 L'+(w/2)+' 14 L'+(-w/2)+' 14Z','#4f86a8')+'</g>';}
function blocks(x,y,w,h,col,line){var s=R(x,y,w,h,col);for(var j=1;j<h/10;j++)s+=L(x,y+j*10,x+w,y+j*10,line,.8);return s;}

A.pyramid=function(){return P('M-70 0 L0 -112 L70 0Z','#d9b872')+P('M0 -112 L70 0 L18 0 L0 -60Z','#c29d52')+L(-40,-40,40,-40,'#b8944b',1)+L(-20,-76,20,-76,'#b8944b',1);};
A.ziggurat=function(){return R(-70,-26,140,26,'#b98b52')+R(-52,-52,104,26,'#c69b60')+R(-34,-78,68,26,'#d3ab6e')+R(-18,-98,36,20,'#a56a3a')+L(0,-26,0,0,'#8e5f35',3)+P('M-70 0 L-52 -26 L-52 0Z','#9d7443')+L(-30,-26,-30,0,'#8e5f35',1);};
A.sphinx=function(){return P('M-60 0 L-60 -26 Q-30 -34 -10 -34 L10 -34 Q28 -60 46 -62 Q64 -58 60 -36 L56 0Z','#d8b878')+R(40,-56,14,22,'#c9a35e')+P('M40 -64 Q54 -76 66 -62 L60 -52 L44 -54Z','#2c5d8c')+L(-60,0,60,0,'#bf9b54',2);};
A.nilbat=function(){return water(120)+P('M-50 0 L50 0 L40 10 L-40 10Z','#8a5a30')+L(0,0,0,-60,'#6a4526',3)+P('M0 -58 L44 -8 L0 -8Z','#f1ead6')+P('M-50 0 Q-60 -14 -48 -22','#8a5a30','');};
A.tempel_grekiskt=function(){var s=R(-70,-8,140,8,'#e5ddc9')+R(-64,-16,128,8,'#d9cfb6');for(var i=0;i<6;i++){s+=R(-56+i*21,-84,10,68,'#efe8d6')+R(-59+i*21,-90,16,6,'#d9cfb6')+L(-52+i*21,-84,-52+i*21,-18,'#d3c9ae',1);}return s+R(-66,-102,132,12,'#e8e0cd')+P('M-70 -102 L0 -134 L70 -102Z','#dcd2b8')+P('M-52 -104 L0 -128 L52 -104Z','#cfc6aa');};
A.trirem=function(){return water(150)+P('M-62 -2 L56 -2 L70 -22 L60 8 L-52 8Z','#7d5632')+L(0,-2,0,-70,'#5f4426',3)+P('M-30 -66 L30 -66 L26 -22 L-26 -22Z','#f1ead6')+L(-40,6,-56,22,'#5f4426',2)+L(-10,6,-20,22,'#5f4426',2)+L(20,6,10,22,'#5f4426',2);};
A.amfora=function(){return P('M-12 0 Q-18 -22 -10 -40 L-6 -52 L6 -52 L10 -40 Q18 -22 12 0Z','#b8643a')+P('M-8 -52 Q-20 -50 -16 -38','#b8643a','')+L(-14,-30,14,-30,'#7d3f20',1.5)+L(-13,-18,13,-18,'#7d3f20',1.5);};
A.colosseum=function(){var s=P('M-90 0 L-90 -64 Q0 -96 90 -64 L90 0Z','#cdbb92');for(var r=0;r<3;r++)for(var i=0;i<9;i++){s+=P('M'+(-80+i*18)+' '+(-8-r*20)+' v-10 a6 6 0 0 1 12 0 v10z','#6e5a3d');}return s+L(-90,-64,90,-64,'#b09b70',2);};
A.akvedukt=function(){var s=R(-100,-96,200,10,'#cdbb92');for(var i=0;i<5;i++){s+=P('M'+(-100+i*40)+' 0 v-58 a20 20 0 0 1 40 0 v58z','#cdbb92')+P('M'+(-94+i*40)+' 0 v-56 a14 14 0 0 1 28 0 v56z','#7aa6c9','opacity=".35"');}return s+R(-100,-86,200,28,'#c4b189')+'<path d="M-100 -96 h200" stroke="#8aa7b5" stroke-width="4"/>';};
A.romerskt_hus=function(){return R(-44,-52,88,52,'#e6d9bd')+P('M-52 -52 L0 -84 L52 -52Z','#b5583a')+R(-10,-30,20,30,'#5a4330')+R(-34,-40,12,14,'#7aa6c9')+R(22,-40,12,14,'#7aa6c9')+R(-48,-56,96,5,'#cdbb92');};
A.legionar=function(){return R(-12,-44,24,44,'#a84330')+R(-10,-42,20,8,'#c8a24a')+C(0,-52,8,'#d6a98a')+P('M-10 -54 Q0 -68 10 -54Z','#c8a24a')+R(-4,-60,8,6,'#a84330')+R(8,-48,22,34,'#a84330','rx="3"')+L(-16,-48,-16,-86,'#6a4526',2.5)+P('M-16 -86 l-4 -8 l8 0z','#9aa3a8')+R(-9,-8,6,8,'#3b2a1d')+R(3,-8,6,8,'#3b2a1d');};
A.galar=function(){return A.trirem();};
A.kogg=function(){return water(140)+P('M-56 0 L56 0 L48 -26 L-48 -26Z','#6b4a2c')+R(-52,-34,18,10,'#6b4a2c')+R(34,-34,18,10,'#6b4a2c')+L(0,-26,0,-92,'#4f3820',3)+P('M-30 -88 L30 -88 L26 -36 L-26 -36Z','#e9e0c8')+P('M-6 -88 L-6 -36 M6 -88 L6 -36','none','stroke="#b83d3d" stroke-width="3"');};
A.karavell=function(){return water(150)+P('M-62 0 L62 0 L52 -24 L-50 -24 L-62 -12Z','#6b4a2c')+R(-58,-34,18,10,'#6b4a2c')+L(-22,-24,-22,-96,'#4f3820',3)+L(20,-24,20,-80,'#4f3820',3)+P('M-44 -92 L0 -92 L-4 -40 L-40 -40Z','#f1ead6')+P('M-16 -92 L-16 -40','none','stroke="#b83d3d" stroke-width="3"')+P('M2 -78 L40 -78 L36 -34 L6 -34Z','#f1ead6')+P('M20 -78 L20 -34','none','stroke="#b83d3d" stroke-width="3"')+P('M-22 -96 l16 4 l-16 4z','#b83d3d');};
A.palm=function(){return P('M-3 0 Q0 -40 8 -78 L12 -78 Q4 -40 3 0Z','#8a5f35')+P('M10 -78 Q-20 -92 -42 -72 Q-18 -80 10 -74Z','#3f8f4d')+P('M10 -78 Q30 -100 52 -82 Q28 -86 10 -74Z','#4aa056')+P('M10 -78 Q0 -104 -16 -108 Q-4 -92 10 -74Z','#3f8f4d')+P('M10 -78 Q26 -98 44 -104 Q28 -88 10 -74Z','#4aa056')+C(8,-72,3,'#6b4a1f')+C(14,-71,3,'#6b4a1f');};
A.hamn=function(){return R(-80,-8,160,8,'#9a7a52')+R(-76,-4,6,12,'#6f5436')+R(-40,-4,6,12,'#6f5436')+R(0,-4,6,12,'#6f5436')+R(40,-4,6,12,'#6f5436')+R(70,-4,6,12,'#6f5436')+R(-60,-30,26,22,'#a56a3a')+R(-28,-24,18,16,'#c08a4e')+R(30,-36,30,28,'#8a5a30');};
A.segelfartyg=function(){return A.karavell();};
A.kanon=function(){return P('M-30 -20 L26 -30 L30 -22 L-26 -12Z','#3a3a3a')+C(-14,0,12,'#6b4a2c')+C(-14,0,4,'#3a3a3a')+R(-30,-14,30,6,'#5b3d22');};
function flag(a,b,c,mid){var s=L(0,0,0,-130,'#4a3b2c',3);s+='<g class="flag">'+(c?R(0,-128,22,40,a)+R(22,-128,22,40,b)+R(44,-128,22,40,c):R(0,-128,66,40,a)+(mid||''))+'</g>';return s;}
A.flagga_rod=function(){return flag('#c8352c',0,0,'');};
A.flagga_bla=function(){return flag('#2b5aa8',0,0,'<circle cx="33" cy="-108" r="8" fill="#f2c94c"/>');};
A.flagga_trikolor=function(){return flag('#244a94','#f2efe6','#c8352c');};
A.bokhylla=function(){var s=R(-44,-90,88,90,'#7d5632')+R(-40,-86,80,82,'#5b3d22');var cols=['#b83d3d','#2b5aa8','#c8a24a','#3f8f4d','#8a4fa8','#d9d2bf'];for(var r=0;r<3;r++){s+=R(-40,-62+r*28,80,3,'#7d5632');for(var i=0;i<8;i++)s+=R(-38+i*9.6,-84+r*28+(i%3)*2,7,22-(i%3)*2,cols[(i+r)%6]);}return s;};
A.tryckpress=function(){return R(-34,-60,68,60,'#6f5436')+R(-30,-56,60,8,'#8a6a44')+L(0,-60,0,-92,'#3a3a3a',5)+L(-22,-94,22,-94,'#3a3a3a',5)+R(-22,-48,44,10,'#e9e0c8')+R(-38,-6,76,6,'#4f3820');};
A.barrikad=function(){return P('M-70 0 L-60 -30 L-30 -42 L10 -38 L40 -46 L70 -22 L74 0Z','#7a5a3a')+L(-40,-40,-52,-62,'#4f3820',3)+R(-20,-42,4,-28,'#4f3820')+'<g class="flag">'+R(8,-100,40,26,'#c8352c')+'</g>'+L(8,-102,8,-36,'#4f3820',3)+R(-60,-24,16,10,'#5b3d22')+R(30,-28,18,10,'#5b3d22');};
A.giljotin=function(){return R(-34,-8,68,8,'#5b3d22')+R(-26,-100,6,92,'#7d5632')+R(20,-100,6,92,'#7d5632')+R(-30,-104,60,8,'#5b3d22')+P('M-18 -80 L18 -80 L18 -64 L-18 -56Z','#aeb6ba');};
A.fabrik=function(){return R(-70,-50,140,50,'#9a6247')+R(-70,-50,140,6,'#7d4a34')+P('M-72 -50 L-40 -76 L-40 -50Z M-40 -50 L-8 -76 L-8 -50Z M-8 -50 L24 -76 L24 -50Z','#7d4a34')+R(30,-120,16,70,'#6f4030')+R(50,-100,14,50,'#6f4030')+'<g class="rok"><circle cx="38" cy="-130" r="10" fill="#9aa0a3" opacity=".7"/><circle cx="50" cy="-148" r="14" fill="#9aa0a3" opacity=".5"/></g>'+R(-56,-34,14,14,'#f2d27a')+R(-34,-34,14,14,'#f2d27a')+R(-12,-34,14,14,'#f2d27a')+R(10,-34,14,14,'#f2d27a');};
A.lok=function(){return R(-52,-34,76,26,'#2f3236')+R(24,-48,26,40,'#2f3236')+R(-60,-56,18,26,'#2f3236')+R(-64,-62,26,6,'#2f3236')+C(-40,-8,14,'#7d1f1f')+C(-6,-8,14,'#7d1f1f')+C(32,-8,10,'#7d1f1f')+R(-70,-4,130,4,'#5a5d60')+'<g class="rok"><circle cx="-52" cy="-76" r="8" fill="#c9ccce" opacity=".8"/><circle cx="-44" cy="-92" r="11" fill="#c9ccce" opacity=".6"/></g>'+R(28,-44,18,16,'#f2d27a');};
A.skorstenar=function(){return R(-40,-120,12,120,'#8a4a36')+R(-12,-96,12,96,'#7d4030')+R(16,-110,12,110,'#8a4a36')+'<g class="rok">'+C(-34,-132,10,'#8d9396')+C(-6,-110,9,'#8d9396')+C(22,-124,10,'#8d9396')+'</g>';};
A.arbetarhus=function(){var s=R(-60,-62,120,62,'#a7774f')+R(-60,-66,120,6,'#7d5632');for(var i=0;i<4;i++){s+=R(-52+i*28,-52,12,14,'#f2d27a')+R(-52+i*28,-28,12,14,i%2?'#f2d27a':'#4f3820');}return s+R(-8,-22,16,22,'#4f3820');};
A.gruva=function(){return P('M-70 0 Q-50 -60 0 -62 Q50 -58 70 0Z','#7a6a58')+P('M-22 0 L-22 -28 Q0 -40 22 -28 L22 0Z','#171717')+R(-26,-32,6,32,'#7d5632')+R(20,-32,6,32,'#7d5632')+R(-28,-36,56,6,'#7d5632')+R(40,-76,6,30,'#5b3d22')+R(30,-78,26,8,'#5b3d22');};
A.angbat=function(){return water(150)+P('M-62 0 L62 0 L48 -22 L-50 -22Z','#2f3236')+R(-24,-40,40,18,'#e9e0c8')+R(-4,-72,14,32,'#8a2f2f')+R(0,-80,6,8,'#2f3236')+'<g class="rok"><circle cx="6" cy="-90" r="9" fill="#a5abae" opacity=".7"/><circle cx="16" cy="-106" r="12" fill="#a5abae" opacity=".5"/></g>'+R(-44,-36,14,14,'#e9e0c8');};
A.skyttegrav=function(){return P('M-80 -4 L-60 -4 L-52 12 L52 12 L60 -4 L80 -4 L80 8 L-80 8Z','#6b5a3d')+R(-56,2,112,10,'#4a3b28')+R(-70,-16,24,12,'#8a7a52')+R(46,-16,24,12,'#8a7a52')+L(-46,-30,46,-30,'#4a3b28',1.5)+L(-46,-30,-46,-4,'#4a3b28',2)+L(46,-30,46,-4,'#4a3b28',2);};
A.taggtrad=function(){var s=L(-70,0,-70,-36,'#4a3b28',3)+L(0,0,0,-36,'#4a3b28',3)+L(70,0,70,-36,'#4a3b28',3);s+=P('M-74 -30 q18 -10 36 0 t36 0 t36 0 t36 0','none','stroke="#2f2f2f" stroke-width="2"');s+=P('M-74 -20 q18 -10 36 0 t36 0 t36 0 t36 0','none','stroke="#2f2f2f" stroke-width="2"');return s;};
A.tank=function(){return R(-44,-24,88,18,'#6f7452')+R(-28,-42,52,20,'#7a805a')+R(24,-36,38,5,'#4f5339')+P('M-52 -6 Q-56 0 -44 2 L44 2 Q56 0 52 -6Z','#3a3d2c')+C(-34,-2,5,'#2a2c20')+C(-14,-2,5,'#2a2c20')+C(6,-2,5,'#2a2c20')+C(26,-2,5,'#2a2c20');};
A.biplan=function(){return '<g class="flyg">'+P('M-30 -10 Q-34 -16 -20 -18 L30 -18 L40 -10 L30 -4 L-20 -4Z','#8a5a3a')+R(-24,-34,52,5,'#c8b46a')+R(-24,-18,52,5,'#c8b46a')+L(-14,-30,-14,-18,'#4f3820',1.5)+L(16,-30,16,-18,'#4f3820',1.5)+P('M-30 -14 L-42 -22 L-42 -8Z','#8a5a3a')+C(42,-10,3,'#2f2f2f')+'</g>';};
A.bombplan=function(){return '<g class="flyg">'+P('M-60 -8 Q-62 -16 -44 -18 L40 -18 L62 -10 L40 -2 L-44 -2Z','#6b7255')+P('M-50 -10 L-20 -14 L-4 -34 L10 -34 L-2 -8Z','#5d6448')+P('M-60 -14 L-70 -34 L-62 -34 L-48 -16Z','#6b7255')+C(-30,-10,4,'#2f2f2f')+C(10,-10,4,'#2f2f2f')+'</g>';};
A.soldat_grupp=function(){var s="";for(var i=0;i<3;i++){var x=-30+i*30;s+=R(x-5,-34,10,34,'#59583a')+C(x,-42,6,'#d6a98a')+P('M'+(x-7)+' -44 Q'+x+' -56 '+(x+7)+' -44Z','#4a4c33')+L(x+8,-30,x+16,-62,'#2c2618',2);}return s;};
A.sjukhustalt=function(){return P('M-48 0 L-48 -30 L0 -60 L48 -30 L48 0Z','#e7e1ce')+P('M-48 -30 L0 -60 L48 -30','none','stroke="#bdb59a" stroke-width="2"')+R(-8,-24,16,24,'#5a4a3a')+R(-5,-46,10,3,'#c8352c')+R(-1.5,-49.5,3,10,'#c8352c');};
A.mur=function(){var s=blocks(-70,-70,140,70,'#9a9a96','#7a7a76');s+=R(-74,-76,148,6,'#7a7a76');s+=P('M-60 -20 q10 -10 20 0 t20 0','none','stroke="#c8352c" stroke-width="3"');s+=L(-80,-14,-80,-30,'#4a4a4a',2)+L(80,-14,80,-30,'#4a4a4a',2);s+=P('M-80 -80 l160 0','none','stroke="#4a4a4a" stroke-width="2" stroke-dasharray="3 5"');return s;};
A.raket=function(){return P('M0 -128 Q14 -100 14 -60 L14 -20 L-14 -20 L-14 -60 Q-14 -100 0 -128Z','#e9eaea')+P('M-14 -34 L-30 -8 L-14 -16Z M14 -34 L30 -8 L14 -16Z','#c8352c')+C(0,-84,6,'#2b5aa8')+R(-14,-70,28,6,'#c8352c')+'<g class="rok">'+P('M-8 -20 L0 6 L8 -20Z','#f2a23a')+'</g>';};
A.satellit=function(){return '<g class="flyg">'+R(-10,-10,20,20,'#c9ccce')+R(-40,-6,26,12,'#2b5aa8')+R(14,-6,26,12,'#2b5aa8')+L(0,-10,0,-24,'#c9ccce',2)+C(0,-26,3,'#c8352c')+'</g>';};
A.villa=function(){return R(-44,-40,88,40,'#e1c35e')+P('M-52 -40 L0 -72 L52 -40Z','#9a4a36')+R(-10,-24,20,24,'#5a4330')+R(-36,-30,16,14,'#7aa6c9')+R(20,-30,16,14,'#7aa6c9')+R(24,-62,10,22,'#7d4030');};
A.riksdagshus=function(){var s=R(-90,-50,180,50,'#cdbb92')+R(-60,-76,120,26,'#d9c9a2')+P('M-60 -76 L0 -100 L60 -76Z','#b5a47a');for(var i=0;i<8;i++)s+=R(-78+i*22,-44,8,36,'#efe6cc');s+=R(-90,-54,180,4,'#a89870')+R(-6,-110,12,12,'#d9c9a2')+L(0,-110,0,-128,'#4a3b2c',2)+'<g class="flag">'+R(0,-128,20,12,'#2b5aa8')+'</g>';return s;};
A.valurna=function(){return R(-26,-40,52,40,'#a56a3a')+R(-26,-44,52,6,'#7d4a2a')+R(-14,-48,28,5,'#2f2f2f')+R(-12,-72,24,26,'#f1ead6','transform="rotate(-8 0 -60)"')+L(-8,-62,8,-64,'#8a8a8a',1.5)+L(-8,-56,8,-58,'#8a8a8a',1.5);};
A.skola=function(){var s=R(-60,-48,120,48,'#c9755a')+P('M-66 -48 L0 -72 L66 -48Z','#8a4a36')+R(-8,-22,16,22,'#5a4330')+R(-4,-98,8,28,'#e9e0c8')+C(0,-92,6,'#fff')+L(0,-92,0,-95,'#333',1);for(var i=0;i<4;i++)s+=R(-52+i*28,-38,14,14,'#f2d27a');return s;};
A.containerfartyg=function(){var s=water(160)+P('M-72 0 L72 0 L58 -16 L-66 -16Z','#2f3a45');var cols=['#c8352c','#2b5aa8','#3f8f4d','#c8a24a','#8a4fa8'];for(var r=0;r<3;r++)for(var i=0;i<6;i++)s+=R(-62+i*16,-30-r*14,15,13,cols[(i+r*2)%5]);return s+R(50,-52,18,36,'#e9e0c8')+R(54,-62,10,10,'#e9e0c8');};
A.jordglob=function(){return C(0,-60,52,'#3b77b8')+P('M-30 -84 q10 -10 24 -4 q10 8 4 20 q-12 6 -22 -2z','#4aa056')+P('M10 -62 q16 -6 24 6 q4 14 -10 20 q-14 -4 -16 -14z','#4aa056')+P('M-26 -46 q10 -2 14 8 q-4 12 -14 8z','#4aa056')+'<ellipse cx="-18" cy="-86" rx="14" ry="6" fill="#fff" opacity=".3"/>'+R(-30,-6,60,6,'#6b6b6b');};
A.flygplan_modernt=function(){return '<g class="flyg">'+P('M-70 -8 Q-72 -18 -50 -20 L50 -18 Q76 -12 78 -8 Q76 -2 50 0 L-50 0Z','#e9eaea')+P('M-10 -12 L20 -12 L-18 22 L-34 22Z','#c9ccce')+P('M-70 -12 L-84 -36 L-72 -36 L-50 -16Z','#2b5aa8')+R(-30,-14,40,3,'#2b5aa8')+'</g>';};
A.dator=function(){return R(-34,-50,68,44,'#2f3236')+R(-30,-46,60,36,'#5fa8d3')+R(-10,-6,20,6,'#2f3236')+R(-26,0,52,5,'#c9ccce')+P('M-22 -36 l10 -6 l8 8','none','stroke="#fff" stroke-width="2"');};
A.vindkraft=function(){return P('M-4 0 L-2 -90 L2 -90 L4 0Z','#e9eaea')+'<g class="rotor" transform="translate(0 -92)">'+P('M0 0 L-4 -46 L4 -46Z','#e9eaea')+P('M0 0 L40 24 L36 30Z','#e9eaea')+P('M0 0 L-40 24 L-36 30Z','#e9eaea')+'</g>'+C(0,-92,4,'#c9ccce');};
A.folkmassa=function(){var s="",cols=['#b83d3d','#2b5aa8','#c8a24a','#3f8f4d','#8a4fa8','#6b4a2c'];for(var i=0;i<9;i++){var x=-60+i*15,h=26+(i*7)%10;s+=R(x-5,-h,10,h,cols[i%6],'rx="3"')+C(x,-h-6,5.5,'#d6a98a');}return s;};
A.trad=function(){return R(-4,-40,8,40,'#6b4a2c')+C(0,-58,26,'#4aa056')+C(-16,-46,18,'#3f8f4d')+C(16,-48,18,'#4aa056');};
A.gran=function(){return R(-3,-12,6,12,'#6b4a2c')+P('M-26 -12 L0 -58 L26 -12Z','#2f6b4f')+P('M-20 -36 L0 -80 L20 -36Z','#3a7d5c')+P('M-14 -62 L0 -104 L14 -62Z','#2f6b4f');};
A.berg=function(){return P('M-90 0 L-40 -78 L-14 -40 L20 -100 L90 0Z','#8d8b86')+P('M20 -100 L40 -64 L28 -68 L20 -56 L10 -70Z','#f2f2f2')+P('M-40 -78 L-30 -62 L-40 -64 L-48 -60Z','#f2f2f2');};
A.flod=function(){return '<g class="vag">'+P('M-110 4 Q-70 -6 -30 4 T50 4 T110 4 L110 14 L-110 14Z','#5aa0cf')+'</g>';};
A.moln=function(){return '<g class="moln">'+E(0,-6,34,12,'#fff')+E(-18,-14,18,12,'#fff')+E(12,-18,20,14,'#fff')+'</g>';};
A.bondgard=function(){return R(-40,-34,52,34,'#a64a3a')+P('M-46 -34 L-14 -58 L18 -34Z','#6f3a2a')+R(-24,-22,12,22,'#e9e0c8')+R(18,-44,32,44,'#8a3d30')+P('M14 -44 L34 -66 L54 -44Z','#5a4a3a')+L(-60,0,-60,-18,'#6b4a2c',2)+L(-60,-10,-80,-10,'#6b4a2c',2);};
A.torp=function(){return R(-34,-28,68,28,'#a64a3a')+P('M-40 -28 L0 -52 L40 -28Z','#6b5a3a')+R(-6,-20,12,20,'#e9e0c8')+R(14,-22,12,10,'#f2d27a')+R(-26,-22,10,10,'#f2d27a')+R(14,-60,8,16,'#7d4030');};
A.marknad=function(){var s="";[['#c8352c',-44],['#2b5aa8',0],['#3f8f4d',44]].forEach(function(c){s+=R(c[1]-18,-34,36,34,'#a57b4f')+P('M'+(c[1]-22)+' -34 L'+c[1]+' -52 L'+(c[1]+22)+' -34Z',c[0])+C(c[1]-6,-14,5,'#e0a03a')+C(c[1]+6,-14,5,'#8a4f2a');});return s;};
A.slott=function(){return R(-60,-60,120,60,'#b9b4a6')+R(-68,-92,28,92,'#a8a392')+R(40,-92,28,92,'#a8a392')+P('M-72 -92 L-54 -118 L-36 -92Z','#7d4a36')+P('M36 -92 L54 -118 L72 -92Z','#7d4a36')+R(-12,-28,24,28,'#4a3b2c','')+R(-44,-44,12,14,'#4a3b2c')+R(32,-44,12,14,'#4a3b2c')+L(-60,-60,60,-60,'#8e897a',2);};
A.kyrka=function(){return R(-40,-44,80,44,'#d6cbb0')+R(-52,-96,24,52,'#cfc4a8')+P('M-56 -96 L-40 -128 L-24 -96Z','#5a4a3c')+L(-40,-128,-40,-142,'#2f2b26',2)+L(-45,-136,-35,-136,'#2f2b26',2)+P('M-40 -44 L0 -70 L40 -44Z','#5a4a3c')+R(-10,-30,20,30,'#4a3b2c')+R(-30,-34,10,14,'#7aa6c9')+R(20,-34,10,14,'#7aa6c9');};
A.tag=function(){return R(-60,-40,120,40,'#c9755a')+R(-64,-46,128,8,'#7d4a36')+R(-50,-30,16,30,'#4a3b2c')+R(-24,-30,16,30,'#4a3b2c')+R(70,-4,60,4,'#5a5d60')+C(0,-56,8,'#efe6cc')+L(0,-56,0,-60,'#333',1.2)+L(0,-56,3,-55,'#333',1.2);};
A.radio=function(){return R(-26,-34,52,34,'#8a5a30')+C(-10,-17,10,'#d9c9a2')+R(8,-26,12,6,'#d9c9a2')+C(14,-10,3,'#d9c9a2')+L(14,-34,30,-62,'#2f2f2f',1.5);};
A.kamera=function(){return R(-24,-34,48,26,'#2f3236')+C(0,-21,10,'#5fa8d3')+R(-20,-38,14,6,'#2f3236')+L(-10,-8,-18,0,'#2f3236',3)+L(10,-8,18,0,'#2f3236',3);};
A.gravsten=function(){return P('M-16 0 L-16 -40 Q0 -54 16 -40 L16 0Z','#a5a39c')+L(0,-34,0,-18,'#8a8880',2)+L(-6,-28,6,-28,'#8a8880',2);};

/* Personer (vandrare). typ: bonde, soldat, handlare, arbetare, medborgare, sjoman, resenar */
var W={bonde:['#6b8a4a','#c9a35e'],soldat:['#59583a','#4a4c33'],handlare:['#a8453a','#d9b872'],arbetare:['#5a6a82','#3f4a5c'],medborgare:['#6b4a8a','#2b3a6b'],sjoman:['#2b4a7a','#e9e0c8'],resenar:['#8a5a30','#c9b88a']};
function walker(typ){var c=W[typ]||W.resenar,body=c[0],hat=c[1];
 var hatSvg={bonde:P('M-9 -43 Q0 -52 9 -43Z','#c9a35e')+R(-12,-44,24,3,'#c9a35e'),soldat:P('M-8 -42 Q0 -54 8 -42Z','#4a4c33'),handlare:R(-10,-45,20,4,'#d9b872')+R(-6,-52,12,8,'#d9b872'),arbetare:P('M-8 -42 Q0 -50 8 -42Z','#3f4a5c')+R(-9,-43,18,3,'#3f4a5c'),medborgare:P('M-8 -43 Q0 -56 8 -43Z','#2b3a6b'),sjoman:P('M-8 -43 Q0 -52 8 -43Z','#e9e0c8')+R(-9,-44,18,3,'#2b4a7a'),resenar:P('M-8 -42 Q0 -52 8 -42Z','#8a5a30')+R(-13,-44,26,3,'#8a5a30')}[typ]||'';
 return '<g class="walk"><g transform="scale(1.35)"><path class="leg l" d="M-3 -16 L-5 0" stroke="#3a3a3a" stroke-width="4.5" stroke-linecap="round"/><path class="leg r" d="M3 -16 L5 0" stroke="#3a3a3a" stroke-width="4.5" stroke-linecap="round"/><rect x="-6" y="-35" width="12" height="20" rx="3" fill="'+body+'"/><line x1="5" y1="-26" x2="12" y2="-38" stroke="#3a3a3a" stroke-width="2.2"/><circle cx="0" cy="-39" r="4.6" fill="#d6a98a"/>'+hatSvg+'</g></g>';}

/* Illustrationsscener: sammansatta bilder (anv. i häften och sajt). Varje scen: [himmel1,himmel2,mark,[[asset,x,skala],...],hav?] */
var SC={
 kallor:['#f3e6c8','#e4d3a6','#b9986a',[['bokhylla',-170,1.1],['tryckpress',-60,1],['amfora',40,1.2],['gravsten',110,1],['kamera',180,1.1]]],
 hogkulturer:['#f7e3b0','#f2c276','#d9b872',[['pyramid',-170,1.1],['sphinx',-30,.9],['ziggurat',130,.9],['nilbat',230,.8],['palm',-250,1]]],
 egypten:['#f7e3b0','#f2c276','#d9b872',[['pyramid',-120,1.3],['pyramid',60,.9],['sphinx',180,.8],['palm',-230,1.1],['nilbat',250,.9]]],
 grekland:['#bfe0f2','#f2f6f8','#c9bfa0',[['tempel_grekiskt',-90,1.3],['amfora',60,1],['trirem',190,.8],['gran',-230,.9]]],
 rom:['#cfe3f2','#f5e9d0','#c9bf98',[['colosseum',-120,1.1],['akvedukt',130,.9],['legionar',-10,1],['romerskt_hus',250,.9]]],
 kolonisation:['#bfe0f2','#e8f2f6','#d9c79a',[['karavell',-120,1.1],['karavell',70,.9],['palm',190,1.2],['hamn',-250,.7]]],
 handel_hav:['#cfe6f2','#eaf3f7','#d4c9a0',[['kogg',-130,1],['segelfartyg',60,1],['hamn',210,.8],['marknad',-250,.7]]],
 upplysning:['#f1e4d0','#e2cfae','#a98f66',[['bokhylla',-150,1.1],['tryckpress',-30,1],['slott',120,.8],['folkmassa',230,.8]]],
 revolution:['#e8d9cf','#cbb8ab','#8a7a6a',[['barrikad',-80,1.2],['folkmassa',90,1],['giljotin',210,.8],['flagga_trikolor',-220,.9]]],
 industri:['#d7d9d9','#b9bdbf','#7a6f60',[['fabrik',-140,1.1],['skorstenar',20,.9],['lok',140,.9],['arbetarhus',250,.8]]],
 arbetare:['#cfd1d1','#aeb2b4','#706658',[['arbetarhus',-150,1.1],['fabrik',10,.9],['folkmassa',150,.9],['flagga_rod',230,.9]]],
 imperialism:['#cfe3f2','#f0e6cc','#c9ba8c',[['angbat',-120,1.1],['kanon',20,1],['palm',110,1.1],['soldat_grupp',200,1]]],
 ww1:['#c8c3b6','#a39f92','#6b5d46',[['skyttegrav',-120,1.2],['taggtrad',40,1],['biplan',100,1.1],['soldat_grupp',200,.9]]],
 ryska_revolutionen:['#e6d3cf','#c9b0ab','#8a7a70',[['folkmassa',-110,1.1],['flagga_rod',20,1],['tag',160,.8]]],
 mellankrig:['#d9d3c4','#bdb6a4','#7a6f5a',[['folkmassa',-110,1.1],['radio',20,1.1],['tag',130,.8],['arbetarhus',250,.7]]],
 ww2:['#c9ccce','#a7acae','#6b6a50',[['tank',-100,1.1],['bombplan',60,1],['soldat_grupp',150,1],['sjukhustalt',250,.8]]],
 kalla_kriget:['#cfd8de','#b3bec6','#7d7d78',[['mur',-90,1.1],['raket',60,1],['satellit',130,1],['flagga_bla',200,.9]]],
 valfard:['#cfe6f2','#eaf3f7','#9ac27a',[['villa',-140,1.1],['skola',10,1],['sjukhustalt',130,.8],['gran',230,1]]],
 rostratt:['#e6efe0','#cfe0c8','#a9bf92',[['valurna',-100,1.2],['riksdagshus',60,1],['folkmassa',230,.9]]],
 globalisering:['#bfe0f2','#eaf3f7','#8fb7a2',[['containerfartyg',-120,1.1],['jordglob',40,.9],['flygplan_modernt',150,1],['vindkraft',240,1]]],
 demokrati:['#cfe3f2','#eaf3f7','#a9bf92',[['riksdagshus',-60,1.2],['valurna',100,1],['folkmassa',210,.9],['flagga_bla',-220,.9]]],
 hamn:['#cfe6f2','#eaf3f7','#d4c9a0',[['hamn',-100,1],['kogg',60,1],['segelfartyg',180,.9]]]
};
var FLY={biplan:-120,bombplan:-130,satellit:-150,flygplan_modernt:-120,moln:-170};
window.PLA={A:A,W:walker,SC:SC,FLY:FLY,
 draw:function(name,o){o=o||{};var f=A[name];if(!f)return '';return f(o);},
 scen:function(key,w,h){var s=SC[key];if(!s)return '';var out='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 260" width="'+(w||640)+'" height="'+(h||260)+'"><defs><linearGradient id="sk'+key+'" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+s[0]+'"/><stop offset="1" stop-color="'+s[1]+'"/></linearGradient></defs><rect width="640" height="260" fill="url(#sk'+key+')"/>'+E(500,50,70,18,'#fff').replace('/>',' opacity=".6"/>')+E(140,36,56,14,'#fff').replace('/>',' opacity=".5"/>')+'<rect y="210" width="640" height="50" fill="'+s[2]+'"/>';
  s[3].forEach(function(it){out+='<g transform="translate('+(320+it[1])+' '+(214+(FLY[it[0]]||0))+') scale('+it[2]+')">'+(A[it[0]]?A[it[0]]({}):'')+'</g>';});
  return out+'</svg>';}
};
})();
