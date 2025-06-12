import os
import argparse
import time
import random
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description="Gestor de procesos hijos")
    parser.add_argument('--num', type=int, required=True, help='Cantidad de procesos hijos a crear')
    parser.add_argument('--verbose', action='store_true', help='Activar salida detallada')

    args = parser.parse_args()

    print(f"[Padre] PID: {os.getpid()} - Creando {args.num} procesos hijos...")

    hijos = []

    for i in range(args.num):
        pid = os.fork()
        if pid == 0:
            duracion = random.randint(1, 5)
            if args.verbose:
                print(f"[Hijo {i}] PID: {os.getpid()}, PPID: {os.getppid()} - Durmiendo {duracion} segundos")
            time.sleep(duracion)
            if args.verbose:
                print(f"[Hijo {i}] PID: {os.getpid()} - Finalizando")
            os._exit(0)
        else:
            hijos.append(pid)

    for pid in hijos:
        os.waitpid(pid, 0)

    print(f"[Padre] Todos los procesos hijos han terminado.")
    print(f"[Padre] Árbol de procesos (pstree -p):")
    subprocess.run(["pstree", "-p", str(os.getpid())])

if __name__ == "__main__":
    main()
