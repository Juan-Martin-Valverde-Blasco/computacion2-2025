import signal
import os
import time

def manejador(sig, frame):
    print(f"Señal recibida: {sig} - PID: {os.getpid()}")

signal.signal(signal.SIGUSR1, manejador)

print(f"Esperando señal SIGUSR1... PID: {os.getpid()}")

while True:
    time.sleep(1)
