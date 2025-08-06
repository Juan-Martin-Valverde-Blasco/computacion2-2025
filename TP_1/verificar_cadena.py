import json
import hashlib
import statistics

BLOCKCHAIN_FILE = "blockchain.json"
REPORTE_FILE = "reporte.txt"

def calcular_hash(bloque):
    bloque_copia = dict(bloque)
    bloque_copia.pop("hash", None)
    bloque_string = json.dumps(bloque_copia, sort_keys=True).encode()
    return hashlib.sha256(bloque_string).hexdigest()

def verificar_cadena():
    try:
        with open(BLOCKCHAIN_FILE, "r") as f:
            blockchain = json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo blockchain.json.")
        return

    if len(blockchain) <= 1:
        print("La blockchain solo tiene el bloque génesis. Nada que verificar.")
        return

    # Verificar integridad
    cadena_valida = True
    for i in range(1, len(blockchain)):
        bloque_actual = blockchain[i]
        bloque_anterior = blockchain[i-1]

        if bloque_actual.get("hash_anterior") != bloque_anterior.get("hash"):
            cadena_valida = False
            break

        if calcular_hash(bloque_actual) != bloque_actual["hash"]:
            cadena_valida = False
            break

    print("Integridad de la cadena:", "VÁLIDA" if cadena_valida else "CORRUPTA")

    # Generar reporte
    total_bloques = len(blockchain) - 1
    alertas = 0
    frecuencias = []
    presiones = []
    oxigenos = []

    for bloque in blockchain[1:]:
        datos = bloque.get("datos", {})

        if not isinstance(datos, dict):
            continue

        tipo = datos.get("tipo")
        media = datos.get("media")
        estado = datos.get("estado")

        if estado == "anormal":
            alertas += 1

        if tipo == "frecuencia_cardiaca" and isinstance(media, (int, float)):
            frecuencias.append(media)
        elif tipo == "presion_arterial" and isinstance(media, (int, float)):
            presiones.append(media)
        elif tipo == "oxigeno_sangre" and isinstance(media, (int, float)):
            oxigenos.append(media)

    promedio_frec = round(statistics.mean(frecuencias), 2) if frecuencias else 0
    promedio_pres = round(statistics.mean(presiones), 2) if presiones else 0
    promedio_oxi = round(statistics.mean(oxigenos), 2) if oxigenos else 0

    with open(REPORTE_FILE, "w") as f:
        f.write("=== REPORTE DE BLOCKCHAIN BIOMÉTRICA ===\n")
        f.write(f"Total de bloques (sin génesis): {total_bloques}\n")
        f.write(f"Bloques con alertas: {alertas}\n")
        f.write(f"Promedio frecuencia cardíaca: {promedio_frec}\n")
        f.write(f"Promedio presión arterial: {promedio_pres}\n")
        f.write(f"Promedio oxígeno en sangre: {promedio_oxi}\n")

    print("\nReporte generado en reporte.txt")

if __name__ == "__main__":
    verificar_cadena()
