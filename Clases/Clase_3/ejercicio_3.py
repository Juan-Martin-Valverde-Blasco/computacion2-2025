import os

def main():
    try:
        pid = os.fork()
    
    except OSError as e:
        print(f"Error al crear el proceso hijo: {e}")
        return

    if pid == 0:
        
        print(f"Hijo Ejecutando 'ls -l' PID: ({os.getpid()})")
        
        try:
            os.execvp("ls", ["ls", "-l"])
        
        except Exception as e:
            print(f"Hijo Error al ejecutar 'ls': {e}")
            os._exit(1)
    else:
        
        os.waitpid(pid, 0)
        print("Padre El hijo ha terminado.")

if __name__ == "__main__":
    main()