fifo_path = "/tmp/test_fifo"

try:
    with open(fifo_path, 'r') as fifo:
        while True:
            line = fifo.readline()
            if line == '':
                break
            print(f"Reader 1 leyó: {line.strip()}")
except Exception as e:
    print(f"Error en reader1.py: {e}")
