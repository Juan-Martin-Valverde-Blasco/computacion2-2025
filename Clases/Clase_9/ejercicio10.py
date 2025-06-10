from multiprocessing import Process, Array, Lock
import random

def worker(bins, lock, M):
    for _ in range(M):
        num = random.randint(0, 99)
        bin_index = num // 10
        with lock:
            bins[bin_index] += 1

if __name__ == "__main__":
    N = 5      # cantidad de procesos
    M = 1000   # números generados por proceso
    bins = Array('i', 10)
    lock = Lock()

    procesos = []
    for _ in range(N):
        p = Process(target=worker, args=(bins, lock, M))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Histograma final (bins de 0-9, 10-19, ..., 90-99):")
    for i, count in enumerate(bins):
        print(f"{i*10:02d}-{i*10+9:02d}: {count}")
    print("Todos los procesos han finalizado.")
    
    