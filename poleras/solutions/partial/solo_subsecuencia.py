# Solo verifica que las poleras no usadas sean subsecuencia de C, olvidando
# comparar los colores de las poleras usadas.
# @ocimatic::expected [st1=WA, st2=WA, st3=WA]
import sys

datos = sys.stdin.buffer.read().split()
n, k = int(datos[0]), int(datos[1])
c = list(map(int, datos[2 : 2 + n]))
d = list(map(int, datos[2 + n : 2 + 2 * n]))

pos = 0
for x in c:
    if pos < n - k and x == d[pos]:
        pos += 1

print("SI" if pos == n - k else "NO")
