from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, unquote
from urllib.robotparser import RobotFileParser
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://crayonsmilegames.github.io/'
PLAY = 'https://play.google.com/store/apps/details?id=com.crayonsmile.somikidsworld&pcampaignid=web_share'
COLORING_PLAY = 'https://play.google.com/store/apps/details?id=com.crayonsmile.somicoloring&pcampaignid=web_share'

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

pages = {}
for path in ROOT.rglob('*.html'):
    raw = path.read_bytes()
    assert not raw.startswith(b'\xef\xbb\xbf'), path
    assert b'\n' not in raw.replace(b'\r\n', b''), path
    s = raw.decode('utf-8')
    assert '\ufffd' not in s and '???' not in s, path
    url = BASE + path.relative_to(ROOT).as_posix().removesuffix('index.html')
    d = Document(s)
    pages[url] = (path, s, d)
    canonical = [a['href'] for t, a in d.tags if t == 'link' and a.get('rel') == 'canonical']
    assert canonical == [url], (path, canonical)
    assert sum(t == 'h1' for t, a in d.tags) == 1, path
    ids = [a['id'] for t, a in d.tags if 'id' in a]
    assert len(ids) == len(set(ids)), (path, 'duplicate IDs')
    alternates = {a['hreflang']: a['href'] for t, a in d.tags if t == 'link' and 'hreflang' in a}
    assert set(alternates) == {'ko', 'en', 'x-default'}, path
    for t, a in d.tags:
        link = a.get('href') or a.get('src') or a.get('data-img')
        if not link or link.startswith(('mailto:', 'data:')):
            continue
        absolute = urljoin(url, link)
        parsed = urlsplit(absolute)
        if parsed.hostname == 'play.google.com':
            assert absolute in {PLAY, COLORING_PLAY}, (path, absolute)
        if parsed.hostname != 'crayonsmilegames.github.io':
            continue
        target = ROOT / unquote(parsed.path.lstrip('/'))
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), (path, 'missing target', target)
        if parsed.fragment:
            assert re.search(r'id=["\']' + re.escape(unquote(parsed.fragment)) + r'["\']', target.read_text(encoding='utf-8')), (path, link)
    if 'privacy' not in url:
        metadata = {a.get('name', a.get('property')): a.get('content') for t, a in d.tags if t == 'meta'}
        assert metadata['og:url'] == url
        for key in ['og:image', 'twitter:image']:
            assert metadata[key].startswith(BASE)
        assert metadata['google-site-verification'] == 'YDlAggfaaH7thYKa-m15mn3zrxZNiwUIRVmhH_BvYEw'
        assert 'max-image-preview:large' in metadata['robots']
        schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)[1])
        apps = {item['@id']: item for item in schema['@graph'] if item['@type'] == 'SoftwareApplication'}
        graph = {item['@type']: item for item in schema['@graph']}
        from html import unescape
        assert {'Organization', 'WebSite'} <= set(graph), path
        assert graph['WebSite']['name'] == 'CrayonSmile'
        for app in apps.values():
            assert 'aggregateRating' not in app and 'review' not in app
            assert (ROOT / app['image'].removeprefix(BASE)).is_file()
            if app.get('installUrl'):
                assert app['installUrl'] in {PLAY, COLORING_PLAY}
                assert app['offers']['url'] == app['installUrl']
                assert app['offers']['price'] == '0'
        if '/games/somi-kids-world/' in url:
            assert set(graph) == {'SoftwareApplication', 'Organization', 'WebPage', 'WebSite', 'FAQPage'}
            assert set(apps) == {BASE + '#app', BASE + '#somi-coloring-app'}
            assert apps[BASE + '#app']['installUrl'] == PLAY
            coloring = apps[BASE + '#somi-coloring-app']
            assert coloring['url'] == BASE + ('en/' if '/en/' in url else '') + 'games/somi-coloring/'
            section = re.search(r'<section[^>]+id="somi-coloring".*?</section>', s, re.S)[0]
            assert coloring['name'] in unescape(section)
            assert coloring['description'] in unescape(section)
            assert COLORING_PLAY in unescape(section)
            for feature in coloring['featureList']:
                assert feature in unescape(section)
            faqs = graph['FAQPage']['mainEntity']
            assert len(faqs) == 6
            for item in faqs:
                id_ = item['@id'].split('#')[1]
                detail = re.search(r'<details id="' + id_ + r'">(.*?)</details>', s, re.S)[1]
                q = unescape(re.search(r'<summary>(.*?)</summary>', detail, re.S)[1])
                a = unescape(re.search(r'<p>(.*?)</p>', detail, re.S)[1])
                assert q == item['name'] and a == item['acceptedAnswer']['text'], id_
        elif '/games/' in url:
            assert set(graph) == {'SoftwareApplication', 'Organization', 'WebPage', 'WebSite'}
            assert len(apps) == 1
            app = next(iter(apps.values()))
            assert app['url'] == url
            assert app['name'] in unescape(s)
            if '/hangul-abc/' in url or '/somi-flashcards/' in url:
                assert not any(k in app for k in ['installUrl', 'downloadUrl', 'offers', 'releaseDate'])
                assert not any(urlsplit(a.get('href', '')).hostname == 'play.google.com' for t, a in d.tags)
                assert 'Coming soon' in s if '/en/' in url else '출시 예정' in s
                assert 'coming-notice' in s
        else:
            assert set(graph) == {'Organization', 'WebSite', 'CollectionPage'}
            entries = graph['CollectionPage']['mainEntity']['itemListElement']
            assert len(entries) == 4
            assert len(set(item['url'] for item in entries)) == 4
            for item in entries:
                assert item['name'] in unescape(s)
                assert item['url'].removeprefix(BASE.rstrip('/')) in s
        assert sum(t == 'main' for t, a in d.tags) == 1
    print('PASS', path.relative_to(ROOT), 'metadata, links, encoding, schema/content parity')

for url, (path, s, d) in pages.items():
    alts = {a['hreflang']: a['href'] for t, a in d.tags if t == 'link' and 'hreflang' in a}
    for alternate in alts.values():
        other = pages[alternate][2]
        assert url in [a.get('href') for t, a in other.tags if 'hreflang' in a]

urls = ET.parse(ROOT / 'sitemap.xml').findall('{*}url')
assert {u.find('{*}loc').text for u in urls} == set(pages)
robot = RobotFileParser()
robot.parse((ROOT / 'robots.txt').read_text(encoding='utf-8').splitlines())
for agent in ['Googlebot', 'Bingbot', 'OAI-SearchBot', 'PerplexityBot']:
    assert all(robot.can_fetch(agent, url) for url in pages), agent
assert robot.site_maps() == [BASE + 'sitemap.xml']
print('PASS reciprocal hreflang, sitemap coverage and search/AI crawler access')
