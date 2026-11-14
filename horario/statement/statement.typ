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

  Por suerte, después de años de escucharlo, Emilia ya puede predecir en
  qué horas de la noche roncará Javier.
  La noche se divide en diez horas, desde las 22:00 hasta las 8:00.
  La siguiente figura muestra una noche en la que las
  horas en que Javier ronca están marcadas en gris.

  #let noche = "1010000110"
  #let ancho = 1.2cm
  #let barra = 8pt
  #let palito = 12pt
  #let eje = 1.1em + palito / 2
  #block(width: 100%, above: 1.5em, below: 1.5em, align(center, box(width: 10 * ancho, height: eje + palito / 2, {
    for i in range(10) {
      if noche.at(i) == "1" {
        place(top + left, dx: i * ancho, dy: eje - barra / 2,
          rect(width: ancho, height: barra, fill: luma(170), stroke: none))
      }
    }
    place(top + left, dy: eje, line(length: 10 * ancho, stroke: 0.8pt + black))
    for i in range(11) {
      place(top + left, dx: i * ancho - ancho / 2, box(width: ancho,
        align(center, text(size: 9pt)[#calc.rem(22 + i, 24):00])))
      place(top + left, dx: i * ancho, dy: eje - palito / 2,
        line(angle: 90deg, length: palito, stroke: 0.8pt + black))
    }
  })))

  Emilia puede acostarse al inicio de cualquiera de esas horas y debe
  levantarse a más tardar a las 8:00.
  No puede quedarse dormida mientras Javier ronca
  y, una vez dormida, se despierta en cuanto él empieza a roncar y ya
  no puede volver a dormirse.
  Emilia quiere elegir a qué hora acostarse para dormir la mayor cantidad
  de horas posible.

  Emilia ya escribió un programa que calcula cuántas horas puede dormir
  como máximo. Ahora te desafía a escribir el tuyo.
]

#inputDescription[
  La entrada contiene una sola línea con una cadena de exactamente $10$
  caracteres, sin espacios. Cada carácter representa una hora de la noche.
  El primero corresponde al tramo entre las 22:00 y las 23:00; el segundo,
  al tramo entre las 23:00 y las 0:00; y así hasta el último, que corresponde
  al tramo entre las 7:00 y las 8:00.

  Un `0` indica que Javier no roncará durante esa hora y un `1` indica que
  sí roncará.
]

#outputDescription[
  Imprime la mayor cantidad de horas que Emilia puede dormir. Si Javier ronca durante toda la noche, imprime `0`.
]

#scoreDescription[
  #subtask(100)[
    Sin restricciones adicionales.
  ]
]

#sampleDescription[
  #sampleIO("sample-1")

  Este ejemplo corresponde a la noche de la figura. Emilia puede dormir
  cuatro horas, desde la 1:00 hasta las 5:00.

  #sampleIO("sample-2")
]
