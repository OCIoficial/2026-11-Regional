# Supone que las poleras usadas también conservan su orden relativo al
# ponerse al final. Correcto cuando K = 1.
# @ocimatic::expected [st1=WA, st2=OK, st3=WA, st4=WA]
import sys

datos = sys.stdin.buffer.read().split()
n, k = int(datos[0]), int(datos[1])
c = list(map(int, datos[2 : 2 + n]))
d = list(map(int, datos[2 + n : 2 + 2 * n]))

pos = 0
lavadas = []
for x in c:
    if pos < n - k and x == d[pos]:
        pos += 1
    else:
        lavadas.append(x)

print("SI" if pos == n - k and lavadas == d[n - k :] else "NO")
