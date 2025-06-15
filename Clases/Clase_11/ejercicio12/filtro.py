import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--min", type=int, required=True)
args = parser.parse_args()

for linea in sys.stdin:
    numero = int(linea.strip())
    if numero > args.min:
        print(numero)
