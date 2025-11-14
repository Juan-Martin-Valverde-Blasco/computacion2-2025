import asyncio
import os
from pathlib import Path
from scraper.async_http import AsyncHTTPClient
from scraper.html_parser import parse_html
from processor.image_processor import generate_thumbnails
from processor.performance import analyze_performance
from common.serialization import Serializer  # si usás el que me pasaste

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

URLS = [
    "https://example.com",
    "https://iana.org",
    "https://www.python.org"
]

async def process_url(url: str):
    result = {"url": url}
    # Scraping
    try:
        html = await AsyncHTTPClient.fetch(url)
        result['scraping_data'] = parse_html(html, base_url=url)
    except Exception as e:
        result['scraping_data'] = {"error": str(e)}
    
    # Processing (thumbnails + performance)
    try:
        thumbnails = generate_thumbnails(url)
        perf = analyze_performance(url)
        result['processing_data'] = {
            "thumbnails": thumbnails,
            "performance": perf
        }
    except Exception as e:
        result['processing_data'] = {"error": str(e)}

    # Status
    if "error" in result['scraping_data'] or "error" in result['processing_data']:
        result['status'] = "error"
    else:
        result['status'] = "success"

    # Guardar JSON
    filename = OUTPUT_DIR / f"{url.replace('https://','').replace('http://','').replace('/','_')}.json"
    Serializer.save_json(result, filename)
    print(f"[Client-C] Guardado JSON: {filename}")
    return result

async def main():
    tasks = [process_url(url) for url in URLS]
    await asyncio.gather(*tasks)
    print("[Client-C] Batch completo.")

if __name__ == "__main__":
    asyncio.run(main())
