import json,html,re,shutil,os
art=json.load(open('src/art.json'))
BASE="https://daveo820.github.io/tom-halseth-demo/"
STORE="https://tom-halseth.pixels.com"
def cat(t):
  t=t.lower()
  if 'minneapolis' in t or 'hennepin' in t: return 'city','Minneapolis'
  if 'tulip' in t or 'fern' in t or 'leaf' in t or 'abstract' in t: return 'macro','Flowers and Details'
  if 'sunset' in t or 'moon' in t: return 'sky','Sunsets and Skies'
  if 'superior' in t or 'temperance' in t or 'gooseberry' in t or 'poplar' in t or 'falls' in t or 'waterfall' in t: return 'north','North Shore and Waterfalls'
  return 'seasons','Seasons'
cats={}
for a in art:
  a['c'],n=cat(a['title']); cats[a['c']]=n
hero=next(a for a in art if a['slug'].startswith('power-and-energy'))
e=html.escape
def fig(a,i):
  s=a['slug']
  return f'''<li class="card" data-c="{a['c']}"><button class="open" type="button" data-i="{i}" aria-label="View {e(a['title'])} larger"><img src="img/{s}-480.webp" srcset="img/{s}-480.webp 480w, img/{s}-900.webp 900w" sizes="(min-width:1100px) 360px,(min-width:700px) 45vw,100vw" width="{a['w']}" height="{a['h']}" alt="{e(a['title'])}, photograph by Tom Halseth" loading="lazy" decoding="async"></button><div class="meta"><h3>{e(a['title'])}</h3><a class="buy" href="{a['url']}" rel="noopener">Buy a print<span class="vh"> of {e(a['title'])}</span></a></div></li>'''
bio=["Thank you for visiting my Gallery and Store. I'm a Minnesota based photographer, and my work reflects my passion and love for photography and the outdoors. I primarily shoot landscape, architectural, abstract and macro images.",
"I've always had an interest in photography, and I believe every photograph should tell a story. I strive to come up with compelling images that capture that unique moment in time, and the nuances of light and shadows in a scene or venue. I'm very fortunate and honored that my work has won awards and been published.",
"If you do order prints I would highly recommend the Luster paper for its very high quality and look. The metal prints look absolutely stunning as well. Along with framed and unframed prints and canvas wraps, artwork is also available on tote bags, greeting cards, coffee mugs and many other products.",
"All images are copyrighted and may not be reproduced or manipulated in any way without written permission. I hope you enjoy my art and find something you like."]
desc="Tom Halseth is a Minnesota based photographer of landscape, architectural, abstract and macro images, from Lake Superior's North Shore to Minneapolis."
ld=[{"@context":"https://schema.org","@type":"Person","name":"Tom Halseth","jobTitle":"Photographer","url":BASE,"image":BASE+"img/"+hero['slug']+"-900.webp","homeLocation":{"@type":"Place","name":"Minnesota"},"sameAs":[STORE],"description":desc},
{"@context":"https://schema.org","@type":"ImageGallery","name":"Tom Halseth Photography","url":BASE,"author":{"@type":"Person","name":"Tom Halseth"},"image":[{"@type":"ImageObject","name":a['title'],"contentUrl":BASE+"img/"+a['slug']+"-900.webp","url":a['url'],"creator":{"@type":"Person","name":"Tom Halseth"}} for a in art]}]
filters=''.join(f'<button type="button" class="f" data-f="{k}" aria-pressed="false">{e(v)}</button>' for k,v in cats.items())
hs=hero['slug']
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tom Halseth Photography | Minnesota Landscape Photographer</title>
<meta name="description" content="{e(desc)}"><meta name="robots" content="noindex, nofollow"><link rel="canonical" href="{BASE}">
<meta property="og:title" content="Tom Halseth Photography"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{BASE}img/{hs}-900.webp"><link rel="icon" href="data:,"><meta name="theme-color" content="#14181a">
<link rel="preload" as="image" href="img/{hs}-hero.webp" fetchpriority="high">
<style>{open('src/style.css').read()}</style>
<script type="application/ld+json">{json.dumps(ld)}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><a class="brand" href="#top">Tom Halseth</a><nav aria-label="Main"><a href="#gallery">Gallery</a><a href="#about">About</a><a href="#contact">Contact</a></nav></header>
<main id="main">
<section class="hero" id="top"><img src="img/{hs}-hero.webp" width="{hero['w']}" height="{hero['h']}" alt="{e(hero['title'])}, photograph by Tom Halseth" fetchpriority="high" decoding="async">
<div class="hero-t"><p class="eyebrow">Minnesota photographer</p><h1>Tom Halseth Photography</h1><p class="lede">Landscape, architectural, abstract and macro images. Every photograph should tell a story.</p><a class="btn" href="#gallery">View the gallery</a></div></section>
<section id="gallery" class="wrap" aria-labelledby="g-h"><h2 id="g-h">Gallery</h2><p class="sub">Prints, canvas, metal and more are available through Tom's store. Each Buy button opens that photograph's own page.</p>
<div class="filters" role="group" aria-label="Filter by collection"><button type="button" class="f" data-f="all" aria-pressed="true">All</button>{filters}</div>
<ul class="grid">{''.join(fig(a,i) for i,a in enumerate(art))}</ul></section>
<section id="about" class="wrap about" aria-labelledby="a-h"><img src="img/{art[15]['slug']}-480.webp" width="{art[15]['w']}" height="{art[15]['h']}" alt="{e(art[15]['title'])}, photograph by Tom Halseth" loading="lazy" decoding="async"><div><h2 id="a-h">About Tom</h2>{''.join(f'<p>{e(p)}</p>' for p in bio)}</div></section>
<section id="contact" class="wrap contact" aria-labelledby="c-h"><h2 id="c-h">Contact</h2><p>Questions about a print, sizing or licensing? Send Tom a message through his store.</p><p class="row"><a class="btn" href="{STORE}/contactus.html?tab=contactus" rel="noopener">Contact Tom</a><a class="btn ghost" href="{STORE}" rel="noopener">Visit the full store</a></p></section>
</main>
<footer class="wrap foot"><p>All images © Tom Halseth. All rights reserved. Prints fulfilled by Pixels with a 30 day money back guarantee.</p><p class="demo">Demo site by LuminArch</p></footer>
<dialog id="lb" aria-label="Photo viewer"><button type="button" class="x" aria-label="Close">×</button><button type="button" class="nav prev" aria-label="Previous photo">‹</button><figure><img alt="" width="900" height="675"><figcaption><span></span><a class="buy" href="https://tom-halseth.pixels.com" rel="noopener">Buy a print</a></figcaption></figure><button type="button" class="nav next" aria-label="Next photo">›</button></dialog>
<script>const ART={json.dumps([[a['slug'],a['title'],a['url']] for a in art])};{open('src/app.js').read()}</script>
</body></html>'''
os.makedirs('site',exist_ok=True)
open('site/index.html','w').write(page)
shutil.copytree('img','site/img',dirs_exist_ok=True)
open('site/robots.txt','w').write("User-agent: *\nDisallow: /\n")
open('site/.nojekyll','w').write('')
print(len(page))
