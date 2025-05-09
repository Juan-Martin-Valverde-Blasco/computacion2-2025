import os

def main():
    
    try:
        pid = os.fork()
    except OSError as e:
        print(f"Error al crear el proceso hijo: {e}")
        return

    if pid == 0:
        
        print(f"Hijo PID: ({os.getpid()}), PPID: ({os.getppid()})")
    else:
        
        print(f"Padre PID: ({os.getpid()}), PPID: ({os.getppid()})")
        
        os.wait()

if __name__ == "__main__":
    main()