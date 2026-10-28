"""Check published content, HTTP indexing controls and search-bot access."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET
from build_brand_pages import ROOT, BASE

BOTS = ['Googlebot', 'Bingbot', 'Yeti', 'OAI-SearchBot', 'PerplexityBot']

def fetch(address, agent='CrayonSmile-Website-Audit'):
    request = Request(address, headers={'User-Agent':agent, 'Cache-Control':'no-cache'})
    with urlopen(request, timeout=25) as response:
        return response.status, response.headers, response.read()

def check_page(address):
    try:
        status, headers, body = fetch(address)
        path = ROOT / unquote(urlsplit(address).path.lstrip('/'))
        if path.is_dir():
            path /= 'index.html'
        # Git normalizes source line endings when publishing the committed site.
        expected = path.read_bytes().replace(b'\r\n', b'\n')
        content = body.replace(b'\r\n', b'\n')
        result = {'url':address, 'status':status,
                  'html':headers.get_content_type() == 'text/html',
                  'no_header_noindex':'noindex' not in headers.get('X-Robots-Tag','').lower(),
                  'matches_local_source':hashlib.sha256(content).digest() == hashlib.sha256(expected).digest()}
        result['ok'] = status == 200 and all(result[k] for k in ['html','no_header_noindex','matches_local_source'])
        return result
    except Exception as error:
        return {'url':address, 'ok':False, 'error':str(error)}

def check_agent(agent, robot):
    try:
        status, headers, body = fetch(BASE+'/', agent)
        allowed = robot.can_fetch(agent, BASE+'/')
        indexable = 'noindex' not in headers.get('X-Robots-Tag','').lower()
        matches_home = body.replace(b'\r\n',b'\n') == (ROOT/'index.html').read_bytes().replace(b'\r\n',b'\n')
        return {'agent':agent,'status':status,'robots_allows':allowed,
                'matches_homepage':matches_home,'ok':status == 200 and allowed and indexable and matches_home}
    except Exception as error:
        return {'agent':agent,'ok':False,'error':str(error)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional JSON evidence file outside the public site.')
    args = parser.parse_args()
    expected = {node.text for node in ET.parse(ROOT/'sitemap.xml').findall('{*}url/{*}loc')}
    sitemap_status, _, sitemap = fetch(BASE+'/sitemap.xml')
    actual = {node.text for node in ET.fromstring(sitemap).findall('{*}url/{*}loc')}
    robot_status, _, robots = fetch(BASE+'/robots.txt')
    robot = RobotFileParser()
    robot.parse(robots.decode('utf-8').splitlines())
    with ThreadPoolExecutor(max_workers=6) as pool:
        pages = list(pool.map(check_page, sorted(expected)))
        agents = list(pool.map(lambda name:check_agent(name, robot), BOTS))
    site_map_ok = sitemap_status == 200 and actual == expected
    robots_ok = robot_status == 200 and robot.site_maps() == [BASE+'/sitemap.xml']
    result = {'ok':site_map_ok and robots_ok and all(r['ok'] for r in pages+agents),
              'sitemap_ok':site_map_ok,'robots_ok':robots_ok,'pages':pages,'agents':agents,
              'limitations':'HTTP and robots checks simulate user-agent headers. They do not verify actual crawler IPs, Search Console/Naver account state, index inclusion, rankings or AI citations.'}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({'ok':result['ok'],'pages_checked':len(pages),'agents_checked':len(agents),
                      'failures':[r for r in pages+agents if not r['ok']]}))
    if not result['ok']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
