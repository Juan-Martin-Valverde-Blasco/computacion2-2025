import os

def main():
    r, w = os.pipe()

    pid = os.fork()
    if pid == 0:
        os.close(r)
        mensaje = "Hola desde el proceso hijo"
        os.write(w, mensaje.encode())
        os.close(w)
        os._exit(0)
    else:
        os.close(w)
        mensaje_leido = b""
        while True:
            dato = os.read(r, 1024)
            if not dato:
                break
            mensaje_leido += dato
        os.close(r)
        print(f"[Padre] Mensaje recibido: {mensaje_leido.decode()}")
        os.waitpid(pid, 0)

if __name__ == "__main__":
    main()
