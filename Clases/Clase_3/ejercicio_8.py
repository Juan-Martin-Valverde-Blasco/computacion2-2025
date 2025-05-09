import os
import time
import random

def atender_cliente(cliente_id):
    print(f"[HIJO] Atendiendo al cliente {cliente_id} (PID: {os.getpid()}, PPID: {os.getppid()})")
    tiempo = random.randint(1, 3)
    time.sleep(tiempo)
    print(f"[HIJO] Cliente {cliente_id} atendido en {tiempo} segundos.")
    os._exit(0)

def main():
    num_clientes = 5
    hijos = []

    print("[SERVIDOR] Iniciando atención de clientes...")

    for cliente_id in range(1, num_clientes + 1):
        try:
            pid = os.fork()
        except OSError as e:
            print(f"[SERVIDOR] Error al crear proceso para cliente {cliente_id}: {e}")
            continue

        if pid == 0:
            atender_cliente(cliente_id)
        else:
            hijos.append(pid)


    for pid in hijos:
        os.waitpid(pid, 0)
        print(f"[SERVIDOR] Cliente atendido por proceso {pid} ha finalizado.")

    print("[SERVIDOR] Todos los clientes han sido atendidos.")

if __name__ == "__main__":
    main()
