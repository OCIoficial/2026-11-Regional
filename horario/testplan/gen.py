# Generador de casos para Una noche de ronquidos (horario).
#
# Uso: gen.py MODO [ARGS...]
#   MODO:
#     exacto K POS   Genera una cadena donde el bloque más largo de 0s tiene largo K
#                    y se ubica al `inicio`, `medio` o `final` (según POS).
#     bloques B1 B2... Genera bloques de 0s de largos B1, B2, ... separados por 1s.
#     azar P         Cada hora tiene probabilidad P/10 de ser 0 (ronquido = 1).

import random
import sys

random.seed(sys.argv[1])

MODO = sys.argv[2]
N = 10


def max_ceros(s):
    return max(len(b) for b in s.split("1"))


if MODO == "exacto":
    k = int(sys.argv[3])
    pos = sys.argv[4]
    assert 0 <= k <= N

    if k == 0:
        s = "1" * N
    elif k == N:
        s = "0" * N
    else:
        while True:
            if pos == "inicio":
                inicio = 0
            elif pos == "final":
                inicio = N - k
            elif pos == "medio":
                inicio = random.randint(1, N - k - 1)
            else:
                raise ValueError(f"posición desconocida: {pos}")

            chars = [random.choice("01") for _ in range(N)]
            for i in range(inicio, inicio + k):
                chars[i] = "0"
            if inicio > 0:
                chars[inicio - 1] = "1"
            if inicio + k < N:
                chars[inicio + k] = "1"

            s = "".join(chars)
            # Verificar que el máximo sea exactamente k y que en el resto sea menor
            # para aislar el bloque en la posición pedida.
            bloques = []
            i = 0
            while i < N:
                if s[i] == "0":
                    j = i
                    while j < N and s[j] == "0":
                        j += 1
                    bloques.append((j - i, i))
                    i = j
                else:
                    i += 1
            if max_ceros(s) == k and sum(1 for largo, _ in bloques if largo == k) == 1:
                break

elif MODO == "bloques":
    largos = [int(x) for x in sys.argv[3:]]
    total_ceros = sum(largos)
    min_unos = max(0, len(largos) - 1)
    assert total_ceros + min_unos <= N
    unos_extra = N - total_ceros - min_unos
    gaps = [0] + [1] * min_unos + [0]
    for _ in range(unos_extra):
        gaps[random.randrange(len(gaps))] += 1
    partes = ["1" * gaps[0]]
    for idx, b in enumerate(largos):
        partes.append("0" * b)
        partes.append("1" * gaps[idx + 1])
    s = "".join(partes)

elif MODO == "azar":
    p = int(sys.argv[3])
    s = "".join("0" if random.randrange(10) < p else "1" for _ in range(N))

else:
    raise ValueError(f"modo desconocido: {MODO}")

assert len(s) == N and set(s) <= {"0", "1"}
print(s)
