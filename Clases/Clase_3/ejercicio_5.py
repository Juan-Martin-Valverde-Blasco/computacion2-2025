import os
import time

def main():
    try:
        pid = os.fork()
    except OSError as e:
        print(f"Error al crear el hijo: {e}")
        return

    if pid == 0:
        
        print(f"Hijo PID: ({os.getpid()}) finalizando inmediatamente.")
        os._exit(0)
    else:

        print(f"Padre Hijo creado con PID ({pid}). Esperando 10 segundos antes de recogerlo...")
        time.sleep(10)
        print(f"Padre Ahora recolectando el estado del hijo.")
        os.waitpid(pid, 0)
        print(f"Padre Hijo ({pid}) recolectado.")
        
if __name__ == "__main__":
    main()