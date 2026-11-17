# Facturas
Facturas emitidas por Marta a pacientes de FisioSur y sus totales por mes.
También: facturación, ingresos, lo facturado, docs

## Ahora
- Octubre-26: facturado 380 € (335 € cobrado + 45 € pendiente de T. Luque, F-1007) · nov-26
- Septiembre-26: facturado 535 € (490 € cobrado + 45 € pendiente de P. Gómez, F-0905); F-0903 anulada no cuenta · nov-26
- Falta: cobrar F-1007 (T. Luque, 45 €) · nov-26
- Falta: cobrar F-0905 (P. Gómez, 45 €, según el CSV de septiembre) · nov-26

## Cómo se hace
- Tablas de facturas sin la columna de concepto («siempre me sobra») · nov-26
- Las anuladas no cuentan nunca en ninguna suma («las anuladas no cuentan nunca, quítalas»); «facturado» = cobradas + pendientes · nov-26

## Lo que sé
- Las facturas están en `docs/facturas-2026/<mes>.csv` · nov-26
- CSV con `;` y coma decimal: numero;fecha;paciente;concepto;importe;estado · nov-26
- Estados que aparecen: cobrada, pendiente, anulada · nov-26
