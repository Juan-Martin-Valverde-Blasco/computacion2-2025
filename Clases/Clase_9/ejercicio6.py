from multiprocessing import Process, Event, current_process
import time
import random

def proceso_a(evento_ab):
    print(f"{current_process().name} comienza su trabajo.")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"{current_process().name} terminó su trabajo. Activa a B.")
    evento_ab.set()

def proceso_b(evento_ab, evento_bc):
    print(f"{current_process().name} esperando a A...")
    evento_ab.wait()
    print(f"{current_process().name} comienza su trabajo.")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"{current_process().name} terminó su trabajo. Activa a C.")
    evento_bc.set()

def proceso_c(evento_bc):
    print(f"{current_process().name} esperando a B...")
    evento_bc.wait()
    print(f"{current_process().name} comienza su trabajo.")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"{current_process().name} terminó su trabajo.")

if __name__ == "__main__":
    evento_ab = Event()
    evento_bc = Event()

    a = Process(target=proceso_a, args=(evento_ab,), name="Proceso-A")
    b = Process(target=proceso_b, args=(evento_ab, evento_bc), name="Proceso-B")
    c = Process(target=proceso_c, args=(evento_bc,), name="Proceso-C")

    c.start()
    b.start()
    a.start()

    a.join()
    b.join()
    c.join()

    print("Pipeline finalizado.")
