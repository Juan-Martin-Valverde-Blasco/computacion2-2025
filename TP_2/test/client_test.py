import asyncio
import aiohttp

URL_TO_SCRAPE = "https://example.com"

async def fetch(url_to_scrape):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=30)) as session:
        async with session.get(f"http://localhost:8000/scrape?url={url_to_scrape}") as resp:
            return await resp.json()

async def main():
    print("[Client-Test] Haciendo request a Servidor A...")
    data = await fetch(URL_TO_SCRAPE)
    print("[Client-Test] Resultado recibido:")
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
