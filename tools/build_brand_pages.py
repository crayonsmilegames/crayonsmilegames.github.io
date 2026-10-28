"""Build the bilingual studio homepage and the focused product pages."""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://crayonsmilegames.github.io'
EMAIL = 'crayonsmile.games@gmail.com'
PLAY = 'https://play.google.com/store/apps/details?id=com.crayonsmile.somikidsworld&pcampaignid=web_share'
PRODUCTS = [
    dict(slug='somi-kids-world', color='peach', upcoming=False,
         name=['소미 키즈월드', 'Somi Kids World'], category=['이야기와 놀이', 'Stories & play'],
         headline=['호기심이 자라는, 우리 아이 첫 놀이터.', 'A little world of big discoveries.'],
         desc=['한글과 영어, 동화책, 색칠과 퍼즐까지. 좋아하는 놀이를 고르며 나만의 배움을 발견해요.', 'Korean and English, storybooks, coloring and puzzles. Follow your child’s curiosity into a world of playful learning.'],
         icon='app_icon.png', art='feature_graphic.png', store=PLAY),
    dict(slug='hangul-abc', color='mint', upcoming=True,
         name=['소미와 가나다 한글놀이', 'Hangul ABC with Somi'], category=['첫 한글', 'First steps in Hangul'],
         headline=['내 이름에서 시작하는 첫 한글.', 'The first letters of their own story.'],
         desc=['듣고, 쓰고, 조립하며 한글과 친해져요. 익숙한 내 이름에서 낱말과 그림 이야기로 한 걸음씩 나아가요.', 'Listen, trace and put letters together. Start with a familiar name, then discover Korean words and illustrated stories.'],
         icon='hangul-abc/app-icon.png', art='hangul-abc/feature-graphic.png',
         features=[['내 이름부터 차근차근', '흩어진 이름 글자를 제자리에 옮기며 친숙한 글자부터 만나요.', 'Start with a familiar name', 'Move the letters of a name into place and meet familiar Korean characters.'],
                   ['듣고, 따라 쓰고, 조립해요', '글자의 소리를 듣고 손가락으로 따라 써요. 자음과 모음을 움직여 글자가 만들어지는 모습을 경험해요.', 'Listen, trace and build', 'Hear each sound, trace each stroke and move consonants and vowels to build Korean syllables.'],
                   ['낱말에서 그림 이야기로', '보고 고르고 움직이는 놀이로 배운 낱말을 다시 만나요. 그림 이야기는 도서관에서 다시 펼쳐볼 수 있어요.', 'From words to little stories', 'Revisit words through playful activities, then return to illustrated stories in your library.']],
         shots=[('name.png', ['내 이름으로 시작해요', 'Begin with a name']), ('trace.png', ['손가락으로 따라 써요', 'Trace with a finger']), ('assemble.png', ['글자 조각을 모아요', 'Put letters together']), ('story.png', ['이야기로 다시 만나요', 'Meet words in stories'])]),
    dict(slug='somi-flashcards', color='butter', upcoming=True,
         name=['소미와 낱말카드 놀이', 'Somi FlashCards'], category=['한글·영어 낱말', 'Korean & English words'],
         headline=['한 장의 카드가, 새로운 발견이 되도록.', 'One little card. A whole new discovery.'],
         desc=['그림을 보고, 소리를 듣고, 알맞은 낱말을 찾아요. 한글과 영어 낱말을 만나며 나만의 마을도 함께 자라요.', 'Look at a picture, hear the word and find the answer. Discover Korean and English words while your own little village grows.'],
         icon='somi-flashcards/app-icon.png', art='somi-flashcards/feature-graphic.png',
         features=[['그림과 소리로 만나는 낱말', '한 번에 다섯 장씩 부담 없이 시작해요. 낱말을 다시 듣고, 세 가지 보기에서 답을 골라요. 틀려도 다시 도전할 수 있어요.', 'Pictures, sounds and small steps', 'Begin with five cards. Replay each word, choose from three answers and try again whenever you need to.'],
                   ['한글도, 영어도 나의 속도로', '한글과 영어를 바꾸어 같은 주제의 낱말을 만나요. 언어별 진도를 따로 기록해 차근차근 이어갈 수 있어요.', 'Two languages, your own pace', 'Explore familiar themes in Korean and English, with separate progress for each language.'],
                   ['배울수록 자라는 나만의 마을', '놀이를 이어가며 새싹과 집, 꽃밭이 더해지는 마을을 만나요. 다양한 주제의 카드와 반짝이는 특별 카드도 찾아보세요.', 'A village that grows with you', 'Watch sprouts, houses and flower gardens appear as you play. Explore themed collections and discover special shimmering cards.']],
         shots=[('korean.png', ['그림과 한글 낱말', 'Pictures and Korean words']), ('english.png', ['익숙한 그림으로 영어도', 'Familiar pictures, English words']), ('village.png', ['함께 자라는 나의 마을', 'Your growing village']), ('library.png', ['다양한 주제의 낱말 꾸러미', 'Explore word collections'])],
         note=['출시 시 앱 설치와 동물 꾸러미 20장은 무료로 제공할 예정입니다. 전체 콘텐츠는 20개 꾸러미, 400장의 카드로 구성되며 일부 꾸러미는 보호자 영역에서 별도 구매가 필요합니다.', 'At launch, the app and the 20-card animal collection are planned to be free. The full catalog has 20 collections and 400 cards; some collections require a separate purchase in the parent area.']),
    dict(slug='somi-coloring', color='rose', upcoming=False,
         name=['소미 색칠놀이', 'Somi Coloring'], category=['자유로운 색칠', 'Creative coloring'],
         headline=['마음 가는 색으로, 나만의 그림 한 장.', 'A little color. A lot of imagination.'],
         desc=['한글 자음과 동물, 가족, 일상의 친근한 그림을 좋아하는 색과 다양한 브러시로 채워보세요.', 'Fill familiar pictures of Korean consonants, animals, family and everyday life with your favorite colors and brushes.'],
         icon='somi-coloring/app-icon.png', art='somi-coloring/feature-graphic.png',
         store='https://play.google.com/store/apps/details?id=com.crayonsmile.somicoloring&pcampaignid=web_share',
         features=[['친근한 그림으로 시작해요', '한글 자음부터 동물과 가족, 일상 그림까지. 오늘 색칠하고 싶은 도안을 골라보세요.', 'Familiar pictures to start with', 'Choose a picture to color, from Korean consonants to animals, family and everyday scenes.'],
                   ['손끝에서 달라지는 색칠', '마커, 크레용, 붓, 반짝이 젤로 저마다 다른 느낌을 표현해요.', 'Different brushes, different discoveries', 'Try markers, crayons, brushes and glitter gel to give each picture its own character.'],
                   ['선 안에서, 내 마음대로', '경계선 안에서 칠하는 선 지키기 기능으로 색칠을 도와줘요. 소미 키즈월드와 별도로 설치하는 색칠 전용 앱입니다.', 'A helping hand for little artists', 'Stay-within-the-lines coloring helps little hands. Somi Coloring is a separate app from the coloring activity in Somi Kids World.']])
]

