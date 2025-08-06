import multiprocessing
from generador import generador
from analizador import analizador
from verificador import verificador
from blockchain import agregar_resultados_a_blockchain

def main():
    # Crear Pipes para enviar datos a cada analizador
    pipe_frec_env, pipe_frec_recv = multiprocessing.Pipe()
    pipe_pres_env, pipe_pres_recv = multiprocessing.Pipe()
    pipe_oxi_env, pipe_oxi_recv = multiprocessing.Pipe()

    # Crear colas de salida para recibir resultados de analizadores
    queue_frecuencia = multiprocessing.Queue()
    queue_presion = multiprocessing.Queue()
    queue_oxigeno = multiprocessing.Queue()

    # Cola para recibir la blockchain final desde el verificador
    salida_blockchain = multiprocessing.Queue()

    # Procesos analizadores
    proc_frec = multiprocessing.Process(target=analizador, args=("frecuencia_cardiaca", pipe_frec_recv, queue_frecuencia))
    proc_pres = multiprocessing.Process(target=analizador, args=("presion_arterial", pipe_pres_recv, queue_presion))
    proc_oxi = multiprocessing.Process(target=analizador, args=("oxigeno_sangre", pipe_oxi_recv, queue_oxigeno))

    # Proceso verificador
    proc_verificador = multiprocessing.Process(target=verificador, args=(queue_frecuencia, queue_presion, queue_oxigeno, salida_blockchain))

    # Iniciar procesos
    proc_frec.start()
    proc_pres.start()
    proc_oxi.start()
    proc_verificador.start()

    # Generar y enviar datos
    generador(pipe_frec_env, pipe_pres_env, pipe_oxi_env)

    # Esperar a que terminen los analizadores
    proc_frec.join()
    proc_pres.join()
    proc_oxi.join()
    proc_verificador.join()

    # Recibir la blockchain desde el verificador
    blockchain = salida_blockchain.get()

    # Guardar blockchain en disco usando la función del módulo blockchain.py
    agregar_resultados_a_blockchain(blockchain)

    print("Blockchain guardada correctamente en 'blockchain.json'")

if __name__ == "__main__":
    main()
