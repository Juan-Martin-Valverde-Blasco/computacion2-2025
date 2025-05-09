import os
import time

def main():
    try:
        pid = os.fork()
    except OSError as e:
        print(f"Error al crear proceso hijo: {e}")
        return

    if pid == 0:
        
        print(f"[HIJO] PID: {os.getpid()}, PPID inicial: {os.getppid()}")
        time.sleep(3)  
        print(f"[HIJO] Ahora soy huérfano. Nuevo PPID: {os.getppid()}")
        print(f"[HIJO] Ejecutando comando externo sin control del padre...")
        os.execvp("ls", ["ls", "-l", "/"])  
    else:
        print(f"[PADRE] PID: {os.getpid()}. Finalizando inmediatamente.")
        os._exit(0)

if __name__ == "__main__":
    main()
