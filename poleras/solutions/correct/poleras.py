# Las poleras no usadas quedan al inicio de D en su orden original, así que D[0..N-K) debe ser
# subsecuencia de C. Además C y D deben tener los mismos colores. Ambas condiciones bastan.
import sys
from collections import Counter


def main():
    datos = sys.stdin.buffer.read().split()
    n, k = int(datos[0]), int(datos[1])
    c = list(map(int, datos[2 : 2 + n]))
    d = list(map(int, datos[2 + n : 2 + 2 * n]))

    if Counter(c) != Counter(d):
        print("NO")
        return

    pos = 0
    for x in c:
        if pos < n - k and x == d[pos]:
            pos += 1

    print("SI" if pos == n - k else "NO")


main()
