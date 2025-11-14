import asyncio
from aiohttp import web
import json
from common.protocol import pack_message
import socket

SERVER_B_HOST = "127.0.0.1"
SERVER_B_PORT = 9001

async def call_server_b(data: dict) -> dict:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_B_HOST, SERVER_B_PORT))
            s.sendall(pack_message(data))
            # leer respuesta completa
            header = s.recv(4)
            length = int.from_bytes(header, byteorder='big')
            payload = b''
            while len(payload) < length:
                chunk = s.recv(length - len(payload))
                if not chunk:
                    break
                payload += chunk
            return json.loads(payload.decode('utf-8'))
    except Exception as e:
        return {"error": str(e)}

async def handle_scrape(request):
    url = request.query.get("url")
    if not url:
        return web.json_response({"status": "error", "msg": "No URL provided"})
    processing_request = {"url": url}
    processing_data = await call_server_b(processing_request)
    # devolvemos un resultado simple
    result = {"url": url, "processing_data": processing_data, "status": "success"}
    return web.json_response(result)

async def main():
    app = web.Application()
    app.add_routes([web.get("/scrape", handle_scrape)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", 8000)
    await site.start()
    print("Server A escuchando en 127.0.0.1:8000")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
