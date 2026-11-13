# Generador de casos para Poleras.
#
# Uso: gen.py N K M MODO
#   M: cantidad de colores distintos en C, o `perm` para que C sea una permutación de 1..N.
#   MODO:
#     si     D se obtiene usando K poleras elegidas al azar.
#     justo  SI con K, pero NO con K - 1 (requiere K < N).
#     casi   NO con K, pero SI con K + 1. C y D tienen los mismos colores.
#     color  NO: se cambia el color de una polera usada. Las no usadas siguen siendo
#            subsecuencia de C, pero los multiconjuntos difieren.
#     suma   Como `color`, pero se cambian dos poleras usadas preservando la suma de los
#            colores (requiere K >= 2).
#     azar   D es una permutación al azar de C.
#     igual  D = C.

import random
import sys

random.seed(sys.argv[1])

N = int(sys.argv[2])
K = int(sys.argv[3])
M = sys.argv[4]
MODO = sys.argv[5]

assert 1 <= K <= N


def es_posible(c, d, k):
    n = len(c)
    if sorted(c) != sorted(d):
        return False
    pos = 0
    for x in c:
        if pos < n - k and x == d[pos]:
            pos += 1
    return pos == n - k


def generar_c():
    if M == "perm":
        c = list(range(1, N + 1))
        random.shuffle(c)
        return c
    paleta = random.sample(range(1, N + 1), int(M))
    return [random.choice(paleta) for _ in range(N)]


def usar(c, k):
    """Retorna las poleras no usadas (en orden) y las usadas (desordenadas)."""
    usadas = set(random.sample(range(len(c)), k))
    no_usadas = [x for i, x in enumerate(c) if i not in usadas]
    lavadas = [c[i] for i in sorted(usadas)]
    random.shuffle(lavadas)
    return no_usadas, lavadas


def justo(k):
    assert k < N
    for _ in range(20):
        c = generar_c()
        no_usadas, lavadas = usar(c, k)
        # Posición en c donde termina el emparejamiento greedy de las no usadas.
        fin, pos = -1, 0
        for i, x in enumerate(c):
            if pos < len(no_usadas) and x == no_usadas[pos]:
                pos += 1
                fin = i
        # Si la primera polera lavada no aparece después de `fin`, no basta con k - 1.
        despues = set(c[fin + 1 :])
        candidatas = [i for i, x in enumerate(lavadas) if x not in despues]
        if candidatas:
            i = random.choice(candidatas)
            lavadas[0], lavadas[i] = lavadas[i], lavadas[0]
            return c, no_usadas + lavadas

    # Construcción explícita: la primera polera tiene un color único y se usa.
    c = generar_c()
    unico = random.choice(sorted(set(range(1, N + 1)) - set(c)))
    c[0] = unico
    usadas = {0} | set(random.sample(range(1, N), k - 1))
    no_usadas = [x for i, x in enumerate(c) if i not in usadas]
    lavadas = [c[i] for i in sorted(usadas) if i != 0]
    random.shuffle(lavadas)
    return c, no_usadas + [unico] + lavadas


def cambiar_color(c, d):
    paleta = sorted(set(c))
    i = random.randrange(N - K, N)
    otros = [x for x in paleta if x != d[i]]
    if not otros:
        otros = [x for x in range(1, N + 1) if x != d[i]]
    d[i] = random.choice(otros)


def cambiar_suma(d):
    assert K >= 2
    while True:
        i, j = random.sample(range(N - K, N), 2)
        a, b = d[i], d[j]
        if a == N or b == 1:
            continue
        t = random.randint(1, min(N - a, b - 1, 3))
        if a + t == b:
            continue
        d[i], d[j] = a + t, b - t
        return


if MODO == "si":
    c = generar_c()
    no_usadas, lavadas = usar(c, K)
    d = no_usadas + lavadas
elif MODO == "justo":
    c, d = justo(K)
    assert not es_posible(c, d, K - 1)
elif MODO == "casi":
    c, d = justo(K + 1)
    assert sorted(c) == sorted(d)
elif MODO == "color":
    c = generar_c()
    no_usadas, lavadas = usar(c, K)
    d = no_usadas + lavadas
    cambiar_color(c, d)
elif MODO == "suma":
    c = generar_c()
    no_usadas, lavadas = usar(c, K)
    d = no_usadas + lavadas
    cambiar_suma(d)
    assert sum(c) == sum(d)
elif MODO == "azar":
    c = generar_c()
    d = c[:]
    random.shuffle(d)
elif MODO == "igual":
    c = generar_c()
    d = c[:]
else:
    raise ValueError(f"modo desconocido: {MODO}")

if MODO in ("si", "justo", "igual"):
    assert es_posible(c, d, K)
if MODO in ("casi", "color", "suma"):
    assert not es_posible(c, d, K)

print(N, K)
print(*c)
print(*d)
