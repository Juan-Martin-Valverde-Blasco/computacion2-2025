from bs4 import BeautifulSoup
from typing import Dict, List
from urllib.parse import urljoin

def parse_html(html: str, base_url: str = "") -> Dict:
    soup = BeautifulSoup(html, 'lxml')
    title_tag = soup.title.string.strip() if soup.title and soup.title.string else ''
    links = []
    for a in soup.find_all('a', href=True):
        links.append(urljoin(base_url, a['href']))
    # meta tags
    metas = {}
    for m in soup.find_all('meta'):
        if m.get('name'):
            metas[m['name'].lower()] = m.get('content','')
        if m.get('property'):
            metas[m['property'].lower()] = m.get('content','')
    # headers count
    structure = {}
    for i in range(1,7):
        structure[f'h{i}'] = len(soup.find_all(f'h{i}'))
    images_count = len(soup.find_all('img'))
    return {
        'title': title_tag,
        'links': links,
        'meta_tags': metas,
        'structure': structure,
        'images_count': images_count
    }

