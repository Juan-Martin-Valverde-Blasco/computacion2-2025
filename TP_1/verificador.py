from blockchain import agregar_resultados_a_blockchain

def verificador(queue_frecuencia, queue_presion, queue_oxigeno, salida_blockchain):
    terminados = 0
    blockchain = []

    while terminados < 3:
        for queue in [queue_frecuencia, queue_presion, queue_oxigeno]:
            if not queue.empty():
                item = queue.get()
                if item == "FIN":
                    terminados += 1
                else:
                    tipo = item["tipo"]
                    media = item["media"]

                    if tipo == "frecuencia_cardiaca":
                        estado = "normal" if 60 <= media <= 100 else "anormal"
                    elif tipo == "presion_arterial":
                        estado = "normal" if 110 <= media <= 140 else "anormal"
                    elif tipo == "oxigeno_sangre":
                        estado = "normal" if media >= 95 else "anormal"
                    else:
                        estado = "desconocido"

                    bloque = {
                        **item,
                        "estado": estado
                    }
                    blockchain.append(bloque)

    agregar_resultados_a_blockchain(blockchain)  # Guarda en disco

    salida_blockchain.put("FIN")  # Avisar que terminó (opcional)
