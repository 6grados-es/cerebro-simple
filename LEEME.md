# cerebro-simple

Una memoria para clientes de 6 Grados que se actualiza sola con el uso: sin cierres, sin rutinas y sin informes.
Claude escribe en la ficha del tema dentro del mismo mensaje, antes de contestar, y avisa con una línea: «Anotado en …».

## Qué hay aquí

- `plantilla/`: lo que se instala a un cliente. Es todo el sistema.
  - `CLAUDE.md`: las reglas (versión 7, 61 líneas).
  - `INDICE.md`: una línea por ficha. Lo mantiene Claude.
  - `fichas/yo.md`: la ficha del dueño. Las demás fichas las crea Claude.
  - `historial/` y `resultados/`: vacías al empezar.
- `pruebas/`: el banco con el que se eligió y se afinó.
  - `correr.py <carpeta> <guion> [modelo]`: pasa un guion por una carpeta con Claude Code sin ventana, aislado de las reglas personales. Deja el registro en `../_logs/<carpeta>`, fuera de la carpeta de prueba.
  - `auditar.py <carpeta> <guion.json> [--detalle]`: compara lo guardado con la verdad del guion, por palabras clave. Es aproximado: los fallos se repasan a mano.
  - `guiones/`: guion corto (27 mensajes), sesión larga (48), seis meses (112), «olvida esto» (6) y las pruebas del abogado del diablo, con los archivos de los dos clientes inventados.
  - `reglas/`: todas las versiones probadas (v4 a v7), el candidato híbrido de cinco líneas y los ganchos descartados.
  - `registros/`: respuestas y memoria final de cada prueba. `primera-pasada-no-valida/` se conserva solo como rastro.
  - `jueces/`: los veredictos de los jueces, el dossier y el debate de seis sombreros.

## Instalar a un cliente

1. Copia `plantilla/` al ordenador del cliente, dentro de la nube que ya use (iCloud, Drive u OneDrive), y llámala `Cerebro`.
2. En la app de Claude, pestaña Code, elige esa carpeta como carpeta de trabajo y déjala por defecto.
3. Modelo: Sonnet o superior. Con Haiku no funciona bien.
4. Primer mensaje del cliente: quién es y a qué se dedica. Debe acabar con «Anotado en yo: …».
5. Comprobación: en un chat nuevo, «¿qué sabes de mí?».

## Lo que no se ha probado

La app de escritorio en sí (las pruebas usan su mismo programa, sin ventana), los permisos fuera del modo sin preguntas, Windows, Cowork y más de seis meses de uso.

Todos los clientes y datos de `pruebas/` son inventados.

El diseño completo y la evaluación están en el cerebro de Pedro: `PROYECTOS/cerebro-simple.md` y `RESULTADOS/comun/2026-11-16-cerebro-simple-*.md`.
