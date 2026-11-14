# No reutiliza las casillas liberadas al derrotar meblins: para cada bloque de
# K meblins consecutivos, dispara a todos desde la casilla libre anterior al
# bloque gastando 1 + 2 + ... + K.
# @ocimatic::expected [st1=OK, st2=WA, st3=WA]
import sys

datos = list(map(int, sys.stdin.buffer.read().split()))
n, e = datos[0], datos[1]
x = sorted(datos[2 : 2 + n])

pos = 0
gasto = 0
i = 0
while i < n:
    j = i
    while j + 1 < n and x[j + 1] == x[j] + 1:
        j += 1
    k = j - i + 1
    gasto += (x[i] - 1) - pos
    pos = x[i] - 1
    gasto += k * (k + 1) // 2
    i = j + 1

print("YES" if gasto <= e else "NO")
