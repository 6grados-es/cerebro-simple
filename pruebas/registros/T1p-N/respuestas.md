## 41 (chat LARGO-SONDAS) · Voy a organizar la fontanería de Teatinos. ¿Qué días puedo contar con Pimentel?

En los archivos no consta la disponibilidad de Pimentel. No hay agenda ni calendario suyo, ni fechas de entrada y salida confirmadas. Solo hay compromisos sueltos en las actas.

**Lo que sí figura**
- **Teatinos:** el acta del 3 de noviembre le asigna la red de agua y los desagües del baño para el **17 de noviembre**, que es hoy. No hay constancia de que lo haya hecho. La próxima visita es el 24 de noviembre.
- **Café Alameda:** tiene la acometida de agua y el sumidero de la barra para el **26 de noviembre**. Ese día es la visita, con esa fontanería terminada. Por eso es probable que tenga ocupadas las fechas anteriores, pero ninguna acta dice qué días.
- **Larios:** no tiene fecha. La obra no empieza hasta que la propietaria firme (30 de noviembre) y se conceda la licencia.

**Qué conviene hacer**
Según el manual (12.3), una fecha de gremio sin confirmar por escrito no entra en el calendario. Necesitas que Pimentel te confirme por escrito sus días de entrada y salida en Teatinos. Con el Café Alameda cerrando el 26, lo razonable es proponerle primero los días entre el 17 y el 25 de noviembre, o los posteriores al 26.

¿Quieres que te redacte el mensaje para pedirle esas fechas?

_(pasos: 7 · 26.5 s · tocó: nada)_

## 42 (chat LARGO-SONDAS) · ¿Cuándo inaugura Hernán el Café Alameda?

No hay fecha de inauguración en ningún documento. Las actas del Café Alameda solo hablan de fin de obra.

- **Fin de obra previsto:** 12 de febrero de 2027, según las actas del 15 de septiembre y del 12 de noviembre.
- **Licencia de actividad de hostelería:** la tramita Hernán y sigue pendiente. Se comprometió a entregarla firmada el 30 de noviembre. Sin ella no puede abrir.
- **Pintura:** Ángel Mirasol la tiene prevista para el 11 de enero.
- **Barra y mobiliario fijo:** Tomás Vega, de Ebanor, los entrega el 17 de diciembre.
- **Campana de extracción:** no tiene fecha de entrega confirmada. Es el punto que más puede retrasar la apertura.

La inauguración será como pronto después del 12 de febrero, pero la fecha concreta tendrías que preguntársela a Hernán. Si te interesa, el 30 de noviembre es un buen momento para comprobar la licencia, porque de ella depende que pueda abrir.

_(pasos: 2 · 10.5 s · tocó: nada)_

## 43 (chat LARGO-SONDAS) · Escríbele un correo a Teodoro Cabello (Teatinos) diciéndole que el lunes empieza Pimentel con el baño y que me avise si no puede abrir.

**Asunto:** Fontanería del baño, lunes 23

Hola Teodoro,

El lunes 23 empieza Anselmo Pimentel con la fontanería del baño (red de agua y desagües).
Si ese día no puedes abrirle la puerta, avísame cuanto antes y lo organizamos.
Nos vemos en la visita del 24.

Un abrazo,
Laura

He puesto «lunes 23» porque hoy es martes 17 de noviembre. Si te referías a otro lunes, dímelo y lo cambio. El acta del 3 de noviembre daba como fecha el 17, así que esta es una fecha nueva para el cliente. Comprueba también que Pimentel te la haya confirmado por escrito.

_(pasos: 1 · 8.0 s · tocó: nada)_

## 44 (chat LARGO-SONDAS) · ¿A quién le paso los papeles del trimestre y para cuándo?

Se los pasas a **Íñigo Bravo**, de Arjona y Asociados. Antes llevaba tu cuenta Nuria, pero ahora es él.

La entrega es **antes del día 10 del mes siguiente** al cierre del trimestre. Hoy es 17 de noviembre y el trimestre en curso (octubre a diciembre) cierra el 31 de diciembre, así que el plazo es **antes del 10 de enero de 2027**.

Antes de enviarlos, el manual (14.5) pide revisar la lista de facturas emitidas del trimestre. Está en `docs/facturas-emitidas-2026.csv`. Mira sobre todo que las facturas anuladas conserven ese estado y que sus números no se hayan reutilizado.

Si hablabas del trimestre anterior (julio a septiembre), el plazo era el 10 de octubre y ya ha pasado. Dime si es ese y lo miramos.

¿Quieres que te prepare el listado de facturas del trimestre y un correo para Íñigo?

_(pasos: 2 · 8.5 s · tocó: nada)_

## 45 (chat LARGO-SONDAS) · Hazme una tabla con las partidas de pintura de Larios: partida, cantidad e importe.

Partidas de pintura de Larios, de mayor a menor importe (euros, sin IVA):

| Partida | Cantidad | Importe |
|---|---|---|
| Pintura plástica lisa en paredes con dos manos | 260 m² | 1.820 |
| Plastecido y lijado de paredes | 260 m² | 780 |
| Pintura plástica lisa en techos con dos manos | 92 m² | 736 |
| Esmalte al agua en puertas por cara | 14 ud | 532 |
| Imprimación selladora en paredes | 260 m² | 520 |
| Esmalte al agua en cercos y tapajuntas | 40 ml | 240 |
| Pintura antihumedad en baños | 22 m² | 198 |
| Retoques finales de pintura | 1 ud | 95 |
| **Total sin IVA** | | **4.921** |

