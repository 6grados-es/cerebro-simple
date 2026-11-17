#!/bin/sh
B="/Users/usuario/Library/Application Support/Claude/claude-code/2.1.325/485fdac4332e/claude.app/Contents/MacOS/claude"
D=<carpeta-de-pruebas>/T14-i; L=<carpeta-de-pruebas>/_logs/T14-i
cd $D
ARGS="--model sonnet --setting-sources project --strict-mcp-config --permission-mode bypassPermissions --output-format json --append-system-prompt"
FECHA="A todos los efectos, hoy es 2026-06-01. Usa esa fecha y ninguna otra."
date +%T > $L/inicio.txt
"$B" -p "Instala mi cerebro. La exportación de claude.ai ya está en instalacion/. De la pestaña Code usa solo esta carpeta, ya te lo digo yo, no listes nada: <carpeta-de-pruebas>/inst-code" $ARGS "$FECHA" > $L/run1.json 2> $L/run1.err < /dev/null &
P=$!
while kill -0 $P 2>/dev/null; do
  n=$(grep -c '^- ' instalacion/progreso.md 2>/dev/null || echo 0)
  if [ "$n" -ge 5 ]; then sleep 5; kill $P; pkill -P $P; echo "cortado con $n hechos a $(date +%T)" > $L/corte.txt; break; fi
  sleep 10
done
wait $P 2>/dev/null
sleep 5
"$B" -p "Sigue con la instalación de mi cerebro. De Code, la misma carpeta de antes: <carpeta-de-pruebas>/inst-code" $ARGS "$FECHA" > $L/run2.json 2> $L/run2.err < /dev/null
date +%T > $L/fin.txt
echo INSTALACION FIN
