# Generador de casos para El arco de Lonk (zolda).
#
# Uso: gen.py N MAX_X ORDEN MODO
#   N: cantidad de meblins (1..100000)
#   MAX_X: cota superior para las posiciones (N..10^9)
#   ORDEN:
#     asc    Posiciones ordenadas de menor a mayor.
#     desc   Posiciones ordenadas de mayor a menor.
#     azar   Posiciones desordenadas al azar (con el máximo fuera del final si N >= 2).
#   MODO:
#     consec_justo   N posiciones consecutivas, E = max(x) + N - 1 (YES exacto).
#     consec_casi    N posiciones consecutivas, E = max(x) + N - 2 (NO por 1).
#     consec_trampa  N posiciones consecutivas, E = max(x) (NO si N >= 2, atrapa `max(x) <= E`).
#     disp_justo     Posiciones dispersas, E = max(x) + N - 1 (YES exacto).
#     disp_casi      Posiciones dispersas, E = max(x) + N - 2 (NO por 1).
#     disp_trampa    Posiciones dispersas con min(x) + 2*N - 2 <= E < max(x) + N - 1 (NO, atrapa fórmula de consecutivos).
#     bloques_justo  Varios bloques de meblins consecutivos, E = max(x) + N - 1 (YES exacto).

import random
import sys

random.seed(sys.argv[1])

N = int(sys.argv[2])
MAX_X = int(sys.argv[3])
ORDEN = sys.argv[4]
MODO = sys.argv[5]

MAX_E = 1_000_000_000
assert 1 <= N <= 100_000
assert N <= MAX_X <= 1_000_000_000


def ordenar(x):
    x = sorted(x)
    if ORDEN == "asc":
        return x
    if ORDEN == "desc":
        return x[::-1]
    if ORDEN == "azar":
        if len(x) >= 2:
            mx = x[-1]
            mn = x[0]
            for _ in range(20):
                random.shuffle(x)
                if x[-1] != mx and x[0] != mn:
                    break
            else:
                # Para N = 2, al poner [mx, mn] ya tenemos x[-1] != mx y x[0] != mn
                x = [mx, mn] + x[1:-1]
        return x
    raise ValueError(f"orden desconocido: {ORDEN}")


if MODO.startswith("consec_"):
    # Para que E = max(x) + N - 1 <= 10^9, limitamos el inicio del bloque
    tope_max_x = min(MAX_X, MAX_E - N + 1)
    min_inicio = 2 if (MODO == "consec_casi" and N == 1) else 1
    inicio = random.randint(min_inicio, max(min_inicio, tope_max_x - N + 1))
    x = list(range(inicio, inicio + N))
    opt = x[-1] + N - 1
    if MODO == "consec_justo":
        e = opt
    elif MODO == "consec_casi":
        assert opt >= 2
        e = opt - 1
    elif MODO == "consec_trampa":
        assert N >= 2
        e = x[-1]
    else:
        raise ValueError(f"modo desconocido: {MODO}")

elif MODO in ("disp_justo", "disp_casi", "disp_trampa"):
    assert N >= 2
    tope_max_x = min(MAX_X, MAX_E - N + 1)
    assert tope_max_x >= 2 * N
    x = sorted(random.sample(range(1, tope_max_x + 1), N))
    # Asegurar que NO sean consecutivos
    if x[-1] - x[0] == N - 1:
        x[-1] = min(tope_max_x, x[-1] + random.randint(1, 10))
    opt = x[-1] + N - 1
    if MODO == "disp_justo":
        e = opt
    elif MODO == "disp_casi":
        e = opt - 1
    elif MODO == "disp_trampa":
        # Queremos que min(x) + 2*N - 2 <= E < max(x) + N - 1
        falso_opt = x[0] + 2 * N - 2
        if falso_opt >= opt:
            x[0] = 1
            x[-1] = tope_max_x
            opt = x[-1] + N - 1
            falso_opt = x[0] + 2 * N - 2
        assert falso_opt < opt
        e = random.randint(falso_opt, opt - 1)

elif MODO == "bloques_justo":
    tope_max_x = min(MAX_X, MAX_E - N + 1)
    pos = set()
    actual = random.randint(1, 20)
    while len(pos) < N and actual <= tope_max_x:
        largo = random.randint(1, min(25, N - len(pos)))
        for p in range(actual, min(tope_max_x + 1, actual + largo)):
            pos.add(p)
        actual += largo + random.randint(2, max(3, tope_max_x // (N + 1)))
    while len(pos) < N:
        pos.add(random.randint(1, tope_max_x))
    x = sorted(pos)
    e = x[-1] + N - 1

else:
    raise ValueError(f"modo desconocido: {MODO}")

x = ordenar(x)
assert 1 <= e <= MAX_E
assert len(x) == N

print(N, e)
print(*x)
