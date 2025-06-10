import random
import time
from multiprocessing import Process, Semaphore, Lock, Value, current_process

TOTAL_ASIENTOS = 50
TOTAL_PROCESOS = 100

def reservar_asientos(semaforo, lock, asientos_restantes, reservas_exitosas):
    nombre = current_process().name
    cantidad_deseada = random.randint(1, 4)

    with lock:
        if asientos_restantes.value >= cantidad_deseada:
            for _ in range(cantidad_deseada):
                semaforo.acquire()
            asientos_restantes.value -= cantidad_deseada
            reservas_exitosas.value += cantidad_deseada
            print(f"{nombre} reservó {cantidad_deseada} asientos. Quedan: {asientos_restantes.value}")
        else:
            print(f"{nombre} intentó reservar {cantidad_deseada} asientos pero solo quedan {asientos_restantes.value}. No se pudo completar.")

if __name__ == "__main__":
    semaforo = Semaphore(TOTAL_ASIENTOS)
    lock = Lock()
    asientos_restantes = Value("i", TOTAL_ASIENTOS)
    reservas_exitosas = Value("i", 0)

    procesos = []

    for i in range(TOTAL_PROCESOS):
        p = Process(target=reservar_asientos, args=(semaforo, lock, asientos_restantes, reservas_exitosas), name=f"Cliente-{i+1}")
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print(f"\nTotal de asientos reservados: {reservas_exitosas.value}")
    print(f"Asientos sin reservar: {asientos_restantes.value}")
    print("Todos los procesos han finalizado.")