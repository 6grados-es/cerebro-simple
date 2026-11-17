---
name: tablas-facturas-sin-concepto
description: "En las tablas de facturas, no incluir la columna de concepto"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 50e1eafe-d907-49eb-83f0-34fb14cfb149
  modified: 2026-11-17T01:03:37.244Z
---

En las tablas de facturas (pendientes, cobradas, resúmenes) no pongo la columna «concepto»; solo número, fecha, paciente e importe (y estado si hace falta).

**Why:** Marta dijo el 17-11-2026: «La tabla sin la columna de concepto, que siempre me sobra».

**How to apply:** Al montar tablas desde `docs/facturas-AAAA/*.csv`, omite `concepto`. Ver [[facturas-anuladas]].
