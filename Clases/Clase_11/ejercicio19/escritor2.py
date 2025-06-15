import multiprocessing
import time
import os

def escribir(id, lock):
    with lock:
        with open("log_concurrente_lock.txt", "a") as f:
            for i in range(10):
                f.write(f"Proceso {id} escribe línea {i}\n")
                time.sleep(0.01)

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    procesos = []
    for i in range(5):
        p = multiprocessing.Process(target=escribir, args=(i, lock))
        p.start()
        procesos.append(p)
    for p in procesos:
        p.join()
#con lock