// Autor: Blaz Korecic
#import "oci.typ": *

#show: problem.with(
  title: "Una noche de ronquidos",
)

#set par(spacing: 0.85em)
#show heading: set block(above: 0.9em, below: 0.6em)

#problemDescription[
  Mañana Emilia tocará su flautanahoria en la Orquesta de Comida
  Instrumental (OCI). Está nerviosa por el concierto y quiere dormir bien,
  pero comparte habitación con su hermano Javier, que ronca tan fuerte
  que la despierta.

  #align(center)[
    #stack(
      dir: ttb,
      spacing: 3pt,
      image("flautanahoria.png", width: 36%, alt: "Una flauta hecha con una zanahoria."),
      text(size: 10pt, style: "italic")[Una flautanahoria.],
    )
  ]

  Por suerte, después de años de escucharlo, Emilia ya sabe en qué horas
  de la noche roncará Javier. Puede acostarse a una hora en punto a partir
  de las 22:00 y debe levantarse a más tardar a las 8:00. Si se despierta
  durante la noche, ya no puede volver a dormir. Por eso quiere elegir la
  hora de acostarse que le permita dormir más horas seguidas sin ronquidos.

  Emilia ya escribió un programa que calcula cuántas horas seguidas
  puede dormir. Ahora te desafía a escribir el tuyo.
]

#inputDescription[
  La entrada contiene una sola línea con una cadena de exactamente $10$
  caracteres, sin espacios. Cada carácter representa una hora de la noche.
  El primero corresponde al tramo entre las 22:00 y las 23:00 y el último,
  al tramo entre las 7:00 y las 8:00.

  Un `0` indica que Javier no roncará durante esa hora y un `1` indica que
  sí roncará.
]

#outputDescription[
  Imprime la mayor cantidad de horas consecutivas que Emilia puede dormir
  sin ronquidos. Si Javier ronca durante toda la noche, imprime `0`.
]

Este problema tiene una sola subtarea de 100 puntos.

#sampleDescription[
  #sampleIO("sample-1")

  Emilia puede dormir cuatro horas seguidas, desde la 1:00 hasta las 5:00.

  #sampleIO("sample-2")
]
