import os
import time

def hijo(id_hijo):
    print(f"Hijo {id_hijo} iniciado - PID: {os.getpid()} - PPID: {os.getppid()}")
    time.sleep(10)

def main():
    for i in range(2):
        pid = os.fork()
        if pid == 0:
            hijo(i)
            os._exit(0)
    time.sleep(10)

if __name__ == "__main__":
    main()
