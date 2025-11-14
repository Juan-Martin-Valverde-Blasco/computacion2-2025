import asyncio
import aiohttp

async def main():
    url = "http://localhost:8000/scrape?url=https://example.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            print(data)

asyncio.run(main())