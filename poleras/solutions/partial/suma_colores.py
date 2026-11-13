# Compara la suma de los colores en vez de los multiconjuntos. Correcto cuando
# K = 1, porque solo queda una polera por comparar.
# @ocimatic::expected [st1=WA, st2=OK, st3=WA, st4=WA]
import sys

datos = sys.stdin.buffer.read().split()
n, k = int(datos[0]), int(datos[1])
c = list(map(int, datos[2 : 2 + n]))
d = list(map(int, datos[2 + n : 2 + 2 * n]))

pos = 0
for x in c:
    if pos < n - k and x == d[pos]:
        pos += 1

print("SI" if sum(c) == sum(d) and pos == n - k else "NO")
