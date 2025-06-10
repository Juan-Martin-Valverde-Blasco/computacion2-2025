from multiprocessing import Process, BoundedSemaphore, Lock, current_process
import time
import random

CAPACIDAD_BUFFER = 5
ITEMS_A_PRODUCIR = 10

def productor(buffer, lock):
    for i in range(ITEMS_A_PRODUCIR):
        time.sleep(random.uniform(0.1, 0.5))
        buffer.release()
        print(f"{current_process().name} produjo el ítem {i+1}")

    # Error intencional: un release de más
    buffer.release()
    print(f"{current_process().name} hizo un release extra (ERROR INTENCIONAL)")

def consumidor(buffer, lock):
    for i in range(ITEMS_A_PRODUCIR):
        buffer.acquire()
        time.sleep(random.uniform(0.1, 0.4))
        print(f"{current_process().name} consumió un ítem {i+1}")

if __name__ == "__main__":
    buffer = BoundedSemaphore(CAPACIDAD_BUFFER)
    lock = Lock()

    p = Process(target=productor, args=(buffer, lock), name="Productor")
    c = Process(target=consumidor, args=(buffer, lock), name="Consumidor")

    p.start()
    c.start()

    p.join()
    c.join()

    print("Ejecución finalizada.")
