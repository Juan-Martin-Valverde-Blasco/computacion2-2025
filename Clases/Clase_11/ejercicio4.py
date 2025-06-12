import os
import sys

def main():
    pid = os.fork()
    if pid == 0:
        os.execvp("ls", ["ls", "-l"])
        sys.exit(1)
    else:
        os.waitpid(pid, 0)

if __name__ == "__main__":
    main()
