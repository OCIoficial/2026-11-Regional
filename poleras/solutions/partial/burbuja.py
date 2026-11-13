# Solución correcta, pero compara los colores ordenando con bubble sort en
# O(N^2).
# @ocimatic::expected [st1=TLE, st2=TLE, st3=OK, st4=TLE]
import sys


def burbuja(v):
    n = len(v)
    for i in range(n):
        for j in range(n - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]


datos = sys.stdin.buffer.read().split()
n, k = int(datos[0]), int(datos[1])
c = list(map(int, datos[2 : 2 + n]))
d = list(map(int, datos[2 + n : 2 + 2 * n]))

sc, sd = c[:], d[:]
burbuja(sc)
burbuja(sd)

if sc != sd:
    print("NO")
else:
    pos = 0
    for x in c:
        if pos < n - k and x == d[pos]:
            pos += 1
    print("SI" if pos == n - k else "NO")
