from multiprocessing import Process, Array, Lock

def incrementar_array(arr, lock):
    for _ in range(1000):
        with lock:
            for i in range(len(arr)):
                arr[i] += 1

if __name__ == '__main__':
    arr = Array('i', 5)  # Array de 5 enteros inicializados en 0
    lock = Lock()

    p1 = Process(target=incrementar_array, args=(arr, lock))
    p2 = Process(target=incrementar_array, args=(arr, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(list(arr))
