#!/bin/sh
# Rehace INDICE.md con el título, la frase y los alias de cada ficha. No falla nunca.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
[ -d fichas ] || exit 0
{
  for f in fichas/*.md; do
    [ -f "$f" ] || continue
    t=$(sed -n '1s/^# *//p' "$f")
    r=$(sed -n '2p' "$f")
    a=$(sed -n 's/^También: *//p' "$f" | head -n 1)
    printf -- '- %s — %s. %s%s\n' "$f" "$t" "$r" "${a:+ · también: $a}"
  done
} > INDICE.md.tmp 2>/dev/null && mv INDICE.md.tmp INDICE.md
exit 0
