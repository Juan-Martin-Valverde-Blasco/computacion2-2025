import asyncio
from scraper.async_http import AsyncHTTPClient

async def test_fetch():
    html = await AsyncHTTPClient.fetch("https://example.com")
    assert "<title>" in html

asyncio.run(test_fetch())