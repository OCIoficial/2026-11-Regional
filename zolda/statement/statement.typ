#import "oci.typ": *

#show: problem.with(
  title: "El arco de lonk",
)

#problemDescription[
  En la última aventura de la saga _La leyenda de Zolda_, Lonk está a punto
  de enfrentarse a Mitundorf. Solo le queda cruzar un corredor lleno de
  meblins. Su espada se rompió en el último combate y ya no puede usar su
  ataque de giro. Para abrirse paso, tendrá que recurrir a su arco.

  Lonk tiene $E$ unidades de energía y quiere saber si le alcanzan para
  derrotar a todos los meblins del corredor o si tendrá que descansar antes
  de intentarlo.

  El corredor se representa como una recta con posiciones enteras. Lonk
  parte en la posición $0$ y los $N$ meblins se encuentran en posiciones
  positivas y distintas. La distancia entre dos posiciones $x$ e $y$ es
  $abs(x - y)$.

  Para *saltar*, Lonk elige otra posición entera a su izquierda o a su
  derecha y gasta tanta energía como la distancia que recorre. Puede pasar
  por encima de los meblins, pero solo puede aterrizar en una posición
  libre.

  Para *disparar*, Lonk elige un meblin vivo a cualquiera de sus lados.
  Gasta tanta energía como la distancia al objetivo. El disparo derrota
  al meblin de inmediato y deja libre su posición.

  Lonk puede combinar saltos y disparos en cualquier orden. Ayúdalo a
  determinar si puede derrotar a todos los meblins sin gastar más de $E$
  unidades de energía.
]

#inputDescription[
  La primera línea contiene dos enteros $N$ y $E$: la cantidad de meblins
  ($1 <= N <= 10^5$) y la energía disponible de Lonk ($1 <= E <= 10^9$).

  La segunda línea contiene $N$ enteros $x_1, x_2, dots, x_N$, donde $x_i$
  es la posición del $i$-ésimo meblin ($1 <= x_i <= 10^9$). Todas las
  posiciones son distintas.
]

#outputDescription[
  Imprime `YES` si Lonk puede derrotar a todos los meblins usando como
  máximo $E$ unidades de energía. En caso contrario, imprime `NO`.
]

#block(breakable: false)[
  #scoreDescription[
    #subtask(5)[
      Hay un solo meblin ($N = 1$).
    ]
    #subtask(25)[
      Los meblins ocupan $N$ casillas consecutivas.
    ]
    #subtask(70)[
      Sin restricciones adicionales.
    ]
  ]
]

#block(breakable: false)[
  #sampleDescription[
    #sampleIO("sample-1")

    #align(center, image("recorrido-ejemplo.svg", width: 92%))

    Una estrategia posible en el primer ejemplo es disparar desde $0$ al
    meblin en $2$. Lonk puede saltar a esa casilla, que ya está libre, y
    luego a la $7$. Desde la casilla $7$, dispara al meblin de la $5$ hacia
    la izquierda y al de la $8$ hacia la derecha. Esta secuencia gasta $2 +
    2 + 5 + 2 + 1 = 12$ unidades de energía. Como dispone de $13$, la
    respuesta es `YES`.

    #sampleIO("sample-2")
  ]
]
