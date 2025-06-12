import os
import time

fifo_path = "/tmp/mi_fifo"

with open(fifo_path, "w") as fifo:
    for i in range(5):
        mensaje = f"Mensaje {i}"
        fifo.write(mensaje + "\n")
        fifo.flush()
        time.sleep(1)
