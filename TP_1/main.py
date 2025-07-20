import multiprocessing
import time
import random
from datetime import datetime
import statistics
import os
import signal

# --- Generador de señales biométricas ---
def generador(pipe_a, pipe_b, pipe_c):
    for i in range(60):
        muestra = {
            "timestamp": datetime.now().isoformat(),
            "Frecuencia Cardiaca": random.randint(60, 180),
            "Presion Sanguinea": [random.randint(110, 180), random.randint(70, 110)],
            "Oxigeno en Sangre": random.randint(90, 100)
        }

        pipe_a.send(muestra)
        pipe_b.send(muestra)
        pipe_c.send(muestra)

        print(f"[Generador] Enviada muestra {i+1}: {muestra}")
        time.sleep(1)

    pipe_a.send("FIN")
    pipe_b.send("FIN")
    pipe_c.send("FIN")

# --- Analizador general (frecuencia, presión u oxígeno) ---
def analizador(nombre, campo, pipe, queue):
    ventana = []

    while True:
        data = pipe.recv()
        if data == "FIN":
            break

        if campo == "Presion Sanguinea":
            valor = data["Presion Sanguinea"][0]  # presión sistólica
        else:
            valor = data[campo]

        ventana.append(valor)
        if len(ventana) > 30:
            ventana.pop(0)

        media = statistics.mean(ventana)
        desv = statistics.stdev(ventana) if len(ventana) > 1 else 0.0

        resultado = {
            "tipo": campo,
            "timestamp": data["timestamp"],
            "media": round(media, 2),
            "desv": round(desv, 2)
        }

        queue.put(resultado)
        print(f"[{nombre}] Resultado: {resultado}")

# --- Proceso principal ---
def main():
    # Pipes (unidireccionales)
    a_principal, a_analizador = multiprocessing.Pipe()
    b_principal, b_analizador = multiprocessing.Pipe()
    c_principal, c_analizador = multiprocessing.Pipe()

    # Queues de salida (para el verificador futuro)
    queue_a = multiprocessing.Queue()
    queue_b = multiprocessing.Queue()
    queue_c = multiprocessing.Queue()

    # Procesos analizadores
    proc_a = multiprocessing.Process(target=analizador, args=("Analizador A", "Frecuencia Cardiaca", a_analizador, queue_a))
    proc_b = multiprocessing.Process(target=analizador, args=("Analizador B", "Presion Sanguinea", b_analizador, queue_b))
    proc_c = multiprocessing.Process(target=analizador, args=("Analizador C", "Oxigeno en Sangre", c_analizador, queue_c))

    proc_a.start()
    proc_b.start()
    proc_c.start()

    # Proceso generador
    generador(a_principal, b_principal, c_principal)

    proc_a.join()
    proc_b.join()
    proc_c.join()

    print("\n[Principal] Todos los procesos terminaron correctamente.")

if __name__ == "__main__":
    main()