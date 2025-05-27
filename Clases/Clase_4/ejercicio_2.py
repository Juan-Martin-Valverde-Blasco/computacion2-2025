from multiprocessing import Process, Pipe

def proceso_a(pipe_ab):
    pipe_ab_out = pipe_ab[1]
    pipe_ab[0].close()
    datos = ["dato1", "dato2", "dato3"]
    for d in datos:
        print(f"Proceso A envía: {d}")
        pipe_ab_out.send(d)
    print("Proceso A envía: FIN")
    pipe_ab_out.send("FIN")
    pipe_ab_out.close()

def proceso_b(pipe_ab, pipe_bc):
    pipe_ab_out, pipe_ab_in = pipe_ab
    pipe_bc_out, pipe_bc_in = pipe_bc
    pipe_ab_out.close()
    pipe_bc_in.close()
    while True:
        dato = pipe_ab_in.recv()
        if dato == "FIN":
            print("Proceso B recibe: FIN")
            print("Proceso B envía: FIN")
            pipe_bc_out.send("FIN")
            break
        print(f"Proceso B recibe: {dato}")
        dato_modificado = dato.upper()
        print(f"Proceso B envía: {dato_modificado}")
        pipe_bc_out.send(dato_modificado)
    pipe_ab_in.close()
    pipe_bc_out.close()

def proceso_c(pipe_bc):
    pipe_bc_out, pipe_bc_in = pipe_bc
    pipe_bc_out.close()
    while True:
        dato = pipe_bc_in.recv()
        if dato == "FIN":
            print("Proceso C recibe: FIN")
            break
        print(f"Proceso C recibe: {dato}")
    pipe_bc_in.close()

if __name__ == "__main__":
    pipe_ab = Pipe()
    pipe_bc = Pipe()
    p_a = Process(target=proceso_a, args=(pipe_ab,))
    p_b = Process(target=proceso_b, args=(pipe_ab, pipe_bc))
    p_c = Process(target=proceso_c, args=(pipe_bc,))
    p_a.start()
    p_b.start()
    p_c.start()
    pipe_ab[0].close()
    pipe_ab[1].close()
    pipe_bc[0].close()
    pipe_bc[1].close()
    p_a.join()
    p_b.join()
    p_c.join()
