import os
import time

for i in range(3):
    pid = os.fork()

    if pid == 0:
        print(f"Hijo {i+1}: Mi PID es {os.getpid()}. Termino después de dormir.")
        time.sleep(2)
        os._exit(0)
    else:
        print(f"Padre: Creé el hijo {i+1} con PID {pid}")

for _ in range(3):
    pid_hijo, status = os.wait()
    print(f"Padre: El hijo con PID {pid_hijo} terminó con estado {status}")