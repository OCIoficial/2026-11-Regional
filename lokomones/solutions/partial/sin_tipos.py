# Ignora la tabla de efectividad de tipos P y usa directamente el ataque base.
# @ocimatic::expected [st1=WA, st2=WA]
import sys

datos = list(map(int, sys.stdin.buffer.read().split()))
k = datos[0]
idx = 1 + k * k
h, a, t = datos[idx : idx + 3]
idx += 3
n = datos[idx]
idx += 1

ans = -1
for i in range(1, n + 1):
    hi, ai, ti = datos[idx : idx + 3]
    idx += 3
    if (h + ai - 1) // ai < (hi + a - 1) // a:
        ans = i
        break

print(ans)
