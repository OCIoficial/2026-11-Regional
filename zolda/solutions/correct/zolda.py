# El costo mínimo para derrotar a todos los meblins es max(x) + N - 1.
import sys


def main():
    datos = list(map(int, sys.stdin.buffer.read().split()))
    n, e = datos[0], datos[1]
    x = datos[2 : 2 + n]
    print("YES" if max(x) + n - 1 <= e else "NO")


main()
