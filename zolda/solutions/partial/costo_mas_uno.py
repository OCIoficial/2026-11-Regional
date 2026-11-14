# Error por 1: calcula max(x) + N en lugar de max(x) + N - 1.
# @ocimatic::expected [st1=WA, st2=WA, st3=WA]
import sys

datos = list(map(int, sys.stdin.buffer.read().split()))
n, e = datos[0], datos[1]
x = datos[2 : 2 + n]
print("YES" if max(x) + n <= e else "NO")
