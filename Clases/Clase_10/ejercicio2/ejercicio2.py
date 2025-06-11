import threading
import queue
import time
import random

entrada = queue.Queue()
salida = queue.Queue()

def procesar_tareas():
    while True:
        tarea = entrada.get()
        if tarea is None:
            entrada.task_done()
            break
        time.sleep(random.uniform(0.5, 2.0))
        mensaje = f"[{threading.current_thread().name}] procesó: {tarea}"
        salida.put(mensaje)
        entrada.task_done()

def registrar_resultados(total_esperado):
    contador = 0
    while True:
        mensaje = salida.get()
        if mensaje == "TERMINAR":
            salida.task_done()
            break
        print(mensaje)
        contador += 1
        print(f"Tareas completadas: {contador}/{total_esperado}")
        salida.task_done()

def main():
    with open("tareas.txt", "r") as archivo:
        tareas = [linea.strip() for linea in archivo if linea.strip()]

    total = len(tareas)
    for tarea in tareas:
        entrada.put(tarea)

    num_procesadores = 4
    for _ in range(num_procesadores):
        entrada.put(None)

    inicio = time.time()

    procesadores = []
    for i in range(num_procesadores):
        hilo = threading.Thread(target=procesar_tareas, name=f"Procesador-{i+1}")
        procesadores.append(hilo)
        hilo.start()

    registrador = threading.Thread(target=registrar_resultados, args=(total,), name="Registrador")
    registrador.start()

    entrada.join()
    salida.put("TERMINAR")
    registrador.join()

    for hilo in procesadores:
        hilo.join()

    fin = time.time()
    print(f"\nTodas las tareas fueron procesadas en {fin - inicio:.2f} segundos.")

if __name__ == "__main__":
    main()
