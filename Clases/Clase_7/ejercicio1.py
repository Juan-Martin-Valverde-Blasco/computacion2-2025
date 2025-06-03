import signal
import time
import sys

flags = {
    'SIGUSR1': False,
    'SIGUSR2': False,
    'SIGINT': False
}

def handle_sigusr1(signum, frame):
    flags['SIGUSR1'] = True
    print("\nSeñal SIGUSR1 recibida.")

def handle_sigusr2(signum, frame):
    flags['SIGUSR2'] = True
    print("\nSeñal SIGUSR2 recibida.")

def handle_sigint(signum, frame):
    flags['SIGINT'] = True
    print("\nSeñal SIGINT recibida.")
    print(f"Estado actual de los flags: {flags}")
    print("Finalizando programa de forma segura...")
    sys.exit(0)

signal.signal(signal.SIGUSR1, handle_sigusr1)
signal.signal(signal.SIGUSR2, handle_sigusr2)
signal.signal(signal.SIGINT, handle_sigint)

contador = 0

print("Esperando señales SIGUSR1, SIGUSR2 y SIGINT (Ctrl+C).")
print("Presiona Ctrl+C para finalizar y mostrar el estado de los flags.")

while True:
    contador += 1
    print(f"Contador: {contador}")
    time.sleep(1)

    if flags['SIGUSR1'] and flags['SIGUSR2']:
        print("Se han recibido SIGUSR1 y SIGUSR2 al menos una vez.")