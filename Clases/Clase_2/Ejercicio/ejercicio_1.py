import os

print("PID actual:", os.getpid())

pid = os.fork()

if pid == 0:
    print("👶 Hijo: Soy el hijo. Mi PID es", os.getpid())
else:
    print("👨‍🦳 Padre: Soy el padre. Mi PID es", os.getpid(), "y mi hijo es", pid)