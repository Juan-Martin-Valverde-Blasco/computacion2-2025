import os
import time

pid = os.fork()

if pid == 0:
    print("Hijo: Voy a trabajar 5 segundos...")
    time.sleep(5)
    print("Hijo: Terminé.")
    os._exit(0)

else:
    print("Padre: Espero que mi hijo termine.")
    os.wait()
    print("Padre: Mi hijo terminó, ahora sigo yo.")