# Cuenta el total de horas sin ronquidos en lugar de las horas consecutivas.
# @ocimatic::expected [st1=WA]
import sys

s = sys.stdin.read().strip()
print(s.count("0"))
