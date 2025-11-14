# TP2 - Sistema de Scraping y Análisis Web Concurrente

Este proyecto implementa un sistema cliente-servidor para analizar sitios web de manera concurrente, generando un JSON con información de scraping y análisis de performance, incluyendo thumbnails de imágenes encontradas.

---

## Estructura de carpetas

TP_2/
│
├── client.py # Cliente que envía URLs al servidor y guarda resultados
├── server_processing.py # Servidor que procesa cada URL, hace scraping y análisis
├── scraper/
│ ├── async_parser.py # Cliente HTTP asíncrono
│ └── html_parser.py # Parseo del HTML
├── processor/
│ ├── image_processor.py # Generación de thumbnails
│ └── performance.py # Análisis de performance de la página
├── common/
│ └── protocol.py # Protocolo de comunicación cliente-servidor
├── output/ # Carpeta donde se guardan los JSON resultantes
└── requirements.txt # Dependencias del proyecto


---

## Instalación

1. Crear y activar un entorno virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

    Instalar todas las dependencias con requirements.txt:

pip install -r requirements.txt

    Esto instalará todas las librerías necesarias: aiohttp, beautifulsoup4, lxml, requests, Pillow, pyppeteer.

Uso
1. Levantar el servidor

python server_processing.py

El servidor escucha en 127.0.0.1:9001 y procesa las URLs que reciba del cliente.
2. Ejecutar el cliente

python client.py

El cliente enviará un batch de URLs al servidor y guardará los resultados en la carpeta output/ como archivos JSON individuales por cada URL.
Contenido de los JSON generados

Cada JSON en output/ tiene la siguiente estructura:

{
    "url": "https://example.com",
    "scraping_data": {
        "title": "Example Domain",
        "links": ["https://iana.org/domains/example"],
        "meta_tags": {
            "description": "",
            "keywords": ""
        },
        "structure": {"h1":1,"h2":0,"h3":0},
        "images_count": 0
    },
    "processing_data": {
        "thumbnails": [],           # Lista de imágenes codificadas en base64
        "performance": {
            "load_time_ms": 123,   # Tiempo de carga aproximado
            "total_size_kb": 456,  # Tamaño total de recursos
            "num_requests": 7
        }
    },
    "status": "success"
}

    Si ocurre un error durante scraping o análisis, status será "error" y processing_data incluirá un campo error con el mensaje correspondiente.

Notas importantes

    El scraping se realiza con un cliente HTTP asíncrono y el análisis de thumbnails y performance es real, no simulado.

    La carpeta output/ se crea automáticamente si no existe.

    Se descargará Chromium la primera vez que se genere un screenshot o thumbnail (necesario para pyppeteer).

    Todos los links y meta tags se extraen directamente del HTML de la página.

Ejemplo de ejecución

python server_processing.py
# En otra terminal:
python client.py

Salida parcial en consola:

[Client] Procesando https://www.python.org...
[Client] Guardado JSON: output/www.python.org.json
[Client] Batch completo.

Créditos

    Implementación: Juan Martin Valverde Blasco

    Curso: Computación II - Universidad de Mendoza

    Fecha: 2025