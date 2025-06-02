import os

fifo_path = "/tmp/test_fifo"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

try:
    with open(fifo_path, 'r') as fifo:
        while True:
            line = fifo.readline()
            if line == '':
                break
            print(f"Leído: {line.strip()}")
except Exception as e:
    print(f"Error en reader.py: {e}")
