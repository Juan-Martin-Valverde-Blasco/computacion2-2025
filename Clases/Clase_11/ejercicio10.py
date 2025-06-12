import multiprocessing
import time
import random

class CuentaBancaria:
    def __init__(self):
        self.saldo = multiprocessing.Value('i', 1000)
        self.lock = multiprocessing.RLock()

    def depositar(self, monto):
        with self.lock:
            self._modificar_saldo(monto)

    def retirar(self, monto):
        with self.lock:
            self._modificar_saldo(-monto)

    def _modificar_saldo(self, monto):
        with self.lock:
            temp = self.saldo.value
            time.sleep(0.01)
            self.saldo.value = temp + monto

    def consultar_saldo(self):
        with self.lock:
            return self.saldo.value

def tarea(cuenta, proceso_id):
    for _ in range(5):
        if random.choice([True, False]):
            cuenta.depositar(100)
            print(f"Proceso {proceso_id}: depositó 100")
        else:
            cuenta.retirar(50)
            print(f"Proceso {proceso_id}: retiró 50")
        time.sleep(random.uniform(0.1, 0.3))

def main():
    cuenta = CuentaBancaria()
    procesos = []

    for i in range(4):
        p = multiprocessing.Process(target=tarea, args=(cuenta, i))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print(f"Saldo final: {cuenta.consultar_saldo()}")

if __name__ == "__main__":
    multiprocessing.set_start_method("fork")
    main()
