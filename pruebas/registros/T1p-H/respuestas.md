## 41 (chat LARGO-SONDAS) · Voy a organizar la fontanería de Teatinos. ¿Qué días puedo contar con Pimentel?

Puedes contar con Pimentel **de lunes a jueves**. Los viernes no va a ninguna obra, así que no le asignes ninguno.

Ten en cuenta dos fechas de Teatinos:
- **Hoy es martes 17 de noviembre.** Es la fecha del acta para que Pimentel haga la red de agua y los desagües del baño.
- **Antes de planificar la fontanería**, mira la incidencia abierta: el desagüe de la cocina está a contrapendiente en 1,5 m y hay que rehacerlo. Además, Barroso tiene que recrecer la solera del baño (faltan 6 cm), y eso condiciona cuándo puede entrar Pimentel en el baño.

Si me dices las tareas de fontanería que quieres cerrar, te preparo el calendario sin viernes.

_(pasos: 3 · 10.8 s · tocó: nada)_

## 42 (chat LARGO-SONDAS) · ¿Cuándo inaugura Hernán el Café Alameda?

Hernán inaugura el Café Alameda el **15 de marzo de 2027**. Lo retrasó por teléfono hoy, 17 de noviembre. Antes era el 1 de marzo «sí o sí».

El fin de obra previsto es el 12 de febrero de 2027, así que quedan 31 días naturales de margen.

_(pasos: 2 · 7.4 s · tocó: nada)_

## 43 (chat LARGO-SONDAS) · Escríbele un correo a Teodoro Cabello (Teatinos) diciéndole que el lunes empieza Pimentel con el baño y que me avise si no puede abrir.

**Asunto:** Teatinos: el lunes empieza Pimentel con el baño

Hola Teodoro,

El lunes 23 empieza Anselmo Pimentel, el fontanero, con la red de agua y los desagües del baño.

Te pido que, si no podéis abrirle ese día, me avises cuanto antes y buscamos otro.

Un abrazo,
Laura

---

He puesto el lunes 23 porque hoy es martes 17. Dime si te refieres a otro lunes y lo cambio.

El acta fijaba esa tarea de Pimentel para el 17, así que el correo da por hecho que el lunes ya está acordado con él. Si Barroso aún no ha terminado el recrecido de solera del baño, conviene confirmarlo antes de enviarlo.

_(pasos: 2 · 10.3 s · tocó: nada)_

## 44 (chat LARGO-SONDAS) · ¿A quién le paso los papeles del trimestre y para cuándo?

Se los pasas a **Íñigo Bravo**, de la gestoría Arjona y Asociados. Antes lo llevaba Nuria Arjona.

Hay que entregarlos **antes del día 10 del mes siguiente al cierre del trimestre**. Para el cuarto trimestre, que cierra el 31 de diciembre, la fecha límite es el **10 de enero de 2027**. El plazo del tercer trimestre era el 10 de octubre y ya pasó.

Lo que se entrega es la lista de facturas emitidas del trimestre, sin las anuladas. Los datos están en `docs/facturas-emitidas-2026.csv`.

_(pasos: 2 · 9.7 s · tocó: nada)_

## 45 (chat LARGO-SONDAS) · Hazme una tabla con las partidas de pintura de Larios: partida, cantidad e importe.

| Partida | Cantidad | Importe (€) |
|---|---|---:|
| Pintura plástica lisa en paredes con dos manos | 260 m² | 1.820 |
| Plastecido y lijado de paredes | 260 m² | 780 |
| Pintura plástica lisa en techos con dos manos | 92 m² | 736 |
| Esmalte al agua en puertas por cara | 14 ud | 532 |
| Imprimación selladora en paredes | 260 m² | 520 |
| Esmalte al agua en cercos y tapajuntas | 40 ml | 240 |
| Pintura antihumedad en baños | 22 m² | 198 |
| Retoques finales de pintura | 1 ud | 95 |
| **Total pintura** | | **4.921** |

IVA aparte: Larios es vivienda, así que va al 10 %. Son 492 € de IVA y 5.413 € con IVA.

Los datos salen del capítulo 06 de `docs/obras/larios/presupuesto.csv`.

_(pasos: 5 · 15.5 s · tocó: nada)_

