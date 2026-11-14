# Supone N = 1 (o ignora el costo de los disparos intermedios) y solo revisa
# si max(x) <= E.
# @ocimatic::expected [st1=OK, st2=WA, st3=WA]
import sys

datos = list(map(int, sys.stdin.buffer.read().split()))
n, e = datos[0], datos[1]
x = datos[2 : 2 + n]
print("SI" if max(x) <= e else "NO")
