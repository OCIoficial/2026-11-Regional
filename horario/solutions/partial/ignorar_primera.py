# Error de borde: empieza desde i = 1, ignorando la primera hora.
# @ocimatic::expected [st1=WA]
import sys

s = sys.stdin.read().strip()[1:]
print(max(len(b) for b in s.split("1")))
