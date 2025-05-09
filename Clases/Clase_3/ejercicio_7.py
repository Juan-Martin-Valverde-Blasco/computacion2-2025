import os
import time

def tarea_hijo(n):
    print(f"Hijo: ({n}) PID: ({os.getpid()}), PPID: ({os.getppid()})")
    print(f"Hijo: ({n}) Realizando tarea breve...")
    time.sleep(1)
    print(f"Hijo: ({n}) Tarea finalizada.")
    os._exit(0)

def main():
    hijos = []

    print("Padre: Creando 3 hijos en paralelo...")

    for i in range(1, 4):
        
        try:
            pid = os.fork()
        
        except OSError as e:
            print(f"Padre: Error al crear el hijo {i}: {e}")
            continue

        if pid == 0:
            tarea_hijo(i)

        else:
            hijos.append(pid)


    for pid in hijos:
        os.waitpid(pid, 0)
        print(f"Padre: Hijo con PID ({pid}) ha finalizado.")

    print("Padre: Todos los hijos han terminado.")

if __name__ == "__main__":
    main()
