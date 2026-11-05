"""Build eight per-app terms pages and durable navigation from shared copy."""
from html import escape
import re
import xml.etree.ElementTree as ET
import build_brand_pages as brand
from terms_content import EFFECTIVE, VERSION, PACKAGES, sections


def terms(p, en):
    name = p['name'][en]
    path = brand.url(p['slug'], en) + 'terms/'
    title = name + brand.tr(' 서비스 이용약관 | CrayonSmile', ' Terms of Service | CrayonSmile', en)
    desc = brand.tr(f'{name}의 서비스 이용약관. 보호자 이용, 무료·유료 콘텐츠, 환불, 기기 내 데이터와 문의 방법을 안내합니다.',
                    f'Terms for {name}: guardian use, free and paid content, refunds, local data and support.', en)
    graph = [brand.ORG, brand.SITE, brand.breadcrumbs(path, title, en), {
        '@type': 'WebPage', '@id': brand.BASE + path + '#webpage', 'url': brand.BASE + path,
        'name': title, 'description': desc, 'inLanguage': 'en' if en else 'ko',
        'dateModified': EFFECTIVE, 'version': VERSION, 'isPartOf': {'@id': brand.BASE + '/#website'},
        'publisher': {'@id': brand.BASE + '/#organization'},
        'breadcrumb': {'@id': brand.BASE + path + '#breadcrumb'},
    }]
    nav = brand.header(en, p['slug']).replace(
        f'href="{brand.url(p["slug"], not en)}" lang=',
        f'href="{brand.url(p["slug"], not en)}terms/" lang=')
    source = brand.head(title, desc, path, en, 'crayonsmile-logo-transparent.png', graph) + nav
    source += f'''<main id="main-content" class="policy-wrap shell" data-terms-app="{p['slug']}">
<a class="back-link" href="{brand.url(p['slug'],en)}">← {escape(name)}</a>
<p class="eyebrow">TERMS OF SERVICE · CRAYONSMILE</p><h1>{escape(name)}<br>{brand.tr('서비스 이용약관','Terms of Service',en)}</h1>
<p class="policy-date"><time datetime="{EFFECTIVE}">{brand.tr('시행일: 2026년 11월 5일','Effective: November 5, 2026',en)}</time> · {brand.tr('버전','Version',en)} {VERSION}<br>{PACKAGES[p['slug']]}</p>
<div class="policy-summary"><strong>{brand.tr('이 앱에 적용되는 이용 안내입니다.','Terms specific to this app.',en)}</strong><p>{escape(p['name'][en])}{brand.tr('에만 적용되며 다른 앱의 이용권이나 기능을 포함하지 않습니다. 기본 설치는 무료이고 광고·구독은 없습니다. 유료 콘텐츠의 현재 제공 여부는 아래에서 안내합니다.',' is covered here; other apps’ entitlements and features are separate. Installation is free, with no ads or subscriptions. Paid-content availability is described below.',en)}</p></div>'''
    if p['upcoming']:
        source += f'''<aside class="coming-notice"><strong>{brand.tr('출시 준비 중','Preparing for launch',en)}</strong><p>{brand.tr('이 페이지의 게시가 앱 출시나 결제 개시를 의미하지 않습니다. 판매 전 최종 기능·상품 범위·가격을 안내합니다.','Publishing these terms does not mean the app has launched or sales have started. Final features, product scope and prices will be shown before sales.',en)}</p></aside>'''
    content = sections(p['slug'])
    source += f'<nav class="policy-toc" aria-label="{brand.tr("약관 목차","Terms contents",en)}"><ol>'
    source += ''.join(f'<li><a href="#{key}">{heading[en]}</a></li>' for key, heading, paragraphs in content)
    source += '</ol></nav>'
    for key, heading, paragraphs in content:
        source += f'<section class="policy-section" id="{key}"><h2>{heading[en]}</h2>'
        source += ''.join('<p>' + pair[en] + '</p>' for pair in paragraphs)
        source += '</section>'
    brand.write(path.lstrip('/') + 'index.html', source + '</main>' + brand.footer(en) + '</body></html>')


def build():
    for en in (False, True):
        for p in brand.PRODUCTS:
            terms(p, en)
    # Rebuilt product pages and preserved legacy Kids World pages use the same
    # idempotent link insertion. Never promote a different app inside Kids World.
    for file in brand.ROOT.rglob('*.html'):
        rel = file.relative_to(brand.ROOT).as_posix()
        en = rel.startswith('en/')
        p = next((p for p in brand.PRODUCTS if '/games/' + p['slug'] + '/' in '/' + rel), None)
        targets = [p] if p else brand.PRODUCTS
        source = file.read_text(encoding='utf-8')
        source = re.sub(r'<div class="terms-links".*?</div>', '', source, flags=re.S)
        links = ' · '.join(f'<a href="{brand.url(item["slug"],en)}terms/">{escape(item["name"][en])} {brand.tr("이용약관","Terms",en)}</a>' for item in targets)
        block = '<div class="terms-links" style="padding:20px;line-height:2;font-size:14px;overflow-wrap:anywhere">' + links + '</div>'
        updated = source.replace('</footer>', block + '</footer>')
        brand.write(rel, updated)
    # Preserve effective dates in the privacy policy; lastmod reflects navigation.
    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', ns)
    root = ET.Element('{' + ns + '}urlset')
    for file in sorted(brand.ROOT.rglob('*.html')):
        node = ET.SubElement(root, '{' + ns + '}url')
        ET.SubElement(node, '{' + ns + '}loc').text = brand.BASE + '/' + file.relative_to(brand.ROOT).as_posix().removesuffix('index.html')
        ET.SubElement(node, '{' + ns + '}lastmod').text = EFFECTIVE
    ET.indent(root, space='  ')
    brand.write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding='unicode'))
    print('Built 8 app-specific terms pages and linked all 20 public pages.')


if __name__ == '__main__':
    build()
