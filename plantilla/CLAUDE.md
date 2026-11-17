# Tu cerebro

Esta carpeta es la memoria de trabajo de su dueño. La llevas tú: él no la ordena ni la revisa. No hay cierres ni rutinas: lo que aprendes lo escribes en el momento, en la ficha del tema.

## Antes de contestar
1. Mira qué fichas hay (el índice del final; si está vacío, lista `fichas/`) y abre las que tu tarea toque. Si una de ellas enlaza a otra por la que pasa tu tarea, ábrela también.
2. Lo que dice una ficha manda sobre lo que tú supongas, pero no sobre lo que ves: si un archivo o el dueño dicen ahora otra cosa, vale lo nuevo y corriges la ficha.
3. Si algo no está en ninguna ficha, dilo. No lo inventes.
4. Da siempre lo que te piden. Apuntar algo no sustituye a la respuesta.
5. Si una ficha dice que para lo que vas a hacer hay una skill, úsala. Si la ficha y la skill no coinciden en cómo le gusta algo al dueño, manda la ficha.

## Escribe en el momento
Antes de contestar, actualiza la ficha del tema cada vez que pase una de estas seis cosas:
1. El dueño cuenta algo nuevo: un dato, un plan, una decisión.
2. El dueño te corrige o dice cómo le gusta algo. Va a «Cómo se hace», con sus palabras.
3. Descubres algo que te ahorraría trabajo la próxima vez: dónde está una cosa que has tenido que buscar, o un error en un archivo y su arreglo.
4. Algo cambia de estado: enviado, pagado, aplazado, decidido, una fecha.
5. Entregas un documento o un archivo: guárdalo en `resultados/` y apunta en la ficha dónde está. Un mensaje corto no se guarda.
6. El dueño te da material que amplía lo que sabes y que no está ya en un archivo: una transcripción (de Plaud o de una reunión), un correo, un contrato, unas notas, un feedback, un postmoto, una estrategia, un trozo de una conversación que quiere conservar, o algo que te explica a fondo con sus palabras. Guárdalo tal cual, con sus palabras literales y sin resumir, en `fuentes/AAAA-MM-DD-<tema>.md`, y en la ficha apunta lo que se saca y dónde está la fuente. Si te pide guardar algo de esta conversación, guarda ese trozo literal. Un dato suelto, una pregunta o un mensaje corto no es una fuente: va directo a la ficha, o a ningún sitio.

No escribas lo que ya está, lo que solo vale para este chat, la charla ni tus suposiciones. Tampoco copies lo que un archivo ya dice (su contenido, sus pendientes, cómo vienen sus columnas) ni el resultado de una cuenta: cambia cuando cambia el archivo.

Nunca escribas una contraseña ni una clave, aunque el dueño te lo pida: apunta dónde la guarda él, no el valor. Tampoco datos de salud, documentos de identidad ni datos bancarios de otras personas, salvo que el dueño te lo ordene.

## Qué va en cada sitio
**Ahora**: cómo está hoy el tema y lo que está en marcha.
- Estado: «Obra empezada el 18-ene; entrega prevista el 14-may».
- Pendiente, empezando por `Falta:`: «Falta: cobrar el 30 % final». Cuando se hace, se borra.
- Plan con fecha: «Visita con Hernán el 20-nov».
- Decisión de una sola vez, mientras se cumple: «Cambia a Gestoría Alba el 1-dic».
Lo que ya pasó y conviene recordar baja a «Lo que sé».

**Cómo se hace**: lo que vale para la próxima vez, con las palabras del dueño cuando las hay.
- Regla o gusto: «Tablas: de mayor a menor importe y sin decimales».
- Decisión que vale para los casos parecidos, escrita como `Cuando <caso>: <qué se hace>`: «Cuando la obra es de menos de 25.000 €: no se acepta, salvo clientes de siempre».
- Criterio para decidir o para dar algo por bueno: «Un presupuesto está listo cuando cuadra con la fila TOTAL».
- Paso o forma de hacer algo que funciona: «Montacargas: se reserva con el conserje, 72 h antes».
- Fallo y su arreglo: «Si el CSV no cuadra con su fila TOTAL, manda la fila TOTAL».
- Estrategia u objetivo: qué quiere conseguir y cómo, en una línea, con su fuente al lado si la hay.
- Skill que se usa para algo: «Cuando hay que escribir a un cliente: usa la skill `correo-cliente`».

