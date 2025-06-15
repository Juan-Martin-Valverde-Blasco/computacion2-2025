import os
import time
import random

def hijo(i):
    duracion = random.randint(1, 5)
    time.sleep(duracion)
    os._exit(i)

def main():
    hijos = []
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            hijo(i)
        else:
            hijos.append(pid)

    finalizados = []
    for _ in hijos:
        pid_terminado, estado = os.waitpid(-1, 0)
        finalizados.append((pid_terminado, os.WEXITSTATUS(estado)))

    print("Orden de finalización:")
    for pid, codigo in finalizados:
        print(f"PID {pid} terminó con código {codigo}")

if __name__ == "__main__":
    main()
