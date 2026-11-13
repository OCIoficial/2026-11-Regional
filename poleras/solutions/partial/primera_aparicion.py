# Greedy incorrecto: compara los colores y luego revisa que la primera
# aparición en C de cada polera no usada vaya creciendo. Funciona si los
# colores son distintos, pero falla con repetidos, por ejemplo con
# C = 1 2 1 3, K = 1, D = 2 1 3 1.
# @ocimatic::expected [st1=OK, st2=WA, st3=WA]
import sys
from collections import Counter

datos = sys.stdin.buffer.read().split()
n, k = int(datos[0]), int(datos[1])
c = list(map(int, datos[2 : 2 + n]))
d = list(map(int, datos[2 + n : 2 + 2 * n]))

if Counter(c) != Counter(d):
    print("NO")
else:
    primera = {}
    for i, x in enumerate(c):
        primera.setdefault(x, i)
    pos = [primera[x] for x in d[: n - k]]
    ok = all(a < b for a, b in zip(pos, pos[1:]))
    print("SI" if ok else "NO")
