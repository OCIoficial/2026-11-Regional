# Simula hasta un tope fijo de 1000 rondas (suficiente para la subtarea 1
# donde H <= 1000, pero insuficiente en la subtarea 2).
# @ocimatic::expected [st1=OK, st2=WA]
import sys


def main():
    datos = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    k = datos[idx]
    idx += 1
    p = [datos[idx + r * k : idx + (r + 1) * k] for r in range(k)]
    idx += k * k
    h, a, t = datos[idx : idx + 3]
    idx += 3
    n = datos[idx]
    idx += 1

    for i in range(1, n + 1):
        hi, ai, ti = datos[idx : idx + 3]
        idx += 3
        dano_v = a * p[t - 1][ti - 1]
        dano_i = ai * p[ti - 1][t - 1]
        vida_v = h
        vida_i = hi
        for _ in range(1000):
            if vida_v <= 0 or vida_i <= 0:
                break
            vida_i -= dano_v
            if vida_i <= 0:
                break
            vida_v -= dano_i
        if vida_v <= 0 and vida_i > 0:
            print(i)
            return

    print(-1)


main()
