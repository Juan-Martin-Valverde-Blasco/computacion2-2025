from multiprocessing import Process, Pipe

def proceso_a(conn_salida):
    for i in range(1, 6):
        conn_salida.send(i)
        print(f"A envió: {i}")
    conn_salida.send('FIN')
    conn_salida.close()

def proceso_b(conn_entrada, conn_salida):
    while True:
        dato = conn_entrada.recv()
        if dato == 'FIN':
            conn_salida.send('FIN')
            break
        resultado = dato * 10
        print(f"B recibió {dato} y envió {resultado}")
        conn_salida.send(resultado)
    conn_entrada.close()
    conn_salida.close()

def proceso_c(conn_entrada):
    while True:
        dato = conn_entrada.recv()
        if dato == 'FIN':
            break
        print(f"C recibió resultado final: {dato}")
    conn_entrada.close()

if __name__ == '__main__':

    a_b_conn1, a_b_conn2 = Pipe()

    b_c_conn1, b_c_conn2 = Pipe()

    a = Process(target=proceso_a, args=(a_b_conn1,))
    b = Process(target=proceso_b, args=(a_b_conn2, b_c_conn1))
    c = Process(target=proceso_c, args=(b_c_conn2,))

    a.start()
    b.start()
    c.start()

    a.join()
    b.join()
    c.join()
