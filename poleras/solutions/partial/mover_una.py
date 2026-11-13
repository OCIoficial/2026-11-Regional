# Supone K = 1: busca la primera posición donde C y D difieren y verifica que
# esa polera sea la que quedó al final.
# @ocimatic::expected [st1=WA, st2=OK, st3=WA, st4=WA]
import sys

datos = sys.stdin.buffer.read().split()
n = int(datos[0])
c = list(map(int, datos[2 : 2 + n]))
d = list(map(int, datos[2 + n : 2 + 2 * n]))

i = 0
while i < n and c[i] == d[i]:
    i += 1

if i == n:
    print("SI")
else:
    ok = c[i] == d[n - 1] and c[i + 1 :] == d[i : n - 1]
    print("SI" if ok else "NO")
