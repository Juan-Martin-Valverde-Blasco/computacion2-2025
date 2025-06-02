import os
import sys
import threading

def crear_fifo(path):
    if not os.path.exists(path):
        os.mkfifo(path)

def leer_fifo(path):
    with open(path, 'r') as fifo:
        while True:
            try:
                msg = fifo.readline()
                if msg == '':
                    print("La otra persona se desconectó.")
                    os._exit(0)
                print(f"\nMensaje recibido: {msg.strip()}\n> ", end='', flush=True)
            except Exception as e:
                print(f"Error leyendo FIFO: {e}")
                break

def escribir_fifo(path):
    with open(path, 'w') as fifo:
        while True:
            try:
                msg = input("> ")
                fifo.write(msg + '\n')
                fifo.flush()
                if msg == '/salir':
                    print("Terminando chat...")
                    os._exit(0)
            except Exception as e:
                print(f"Error escribiendo FIFO: {e}")
                break

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['1', '2']:
        print("Uso: python3 chat.py [1|2]")
        sys.exit(1)

    user = sys.argv[1]

    if user == '1':
        fifo_lectura = "/tmp/fifo_2to1"
        fifo_escritura = "/tmp/fifo_1to2"
    else:
        fifo_lectura = "/tmp/fifo_1to2"
        fifo_escritura = "/tmp/fifo_2to1"

    crear_fifo(fifo_lectura)
    crear_fifo(fifo_escritura)

    lector = threading.Thread(target=leer_fifo, args=(fifo_lectura,), daemon=True)
    escritor = threading.Thread(target=escribir_fifo, args=(fifo_escritura,), daemon=True)

    lector.start()
    escritor.start()

    lector.join()
    escritor.join()