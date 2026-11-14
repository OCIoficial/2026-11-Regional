# Supone que la entrada viene ordenada de menor a mayor y toma x[-1] como
# la posición más lejana sin ordenar ni buscar el máximo.
# @ocimatic::expected [st1=OK, st2=WA, st3=WA]
import sys

datos = list(map(int, sys.stdin.buffer.read().split()))
n, e = datos[0], datos[1]
x = datos[2 : 2 + n]
print("YES" if x[-1] + n - 1 <= e else "NO")
