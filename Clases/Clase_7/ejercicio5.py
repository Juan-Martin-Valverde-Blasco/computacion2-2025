import signal
import time

flag_usr1 = False
flag_usr2 = False

def handler_sigusr1(signum, frame):
    global flag_usr1
    flag_usr1 = True

def handler_sigusr2(signum, frame):
    global flag_usr2
    flag_usr2 = True

signal.signal(signal.SIGUSR1, handler_sigusr1)
signal.signal(signal.SIGUSR2, handler_sigusr2)

print("Esperando señales SIGUSR1 y SIGUSR2...")

while True:
    if flag_usr1 and flag_usr2:
        print("Ambas señales recibidas")
        flag_usr1 = False
        flag_usr2 = False
    time.sleep(0.5)
