#!/bin/sh
S=/private/tmp/claude-501/-Users-usuario-Desktop-cerebro/84e7a4da-7dca-4e94-b139-edde4691d388/scratchpad/simple
for a in C-S4 C-S5 C-N C-H; do
  d=$S/baratas/$a
  python3 $S/correr.py $d $S/baratas/ga.txt sonnet
  sed -i '' 's/^F-1007;\(.*\);pendiente$/F-1007;\1;cobrada/' $d/docs/facturas-2026/octubre.csv
  python3 $S/correr.py $d $S/baratas/gb.txt sonnet
  case $a in C-S4|C-S5) python3 $S/correr.py $d $S/baratas/gc.txt sonnet;; esac
done
echo BARATAS FIN
