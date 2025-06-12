fifo_path = "/tmp/mi_fifo"

with open(fifo_path, "r") as fifo:
    for linea in fifo:
        print(f"[Receptor] Recibido: {linea.strip()}")
