import os

def main():
    hijos = []

    for i in range(2):
        
        try:
            pid = os.fork()
        except OSError as e:
            print(f"Error al crear el proceso hijo {i+1}: {e}")
            return

        if pid == 0:    
            print(f"Hijo ({i+1})  PID: ({os.getpid()}), PPID: ({os.getppid()})")
            os._exit(0)  
        
        else:    
            hijos.append(pid)
            
    for pid in hijos:
        os.waitpid(pid, 0)
    print("Padre Todos los hijos han terminado.")

if __name__ == "__main__":
    main()