import signal
import os
import time

def manejador_sigusr1(signum, frame):
    print(f"PID {os.getpid()}: Señal SIGUSR1 recibida")

def manejador_sigusr2(signum, frame):
    print(f"PID {os.getpid()}: Señal SIGUSR2 recibida")

signal.signal(signal.SIGUSR1, manejador_sigusr1)
signal.signal(signal.SIGUSR2, manejador_sigusr2)

print(f"Receptor iniciado. PID: {os.getpid()}")
while True:
    signal.pause()
