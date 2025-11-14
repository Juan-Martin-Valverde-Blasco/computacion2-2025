# server_processing.py
import socket
import json
import time

HOST = '127.0.0.1'
PORT = 9001

def send_msg(conn, data):
    encoded = json.dumps(data).encode()
    length = len(encoded)
    conn.sendall(length.to_bytes(8, byteorder='big'))  # enviar largo 8 bytes
    conn.sendall(encoded)

def recv_msg(conn):
    raw_len = conn.recv(8)
    if not raw_len:
        return None
    msg_len = int.from_bytes(raw_len, byteorder='big')
    data = b''
    while len(data) < msg_len:
        packet = conn.recv(msg_len - len(data))
        if not packet:
            return None
        data += packet
    return json.loads(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[B] Escuchando en {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[B] Conexión recibida de {addr}")
            request = recv_msg(conn)
            print(f"[B] Procesando solicitud: {request}")
            time.sleep(1.5)  # simular procesamiento
            result = {
                "screenshot": "mock_base64_image",
                "performance": {"load_time_ms": 123, "total_size_kb": 456, "num_requests": 7},
                "thumbnails": []
            }
            send_msg(conn, result)
            print("[B] Resultado enviado y conexión cerrada")
