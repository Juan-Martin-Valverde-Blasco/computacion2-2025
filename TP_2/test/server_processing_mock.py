import socket
import json
import time
import random
import struct  # Para empaquetar longitud en 8 bytes

HOST = "127.0.0.1"
PORT = 9001

def process_request(data):
    """Simula un procesamiento pesado de B"""
    print(f"[B-Mock] Procesando solicitud: {data.decode()}")
    
    # Simulamos un delay aleatorio
    delay = random.uniform(1, 3)
    print(f"[B-Mock] Simulando procesamiento durante {delay:.2f}s")
    time.sleep(delay)
    
    # Resultado simulado
    result = {
        "screenshot": "simulated_base64_image",
        "performance": {
            "load_time_ms": random.randint(50, 200),
            "total_size_kb": random.randint(10, 100),
            "num_requests": random.randint(1, 10)
        },
        "thumbnails": ["sim_thumb1", "sim_thumb2"]
    }
    
    return json.dumps(result).encode()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[B-Mock] Escuchando en {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[B-Mock] Conexión recibida de {addr}")
                data = conn.recv(4096)
                if not data:
                    continue
                
                result_bytes = process_request(data)
                
                # Empaquetamos la longitud en 8 bytes big-endian
                length_prefix = struct.pack(">Q", len(result_bytes))
                conn.sendall(length_prefix + result_bytes)
                
                print(f"[B-Mock] Resultado enviado a A con longitud {len(result_bytes)} bytes")
                
                conn.close()
                print("[B-Mock] Conexión cerrada")

if __name__ == "__main__":
    main()