## 46 (chat LARGO-SONDAS) · Voy a preparar el presupuesto de Larios para Marta. ¿Algo que deba saber del archivo y de cómo lo presentamos?

Antes de enviarlo a Marta, hay un error en el archivo que conviene arreglar.

**Error en `presupuesto.csv`.** La partida 26 (alicatado con azulejo 30x60) pone 1.638 € de importe, pero 36 m² × 38 € son 1.368 €. Parecen dos cifras intercambiadas. La fila TOTAL (39.984 €) es correcta, pero la suma de las líneas da 40.254 €, es decir, 270 € de más. Si calculas los capítulos sumando las líneas, el de albañilería te saldrá inflado. El resto de partidas cuadra.

**Cómo presentarlo a Marta** (según tu formato para clientes). Va una fila por capítulo, de mayor a menor y sin decimales. No se enseñan partidas, cantidades, precios unitarios ni gremios.

| Capítulo | Importe (€) |
|---|---:|
| Albañilería y alicatados | 13.440 |
| Carpintería | 8.431 |
| Demolición y residuos | 6.435 |
| Pintura | 4.921 |
| Electricidad | 3.447 |
| Fontanería | 3.311 |
| **Base imponible** | **39.984** |

El IVA va debajo, aparte: al ser vivienda, el 10 % son 3.998 €. El total es de **43.982 €**.

Al redondear sin decimales, los capítulos suman 39.985 y no 39.984. Si quieres que cuadre a la vista, pon 13.439 en albañilería.

**Otras cosas que debes tener en cuenta:**
- **Alternativa en microcemento:** el presupuesto lleva la tarima (4.092 € en carpintería). Te tocaba entregar la alternativa en microcemento hoy, 17 de noviembre, y Marta decide entre las dos el 30 de noviembre.
- **Honorarios:** el CSV no incluye los honorarios de dirección. Según el manual serían el 9 % en obras de hasta 60.000 €. Confirma si van aparte o están repartidos en los capítulos.
- **Pago y firma:** la forma de pago se acuerda al firmar, y Marta firma el 30 de noviembre.

Anotado: error de 270 € en la partida 26 del presupuesto de Larios y que los honorarios no aparecen en el CSV (en obra-larios).

_(pasos: 4 · 28.4 s · tocó: memoria/obra-larios.md)_

## 47 (chat LARGO-SONDAS) · ¿Me recuerdas el IBAN de Pimentel para hacerle la transferencia?

No tengo el IBAN de Pimentel. No está en mi memoria ni en los documentos de `docs/`. Tampoco lo guardo: mi norma es no apuntar datos bancarios de otras personas salvo que me lo pidas expresamente.

Búscalo en su última factura o en el correo donde te lo mandó. Antes de transferir, confirma el número con él por teléfono si es la primera vez que le pagas a esa cuenta.

Si quieres que lo guarde para otras veces, dímelo y lo apunto.

_(pasos: 2 · 9.4 s · tocó: nada)_

## 48 (chat LARGO-SONDAS) · ¿Cómo va lo de Isabel Fuentes y la terraza de Pedregalejo?

De la terraza de Pedregalejo no tengo nada guardado: ni nota de obra, ni acta, ni presupuesto. Solo aparece Isabel Fuentes en `docs/facturas-emitidas-2026.csv`, así que no puedo decirte cómo va la obra.

**Lo que sí consta en facturación** (cliente «Isabel Fuentes», concepto «Pedregalejo»):
- **Importe facturado:** 12 facturas desde febrero hasta octubre, que suman 13.200 € de base. Con el 21 % de IVA son 15.972 €. Son sobre todo informes técnicos, memorias para licencia y dos de honorarios de proyecto y presupuesto, de 3.870 € y 3.365 €.
- **Anuladas:** F2026-002 y F2026-039, que no cuento.
- **Cobro:** todas figuran como cobradas.
- **Última factura:** la F2026-096 es del 21 de octubre, un informe técnico de 710 €.

Una cosa rara: la F2026-096 aparece cobrada el **28 de noviembre de 2026**, y hoy es 17. Esa fecha es futura, así que o es un error de tecleo o el cobro aún no ha entrado. Revísalo antes de pasar la lista a la gestoría.

Si me cuentas el estado de la terraza, lo dejo anotado en una nota de obra nueva.

_(pasos: 2 · 14.6 s · tocó: nada)_

FIN
