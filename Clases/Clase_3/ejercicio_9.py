import os

def es_zombi(pid):
    try:
        with open(f"/proc/{pid}/status", "r") as f:
            status_info = f.readlines()

        estado = None
        ppid = None
        nombre = None

        for linea in status_info:
            if linea.startswith("State:"):
                estado = linea.split()[1]
            elif linea.startswith("PPid:"):
                ppid = linea.split()[1]
            elif linea.startswith("Name:"):
                nombre = linea.split()[1]

        return estado == "Z", ppid, nombre

    except FileNotFoundError:
        return False, None, None  
    except Exception as e:
        print(f"Error al leer /proc/{pid}/status: {e}")
        return False, None, None

def main():
    print(f"{'PID':>6} {'PPID':>6} {'Nombre':<20}")
