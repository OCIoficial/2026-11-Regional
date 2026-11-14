# Supone que los meblins ocupan N casillas consecutivas a partir de min(x),
# por lo que max(x) = min(x) + N - 1 y el costo es min(x) + 2*N - 2.
# @ocimatic::expected [st1=OK, st2=OK, st3=WA]
import sys

datos = list(map(int, sys.stdin.buffer.read().split()))
n, e = datos[0], datos[1]
x = datos[2 : 2 + n]
print("SI" if min(x) + 2 * n - 2 <= e else "NO")
