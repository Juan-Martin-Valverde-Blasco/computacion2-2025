import os

fifo_path = "/tmp/test_fifo"

try:
    if os.path.exists(fifo_path):
        print(f"El FIFO ya existe en {fifo_path}")
    else:
        os.mkfifo(fifo_path)
        print(f"FIFO creado en {fifo_path}")
finally:
    try:
        if os.path.exists(fifo_path):
            os.remove(fifo_path)
            print(f"FIFO eliminado en {fifo_path}")
    except OSError as e:
        print(f"Error al eliminar el FIFO: {e}")