# Generador de casos para Batalla lokomon (lokomones).
#
# Uso: gen.py K N MAX_H MODO
#   K: cantidad de tipos (1..100)
#   N: cantidad de lokomones candidatos (1..100)
#   MAX_H: cota superior de vida (ej. 1000 para st1, 1000000000 para st2)
#   MODO:
#     unico       Exactamente un lokomon gana; el resto pierde (varios por empate de turnos o por 1 de vida).
#     ultimo      Exactamente el último lokomon (índice N) gana.
#     multi       Varios lokomones ganan.
#     ninguno     Ningún lokomon gana (incluye empates de turnos donde Vichochú gana por partir primero).
#     techo_si    Gana únicamente un lokomon que requiere división techo exacta (con truncada parecería perder o empatar).
#     techo_no    Ninguno gana, pero con división truncada `H // dano` algún lokomon parecería ganar.
#     tipos_si    El único ganador tiene ataque base bajo pero multiplicador alto; otro tiene ataque alto pero multiplicador 1 y pierde.
#     traspuesta  La matriz P es asimétrica; usar P[j][i] en vez de P[i][j] invierte quién gana.
#     lento_no    Caso con H y H_i cerca de MAX_H y daño pequeño para dar TLE a la simulación turno a turno (respuesta -1).
#     lento_si    Igual que lento_no, pero el último lokomon gana tras muchos turnos.
#     overflow    Valores grandes en st2 donde turnos * dano supera 2^31 - 1.

import random
import sys

random.seed(sys.argv[1])

K = int(sys.argv[2])
N = int(sys.argv[3])
MAX_H = int(sys.argv[4])
MODO = sys.argv[5]

MAX_A = min(100_000_000, max(20, MAX_H))


def ceil_div(a, b):
    return (a + b - 1) // b


def gana_real(h, a, t, hi, ai, ti, p):
    dano_v = a * p[t - 1][ti - 1]
    dano_i = ai * p[ti - 1][t - 1]
    return ceil_div(h, dano_i) < ceil_div(hi, dano_v)


