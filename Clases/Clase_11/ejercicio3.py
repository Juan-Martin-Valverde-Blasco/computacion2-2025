import os
import time

def main():
    pid = os.fork()
    if pid == 0:
        time.sleep(20)
        print(f"[Hijo] PID: {os.getpid()} - Nuevo PPID: {os.getppid()}")
        os._exit(0)
    else:
        print(f"[Padre] PID: {os.getpid()} - Creó hijo con PID: {pid}")
        os._exit(0)

if __name__ == "__main__":
    main()
