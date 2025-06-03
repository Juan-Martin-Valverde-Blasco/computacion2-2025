import multiprocessing
import signal
import time
import os
import sys

def hijo():
    flag_usr1 = False
    flag_usr2 = False
    terminar = False

    def handler_sigusr1(signum, frame):
        nonlocal flag_usr1
        flag_usr1 = True

    def handler_sigusr2(signum, frame):
        nonlocal flag_usr2
        flag_usr2 = True

    def handler_sigint(signum, frame):
        nonlocal terminar
        print("\nSIGINT recibida. Terminando proceso hijo...")
        terminar = True

    signal.signal(signal.SIGUSR1, handler_sigusr1)
    signal.signal(signal.SIGUSR2, handler_sigusr2)
    signal.signal(signal.SIGINT, handler_sigint)

    print(f"Proceso hijo PID {os.getpid()} esperando señales...")

    while not terminar:
        if flag_usr1 and flag_usr2:
            print("Señales sincronizadas recibidas")
            flag_usr1 = False
            flag_usr2 = False
        time.sleep(0.5)

    print("Proceso hijo finalizado limpiamente.")

def padre(pid_hijo):
    print(f"Proceso padre PID {os.getpid()} enviando señales al hijo PID {pid_hijo}")
    señales = [signal.SIGUSR1, signal.SIGUSR2]

    try:
        while True:
            for sig in señales:
                os.kill(pid_hijo, sig)
                print(f"Señal {sig.name} enviada al hijo")
                time.sleep(2)
    except KeyboardInterrupt:
        print("\nSIGINT recibida en proceso padre. Terminando...")

if __name__ == "__main__":
    proceso_hijo = multiprocessing.Process(target=hijo)
    proceso_hijo.start()
    try:
        padre(proceso_hijo.pid)
    except KeyboardInterrupt:
        pass
    proceso_hijo.join()
    print("Programa finalizado.")
