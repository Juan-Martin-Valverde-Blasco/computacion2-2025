import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

for _ in range(args.n):
    print(random.randint(0, 100))
