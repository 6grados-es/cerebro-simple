---
name: facturas-anuladas
description: "Al sumar facturación, las facturas anuladas nunca cuentan"
metadata:
  node_type: memory
  type: feedback
  originSessionId: db14e3b3-90c7-4a29-862c-f62866a69877
  modified: 2026-11-16T21:28:42.826Z
---

Al sumar o informar de facturación, excluir siempre las facturas con estado "anulada".

**Why:** Marta lo dijo explícitamente: "las anuladas no cuentan nunca".
**How to apply:** En los CSV de docs/facturas-*, filtrar estado=anulada antes de sumar. Las pendientes sí cuentan como facturadas (mostrarlas aparte de lo cobrado). Ver [[fisiosur-clinica]].
