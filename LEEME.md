# cerebro-simple

Una memoria para clientes de 6 Grados que se actualiza sola con el uso: sin cierres, sin rutinas y sin informes.
Claude escribe en la ficha del tema dentro del mismo mensaje, antes de contestar, y avisa con una línea: «Anotado en …».

## Qué se instala: `plantilla/`

Es todo el sistema. Se copia tal cual al ordenador del cliente.

| Pieza | Qué es | Quién la escribe |
| --- | --- | --- |
| `CLAUDE.md` | Las reglas (versión 14, 100 líneas; la 13 más el tope de 40 por ficha, bitácora y «Dónde mirar», sin probar todavía) | Nadie: viene con la plantilla |
| `INDICE.md` | Una línea por ficha | Claude |
| `fichas/` | Una ficha por tema (cliente, proveedor, obra, el dueño). Tres secciones: Ahora, Cómo se hace, Lo que sé. Enlazadas entre sí con `[[ficha]]` | Claude |
| `fichas/yo.md` | Quién es el dueño y cómo le gusta trabajar. Se carga sola en cada chat | Claude |
| `fuentes/` | Los originales que amplían una ficha, tal cual: transcripciones de Plaud, correos, contratos, feedback, postmotos, estrategias, trozos de conversación, las palabras literales del dueño | El dueño los trae; Claude los guarda |
| `resultados/` | Lo que Claude entrega: documentos, presupuestos, resúmenes | Claude |
| `.claude/skills/instalar-cerebro/` | El instalador: lee los chats antiguos del cliente y llena fichas, fuentes y resultados. Se usa una vez | Viene con la plantilla |

No hay historial: las versiones anteriores las guarda donde viva la carpeta (GitHub si el cliente lo usa; si no, las versiones de iCloud, Drive u OneDrive).
Las skills del cliente viven en `.claude/skills/`: la ficha dice cuándo se usa cada una, y lo que se aprende al usarlas va a la ficha, no a la skill.

## Instalar a un cliente

1. Copia `plantilla/` a su ordenador, dentro de la nube que ya use (iCloud, Drive u OneDrive), y llámala `Cerebro`.
2. En la app de Claude, pestaña Code, elige esa carpeta como carpeta de trabajo y déjala por defecto.
3. Modelo: Sonnet o superior.
4. Modo sin preguntas (es el único probado).
5. Llenar el cerebro con sus chats antiguos:
   - El cliente pide la exportación en claude.ai: Ajustes › Privacidad › Exportar datos. Llega un correo con un enlace que caduca en 24 horas; descarga el zip y lo deja, sin abrir, en `Cerebro/instalacion/`.
   - En la app, dentro de la carpeta, dice «instala mi cerebro». Claude le pregunta qué carpetas de la pestaña Code son de su trabajo y lee cada chat con un agente: los originales a `fuentes/`, lo entregado a `resultados/` y lo demás a las fichas.
   - Si se corta por el límite de uso, al decir otra vez «instala mi cerebro» sigue por donde iba.
   - Al acabar, el cliente lee `fichas/yo.md` y corrige lo que no esté bien.
   - Si no tiene chats antiguos, se salta este paso y el primer mensaje es quién es y a qué se dedica; la respuesta debe acabar con «Anotado en yo: …».
6. Comprobación: en un chat nuevo, «¿qué sabes de mí?».
7. Si la app pide permiso para cargar `fichas/yo.md` o `INDICE.md` la primera vez, acéptalo.

Lo que hay que contarle al cliente:
- «Habla con Claude como siempre. Lo que le cuentes de ti, de tus clientes y de cómo te gustan las cosas, lo apunta solo.»
- «Cuando apunta algo, te lo dice en una línea al final. Si no quieres que lo guarde, dile "quita eso".»
- «Si le pegas una transcripción, un correo o unas notas, guarda el original en fuentes.»
- «No le des contraseñas para que las guarde: no lo hará.»

Para cambiar las reglas a un cliente que ya lo tiene: sustituye solo `CLAUDE.md`. Sus fichas, fuentes y resultados no se tocan.

## `pruebas/`: el banco con el que se eligió y se afinó

- `correr.py <carpeta> <guion> [modelo]`: pasa un guion por una carpeta con Claude Code sin ventana, aislado de las reglas personales. Deja el registro en `../_logs/<carpeta>`, fuera de la carpeta de prueba. Si salta el límite de uso, espera y reintenta.
- `auditar.py <carpeta> <guion.json> [--detalle]`: compara lo guardado con la verdad del guion, por palabras clave. Es aproximado: los fallos se repasan a mano.
- `guiones/`: guion corto (27 mensajes), sesión larga (48), seis meses (112), «olvida esto» (6), fuentes (7 y 11), skills (4), el instalador (una exportación inventada de 12 chats y 2 sesiones de Code, y 7 preguntas) y las pruebas del abogado del diablo, con los archivos de los dos clientes inventados y una skill de prueba.
- `reglas/`: todas las versiones probadas (v4 a v13), el candidato híbrido de cinco líneas y los ganchos descartados.
- `registros/`: respuestas y memoria final de cada prueba. `primera-pasada-no-valida/` se conserva solo como rastro.
- `jueces/`: los veredictos, el dossier y el debate de seis sombreros.

Las carpetas de prueba tienen que estar fuera de cualquier ruta que nombre un cerebro real: sin memoria, Claude busca por el disco.

## Lo que no se ha probado

La app de escritorio en sí (las pruebas usan su mismo programa, sin ventana), los permisos fuera del modo sin preguntas, Windows, Cowork y más de seis meses de uso.

Todos los clientes y datos de `pruebas/` son inventados.

Diseño completo: documento «Cerebro simple: diseño» (Claude Docs) y, en el cerebro de Pedro, `PROYECTOS/cerebro-simple.md`.

## El instalador, pensado para un plan Pro (18-nov-2026)

Qué hace `.claude/skills/instalar-cerebro/` y por qué:

| Paso | Con qué | Gasta uso |
| --- | --- | --- |
| Trocear y limpiar los chats: sin el texto de las skills, con lo que no escribió el dueño marcado, turnos numerados y con su fecha real, solo el último mes y con tope de texto | `trocear.py` | No |
| Leer: un agente por chat, con los criterios de qué vale para la próxima vez dentro de su encargo | Sonnet | Sí |
| Quitar las comillas a lo que el dueño no escribió tal cual; apartar listas de teléfonos y correos; tapar claves | `comprobar.py citas` y `reten` | No |
| Escribir: un agente por ficha | Sonnet | Sí |
| Comprobar que no se pierde ninguna línea de las que había, enlaces y tope de 40 por ficha | `comprobar.py fichas` | No |

El tope por defecto (30 días y 1.500.000 caracteres) es una estimación para que quepa en media sesión de cinco horas de un plan Pro; no está medido todavía con una cuenta Pro real. Si se queda corto o largo, se cambia en `trocear.py` (`TOPE`).

Las mejoras caras (segundo lector, criba con revisor, reparto por subtemas, verificador) quedan como paso opcional al final de la skill, para quien tenga un plan con mucho uso.
