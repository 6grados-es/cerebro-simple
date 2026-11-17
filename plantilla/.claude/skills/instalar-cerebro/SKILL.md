---
name: instalar-cerebro
description: Llena el cerebro la primera vez leyendo los chats de Claude del dueño del último mes (la exportación de claude.ai y los chats de la pestaña Code), con un lector por chat y un escritor por ficha, y crea las fichas, las fuentes y los resultados. Pensada para caber en media sesión de un plan Pro. Úsala cuando el dueño diga «instala mi cerebro», «carga mis chats», «lee mis chats antiguos» o «sigue con la instalación». Se puede cortar y seguir.
---

# Instalar el cerebro

Lee los chats recientes del dueño y llena `fichas/`, `fuentes/` y `resultados/` con las reglas de `CLAUDE.md`. Se hace una vez. Si se corta por el límite de uso, al volver a decir «instala mi cerebro» sigue por donde iba.

Lo que gasta uso son los agentes; lo que no gasta son los guiones (`trocear.py` y `comprobar.py`). Por eso todo lo que se puede comprobar con un guion se comprueba con un guion, y cada chat lo lee un solo agente.

## 1. Reunir y limpiar los chats (sin agentes)

1. Mira si hay una exportación de claude.ai en `instalacion/`: un `.zip` o un `conversations.json`.
   - Si no la hay y es la primera vez, explícale al dueño cómo pedirla, en cuatro líneas: en claude.ai, Ajustes › Privacidad › Exportar datos. Llega un correo con un enlace que caduca en 24 horas; tiene que descargar el zip y dejarlo, sin abrir, en la carpeta `instalacion/` del cerebro. Mientras tanto, se puede seguir con los chats de Code.
2. Lista los chats de la pestaña Code de este ordenador:
   `python3 .claude/skills/instalar-cerebro/trocear.py --listar-code`
   Enséñale al dueño la lista de carpetas y pregúntale cuáles son de su trabajo. Es la única pregunta de toda la instalación. Si ya te lo ha dicho en este chat, o te dice «todas», no preguntes.
3. Trocea:
   `python3 .claude/skills/instalar-cerebro/trocear.py --code <carpeta> --code <carpeta>` (o `--code-todas`).
   - Deja en `instalacion/chats/` un archivo por chat (los largos, en partes), ya limpio: sin el texto de las skills, con «Sistema» en lo que no escribió el dueño, los turnos numerados y cada uno con su fecha real.
   - Solo entran los chats con mensajes de los últimos 30 días (`--desde AAAA-MM-DD` para cambiarlo) y hasta 1.500.000 caracteres (`--tope N`). Si no cabe todo, entran los más recientes y los demás quedan listados en `instalacion/fuera-por-tope.md`. No subas el tope por tu cuenta: es lo que hace que la instalación quepa en media sesión.
4. `python3 .claude/skills/instalar-cerebro/comprobar.py copia` (guarda cómo están las fichas antes de escribir).

## 2. Un lector por chat, en tandas de 5

Coge los 5 chats más antiguos que queden por leer y lanza un agente por chat, los 5 a la vez, con `model: "sonnet"`. A cada uno le das el encargo de abajo, con el nombre de su chat. Espera a que acaben los 5 antes de seguir.

Encargo para cada agente (sustituye `<chat>`):

> Lee entero `instalacion/chats/<chat>` y las reglas de `CLAUDE.md`. Es un chat antiguo del dueño con Claude. Los turnos van numerados y con su fecha: «## Dueño [3] · 2026-11-12». Solo lo que va bajo «Dueño» lo escribió él; «Sistema» son avisos de la app.
> 1. Si en el chat hay un original que amplía lo que se sabe (una transcripción, un correo, un contrato, unas notas, un feedback, una estrategia, algo que el dueño explica a fondo con sus palabras), guárdalo tal cual, con sus palabras literales, en `fuentes/<fecha del turno>-<tema>.md`. Si el archivo ya existe, añade `-2` al nombre.
> 2. Si Claude entregó en el chat un documento acabado (un presupuesto, un informe, un texto largo para usar), guárdalo en `resultados/<fecha del turno>-<tema>.md`. Un mensaje corto no se guarda.
> 3. No toques `fichas/` ni `INDICE.md`. Escribe en `instalacion/notas/<chat>` las líneas que irían a las fichas, una por línea, con este formato:
>    `<tema> | <Ahora, Cómo se hace o Lo que sé> | <la línea> | <fecha del turno, AAAA-MM-DD> | <enlace a la fuente o al resultado, si lo hay>`
>    Los pendientes empiezan por `Falta:`. Una decisión que vale para el futuro se escribe «Cuando <caso>: <qué se hace>». Una frase va entre «» solo si el dueño la escribió tal cual.
> 4. Apunta solo lo que sirve para la próxima vez:
>    - lo que el dueño ha dicho de cómo quiere algo, o una corrección suya;
>    - una regla, un criterio o un paso; un fallo que puede repetirse y su arreglo;
>    - quién es quién; qué tiene o qué se le ha entregado a cada cliente; precios, condiciones y plazos;
>    - dónde está cada cosa hoy;
>    - un plan o un pendiente que sigue vivo (de las dos últimas semanas).
> 5. No apuntes:
>    - el detalle de un trabajo ya pasado que no se repite (qué se hizo ese día, qué versión se rehízo); de un documento vale cómo quedó al final y dónde está, no sus borradores;
>    - un fallo que ya se arregló y no va a volver;
>    - cómo está hecho por dentro el código de un proyecto: lo guarda su repositorio;
>    - un plan o un estado que el propio chat da después por hecho o por cambiado: apunta solo cómo quedó;
>    - la charla, las suposiciones y lo que solo valía para ese chat.
> 6. Nunca contraseñas ni claves. Tampoco datos de salud, documentos de identidad, cuentas bancarias ni listas de teléfonos o correos de otras personas.
> 7. Si no hay nada que guardar, escribe solo `nada` en la nota.
> Devuelve una línea: cuántas líneas de ficha, fuentes y resultados has dejado.

