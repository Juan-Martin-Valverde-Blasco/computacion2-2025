import argparse

def funcion_1():
    parser = argparse.ArgumentParser(description='Procesa un archivo de texto')
    
    parser.add_argument('--input', type=str, help='Nombre del archivo a procesar', required=True)
    parser.add_argument('--output', type=str, help='Archivo procesado', required=True)
    
    args = parser.parse_args()
    
    print(f"Archivo a procesar: {args.input}")
    print(f"Archivo Procesado: {args.output}")
    
if __name__ == '__main__':
    funcion_1()