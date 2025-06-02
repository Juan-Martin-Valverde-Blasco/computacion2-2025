import os
import time
import random

fifo_path = "/tmp/log_fifo"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

eventos = [
    "Inicio de sesión",
    "Error en módulo X",
    "Usuario desconectado",
    "Archivo guardado",
    "Conexión perdida",
    "Reconexión exitosa"
]

try:
    with open(fifo_path, 'w') as fifo:
        for i in range(20):
            evento = random.choice(eventos)
            mensaje = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Evento: {evento}\n"
            fifo.write(mensaje)
            fifo.flush()
            print(f"Log enviado: {mensaje.strip()}")
            time.sleep(random.uniform(0.5, 1.5))
except Exception as e:
    print(f"Error en logger_writer.py: {e}")