Cuando acaben los 5, apúntalos al final de `instalacion/progreso.md`, uno por línea, como `- <chat>`, y sigue con la tanda siguiente hasta que no quede ninguno. Entre tanda y tanda no le cuentes nada al dueño.

## 3. Comprobar sin agentes

Con todas las notas escritas:

1. `python3 .claude/skills/instalar-cerebro/comprobar.py citas`: quita las «» a lo que el dueño no escribió tal cual.
2. `python3 .claude/skills/instalar-cerebro/comprobar.py reten`: aparta a `instalacion/retenidas/` las fuentes y resultados con listas de teléfonos o correos, y tapa claves, cuentas bancarias y documentos de identidad.

## 4. Un escritor por ficha

1. Junta las líneas de todas las notas por tema (el primer campo) y ordénalas por fecha. Los temas que son lo mismo con otro nombre, o una sola línea suelta, júntalos tú con el tema más cercano; no lances un agente para eso.
2. Lanza un agente por tema, de 5 en 5, con `model: "sonnet"` y este encargo:

> Lee las reglas de `CLAUDE.md` y `INDICE.md`. Eres el único que escribe en la ficha `<tema>`. Estas son sus líneas, de la más antigua a la más nueva: <líneas>. Pásalas a `fichas/<tema>.md` siguiendo las reglas: si varias dicen lo mismo, una sola con todos los datos; si una posterior cambia lo que decía otra, queda solo cómo es al final; si la ficha ya decía algo y la línea es más antigua que lo que dice la ficha, manda la ficha; enlaces `[[ficha]]` a otras fichas, a fuentes y a resultados; tope de 12 líneas por sección (si no cabe, parte la ficha por subtema como dice `CLAUDE.md`). No escribas nada que no esté en las líneas ni metas comentarios tuyos. No toques otras fichas. Devuelve una línea: líneas escritas y partes creadas.

3. Rehaz `INDICE.md` con una línea por ficha.
4. `python3 .claude/skills/instalar-cerebro/comprobar.py fichas`: dice si se ha perdido alguna línea de las que había, si hay enlaces rotos y si alguna sección pasa de 12. Arregla tú lo que salga, sin lanzar más agentes.

## 5. Al acabar

1. Borra `instalacion/chats/`, `instalacion/notas/` e `instalacion/fichas-antes/`. Deja `instalacion/progreso.md`, la exportación y, si existen, `fuera-por-tope.md` y `retenidas/`.
2. Dile al dueño, en un mensaje corto:
   - cuántos chats has leído, y cuántos se quedaron fuera por el tope;
   - cuántas fichas, fuentes y resultados han quedado;
   - si hay archivos apartados por llevar listas de contactos;
   - que lea `fichas/yo.md` y te diga lo que no esté bien, porque es la que más se usa.
3. No hagas informe ni resumen de lo que has guardado. Si quiere saber algo, que pregunte.

## Opcional: si sobra uso

Solo si el dueño lo pide o tiene un plan con mucho uso (Max). Cada paso mejora la calidad y multiplica el gasto; dile cuántos agentes son antes de lanzarlo.

1. **Más chats**: `--desde` más atrás y `--tope` más alto.
2. **Segundo lector**: otro agente relee cada chat con su nota delante y añade lo que falte o corrige lo que esté mal. Duplica el gasto de la lectura.
3. **Criba con revisor**: antes de escribir, un agente por tema decide línea a línea qué vale y otro repasa solo lo quitado. Lo que se quite por caducado necesita prueba: la línea posterior que lo da por hecho.
4. **Reparto por subtemas**: en los temas con más de 30 líneas, un agente las reparte entre la ficha y sus partes antes de escribir, y cada parte la escribe un agente.
5. **Verificador**: tras cada escritor, un agente independiente comprueba contra las líneas que nada se ha perdido, cambiado ni inventado, y otro arregla lo que encuentre. Es lo más caro: triplica el gasto de la escritura.
