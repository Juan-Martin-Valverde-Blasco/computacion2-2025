import threading
import requests
import time

URLS_TO_CRAWL = [
    "http://python.org",
    "http://example.com",
    "https://www.djangoproject.com/",
    "https://flask.palletsprojects.com/",
    "http://invalid.url.that.will.fail",
    "https://docs.python.org/3/library/threading.html"
]

results = {}
lock = threading.Lock()

def crawl(url, thread_id):
    print(f"[Hilo {thread_id}] Iniciando descarga de: {url}")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        content_length = len(response.text)
        print(f"[Hilo {thread_id}] Descarga completa: {url} ({content_length} bytes)")
    except requests.RequestException as e:
        content_length = -1
        print(f"[Hilo {thread_id}] Error al descargar {url}: {e}")

    with lock:
        results[url] = content_length
        print(f"[Hilo {thread_id}] Resultado almacenado.")

def main():
    start = time.time()
    threads = []

    print(f"Iniciando crawler con {len(URLS_TO_CRAWL)} hilos...\n")

    for i, url in enumerate(URLS_TO_CRAWL):
        t = threading.Thread(target=crawl, args=(url, i), name=f"Crawler-{i}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time.time() - start

    print("\n--- Resultados del Crawling ---")
    for url, size in results.items():
        if size != -1:
            print(f"{url} -> {size} bytes")
        else:
            print(f"{url} -> Falló la descarga")
    
    print(f"\nTiempo total: {duration:.2f} segundos")

if __name__ == "__main__":
    main()
