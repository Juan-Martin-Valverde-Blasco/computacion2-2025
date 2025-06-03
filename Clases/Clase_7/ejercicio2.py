import threading
import signal
import time
import sys

evento_hilo1 = threading.Event()
evento_hilo2 = threading.Event()
terminar = threading.Event()

def trabajador(id_hilo, evento):
    while not terminar.is_set():
        evento.wait()
        if terminar.is_set():
            break
        print(f"Hilo {id_hilo} activado.")
        for i in range(1, 6):
            print(f"Hilo {id_hilo} contando: {i}")
            time.sleep(1)
            if terminar.is_set():
                break
        print(f"Hilo {id_hilo} tarea finalizada.")
        evento.clear()

def handle_sigusr1(signum, frame):
    print("\nSIGUSR1 recibida. Activando hilo 1.")
    evento_hilo1.set()

def handle_sigusr2(signum, frame):
    print("\nSIGUSR2 recibida. Activando hilo 2.")
    evento_hilo2.set()

def handle_sigint(signum, frame):
    print("\nSIGINT recibida. Terminando programa...")
    terminar.set()
    evento_hilo1.set()
    evento_hilo2.set()
    hilo1.join()
    hilo2.join()
    print("Hilos terminados. Saliendo.")
    sys.exit(0)

signal.signal(signal.SIGUSR1, handle_sigusr1)
signal.signal(signal.SIGUSR2, handle_sigusr2)
signal.signal(signal.SIGINT, handle_sigint)

hilo1 = threading.Thread(target=trabajador, args=(1, evento_hilo1))
hilo2 = threading.Thread(target=trabajador, args=(2, evento_hilo2))

hilo1.start()
hilo2.start()

print("Programa en ejecución. Esperando señales SIGUSR1, SIGUSR2 y SIGINT (Ctrl+C).")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    handle_sigint(None, None)
