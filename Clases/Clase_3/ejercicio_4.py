import os
import time

def crear_hijo(numero):
    try:
        pid = os.fork()
    except OSError as e:
        print(f"Error al crear el hijo {numero}: {e}")
        return -1

    if pid == 0:
        
        print(f"Hijo ({numero}) PID: ({os.getpid()}), PPID: ({os.getppid()})")
        print(f"Hijo ({numero}) Realizando tarea mínima...")
        time.sleep(1)
        print(f"Hijo ({numero}) Tarea finalizada.")
        os._exit(0)  
    else:
        
        os.waitpid(pid, 0)  
        print(f"Padre Hijo {numero} finalizado.")
        return pid

def main():
    print("[Padre: Iniciando creación secuencial de hijos.")
    
    crear_hijo(1) 
    crear_hijo(2) 

    print("Padre: Ambos hijos han terminado.")

if __name__ == "__main__":
    main()
