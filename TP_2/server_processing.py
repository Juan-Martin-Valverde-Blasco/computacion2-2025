import argparse
import socketserver
import json
from multiprocessing import Pool
from processor.screenshot import generate_screenshot_placeholder
from processor.performance import analyze_performance
from processor.image_processor import generate_thumbnails
from common.protocol import pack_message, unpack_message_from_socket

def process_task(data):
    url = data['url']
    return {
        "screenshot": generate_screenshot_placeholder(url),
        "performance": analyze_performance(url),
        "thumbnails": generate_thumbnails(url)
    }

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            data = unpack_message_from_socket(self.request)
            with Pool() as pool:
                result = pool.apply(process_task, (data,))
            self.request.sendall(pack_message(result))
        except Exception as e:
            self.request.sendall(pack_message({"error": str(e)}))

def main():
    parser = argparse.ArgumentParser(description="Servidor de Procesamiento Distribuido")
    parser.add_argument("-i","--ip", required=True, help="IP de escucha")
    parser.add_argument("-p","--port", required=True, type=int, help="Puerto de escucha")
    args = parser.parse_args()

    server = socketserver.ThreadingTCPServer((args.ip, args.port), ThreadedTCPRequestHandler)
    print(f"Servidor B escuchando en {args.ip}:{args.port}")
    server.serve_forever()

if __name__ == "__main__":
    main()