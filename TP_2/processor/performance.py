import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def analyze_performance(url: str, timeout: int = 15) -> dict:
    start = time.time()
    try:
        resp = requests.get(url, timeout=timeout)
        load_time_ms = int((time.time()-start)*1000)
        total_size = len(resp.content)
        num_requests = 1
        soup = BeautifulSoup(resp.text, 'lxml')
        resources = []
        for tag, attr in (('img','src'), ('script','src'), ('link','href')):
            for t in soup.find_all(tag):
                if t.get(attr):
                    resources.append(urljoin(url, t.get(attr)))
        for r in resources:
            try:
                rr = requests.head(r, timeout=5)
                total_size += int(rr.headers.get('content-length',0))
                num_requests += 1
            except Exception:
                continue
        return {'load_time_ms': load_time_ms, 'total_size_kb': max(1,total_size//1024), 'num_requests': num_requests}
    except Exception as e:
        return {'load_time_ms': None, 'total_size_kb': None, 'num_requests':0, 'error': str(e)}

