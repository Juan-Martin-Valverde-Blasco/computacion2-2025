import time
import random

def generador(pipe_frec, pipe_pres, pipe_oxi):
    for i in range(60):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        frecuencia = random.randint(60, 180)
        presion_sistolica = random.randint(110, 180)
        presion_diastolica = random.randint(70, 110)
        oxigeno = random.randint(90, 100)

        data = {
            "timestamp": timestamp,
            "frecuencia_cardiaca": frecuencia,
            "presion_arterial": [presion_sistolica, presion_diastolica],
            "oxigeno_sangre": oxigeno
        }

        print(f"[{i+1:02d}/60] Frecuencia: {frecuencia} | Presión: {presion_sistolica} | Oxígeno: {oxigeno}", flush=True)

        pipe_frec.send(data)
        pipe_pres.send(data)
        pipe_oxi.send(data)

        time.sleep(1)

    # Enviar señal de finalización a los analizadores
    pipe_frec.send("FIN")
    pipe_pres.send("FIN")
    pipe_oxi.send("FIN")
    print("Generador finalizado. Enviando FIN a analizadores.", flush=True)