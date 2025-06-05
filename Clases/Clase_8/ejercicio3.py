from multiprocessing import Process, Value, Lock

def incrementar(valor_compartido, cerrojo):
    for _ in range(1000):
        with cerrojo:  # aseguramos exclusión mutua
            valor_compartido.value += 1

if __name__ == '__main__':
    valor = Value('i', 0)  # entero inicializado en 0
    lock = Lock()

    p1 = Process(target=incrementar, args=(valor, lock))
    p2 = Process(target=incrementar, args=(valor, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Valor final:", valor.value)
