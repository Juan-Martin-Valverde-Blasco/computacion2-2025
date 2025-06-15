import os
import time

r, w = os.pipe()

pid = os.fork()
if pid == 0:
    os.close(w)
    r_fd = os.fdopen(r)
    print("Hijo leyendo del pipe...")
    linea = r_fd.readline()
    print(f"Hijo recibió: {linea.strip()}")
    r_fd.close()
else:
    os.close(r)
    w_fd = os.fdopen(w, "w")
    print(f"Padre escribiendo en pipe. PID: {os.getpid()}")
    w_fd.write("Mensaje desde padre\n")
    w_fd.flush()
    time.sleep(15)
    w_fd.close()
