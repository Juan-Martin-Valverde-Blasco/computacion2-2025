import multiprocessing
import time
import os

def escribir(id):
    with open("log_concurrente.txt", "a") as f:
        for i in range(10):
            f.write(f"Proceso {id} escribe línea {i}\n")
            time.sleep(0.01)

if __name__ == "__main__":
    procesos = []
    for i in range(5):
        p = multiprocessing.Process(target=escribir, args=(i,))
        p.start()
        procesos.append(p)
    for p in procesos:
        p.join()
 #sin lock