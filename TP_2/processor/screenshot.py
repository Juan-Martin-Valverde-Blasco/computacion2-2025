import io, base64
from PIL import Image

def generate_screenshot_placeholder(url: str) -> str:
    # 800x600 gris
    im = Image.new('RGB',(800,600),(200,200,200))
    buf = io.BytesIO()
    im.save(buf,format='PNG')
    return base64.b64encode(buf.getvalue()).decode('ascii')
