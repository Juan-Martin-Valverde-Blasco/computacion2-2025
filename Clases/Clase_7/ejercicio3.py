import multiprocessing
import signal
import time
import sys

def proceso_emisor(q):
    mensajes = ["Mensaje 1", "Mensaje 2", "Mensaje 3", "Mensaje 4", "Mensaje 5"]
    for msg in mensajes:
        q.put(msg)
        print(f"[Emisor] Enviado: {msg}")
        time.sleep(1)
    q.put(None)
    print("[Emisor] Finalizó el envío de mensajes.")

def proceso_receptor(q):
    while True:
        msg = q.get()
        if msg is None:
            print("[Receptor] Señal de terminación recibida. Saliendo...")
            break
        print(f"[Receptor] Recibido: {msg}")

def manejador_sigint(signum, frame):
    print("\nSIGINT recibida. Terminando procesos...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, manejador_sigint)

    cola = multiprocessing.Queue()

    emisor = multiprocessing.Process(target=proceso_emisor, args=(cola,))
    receptor = multiprocessing.Process(target=proceso_receptor, args=(cola,))

    emisor.start()
    receptor.start()

    try:
        emisor.join()
        receptor.join()
    except KeyboardInterrupt:
        print("\nInterrupción detectada en el proceso principal.")
        emisor.terminate()
        receptor.terminate()
        emisor.join()
        receptor.join()
    print("Programa finalizado limpiamente.")
