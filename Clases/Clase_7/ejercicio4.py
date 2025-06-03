import signal
import time

flag = False

def handler_sigusr1(signum, frame):
    global flag
    flag = True

signal.signal(signal.SIGUSR1, handler_sigusr1)

print("Esperando señal SIGUSR1...")

while True:
    if flag:
        print("Señal SIGUSR1 recibida")
        flag = False
    time.sleep(0.5)
