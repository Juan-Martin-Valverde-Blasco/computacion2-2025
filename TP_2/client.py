import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://127.0.0.1:8000/scrape?url={url}") as resp:
            return await resp.json()

async def main():
    url_to_scrape = "https://example.com"
    print("[Client] Haciendo request a Servidor A...")
    data = await fetch(url_to_scrape)
    print("[Client] Resultado recibido:")
    print(data)

asyncio.run(main())