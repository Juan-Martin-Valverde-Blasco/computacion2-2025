import time
import os
import signal
import sys

def terminar(sig, frame):
    print(f"Recibida señal {sig}. Terminando proceso PID {os.getpid()}")
    sys.exit(0)

signal.signal(signal.SIGTERM, terminar)

print(f"Proceso iniciado. PID: {os.getpid()}")
time.sleep(10)
print("Proceso completado.")
