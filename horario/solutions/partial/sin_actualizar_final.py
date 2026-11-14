# Solo actualiza el máximo cuando encuentra un '1', olvidando actualizar al
# terminar la cadena (falla cuando el bloque más largo llega hasta el final).
# @ocimatic::expected [st1=WA]
import sys

s = sys.stdin.read().strip()
actual = 0
mejor = 0
for c in s:
    if c == "0":
        actual += 1
    else:
        mejor = max(mejor, actual)
        actual = 0

print(mejor)
