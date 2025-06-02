import os
import signal
import sys

fifo_path = "/tmp/log_fifo"
log_file_path = "eventos.log"

def cerrar_archivo(signum, frame):
    global log_file
    print("\nTerminando y cerrando archivo log...")
    if log_file:
        log_file.close()
    sys.exit(0)

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

log_file = open(log_file_path, "a")

signal.signal(signal.SIGINT, cerrar_archivo)
signal.signal(signal.SIGTERM, cerrar_archivo)

try:
    with open(fifo_path, 'r') as fifo:
        while True:
            linea = fifo.readline()
            if linea == '':
                # EOF o cierre del escritor
                break
            log_file.write(linea)
            log_file.flush()
            print(f"Log guardado: {linea.strip()}")
except Exception as e:
    print(f"Error en logger_reader.py: {e}")
finally:
    log_file.close()
