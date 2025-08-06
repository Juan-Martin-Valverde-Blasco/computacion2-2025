import statistics

def analizador(tipo_dato, pipe_entrada, queue_salida):
    ventana = []
    while True:
        data = pipe_entrada.recv()
        if data == "FIN":
            queue_salida.put("FIN")
            break

        if tipo_dato == "presion_arterial":
            valor = data["presion_arterial"][0]  # presión sistólica
        else:
            valor = data[tipo_dato]

        ventana.append(valor)
        if len(ventana) > 30:
            ventana.pop(0)

        media = statistics.mean(ventana)
        desv = statistics.stdev(ventana) if len(ventana) > 1 else 0.0

        resultado = {
            "tipo": tipo_dato,
            "timestamp": data["timestamp"],
            "media": round(media, 2),
            "desv": round(desv, 2)
        }

        queue_salida.put(resultado)
