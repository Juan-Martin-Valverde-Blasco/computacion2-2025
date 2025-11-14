import asyncio
import aiohttp
from aiohttp import web
import socket
import json

HOST_B = '127.0.0.1'
PORT_B = 9001

async def fetch_from_B(data):
    reader, writer = await asyncio.open_connection(HOST_B, PORT_B)
    encoded = json.dumps(data).encode()
    writer.write(len(encoded).to_bytes(8, byteorder='big'))
    writer.write(encoded)
    await writer.drain()
    # recibir respuesta
    raw_len = await reader.readexactly(8)
    msg_len = int.from_bytes(raw_len, byteorder='big')
    data_bytes = await reader.readexactly(msg_len)
    writer.close()
    await writer.wait_closed()
    return json.loads(data_bytes.decode())

async def scrape_handler(request):
    url = request.query.get("url")
    # mock scraping simple
    scraping_data = {
        "title": "Example Domain",
        "links": ["https://iana.org/domains/example"],
        "meta_tags": {"description": "", "keywords": ""},
        "structure": {"h1": 1, "h2":0, "h3":0},
        "images_count": 0
    }
    try:
        processing_data = await fetch_from_B({"url": url})
        return web.json_response({
            "url": url,
            "scraping_data": scraping_data,
            "processing_data": processing_data,
            "status": "success"
        })
    except Exception as e:
        return web.json_response({"status":"error", "msg": str(e)})

app = web.Application()
app.router.add_get('/scrape', scrape_handler)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8000)