# Supone que Emilia se acuesta en el primer tramo sin ronquidos disponible y
# devuelve el largo de ese primer bloque de '0's.
# @ocimatic::expected [st1=WA]
import sys

s = sys.stdin.read().strip()
bloques = [len(b) for b in s.split("1") if b]
print(bloques[0] if bloques else 0)
