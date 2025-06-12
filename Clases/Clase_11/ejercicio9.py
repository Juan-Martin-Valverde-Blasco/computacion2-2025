import multiprocessing
import time
import random
import os

def zona_critica(sem, id_proceso):
    print(f"Proceso {id_proceso} esperando acceso (PID: {os.getpid()})")
    with sem:
        print(f"Proceso {id_proceso} ENTRA a la zona crítica")
        time.sleep(random.uniform(1, 3))
        print(f"Proceso {id_proceso} SALE de la zona crítica")

def main():
    sem = multiprocessing.Semaphore(3)
    procesos = []

    for i in range(10):
        p = multiprocessing.Process(target=zona_critica, args=(sem, i))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

if __name__ == "__main__":
    main()
