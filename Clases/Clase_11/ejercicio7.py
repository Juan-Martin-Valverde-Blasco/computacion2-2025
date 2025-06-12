import multiprocessing
import time
from datetime import datetime

def escribir_log(lock, id_proceso):
    for _ in range(3):
        with lock:
            with open("log.txt", "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"Proceso {id_proceso} - {timestamp}\n")
        time.sleep(1)

def main():
    lock = multiprocessing.Lock()
    procesos = []

    for i in range(4):
        p = multiprocessing.Process(target=escribir_log, args=(lock, i))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

if __name__ == "__main__":
    main()
