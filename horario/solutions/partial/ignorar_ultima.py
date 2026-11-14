# Error de borde: itera solo hasta i < 9, ignorando la última hora.
# @ocimatic::expected [st1=WA]
import sys

s = sys.stdin.read().strip()[:9]
print(max(len(b) for b in s.split("1")))
