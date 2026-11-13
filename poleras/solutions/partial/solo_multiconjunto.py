# Solo compara los colores de C y D. Correcto cuando K = N, porque las
# poleras se pueden reordenar como se quiera.
# @ocimatic::expected [st1=OK, st2=WA, st3=WA, st4=WA]
import sys

datos = sys.stdin.buffer.read().split()
n = int(datos[0])
c = sorted(map(int, datos[2 : 2 + n]))
d = sorted(map(int, datos[2 + n : 2 + 2 * n]))

print("SI" if c == d else "NO")
