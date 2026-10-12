const fs=document.querySelectorAll('.f'),cards=document.querySelectorAll('.card');
fs.forEach(b=>b.onclick=()=>{fs.forEach(x=>x.setAttribute('aria-pressed',x===b));cards.forEach(c=>c.hidden=b.dataset.f!=='all'&&c.dataset.c!==b.dataset.f)});
const lb=document.getElementById('lb'),im=lb.querySelector('img'),cap=lb.querySelector('span'),buy=lb.querySelector('.buy');let cur=0;
function show(i){cur=(i+ART.length)%ART.length;const[s,t,u]=ART[cur];im.src='img/'+s+'-900.webp';im.alt=t+', photograph by Tom Halseth';cap.textContent=t;buy.href=u}
document.querySelectorAll('.open').forEach(b=>b.onclick=()=>{show(+b.dataset.i);lb.showModal()});
lb.querySelector('.x').onclick=()=>lb.close();lb.querySelector('.prev').onclick=()=>show(cur-1);lb.querySelector('.next').onclick=()=>show(cur+1);
lb.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')show(cur-1);if(e.key==='ArrowRight')show(cur+1)});
lb.addEventListener('click',e=>{if(e.target===lb)lb.close()});
addEventListener('load',()=>{const sl=[...document.querySelectorAll('.sl')],bars=document.querySelectorAll('.bars i'),num=document.querySelector('.num'),ct=document.querySelector('.ct'),cb=document.querySelector('.cb');
sl.slice(1).forEach(i=>i.src=i.dataset.src);let k=0;
setInterval(()=>{if(document.hidden)return;sl[k].classList.remove('on');bars[k].classList.remove('on');k=(k+1)%sl.length;sl[k].classList.add('on');bars[k].classList.add('on');num.textContent='0'+(k+1)+' / 0'+sl.length;ct.textContent=HERO[k][0];cb.href=HERO[k][1]},7000)});
