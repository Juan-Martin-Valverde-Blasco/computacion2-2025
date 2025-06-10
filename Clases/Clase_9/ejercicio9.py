from multiprocessing import Process, Value, Lock, current_process
import random
import time

def sensor(temp_actual, temp_max, temp_min):
    while True:
        nueva_temp = random.uniform(-10, 40)
        with temp_actual.get_lock():
            temp_actual.value = nueva_temp
        
        with temp_max.get_lock():
            if nueva_temp > temp_max.value:
                temp_max.value = nueva_temp
        
        with temp_min.get_lock():
            if nueva_temp < temp_min.value:
                temp_min.value = nueva_temp

        print(f"{current_process().name} mide {nueva_temp:.2f}°C")
        time.sleep(random.uniform(0.5, 1.5))

def display(temp_actual, temp_max, temp_min):
    while True:
        with temp_actual.get_lock():
            actual = temp_actual.value
        with temp_max.get_lock():
            máximo = temp_max.value
        with temp_min.get_lock():
            mínimo = temp_min.value
        
        print(f"Display → Actual: {actual:.2f}°C | Máxima: {máximo:.2f}°C | Mínima: {mínimo:.2f}°C")
        time.sleep(2)

if __name__ == "__main__":
    temperatura_actual = Value('d', 0.0)
    temperatura_maxima = Value('d', float('-inf'))
    temperatura_minima = Value('d', float('inf'))

    sensores = [Process(target=sensor, args=(temperatura_actual, temperatura_maxima, temperatura_minima), name=f"Sensor-{i+1}") for i in range(3)]
    monitor = Process(target=display, args=(temperatura_actual, temperatura_maxima, temperatura_minima), name="Display")

    for s in sensores:
        s.start()
    monitor.start()

    for s in sensores:
        s.join()
    monitor.join()
    print("Sistema de monitoreo de temperatura finalizado.")