#import "oci.typ": *

#show: problem.with(
  title: "El arco de Lonk",
)

#problemDescription[
  En la última aventura de la saga _La leyenda de Zolda_, Lonk está a punto
  de enfrentarse a Mitundorf. Solo le queda cruzar un corredor lleno de
  meblins. Su espada se rompió en el último combate y ya no puede usar su
  ataque de giro. Para abrirse paso, tendrá que recurrir a su arco.

  Lonk tiene $E$ unidades de energía y quiere saber si le alcanzan para
  derrotar a todos los meblins del corredor o si tendrá que descansar antes
  de intentarlo.

  El corredor se representa como una recta con posiciones enteras.
  Lonk comienza en la posición $0$ y su objetivo es derrotar a los $N$ meblins
  distribuidos a lo largo del corredor.
  Los meblins se numeran de $1$ a $N$ y el meblin número $i$ se
  mantiene fijo en la posición $x_i$ hasta ser derrotado.
  Dadas dos posiciones $p$ y $q$ sobre el corredor, la distancia entre ellas
  se define como $abs(p - q)$.

  Para derrotar a los meblins, Lonk puede realizar dos acciones:

  - *Saltar.* Lonk elige otra posición entera a su izquierda o a su
    derecha y salta a esta gastando tanta energía como la distancia
    que recorre.
    Puede pasar por encima de los meblins, pero siempre debe aterrizar
    en una posición libre.

  - *Disparar.* Lonk elige un meblin vivo a cualquiera de sus lados y
    dispara una de sus flechas.
    Gasta tanta energía como la distancia al objetivo.
    El disparo derrota al meblin de inmediato y deja libre su posición,
    por lo que luego Lonk puede aterrizar en ella.

  Lonk puede combinar saltos y disparos en cualquier orden. Ayúdalo a
  determinar si puede derrotar a todos los meblins sin gastar más de $E$
  unidades de energía.
]

#inputDescription[
  La primera línea contiene dos enteros $N$ y $E$: la cantidad de meblins
  ($1 <= N <= 10^5$) y la energía disponible de Lonk ($1 <= E <= 10^9$).

  La segunda línea contiene $N$ enteros $x_1, x_2, dots, x_N$, donde $x_i$
  es la posición del meblin número $i$ ($1 <= x_i <= 10^9$). Todas las
  posiciones son distintas.
]

#outputDescription[
  Imprime `YES` si Lonk puede derrotar a todos los meblins gastando como
  máximo $E$ unidades de energía. En caso contrario, imprime `NO`.
]

#block(breakable: false)[
  #scoreDescription[
    #subtask(5)[
      Hay un solo meblin ($N = 1$).
    ]
    #subtask(25)[
      Los meblins ocupan $N$ posiciones consecutivas.
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

    En el primer ejemplo, una estrategia posible es la siguiente:

    #[
      #set enum(numbering: "a.")
      + Desde la posición $0$, dispara al meblin en la posición $2$ (gasta $2$).
      + Salta a la posición $2$, que ya está libre (gasta $2$).
      + Salta por encima del meblin en $5$ hasta la posición $7$ (gasta $5$).
      + Desde la posición $7$, dispara al meblin en la posición $5$ (gasta $2$).
      + Desde la posición $7$, dispara al meblin en la posición $8$ (gasta $1$).
    ]

    En total, Lonk gasta $2 + 2 + 5 + 2 + 1 = 12$ unidades de energía. Como
    dispone de $13$, la respuesta es `YES`.

    #sampleIO("sample-2")
  ]
]
