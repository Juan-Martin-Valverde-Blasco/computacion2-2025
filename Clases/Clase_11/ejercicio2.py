import os
import time

def main():
    pid = os.fork()
    if pid == 0:
        os._exit(0)
    else:
        print(f"[Padre] PID: {os.getpid()} - PID hijo: {pid} creado y terminó.")
        print("[Padre] Esperando 10 segundos antes de recolectar el estado del hijo...")
        time.sleep(10)
        os.waitpid(pid, 0)
        print("[Padre] Estado del hijo recolectado, proceso zombi eliminado.")

if __name__ == "__main__":
    main()
