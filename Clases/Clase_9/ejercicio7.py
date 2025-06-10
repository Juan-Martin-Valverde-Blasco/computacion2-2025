from multiprocessing import Process, Barrier, current_process
import time
import random

def corredor(barrier, vueltas):
    nombre = current_process().name

    print(f"{nombre} listo en la línea de salida.")
    barrier.wait()
    print(f"{nombre} ¡comienza la carrera!")

    for vuelta in range(1, vueltas + 1):
        tiempo = random.uniform(0.5, 1.5)
        time.sleep(tiempo)
        print(f"{nombre} completó la vuelta {vuelta} en {tiempo:.2f} segundos.")
        barrier.wait()
        if vuelta < vueltas:
            print(f"{nombre} espera a los demás para comenzar la vuelta {vuelta + 1}.")

    print(f"{nombre} terminó la carrera.")

if __name__ == "__main__":
    NUM_CORREDORES = 5
    VUELTAS = 3
    barrier = Barrier(NUM_CORREDORES)

    procesos = []

    for i in range(NUM_CORREDORES):
        p = Process(target=corredor, args=(barrier, VUELTAS), name=f"Corredor-{i+1}")
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("La carrera ha finalizado.")
