#!/usr/bin/env python3
import argparse
import asyncio
from aiohttp import web
from scraper.async_http import AsyncHTTPClient
from scraper.html_parser import parse_html
from datetime import datetime, timezone
from common.protocol import pack_message
import struct
import json

# --------------------------
# Función para recibir mensajes desde Servidor B (asyncio)
# --------------------------
async def unpack_message_async(reader: asyncio.StreamReader) -> dict:
    LEN_HEADER = 4
    header = await reader.readexactly(LEN_HEADER)
    (length,) = struct.unpack(">I", header)
    payload = await reader.readexactly(length)
    return json.loads(payload.decode("utf-8"))

# --------------------------
# Comunicación con Servidor B
# --------------------------
async def process_with_server_b(url: str, host: str, port: int) -> dict:
    reader, writer = await asyncio.open_connection(host, port)
    # Enviar mensaje
    writer.write(pack_message({"url": url}))
    await writer.drain()
    # Leer respuesta asíncronamente
    data = await unpack_message_async(reader)
    writer.close()
    await writer.wait_closed()
    return data

# --------------------------
# Handler HTTP para /scrape
# --------------------------
async def handle_scrape(request):
    params = request.rel_url.query
    url = params.get("url")
    if not url:
        return web.json_response({"status":"error","msg":"Missing url"}, status=400)

    try:
        # Scraping de la página
        html = await AsyncHTTPClient.fetch(url)
        scraping_data = parse_html(html, base_url=url)

        # Procesamiento CPU-bound en Servidor B
        processing_data = await process_with_server_b(url, "127.0.0.1", 9001)

        response = {
            "url": url,
            "timestamp": datetime.now(timezone.utc).isoformat(),  # timezone-aware UTC
            "scraping_data": scraping_data,
            "processing_data": processing_data,
            "status": "success"
        }
        return web.json_response(response)

    except Exception as e:
        return web.json_response({"status":"error","msg": str(e)}, status=500)

# --------------------------
# Main
# --------------------------
def main():
    parser = argparse.ArgumentParser(description="Servidor de Scraping Web Asíncrono")
    parser.add_argument("-i","--ip", required=True, help="Dirección de escucha (IPv4/IPv6)")
    parser.add_argument("-p","--port", required=True, type=int, help="Puerto de escucha")
    args = parser.parse_args()

    app = web.Application()
    app.router.add_get("/scrape", handle_scrape)
    web.run_app(app, host=args.ip, port=args.port)

if __name__ == "__main__":
    main()
