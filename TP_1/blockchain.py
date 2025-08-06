import hashlib
import json
import os
from datetime import datetime

def calcular_hash(bloque):
    bloque_string = json.dumps(bloque, sort_keys=True).encode()
    return hashlib.sha256(bloque_string).hexdigest()

def crear_bloque(index, datos, hash_anterior):
    bloque = {
        "index": index,
        "timestamp": datetime.now().isoformat(),
        "datos": datos,
        "hash_anterior": hash_anterior
    }
    bloque["hash"] = calcular_hash(bloque)
    return bloque

def cargar_blockchain(path="blockchain.json"):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def guardar_blockchain(blockchain, path="blockchain.json"):
    with open(path, "w") as f:
        json.dump(blockchain, f, indent=4)

def validar_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        bloque_actual = blockchain[i]
        bloque_anterior = blockchain[i-1]

        if bloque_actual["hash_anterior"] != bloque_anterior["hash"]:
            return False
        copia = dict(bloque_actual)
        copia.pop("hash")
        if calcular_hash(copia) != bloque_actual["hash"]:
            return False
    return True

def agregar_resultados_a_blockchain(resultados):
    blockchain = cargar_blockchain()

    if not blockchain:
        genesis = crear_bloque(0, {"mensaje": "Bloque génesis"}, "0")
        blockchain.append(genesis)

    for resultado in resultados:
        index = len(blockchain)
        hash_anterior = blockchain[-1]["hash"]
        nuevo_bloque = crear_bloque(index, resultado, hash_anterior)
        blockchain.append(nuevo_bloque)

    guardar_blockchain(blockchain)

    print("\nBlockchain actualizada.")
    if validar_blockchain(blockchain):
        print("La cadena es válida.")
    else:
        print("La cadena es inválida.")

    return blockchain
