import os
import time

def main():
    try:
        pid = os.fork()
    except OSError as e:
        print(f"Error al crear el hijo: {e}")
        return

    if pid == 0:
        
        print(f"Hijo: PID: ({os.getpid()}), PPID inicial: ({os.getppid()})")
        print("Hijo: Durmiendo 5 segundos para esperar que el padre termine...")
        time.sleep(5)
        print(f"Hijo: PPID después de que el padre termina: ({os.getppid()})")
        print("Hijo: Finalizando.")
    else:
        
        print(f"Padre: PID: ({os.getpid()}), ha creado al hijo con PID ({pid}). Terminando ahora.")
        os._exit(0)

if __name__ == "__main__":
    main()
