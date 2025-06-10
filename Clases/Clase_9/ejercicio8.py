from multiprocessing import Process, JoinableQueue, Queue, current_process
import time
import random

def worker(entrada, salida):
    while True:
        tarea = entrada.get()
        if tarea is None:
            entrada.task_done()
            break
        time.sleep(random.uniform(0.1, 0.3))
        resultado = tarea ** 2
        print(f"{current_process().name} procesó {tarea} → {resultado}")
        salida.put((tarea, resultado))
        entrada.task_done()

if __name__ == "__main__":
    NUM_WORKERS = 4
    TOTAL_TAREAS = 50

    cola_entrada = JoinableQueue()
    cola_salida = Queue()

    workers = []
    for i in range(NUM_WORKERS):
        p = Process(target=worker, args=(cola_entrada, cola_salida), name=f"Worker-{i+1}")
        p.start()
        workers.append(p)

    for i in range(1, TOTAL_TAREAS + 1):
        cola_entrada.put(i)

    for _ in range(NUM_WORKERS):
        cola_entrada.put(None)

    cola_entrada.join()

    resultados = []
    while not cola_salida.empty():
        resultado = cola_salida.get()
        resultados.append(resultado)

    print("Todos los resultados fueron procesados.")
    print(f"Cantidad total de resultados: {len(resultados)}")
