import os
import sys
import time
import signal

if len(sys.argv) != 2:
    print("Uso: ./emisor.py [PID_receptor]")
    sys.exit(1)

pid_receptor = int(sys.argv[1])

señales = [signal.SIGUSR1, signal.SIGUSR2]

while True:
    for s in señales:
        os.kill(pid_receptor, s)
        print(f"Enviada señal {s} a PID {pid_receptor}")
        time.sleep(2)
