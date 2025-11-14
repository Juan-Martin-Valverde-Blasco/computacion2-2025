import aiohttp
import asyncio

class AsyncHTTPClient:
    @staticmethod
    async def fetch(url: str, timeout: int = 15) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=timeout) as resp:
                resp.raise_for_status()
                return await resp.text()