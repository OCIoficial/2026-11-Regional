# Simula la batalla turno por turno restando vida en un ciclo while.
# Pasa la subtarea 1 (H <= 1000), pero da TLE en la subtarea 2.
# @ocimatic::expected [st1=OK, st2=TLE]
import sys


def main():
    datos = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0

    k = datos[idx]
    idx += 1

    p = []
    for _ in range(k):
        p.append(datos[idx : idx + k])
        idx += k

    h, a, t = datos[idx], datos[idx + 1], datos[idx + 2]
    idx += 3

    n = datos[idx]
    idx += 1

    for i in range(1, n + 1):
        hi, ai, ti = datos[idx], datos[idx + 1], datos[idx + 2]
        idx += 3

        dano_v = a * p[t - 1][ti - 1]
        dano_i = ai * p[ti - 1][t - 1]

        vida_v = h
        vida_i = hi
        while True:
            vida_i -= dano_v
            if vida_i <= 0:
                break
            vida_v -= dano_i
            if vida_v <= 0:
                print(i)
                return

    print(-1)


main()
