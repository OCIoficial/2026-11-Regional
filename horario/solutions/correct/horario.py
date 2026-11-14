# Separa la cadena por los '1' y obtiene el largo del bloque más grande de '0'.
import sys


def main():
    s = sys.stdin.read().strip()
    print(max(len(bloque) for bloque in s.split("1")))


main()