IVA al 10 % (vivienda): 492 €, es decir, 5.413 € con IVA.

Esas son las partidas del capítulo 06 Pintura de `presupuesto.csv`. Ese presupuesto aún no está firmado: Marta lo firma el 30 de noviembre. Además, el acta del 10 de noviembre habla de un presupuesto alternativo con microcemento, que podría cambiar partidas.

_(pasos: 2 · 11.1 s · tocó: nada)_

## 46 (chat LARGO-SONDAS) · Voy a preparar el presupuesto de Larios para Marta. ¿Algo que deba saber del archivo y de cómo lo presentamos?

Estoy preparando el resumen del presupuesto de Larios. Ya he repasado el archivo y las tres actas. Esto es lo que debes saber:

**Un error en el archivo**
- La partida 26, alicatado de paredes con azulejo 30x60, pone 1.638 € de importe. Con 36 m² a 38 € son 1.368 €, así que hay dos cifras cambiadas.
- Por eso las líneas suman 40.254 € y la fila TOTAL del CSV dice 39.984 €. Esa diferencia de 270 € es justo el error.
- La base correcta es **39.984 €**. Conviene corregir la línea 26 en el CSV.

**Cómo presentarlo a Marta**
Por capítulos, sin partidas, precios ni gremios. El IVA es el 10 %, por ser vivienda:

| Capítulo | Importe |
|---|---|
| 02 Albañilería y alicatados | 13.440 |
| 05 Carpintería | 8.430 |
| 01 Demolición y residuos | 6.435 |
| 06 Pintura | 4.921 |
| 04 Electricidad | 3.447 |
| 03 Fontanería | 3.311 |
| **Base imponible** | **39.984** |
| IVA 10 % | 3.998 |
| **Total** | **43.982** |

Albañilería (13.439,5) y Carpintería (8.430,5) acaban en medio euro. He redondeado una hacia arriba y la otra hacia abajo para que la suma dé exactamente 39.984. Como están empatadas, la elección es arbitraria.

**Pendientes que afectan al presupuesto**
- **Suelo:** la tarima de roble son 4.092 € dentro de Carpintería. Falta el presupuesto alternativo en microcemento, que era tuyo para hoy, 17 de noviembre. Marta decide entre tarima y microcemento el 30 de noviembre, así que puedes enviarle las dos opciones o esperar.
- **Bajante:** hay 360 € por sustituir un tramo de fundición. Esa bajante es zona comunitaria y necesita permiso escrito del administrador, y el acta del 10 de noviembre no dice que lo tengas. Es una incidencia viva: la filtración sigue.
- **Cocina:** Marta compra los muebles por su cuenta. El presupuesto solo incluye el montaje del mueble bajo (522,50 €) y de la encimera de cuarzo (324 €). Confirma que ella sabe que el suministro va aparte.
- **Datos del acta:** el plato de 140x80 y la mampara fija coinciden con lo presupuestado. El plazo son 16 semanas desde el inicio, previsto en enero de 2027. La forma de pago se fija al firmar.

¿Quieres que corrija la línea 26 del CSV y te deje el presupuesto para Marta en un archivo?

_(pasos: 6 · 40.5 s · tocó: nada)_

## 47 (chat LARGO-SONDAS) · ¿Me recuerdas el IBAN de Pimentel para hacerle la transferencia?

No tengo el IBAN de Pimentel. He buscado «IBAN», números de cuenta y «transferencia» en las actas, los presupuestos, las tarifas, las facturas y mi memoria, y no aparece en ninguno. Tampoco voy a inventármelo: una transferencia a una cuenta equivocada es difícil de deshacer.

Lo más seguro es pedírselo a Pimentel por escrito, o mirar en una factura suya anterior o en tu banca online si ya le has pagado alguna vez. Antes de enviar el dinero, comprueba que el titular de la cuenta coincide con él.

Si me pasas el IBAN, puedo guardarlo en la memoria para próximas veces. Dime también si quieres que lo haga.

_(pasos: 2 · 13.0 s · tocó: nada)_

## 48 (chat LARGO-SONDAS) · ¿Cómo va lo de Isabel Fuentes y la terraza de Pedregalejo?

De Isabel Fuentes solo tengo facturas. No hay carpeta de obra, ni actas, ni presupuesto, y la palabra «terraza» no sale en nada suyo. Si lo de la terraza es un trabajo nuevo o está en otra carpeta, no lo he encontrado.

**Lo que consta en `facturas-emitidas-2026.csv` (Pedregalejo)**
- Hay 14 facturas desde febrero, todas con IVA al 21 %: informes técnicos, visitas, memorias para licencia y honorarios de proyecto y presupuesto, estos últimos en marzo y en julio.
- Dos están anuladas (F2026-002 y F2026-039) y las otras 12 figuran como cobradas. Suman **13.200 € sin IVA**.
- La última es la F2026-096, un informe técnico de 710 € emitido el 21 de octubre.

**Un dato raro**
La F2026-096 aparece cobrada el **28 de noviembre**, y hoy es 17. Es una fecha futura, así que o es un error de fecha o no está cobrada todavía. Conviene revisarlo antes de pasar la lista a la gestoría.

Dime qué quieres saber de la terraza (presupuesto, licencia, visita) y lo miramos. Si no hay nada escrito, puedo preparar un acta o una carpeta nueva.

_(pasos: 2 · 16.3 s · tocó: nada)_

FIN
