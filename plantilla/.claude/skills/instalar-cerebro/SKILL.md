---
name: instalar-cerebro
description: Llena el cerebro la primera vez leyendo todos los chats de Claude del dueño (la exportación de claude.ai y los chats de la pestaña Code), con un agente por chat, y crea las fichas, las fuentes y los resultados. Úsala cuando el dueño diga «instala mi cerebro», «carga mis chats», «lee mis chats antiguos» o «sigue con la instalación». Se puede cortar y seguir.
---

# Instalar el cerebro

Lee los chats antiguos del dueño y llena `fichas/`, `fuentes/` y `resultados/` con las reglas de `CLAUDE.md`. Se hace una vez. Si se corta por el límite de uso, al volver a decir «instala mi cerebro» sigue por donde iba.

## 1. Reunir los chats

1. Mira si hay una exportación de claude.ai en `instalacion/`: un `.zip` o un `conversations.json`.
   - Si no la hay y es la primera vez, explícale al dueño cómo pedirla, en cuatro líneas: en claude.ai, Ajustes › Privacidad › Exportar datos. Llega un correo con un enlace que caduca en 24 horas; tiene que descargar el zip y dejarlo, sin abrir, en la carpeta `instalacion/` del cerebro. Mientras tanto, se puede seguir con los chats de Code.
2. Lista los chats de la pestaña Code de este ordenador:
   `python3 .claude/skills/instalar-cerebro/trocear.py --listar-code`
   Enséñale al dueño la lista de carpetas y pregúntale cuáles son de su trabajo. Es la única pregunta de toda la instalación. Si ya te lo ha dicho en este chat, o te dice «todas», no preguntes.
3. Trocea:
   `python3 .claude/skills/instalar-cerebro/trocear.py --code <carpeta> --code <carpeta>` (o `--code-todas`).
   Deja en `instalacion/chats/` un archivo por chat, ordenados por fecha, y dice cuántos quedan por leer. Los chats de menos de 3 mensajes y los ya hechos se saltan solos.

## 2. Un agente por chat, en tandas de 5

Coge los 5 chats más antiguos que queden por leer y lanza un agente por chat, los 5 a la vez, con `model: "sonnet"`. A cada uno le das el encargo de abajo, con el nombre de su chat. Espera a que acaben los 5 antes de seguir.

Encargo para cada agente (sustituye `<chat>`):

> Lee entero `instalacion/chats/<chat>` y las reglas de `CLAUDE.md`. Es un chat antiguo del dueño con Claude; su fecha está en la cabecera.
> 1. Si en el chat hay un original que amplía lo que se sabe (una transcripción, un correo, un contrato, unas notas, un feedback, un postmoto, una estrategia, algo que el dueño explica a fondo con sus palabras), guárdalo tal cual, con sus palabras literales, en `fuentes/<fecha del chat>-<tema>.md`. Si el archivo ya existe, añade `-2` al nombre.
> 2. Si Claude entregó en el chat un documento acabado (un presupuesto, un informe, un texto largo para usar), guárdalo en `resultados/<fecha del chat>-<tema>.md`. Un mensaje corto no se guarda.
> 3. No toques `fichas/` ni `INDICE.md`. Escribe en `instalacion/notas/<chat>` las líneas que irían a las fichas, una por línea, con este formato:
>    `<tema> | <Ahora, Cómo se hace o Lo que sé> | <la línea, con las palabras del dueño si son suyas> | <mes del chat, como nov-26> | <enlace a la fuente o al resultado, si lo hay>`
>    Usa las reglas de `CLAUDE.md` para saber qué va en cada sección. Los pendientes empiezan por `Falta:`. Una decisión que vale para el futuro se escribe «Cuando <caso>: <qué se hace>».
> 4. Nunca contraseñas ni claves. Tampoco datos de salud, documentos de identidad ni datos bancarios de otras personas, salvo que el dueño pidiera expresamente guardarlos. No guardes la charla, las suposiciones ni lo que solo valía para ese chat.
> 5. Si no hay nada que guardar, escribe solo `nada` en la nota.
> Devuelve una línea: cuántas líneas de ficha, fuentes y resultados has dejado.

## 3. Un solo escritor de fichas

Cuando acaben los 5, lanza **un** agente (`model: "sonnet"`) con este encargo:

> Lee las reglas de `CLAUDE.md`, `INDICE.md` y estas notas, en este orden, de la más antigua a la más nueva: <lista de las 5 notas>. Pasa cada línea a su ficha siguiendo las reglas: una ficha por tema, un dato en un solo sitio, si un dato ya está y la nota es más nueva lo corriges en el sitio, enlaces `[[ficha]]` entre fichas y a fuentes y resultados, e índice al día. Lo que ya no vale (un pendiente que una nota posterior da por hecho) se borra. No escribas nada que no esté en las notas. Devuelve una línea: fichas creadas y fichas cambiadas.

Después apunta los 5 chats al final de `instalacion/progreso.md`, uno por línea, como `- <chat>`. Sigue con la tanda siguiente hasta que no quede ninguno.

Entre tanda y tanda no le cuentes nada al dueño. Si te corta el límite de uso, no pasa nada: `progreso.md` sabe por dónde iba.

## 4. Al acabar

1. Borra `instalacion/chats/` e `instalacion/notas/`. Deja `instalacion/progreso.md` y la exportación.
2. Dile al dueño, en un mensaje corto:
   - cuántos chats has leído;
   - cuántas fichas, fuentes y resultados han quedado;
   - que lea `fichas/yo.md` y te diga lo que no esté bien, porque es la que más se usa.
3. No hagas informe ni resumen de lo que has guardado. Si quiere saber algo, que pregunte.
