---
name: facturas-anuladas
description: "Al sumar o resumir facturación, las facturas anuladas no se cuentan nunca ni se muestran"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 736e30ad-7634-455f-b8be-9cd439f843a3
  modified: 2026-11-17T01:02:37.143Z
---

Las facturas con estado «anulada» no cuentan nunca en los totales de facturación, y no hace falta ni mencionarlas en el desglose.

**Why:** Marta lo dijo tras un resumen de octubre 2026 donde las enseñé aparte: «Las anuladas no cuentan nunca, quítalas».

**How to apply:** Al sumar facturas (carpeta `docs/facturas-AAAA/*.csv`, separador `;`, importes con coma), filtra `estado = anulada` y presenta solo cobradas y pendientes. Los CSV no se tocan. Ver [[clinica-fisiosur]].
