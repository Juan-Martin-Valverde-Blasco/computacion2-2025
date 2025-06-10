import os
from multiprocessing import Process, Manager, RLock, current_process

def contar_archivos(path, contador, rlock):
    nombre = current_process().name
    for raiz, dirs, archivos in os.walk(path):
        for archivo in archivos:
            ext = os.path.splitext(archivo)[1].lower()
            with rlock:
                if ext in contador:
                    contador[ext] += 1
                else:
                    contador[ext] = 1
            print(f"{nombre} encontró {archivo} ({ext}) en {raiz}")

def explorar_directorio(raiz, contador, rlock):
    subdirectorios = [os.path.join(raiz, d) for d in os.listdir(raiz)
                      if os.path.isdir(os.path.join(raiz, d))]
    procesos = []

    for sub in subdirectorios:
        p = Process(target=contar_archivos, args=(sub, contador, rlock), name=f"Proceso-{os.path.basename(sub)}")
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print(f"{current_process().name} terminó de coordinar la exploración.")

if __name__ == "__main__":
    directorio_raiz = "mi_directorio"  # Cambiar por el directorio a explorar

    with Manager() as manager:
        contador = manager.dict()
        rlock = RLock()

        print("Iniciando exploración del directorio...")
        explorar_directorio(directorio_raiz, contador, rlock)

        print("\nConteo final de archivos por extensión:")
        for ext, cantidad in contador.items():
            print(f"{ext if ext else '[sin extensión]'}: {cantidad}")
