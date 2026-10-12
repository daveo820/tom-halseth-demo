const p=require('puppeteer-core');(async()=>{const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
for(const [w,h] of [[360,740],[390,844],[430,932],[1440,900]]){const pg=await b.newPage();await pg.setViewport({width:w,height:h,isMobile:w<800,hasTouch:w<800,deviceScaleFactor:1});
await pg.goto('http://localhost:8765/',{waitUntil:'networkidle0'});await pg.screenshot({path:`/workspace/halseth-demo/shots/fix-${w}x${h}-top.png`});
await pg.evaluate(()=>{document.documentElement.style.scrollBehavior='auto';scrollTo(0,300)});await new Promise(r=>setTimeout(r,600));
await pg.screenshot({path:`/workspace/halseth-demo/shots/fix-${w}x${h}-scroll300.png`});
const r=await pg.evaluate(()=>{const R=s=>document.querySelector(s).getBoundingClientRect();scrollTo(0,0);return {hdr:R('.top').bottom,h1:R('h1').top,btnB:R('.hero-t .row').bottom,cap:R('.hero-cap').top,navW:R('.top nav').width,brandR:R('.brand').right,navL:R('.top nav').left}});console.log(w,JSON.stringify(r));await pg.close()}
await b.close()})();
