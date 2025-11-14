# server_processing.py
import asyncio
import json
from aiohttp import web
from pyppeteer import launch
from processor.performance import analyze_performance
from processor.image_processor import generate_thumbnails

HOST = '127.0.0.1'
PORT = 9001

async def fetch_screenshot(url: str) -> str:
    """Genera un screenshot en base64 usando pyppeteer"""
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(url, timeout=15000)
    screenshot_bytes = await page.screenshot()
    await browser.close()
    import base64
    return base64.b64encode(screenshot_bytes).decode('ascii')

async def process_url(url: str) -> dict:
    """Procesa un URL: screenshot, performance y thumbnails"""
    try:
        screenshot = await fetch_screenshot(url)
        performance_data = analyze_performance(url)
        thumbnails = generate_thumbnails(url)
        return {
            "screenshot": screenshot,
            "performance": performance_data,
            "thumbnails": thumbnails
        }
    except Exception as e:
        return {"error": str(e)}

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    try:
        # Leer el tamaño del payload (4 bytes big endian)
        header = await reader.readexactly(4)
        length = int.from_bytes(header, byteorder='big')
        payload = await reader.readexactly(length)
        data = json.loads(payload.decode('utf-8'))

        url = data.get("url")
        print(f"[B] Procesando solicitud: {url}")

        result = await process_url(url)

        # Enviar respuesta con el mismo protocolo
        response_bytes = json.dumps(result, ensure_ascii=False).encode('utf-8')
        writer.write(len(response_bytes).to_bytes(4, byteorder='big') + response_bytes)
        await writer.drain()
        print(f"[B] Resultado enviado y conexión cerrada")
    except Exception as e:
        print(f"[B] Error procesando solicitud: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"[B] Escuchando en {addr}")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
