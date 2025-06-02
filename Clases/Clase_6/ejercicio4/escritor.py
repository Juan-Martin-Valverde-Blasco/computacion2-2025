import os
import time

fifo_path = "/tmp/test_fifo"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

try:
    with open(fifo_path, 'w') as fifo:
        for i in range(1, 11):
            msg = f"Mensaje {i}\n"
            fifo.write(msg)
            fifo.flush()
            print(f"Escrito: {msg.strip()}")
            time.sleep(0.5)
except Exception as e:
    print(f"Error en writer.py: {e}")