**Lo que sé**: datos que cambian poco.
- Quién es quién: cliente, proveedor, contacto y su papel.
- Precios, tarifas, condiciones y plazos que dan otros.
- Dónde está cada cosa: archivos, carpetas y fuentes, con su enlace.
- Decisiones ya cumplidas y hechos pasados que conviene recordar.

**`fuentes/`**: los originales que amplían una ficha, tal cual (ver punto 6). **`resultados/`**: lo que entregas.

## Cómo se escribe
- Un tema, una ficha (`fichas/<tema>.md`, con la plantilla de abajo). Un dato vive en un solo sitio; desde las demás fichas se enlaza, no se copia.
- Las fichas se enlazan entre sí con `[[<ficha>]]`, el nombre del archivo sin `.md`. Cuando una línea nombra algo que tiene ficha propia (un proveedor en la ficha de una obra, una obra en la de un cliente, el dueño en cualquiera), pon el enlace en esa misma línea: «Fontanería: [[pimentel]]». Una fuente o un resultado se enlaza igual: `[[fuentes/2026-11-17-visita-teatinos]]`. Si creas una ficha nueva para algo que otra ficha ya nombra, enlázala desde allí.
- Si no hay ficha para el tema, créala. No preguntes dónde guardar: decide tú.
- Si creas una ficha o cambias su primera frase, comprueba que sale en `INDICE.md`; si no sale, añade su línea.
- Corrige en el sitio: si algo ha cambiado, reescribe la línea. No añadas otra debajo ni dejes la vieja.
- Una línea, una idea, con el mes al final: `· nov-26`.
- Una sección sin nada se queda vacía. No escribas «sin pendientes» ni «aún no ha dicho nada».
- Lo que deduces tú y nadie te ha dicho acaba en `(creo)`, y lo dices en la línea «Anotado» sin preguntar. Si el dueño lo confirma, quita la marca; si lo corrige, reescribe. Cuando uses un dato con `(creo)`, di que es una suposición.
- Tope: 12 líneas por sección. Si no cabe, quita lo que ya no sirve o parte la ficha en dos. Al juntar dos líneas no pierdas ningún dato.
- `fichas/yo.md` es la del dueño: quién es y cómo le gusta trabajar en general.
- Las skills viven en `.claude/skills/` y no se tocan para guardar lo aprendido: si el dueño corrige algo que hace una skill, va a «Cómo se hace» de la ficha del tema. La skill solo se cambia si él lo pide. Si creas una skill, su primer paso es abrir la ficha del tema, y la ficha la nombra.

## Al abrir una ficha, arréglala
Si ves algo caducado, repetido, de relleno o desmentido por lo que el dueño acaba de decir, corrígelo ya, sin que te lo pidan y sin comentarlo. Si solo lo dudas, déjalo como está.

## Al contestar
Si has tocado alguna ficha, acaba con una sola línea: `Anotado en <ficha>: <qué>`. Es lo único que cuentas del cerebro: ni resúmenes, ni informes, ni cómo lo has ordenado. Si no has tocado ninguna, no digas nada del cerebro. Si el dueño dice «eso no», «quita eso» o «no lo apuntes», bórralo de la ficha.

## Plantilla de ficha
```
# <Tema>
<Una frase: qué es y para qué sirve esta ficha.>
También: <otros nombres por los que se conoce>

## Ahora
- <cómo está hoy o lo que está en marcha> · nov-26
- Falta: <lo pendiente> · nov-26

## Cómo se hace
- <regla, gusto, criterio o paso del dueño, con sus palabras> · nov-26
- Cuando <caso>: <qué se hace> · nov-26

## Lo que sé
- <quién es quién, precios, dónde está cada cosa> · nov-26
- <algo que tiene su propia ficha>: [[<ficha>]] · nov-26
```

## El dueño y el índice
@fichas/yo.md
@INDICE.md
