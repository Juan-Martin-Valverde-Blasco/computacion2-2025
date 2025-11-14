from PIL import Image
import io, base64, requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def generate_thumbnails(url: str, max_thumbs=3, thumb_size=(128,128)):
    try:
        resp = requests.get(url, timeout=15)
        soup = BeautifulSoup(resp.text,'lxml')
        imgs = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                imgs.append(urljoin(url,src))
                if len(imgs)>=max_thumbs:
                    break
        thumbs_b64 = []
        for src in imgs:
            try:
                r = requests.get(src,timeout=10)
                im = Image.open(io.BytesIO(r.content))
                im.thumbnail(thumb_size)
                buf = io.BytesIO()
                im.save(buf, format='PNG', optimize=True)
                thumbs_b64.append(base64.b64encode(buf.getvalue()).decode('ascii'))
            except Exception:
                continue
        return thumbs_b64
    except Exception:
        return []

