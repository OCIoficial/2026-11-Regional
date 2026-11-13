# Greedy incorrecto: saca de C las poleras del final de D eligiendo siempre la
# primera aparición de cada color, y compara lo que queda con el inicio de D.
# Falla, por ejemplo, con C = 1 2 1, K = 1, D = 1 2 1.
# @ocimatic::expected [st1=OK, st2=WA, st3=WA]
import sys
from collections import Counter

datos = sys.stdin.buffer.read().split()
n, k = int(datos[0]), int(datos[1])
c = list(map(int, datos[2 : 2 + n]))
d = list(map(int, datos[2 + n : 2 + 2 * n]))

resta = Counter(d[n - k :])
quedan = []
for x in c:
    if resta[x] > 0:
        resta[x] -= 1
    else:
        quedan.append(x)

print("SI" if quedan == d[: n - k] else "NO")
