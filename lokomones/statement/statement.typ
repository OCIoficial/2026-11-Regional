#import "oci.typ": *

#show: problem.with(
  title: "Batalla lokomon",
)

#problemDescription[
  Después de una larga travesía, Ashrias está a punto de salir de la calle
  Accepted para competir en la Liga Lokomon. A pocos metros de la salida
  aparece Mr. Nachianni, líder del equipo WAcket, y lo reta a una batalla.

  Los lokomones de Ashrias están agotados por los combates del camino.
  Mr. Nachianni quiere una victoria de la que pueda presumir, así que le
  permite capturar un nuevo lokomon antes de la batalla.
  La batalla será de uno contra uno: el nuevo lokomon de Ashrias
  contra Vichochú, el lokomon favorito de Mr. Nachianni.

  Por suerte, Ashrias tomó nota de los $N$ lokomones que vio mientras
  recorría la calle Accepted. Además, conoce las características de
  Vichochú. Ahora necesita tu ayuda para decidir cuál capturar.

  Cada lokomon tiene una cantidad de *vida*, un valor de *ataque* y un
  *tipo*. Hay $K$ tipos, numerados del $1$ al $K$. La efectividad de un
  ataque depende tanto del tipo de quien ataca como del tipo de quien lo
  recibe. Esta relación se describe mediante una matriz $P$: si un lokomon
  con ataque $A$ y tipo $i$ ataca a uno de tipo $j$, le resta $A dot.op P[i][j]$
  puntos de vida. Un lokomon queda derrotado cuando su vida llega a $0$ o
  menos.

  *Vichochú ataca primero.* Desde ese momento, los lokomones se turnan
  para atacar. La batalla termina en cuanto uno de los dos cae derrotado
  y gana el entrenador del lokomon que sigue en pie.

  Ayuda a Ashrias a elegir uno de los $N$ lokomones con el que pueda
  derrotar a Vichochú, o determina que ninguno le permite ganar.
]

#inputDescription[
  La primera línea contiene un entero $K$ ($1 <= K <= 100$), la cantidad
  de tipos de lokomon.

  Las siguientes $K$ líneas contienen $K$ enteros cada una. El $j$-ésimo
  entero de la $i$-ésima línea es $P[i][j]$ ($1 <= P[i][j] <= 10$), el
  multiplicador del ataque de un lokomon de tipo $i$ contra uno de tipo $j$.

  La siguiente línea contiene tres enteros $H$, $A$ y $T$: la vida, el
  ataque y el tipo de Vichochú, respectivamente
  ($1 <= H <= 10^9$; $1 <= A <= 10^8$; $1 <= T <= K$).

  La siguiente línea contiene un entero $N$ ($1 <= N <= 100$), la cantidad
  de lokomones que Ashrias tiene como opción para capturar.

  Luego vienen $N$ líneas. La $i$-ésima contiene tres enteros $H_i$,
  $A_i$ y $T_i$: la vida, el ataque y el tipo del $i$-ésimo lokomon que
  Ashrias puede capturar
  ($1 <= H_i <= 10^9$; $1 <= A_i <= 10^8$; $1 <= T_i <= K$).
  Estos lokomones están numerados del $1$ al $N$ según su orden en la
  entrada.
]

#outputDescription[
  Si existe algún lokomon con el que Ashrias pueda ganar la batalla,
  imprime su índice (un entero entre $1$ y $N$). Si hay varias opciones,
  puedes imprimir cualquiera de ellas. Si ninguno le permite ganar,
  imprime $-1$.
]

#scoreDescription[
  #subtask(30)[
    La vida de Vichochú y la de cada uno de los $N$ lokomones que Ashrias
    puede capturar es a lo más $1000$ ($H <= 1000$ y $H_i <= 1000$ para todo $i$).
  ]

  #subtask(70)[
    Sin restricciones adicionales.
  ]
]

#sampleDescription[
  #sampleIO("sample-1")

  En este ejemplo, si Ashrias captura el segundo lokomon, Vichochú le
  quita $3 dot.op 2 = 6$ puntos de vida. Como este tenía $7$ puntos de
  vida, alcanza a responder. Su ataque causa $4 dot.op 3 = 12$ puntos de
  daño, suficientes para derrotar a Vichochú, que tenía $12$ puntos de vida.

  #sampleIO("sample-2")
]
