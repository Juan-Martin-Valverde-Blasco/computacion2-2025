import os
import time

for i in range(3):
    pid = os.fork()

    if pid == 0:
        print(f"Hijo {i+1}: Mi PID es {os.getpid()} y el de mi padre es {os.getppid()}")
        os._exit(0)  

    else:
        print(f"Padre: Creé un hijo {i+1} con PID {pid}")
        time.sleep(1)  