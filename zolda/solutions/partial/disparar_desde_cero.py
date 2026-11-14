# Nunca salta: dispara a todos los meblins desde la posición 0.
# @ocimatic::expected [st1=OK, st2=WA, st3=WA]
import sys

datos = list(map(int, sys.stdin.buffer.read().split()))
n, e = datos[0], datos[1]
x = datos[2 : 2 + n]
print("YES" if sum(x) <= e else "NO")
