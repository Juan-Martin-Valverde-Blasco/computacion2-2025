from multiprocessing import Process, Condition, Value, Lock, current_process
import time
import random

class ReusableBarrier:
    def __init__(self, n):
        self.n = n
        self.count = Value('i', 0)
        self.generation = Value('i', 0)
        self.lock = Lock()
        self.cond = Condition(self.lock)

    def wait_on_barrier(self):
        with self.cond:
            gen = self.generation.value
            self.count.value += 1
            print(f"{current_process().name} llegó a la barrera (generación {gen})")

            if self.count.value == self.n:
                self.count.value = 0
                self.generation.value += 1
                self.cond.notify_all()
                print(f"{current_process().name} libera la barrera (todos llegaron)")
            else:
                while gen == self.generation.value:
                    self.cond.wait()
            print(f"{current_process().name} cruza la barrera (generación {self.generation.value})")

def tarea(barrier, rondas):
    for ronda in range(rondas):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"{current_process().name} trabajando en ronda {ronda}")
        barrier.wait_on_barrier()

if __name__ == "__main__":
    N = 5
    RONDAS = 3
    barrier = ReusableBarrier(N)
    procesos = []

    for i in range(N):
        p = Process(target=tarea, args=(barrier, RONDAS), name=f"Proceso-{i+1}")
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Todos los procesos completaron todas las rondas.")
