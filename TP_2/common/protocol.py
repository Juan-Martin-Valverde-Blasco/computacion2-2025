import struct
import json

LEN_HEADER = 4

def pack_message(obj: dict) -> bytes:
    payload = json.dumps(obj, ensure_ascii=False).encode('utf-8')
    return struct.pack('>I', len(payload)) + payload

def recv_exact(sock, n) -> bytes:
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            raise ConnectionError("Connection closed while reading")
        data += chunk
    return data

def unpack_message_from_socket(sock) -> dict:
    header = recv_exact(sock, LEN_HEADER)
    (length,) = struct.unpack('>I', header)
    payload = recv_exact(sock, length)
    return json.loads(payload.decode('utf-8'))