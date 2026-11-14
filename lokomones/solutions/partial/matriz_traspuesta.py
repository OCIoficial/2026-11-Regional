# Invierte los índices de la matriz de tipos: usa P[defensor][atacante] en
# lugar de P[atacante][defensor].
# @ocimatic::expected [st1=WA, st2=WA]
import sys

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

ans = -1
for i in range(1, n + 1):
    hi, ai, ti = datos[idx : idx + 3]
    idx += 3
    dano_v = a * p[ti - 1][t - 1]
    dano_i = ai * p[t - 1][ti - 1]
    if (h + dano_i - 1) // dano_i < (hi + dano_v - 1) // dano_v:
        ans = i
        break

print(ans)
