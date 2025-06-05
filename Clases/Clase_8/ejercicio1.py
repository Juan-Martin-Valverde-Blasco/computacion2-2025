from multiprocessing import Pool

def calcular_cuadrado(n):
    return n * n

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5]
    print("Calculando cuadrados de:", numeros)
    
    with Pool(4) as pool:
        resultados = pool.map(calcular_cuadrado, numeros)
    
    print("Los cuadrados son:", resultados)