def write(path, text):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((text.rstrip() + '\n').replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8'))

def url(slug='', en=False):
    return ('/en' if en else '') + (f'/games/{slug}/' if slug else '/')

def tr(ko, en, lang):
    return en if lang else ko

def status(p, en):
    return tr('출시 예정', 'Coming soon', en) if p['upcoming'] else tr('지금 플레이', 'Available now', en)

def header(en, slug=''):
    home = url(en=en)
    return f'''<a class="skip-link" href="#main-content">{tr('본문으로 건너뛰기', 'Skip to content', en)}</a>
<header class="brand-header"><div class="shell header-inner">
<a class="brand" href="{home}" aria-label="CrayonSmile {tr('홈', 'home', en)}"><img src="/assets/crayonsmile-logo-transparent.png" width="48" height="48" alt=""><span>Crayon<span class="brand-smile">Smile</span></span></a>
<nav aria-label="{tr('메인 메뉴', 'Main navigation', en)}"><a href="{home}#games">{tr('우리의 게임', 'Our games', en)}</a><a href="{home}#about">{tr('우리가 만드는 시간', 'Our story', en)}</a><a class="language" href="{url(slug, not en)}" lang="{'ko' if en else 'en'}">{'한국어' if en else 'EN'}</a></nav>
</div></header>'''

def footer(en):
    return f'''<footer class="brand-footer"><div class="shell footer-top"><div><a class="wordmark" href="{url(en=en)}">CrayonSmile<span class="coral">.</span></a><p>{tr('아이의 작은 발견을 함께합니다.', 'Here for their little discoveries.', en)}</p></div><div class="footer-links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{'/en' if en else ''}/privacy/">{tr('개인정보처리방침', 'Privacy policy', en)}</a></div></div><div class="shell footer-bottom"><span>© 2026 CrayonSmile. All rights reserved.</span><span>{tr('작은 놀이, 자라는 미소.', 'Little moments. Growing smiles.', en)}</span></div></footer>'''

def head(title, desc, path, en, art, graph):
    canonical = BASE + path
    ko_path = path.removeprefix('/en') if en else path
    return f'''<!doctype html>
<html lang="{'en' if en else 'ko'}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(desc, quote=True)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="google-site-verification" content="YDlAggfaaH7thYKa-m15mn3zrxZNiwUIRVmhH_BvYEw">
<meta name="naver-site-verification" content="67e1dfaeec915db0f5aa036575c893d1eab5b3f1">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="ko" href="{BASE}{ko_path}"><link rel="alternate" hreflang="en" href="{BASE}/en{ko_path}"><link rel="alternate" hreflang="x-default" href="{BASE}{ko_path}">
<meta property="og:type" content="website"><meta property="og:site_name" content="CrayonSmile"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(desc, quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="{'en_US' if en else 'ko_KR'}"><meta property="og:image" content="{BASE}/assets/{art}"><meta property="og:image:alt" content="{escape(title, quote=True)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(title, quote=True)}"><meta name="twitter:description" content="{escape(desc, quote=True)}"><meta name="twitter:image" content="{BASE}/assets/{art}">
<link rel="icon" type="image/png" href="/assets/crayonsmile-logo-transparent.png"><link rel="stylesheet" href="/assets/brand.css"><script src="/assets/brand.js" defer></script>
<script type="application/ld+json">{json.dumps({'@context':'https://schema.org', '@graph':graph}, ensure_ascii=False, indent=2)}</script>
</head><body>'''

ORG = {'@type':'Organization', '@id':BASE+'/#organization', 'name':'CrayonSmile', 'alternateName':'크레용스마일', 'url':BASE+'/', 'logo':BASE+'/assets/crayonsmile-logo-transparent.png', 'email':EMAIL}
SITE = {'@type':'WebSite', '@id':BASE+'/#website', 'url':BASE+'/', 'name':'CrayonSmile', 'inLanguage':['ko','en'], 'publisher':{'@id':BASE+'/#organization'}}

def home(en):
    title = tr('크레용스마일 | 놀이로 만나는 작은 배움', 'CrayonSmile | Little moments. Growing smiles.', en)
    desc = tr('아이와 가족을 위한 따뜻한 게임을 만드는 크레용스마일. 소미 키즈월드, 소미 색칠놀이, 출시 예정인 소미와 가나다 한글놀이와 소미와 낱말카드 놀이를 만나보세요.', 'Warm, playful games for children and families. Explore Somi Kids World, Somi Coloring, and the upcoming Hangul ABC with Somi and Somi FlashCards.', en)
    graph = [ORG, SITE, {'@type':'CollectionPage','@id':BASE+url(en=en)+'#webpage','url':BASE+url(en=en),'name':title,'description':desc,'inLanguage':'en' if en else 'ko','dateModified':'2026-10-28','isPartOf':{'@id':BASE+'/#website'},'mainEntity':{'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'name':p['name'][en],'url':BASE+url(p['slug'],en)} for i,p in enumerate(PRODUCTS)]}}]
    s = head(title, desc, url(en=en), en, 'crayonsmile-logo-transparent.png', graph) + header(en)
    s += f'''<main id="main-content"><section class="shell studio-hero"><div class="hero-copy"><p class="eyebrow"><span class="tiny-crayon" aria-hidden="true"></span> LITTLE MOMENTS, GROWING SMILES</p><h1>{tr('작은 놀이가,<br>커다란 <span class="smile-word">미소로.</span>', 'Little moments.<br><span class="smile-word">Growing smiles.</span>', en)}</h1><p class="hero-intro">{tr('처음 만나는 글자, 좋아하는 이야기, 마음껏 칠한 그림.<br>크레용스마일은 아이의 작은 발견이 자라는 게임을 만듭니다.', 'A first letter. A favorite story. A splash of color.<br>We make games where little discoveries grow.', en)}</p><a class="button primary" href="#games">{tr('우리의 게임 만나보기', 'Find your next little adventure', en)} <span aria-hidden="true">↗</span></a><p class="hero-footnote">{tr('아이의 속도로, 가족과 함께.', 'At their own pace. Together as a family.', en)}</p></div><div class="hero-gallery" aria-label="{tr('크레용스마일의 네 가지 게임', 'Four games from CrayonSmile', en)}">'''
    for i,p in enumerate(PRODUCTS):
        s += f'''<a class="mini-game mini-{i} {p['color']}" href="{url(p['slug'],en)}"><img src="/assets/{p['art']}" width="1024" height="500" alt="{escape(p['name'][en])}" fetchpriority="{'high' if i==0 else 'auto'}"><span>{p['name'][en]} <span aria-hidden="true">↗</span></span></a>'''
    s += f'''</div></section><div class="studio-ribbon"><div class="shell ribbon-inner"><span>{tr('호기심을 따라', 'Follow their curiosity', en)}</span><span aria-hidden="true">✳</span><span>{tr('저마다의 속도로', 'At their own pace', en)}</span><span aria-hidden="true">✳</span><span>{tr('함께하는 즐거움', 'Make room for joy', en)}</span></div></div><section class="shell games-section" id="games"><div class="section-heading"><div><p class="eyebrow">OUR LITTLE WORLDS</p><h2>{tr('오늘은 어떤 놀이를 해볼까요?', 'What shall we discover today?', en)}</h2></div><p>{tr('좋아하는 놀이에서 시작하는 배움.<br>소미와 함께 하나씩 만나보세요.', 'A little learning starts with a favorite game.<br>Meet the worlds we’re making with Somi.', en)}</p></div><div class="games-grid">'''
    for p in PRODUCTS:
        s += f'''<article class="game-card {p['color']}" id="{p['slug']}"><a class="game-art" href="{url(p['slug'],en)}" aria-label="{escape(p['name'][en])} {tr('소개', 'details', en)}"><img src="/assets/{p['art']}" width="1024" height="500" alt="{escape(p['name'][en])} {tr('공식 소개 이미지', 'official artwork', en)}" loading="lazy"></a><div class="game-info"><div class="game-meta"><span>{p['category'][en]}</span><span class="status {'soon' if p['upcoming'] else 'available'}">{status(p,en)}</span></div><h3><a href="{url(p['slug'],en)}">{p['name'][en]}</a></h3><p>{p['desc'][en]}</p><a class="text-link" href="{url(p['slug'],en)}">{tr('게임 알아보기', 'Explore the game', en)} <span aria-hidden="true">↗</span></a></div></article>'''
    s += f'''</div><p class="launch-note">{tr('출시 예정 게임의 일정과 다운로드 안내는 각 소개 페이지에서 전해드릴게요.', 'Launch news and download details for upcoming games will appear on their own pages.', en)}</p></section><section class="about-section" id="about"><div class="shell about-inner"><div class="brand-illustration"><img src="/assets/crayonsmile-logo-transparent.png" width="320" height="320" alt="{tr('미소 짓는 크레용과 CrayonSmile 로고', 'A smiling crayon and the CrayonSmile logo', en)}" loading="lazy"></div><div><p class="eyebrow">A NOTE FROM CRAYONSMILE</p><h2>{tr('잘하는 것보다,<br>좋아하는 마음이 먼저.', 'A little joy comes<br>before a big achievement.', en)}</h2><p>{tr('글자를 하나 알아보고, 이야기의 다음 장을 넘기고,<br>마음에 드는 색을 고르는 작은 순간들.<br>우리는 그 안에 담긴 호기심과 스스로 해보는 기쁨을 소중히 여깁니다.', 'Recognizing a letter. Turning a story’s next page.<br>Picking just the right color.<br>We care about the curiosity and quiet joy in doing it yourself.', en)}</p><p>{tr('아이의 하루에 다정한 놀이 하나를 더하는 일.<br>크레용스마일이 만들고 싶은 시간입니다.', 'One more warm, playful moment in a child’s day.<br>That’s what we’re here to make.', en)}</p></div></div></section><section class="shell contact-section" id="contact"><p class="eyebrow">SAY HELLO</p><h2>{tr('함께 나누고 싶은 이야기가 있나요?', 'Have a little something to share?', en)}</h2><p>{tr('게임 이용 중 궁금한 점이나 전하고 싶은 이야기를 들려주세요.', 'Questions about a game, or a thought you’d like to share? We’d love to hear it.', en)}</p><a class="button secondary" href="mailto:{EMAIL}">{tr('크레용스마일에 연락하기', 'Say hello to CrayonSmile', en)} <span aria-hidden="true">↗</span></a></section></main>'''
    write(('en/' if en else '')+'index.html', s + footer(en) + '</body></html>')

def product(p,en):
    name=p['name'][en]; path=url(p['slug'],en)
    title=name+' | CrayonSmile'+(' · '+status(p,en) if p['upcoming'] else '')
    app={'@type':'SoftwareApplication','@id':BASE+url(p['slug'])+'#app','name':name,'url':BASE+path,'description':p['desc'][en],'image':BASE+'/assets/'+p['art'],'operatingSystem':'Android','applicationCategory':'EducationalApplication','publisher':{'@id':BASE+'/#organization'}}
    if not p['upcoming']:
        app.update(installUrl=p['store'],downloadUrl=p['store'],isAccessibleForFree=True,offers={'@type':'Offer','price':'0','priceCurrency':'KRW','url':p['store']})
    graph=[ORG,SITE,app,{'@type':'WebPage','@id':BASE+path+'#webpage','url':BASE+path,'name':title,'inLanguage':'en' if en else 'ko','dateModified':'2026-10-28','isPartOf':{'@id':BASE+'/#website'},'about':{'@id':app['@id']}}]
    s=head(title,p['desc'][en],path,en,p['art'],graph)+header(en,p['slug'])
    s+=f'''<main id="main-content"><section class="product-hero {p['color']}"><div class="shell"><a class="back-link" href="{url(en=en)}#games">← {tr('모든 게임', 'All games', en)}</a><div class="product-top"><div class="product-copy"><div class="product-identity"><img src="/assets/{p['icon']}" width="72" height="72" alt=""><div><p class="eyebrow">CRAYONSMILE · {p['category'][en]}</p><span class="status {'soon' if p['upcoming'] else 'available'}">{status(p,en)}</span></div></div><h1>{name}</h1><p class="product-tagline">{p['headline'][en]}</p><p class="product-description">{p['desc'][en]}</p>'''
    if p['upcoming']:
        s+=f'''<div class="coming-notice"><strong>{tr('곧 만나요!', 'See you soon!', en)}</strong><p>{tr('출시를 준비하고 있어요. 다운로드 안내는 출시 후 이 페이지에 추가됩니다.', 'We’re getting ready for launch. Download details will be added here when the game is available.', en)}</p></div>'''
    else:
        s+=f'''<a class="button primary" href="{escape(p['store'],quote=True)}" target="_blank" rel="noopener noreferrer">{tr('Google Play에서 무료 다운로드', 'Get it free on Google Play', en)} <span aria-hidden="true">↗</span></a>'''
    s+=f'''</div><figure class="product-art"><img src="/assets/{p['art']}" width="1024" height="500" alt="{name} {tr('공식 소개 이미지', 'official artwork', en)}" fetchpriority="high"></figure></div></div></section><section class="shell product-features" id="features"><p class="eyebrow">LITTLE WAYS TO PLAY</p><h2>{tr('이렇게 함께 놀아요', 'Little ways to learn and play', en)}</h2><div class="feature-grid">'''
    for i,f in enumerate(p['features']):
        s+=f'<article><span class="feature-number">0{i+1}</span><h3>{f[2 if en else 0]}</h3><p>{f[3 if en else 1]}</p></article>'
    s+='</div></section>'
    if p.get('shots'):
        s+=f'''<section class="screens-section"><div class="shell"><p class="eyebrow">A PEEK INSIDE</p><h2>{tr('미리 만나는 놀이 시간', 'A peek at playtime', en)}</h2><p class="screens-note">{tr('개발 중인 화면으로, 출시 버전에서는 달라질 수 있습니다.', 'Screens shown are from development and may change before launch.', en)}</p><div class="screenshot-grid {'portrait' if p['slug']=='hangul-abc' else ''}">'''
        for file,caption in p['shots']:
            s+=f'''<figure><img src="/assets/{p['slug']}/{file}" alt="{escape(caption[en])}" loading="lazy"><figcaption>{caption[en]}</figcaption></figure>'''
        s+='</div></div></section>'
    if p.get('note'):
        s+=f'''<aside class="shell purchase-note"><h2>{tr('보호자에게 전하는 이용 안내', 'A note for parents', en)}</h2><p>{p['note'][en]}</p></aside>'''
    s+=f'''<section class="shell related-section"><h2>{tr('다른 놀이도 만나보세요', 'More little worlds to explore', en)}</h2><div class="related-grid">'''
    for other in PRODUCTS:
        if other is p: continue
        s+=f'''<a class="related-card" href="{url(other['slug'],en)}"><img src="/assets/{other['icon']}" width="56" height="56" alt="" loading="lazy"><span><strong>{other['name'][en]}</strong><small>{status(other,en)}</small></span><span aria-hidden="true">↗</span></a>'''
    s+='</div></section></main>'+footer(en)+'</body></html>'
    write(path.lstrip('/')+'index.html',s)

def main():
    for en in [False,True]:
        home(en)
        for p in PRODUCTS:
            if p['slug'] != 'somi-kids-world': product(p,en)
    print('Built 2 brand homepages and 6 product pages.')

if __name__=='__main__': main()
