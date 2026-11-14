# Calcula en O(1) los ataques necesarios con división entera techo.
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

        turnos_v = (hi + dano_v - 1) // dano_v
        turnos_i = (h + dano_i - 1) // dano_i

        if turnos_i < turnos_v:
            print(i)
            return

    print(-1)


main()