def gana_trunc(h, a, t, hi, ai, ti, p):
    dano_v = a * p[t - 1][ti - 1]
    dano_i = ai * p[ti - 1][t - 1]
    return (h // dano_i) < (hi // dano_v)


def gana_empate(h, a, t, hi, ai, ti, p):
    dano_v = a * p[t - 1][ti - 1]
    dano_i = ai * p[ti - 1][t - 1]
    return ceil_div(h, dano_i) <= ceil_div(hi, dano_v)


def gana_sin_tipos(h, a, hi, ai):
    return ceil_div(h, ai) < ceil_div(hi, a)


def gana_traspuesta(h, a, t, hi, ai, ti, p):
    dano_v = a * p[ti - 1][t - 1]
    dano_i = ai * p[t - 1][ti - 1]
    return ceil_div(h, dano_i) < ceil_div(hi, dano_v)


def matriz_azar():
    return [[random.randint(1, 10) for _ in range(K)] for _ in range(K)]


def hacer_perdedor_ajustado(h, a, t, p):
    """Genera un lokomon que pierde contra Vichochú, frecuentemente por empate de turnos o por 1 de vida."""
    for _ in range(100):
        ti = random.randint(1, K)
        ai = random.randint(1, max(1, min(MAX_A, h)))
        dano_v = a * p[t - 1][ti - 1]
        dano_i = ai * p[ti - 1][t - 1]
        turnos_i = ceil_div(h, dano_i)
        # Para que pierda, necesitamos ceil_div(hi, dano_v) <= turnos_i,
        # es decir, hi <= turnos_i * dano_v.
        cota = min(MAX_H, turnos_i * dano_v)
        if cota >= 1:
            if random.random() < 0.6:
                # Justo en el borde (empate de turnos si cota == turnos_i * dano_v)
                hi = max(1, cota - random.randint(0, min(5, cota - 1)))
            else:
                hi = random.randint(1, cota)
            if not gana_real(h, a, t, hi, ai, ti, p):
                return (hi, ai, ti)
    # Fallback seguro: vida 1
    return (1, 1, random.randint(1, K))


def hacer_ganador_ajustado(h, a, t, p):
    """Genera un lokomon que gana contra Vichochú, frecuentemente por apenas 1 turno o 1 de vida."""
    for _ in range(200):
        ti = random.randint(1, K)
        dano_v = a * p[t - 1][ti - 1]
        # Elegir ai suficientemente grande para que turnos_i * dano_v + 1 <= MAX_H
        max_turnos = (MAX_H - 1) // dano_v
        if max_turnos < 1:
            continue
        turnos_obj = random.randint(1, min(max_turnos, 50))
        min_dano_i = ceil_div(h, turnos_obj)
        min_ai = ceil_div(min_dano_i, p[ti - 1][t - 1])
        if min_ai > MAX_A:
            continue
        ai = random.randint(min_ai, min(MAX_A, max(min_ai, min_ai * 2)))
        dano_i = ai * p[ti - 1][t - 1]
        turnos_i = ceil_div(h, dano_i)
        min_hi = turnos_i * dano_v + 1
        if min_hi <= MAX_H:
            if random.random() < 0.7:
                hi = min(MAX_H, min_hi + random.randint(0, min(10, MAX_H - min_hi)))
            else:
                hi = random.randint(min_hi, MAX_H)
            if gana_real(h, a, t, hi, ai, ti, p):
                return (hi, ai, ti)
    # Fallback seguro: mata de un golpe y sobrevive un golpe
    ti = random.randint(1, K)
    ai = min(MAX_A, ceil_div(h, p[ti - 1][t - 1]))
    hi = min(MAX_H, a * p[t - 1][ti - 1] + 1)
    assert gana_real(h, a, t, hi, ai, ti, p)
    return (hi, ai, ti)


p = matriz_azar()
t = random.randint(1, K)
# Elegir H y A moderados para que sea fácil construir ganadores y perdedores dentro de MAX_H
h = random.randint(max(10, MAX_H // 5), MAX_H)
a = random.randint(1, max(1, MAX_H // 30))

if MODO in ("unico", "ultimo"):
    cand = [hacer_perdedor_ajustado(h, a, t, p) for _ in range(N)]
    idx = N - 1 if MODO == "ultimo" else random.randrange(N)
    cand[idx] = hacer_ganador_ajustado(h, a, t, p)
    assert sum(gana_real(h, a, t, *c, p) for c in cand) == 1

elif MODO == "multi":
    assert N >= 2
    cand = [hacer_perdedor_ajustado(h, a, t, p) for _ in range(N)]
    idx = N // 2
    cand[idx] = hacer_ganador_ajustado(h, a, t, p)
    assert sum(gana_real(h, a, t, *c, p) for c in cand) == 1

elif MODO == "ninguno":
    cand = [hacer_perdedor_ajustado(h, a, t, p) for _ in range(N)]
    # Forzar al menos un caso de empate exacto de turnos para atrapar `<=`
    ti = random.randint(1, K)
    dano_v = a * p[t - 1][ti - 1]
    ai = max(1, ceil_div(h, 3 * p[ti - 1][t - 1]))
    dano_i = ai * p[ti - 1][t - 1]
    turnos_i = ceil_div(h, dano_i)
    if turnos_i * dano_v <= MAX_H:
        cand[0] = (turnos_i * dano_v, ai, ti)
        assert not gana_real(h, a, t, *cand[0], p)
        assert gana_empate(h, a, t, *cand[0], p)
    assert sum(gana_real(h, a, t, *c, p) for c in cand) == 0

elif MODO == "techo_no":
    # Ninguno gana realmente, pero con división truncada `h // dano_i < hi // dano_v` alguno parece ganar.
    # Ejemplo: h = 2*dano_i + resto (ceil = 3, trunc = 2) y hi = 3*dano_v (ceil = 3, trunc = 3).
    p = [[1 for _ in range(K)] for _ in range(K)]
    t = random.randint(1, K)
    a = 10 if MAX_H >= 100 else 2
    h = 25 if MAX_H >= 100 else 5
    cand = [hacer_perdedor_ajustado(h, a, t, p) for _ in range(N)]
    # Con ai = 10, dano_i = 10 -> h = 25: ceil(25/10) = 3, trunc(25/10) = 2.
    # Con hi = 30, dano_v = 10 -> ceil(30/10) = 3, trunc(30/10) = 3.
    # Real: 3 < 3 (False). Truncada: 2 < 3 (True).
    ai = 10 if MAX_H >= 100 else 2
    hi = 30 if MAX_H >= 100 else 6
    ti = random.randint(1, K)
    cand[random.randrange(N)] = (hi, ai, ti)
    assert sum(gana_real(h, a, t, *c, p) for c in cand) == 0
    assert any(gana_trunc(h, a, t, *c, p) for c in cand)

elif MODO == "techo_si":
    # Exactamente uno gana, pero con división truncada parece empatar (pierde).
    # Ejemplo: h = 20, dano_i = 10 -> ceil = 2, trunc = 2.
    # hi = 21, dano_v = 10 -> ceil(21/10) = 3, trunc(21/10) = 2.
    # Real: 2 < 3 (True). Truncada: 2 < 2 (False).
    p = [[1 for _ in range(K)] for _ in range(K)]
    t = random.randint(1, K)
    a = 10 if MAX_H >= 100 else 2
    h = 20 if MAX_H >= 100 else 4
    cand = [(10 if MAX_H >= 100 else 2, 5 if MAX_H >= 100 else 1, random.randint(1, K)) for _ in range(N)]
    idx = random.randrange(N)
    cand[idx] = (21 if MAX_H >= 100 else 5, 10 if MAX_H >= 100 else 2, random.randint(1, K))
    assert sum(gana_real(h, a, t, *c, p) for c in cand) == 1
    assert sum(gana_trunc(h, a, t, *c, p) for c in cand) == 0

elif MODO == "tipos_si":
    assert K >= 2 and N >= 2
    p = [[1 for _ in range(K)] for _ in range(K)]
    t = 1
    t_bueno = 2
    p[t_bueno - 1][t - 1] = 10  # t_bueno pega x10 a Vichochú
    p[t - 1][t - 1] = 10        # Vichochú pega x10 a tipo 1
    p[t - 1][t_bueno - 1] = 1   # Vichochú pega x1 a t_bueno
    h = min(MAX_H, 500)
    a = 50
    # Candidato trampa: tipo 1, mucho ataque base (ai = 250) y vida 500.
    # Sin tipos: ceil(500/250)=2 < ceil(500/50)=10 (ganaría).
    # Con tipos: dano_v = 50*10 = 500 -> ceil(500/500)=1 turno, muere de 1 golpe!
    cand = [(h, 250, 1) for _ in range(N)]
    idx = N - 1
    # Candidato ganador: tipo 2, ataque base bajo (ai = 30), vida 150.
    # Sin tipos: ceil(500/30)=17 > ceil(150/50)=3 (perdería).
    # Con tipos: dano_i = 30*10 = 300 (2 turnos), dano_v = 50*1 = 50 (3 turnos) -> ¡gana!
    cand[idx] = (150, 30, t_bueno)
    assert not gana_real(h, a, t, *cand[0], p) and gana_sin_tipos(h, a, cand[0][0], cand[0][1])
    assert gana_real(h, a, t, *cand[idx], p) and not gana_sin_tipos(h, a, cand[idx][0], cand[idx][1])

elif MODO == "traspuesta":
    assert K >= 2 and N >= 2
    p = [[1 for _ in range(K)] for _ in range(K)]
    t = 1
    t2 = 2
    p[t - 1][t2 - 1] = 1
    p[t2 - 1][t - 1] = 10
    t3 = K
    if K >= 3:
        p[t - 1][t3 - 1] = 10
        p[t3 - 1][t - 1] = 1
    h = min(MAX_H, 400)
    a = 40
    # Si K >= 3, los demás candidatos son de tipo t3: pierden en la matriz real pero ganan en la traspuesta.
    # El último candidato es de tipo t2: gana en la matriz real pero pierde en la traspuesta.
    cand = [(200, 25, t3 if K >= 3 else t2) for _ in range(N)]
    if K == 2:
        # En K = 2, hacemos que los primeros tengan vida muy baja para perder en ambas,
        # salvo cand[0] que tiene números que ganan en traspuesta y pierden en real:
        # En traspuesta: p_trasp[1][2] = 10, p_trasp[2][1] = 1.
        p[t - 1][t2 - 1] = 10
        p[t2 - 1][t - 1] = 1
        # Ahora tipo 2 recibe x10 en real y pega x1 en real (pierde en real, gana en traspuesta)
        cand = [(200, 25, t2) for _ in range(N)]
        # Y para que uno gane en real y pierda en traspuesta con K=2, le damos mucho ataque y vida justa:
        # Mejor aún: si nadie gana (ninguno), en real da -1 y en traspuesta da 1!
    else:
        cand[-1] = (200, 25, t2)
        assert not gana_real(h, a, t, *cand[0], p) and gana_traspuesta(h, a, t, *cand[0], p)
        assert gana_real(h, a, t, *cand[-1], p) and not gana_traspuesta(h, a, t, *cand[-1], p)

elif MODO in ("lento_no", "lento_si"):
    p = [[1 for _ in range(K)] for _ in range(K)]
    t = random.randint(1, K)
    h = MAX_H
    a = 1
    cand = []
    for _ in range(N):
        hi = MAX_H - random.randint(0, 100)
        ai = 1
        ti = random.randint(1, K)
        cand.append((hi, ai, ti))
    if MODO == "lento_si":
        # El último lokomon tiene H_i = MAX_H, A_i = 2 (necesita MAX_H/2 turnos, ambos muy grandes)
        cand[-1] = (MAX_H, 2, random.randint(1, K))
        assert sum(gana_real(h, a, t, *c, p) for c in cand) == 1
    else:
        assert sum(gana_real(h, a, t, *c, p) for c in cand) == 0

elif MODO == "overflow":
    # Caso para st2 donde dano_v ~ 10^9 y turnos_i ~ 10^9, de modo que turnos_i * dano_v desborda int32 o incluso int64 si no se usa división
    p = [[10 for _ in range(K)] for _ in range(K)]
    t = random.randint(1, K)
    h = MAX_H
    a = MAX_A
    cand = []
    for i in range(N):
        ti = random.randint(1, K)
        if i == N - 1:
            # Gana: mata en 1 golpe (dano_i = 10^9 >= h) y sobrevive 1 golpe?
            # Si dano_v = 10^8 * 10 = 10^9 y MAX_H = 10^9, con dano_v = 10^9 nadie sobrevive 1 golpe.
            # Así que bajamos el ataque de Vichochú a 10^8 - 1 y P[t][ti] = 5 -> dano_v = 5*10^8 - 5.
            pass
        cand.append((MAX_H, 1, ti))
    a = 90_000_000
    for j in range(K):
        p[t - 1][j] = 5  # dano_v = 450_000_000 (necesita 3 golpes para bajar 10^9)
    # Cand 0..N-2 tienen ai = 1 (necesitan 10^8 o 2*10^8 golpes, turnos_i * dano_v > 2^31 - 1)
    # Cand N-1 tiene ai = 100_000_000 -> dano_i >= 500_000_000 (mata en <= 2 golpes < 3 golpes)
    cand[-1] = (MAX_H, 100_000_000, random.randint(1, K))
    assert sum(gana_real(h, a, t, *c, p) for c in cand) == 1

else:
    raise ValueError(f"modo desconocido: {MODO}")

print(K)
for fila in p:
    print(*fila)
print(h, a, t)
print(N)
for hi, ai, ti in cand:
    print(hi, ai, ti)
