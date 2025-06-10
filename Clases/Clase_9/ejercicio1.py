from multiprocessing import Process, Lock, current_process
from datetime import datetime
import time
import random

def obtener_timestamp():
    return datetime.now().strftime("[%H:%M:%S]")

def tarea_log(lock):
    nombre = current_process().name
    for _ in range(3):
        timestamp = obtener_timestamp()
        mensaje = f"{timestamp} {nombre} (PID {current_process().pid}) escribió una línea.\n"
        print(f"{timestamp} {nombre} quiere acceso al log.")
        with lock:
            with open("log.txt", "a") as archivo:
                archivo.write(mensaje)
            print(f"{timestamp} {nombre} accedió y escribió en el log.")
        time.sleep(random.uniform(0.3, 1.2))

if __name__ == "__main__":
    lock = Lock()
    procesos = []

    for i in range(5):
        p = Process(target=tarea_log, args=(lock,), name=f"Worker-{i+1}")
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print(f"{obtener_timestamp()} Todos los procesos terminaron.")
