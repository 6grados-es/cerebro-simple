#!/usr/bin/env python3
"""Saca los chats de Claude del dueño a un archivo de texto por chat, para la instalación del cerebro.

Uso (desde la carpeta del cerebro):
  python3 .claude/skills/instalar-cerebro/trocear.py --listar-code
      Lista las carpetas con chats de la pestaña Code de este ordenador.
  python3 .claude/skills/instalar-cerebro/trocear.py [--code <carpeta> ...] [--code-todas]
      Lee la exportación de claude.ai que haya en instalacion/ (el .zip o conversations.json)
      y los chats de Code que se le indiquen, y deja en instalacion/chats/ un .md por chat,
      ordenados por fecha. Se salta los chats de menos de 3 mensajes y los ya hechos
      (los que salen en instalacion/progreso.md).
No necesita nada instalado: solo Python 3.
"""
import sys, json, re, zipfile, unicodedata
from pathlib import Path

CEREBRO = Path.cwd()
INST = CEREBRO / "instalacion"
CHATS = INST / "chats"
PROYECTOS = Path.home() / ".claude" / "projects"
MIN_MENSAJES = 3
MAX_CARACTERES = 400_000  # un chat más largo se corta en partes


def slug(t, n=50):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return (t[:n].rstrip("-") or "chat")


def hechos():
    p = INST / "progreso.md"
    if not p.exists():
        return set()
    nombres = re.findall(r"^- `?([^\s`]+?)(?:\.md)?`?\s*$", p.read_text(), re.M)
    return {n + ".md" for n in nombres}


def texto_bloques(c):
    if isinstance(c, str):
        return c
    out = []
    for b in c or []:
        if isinstance(b, dict) and b.get("type") == "text" and b.get("text"):
            out.append(b["text"])
    return "\n".join(out)


# ---------- claude.ai (exportación) ----------
def leer_export():
    datos = None
    for z in sorted(INST.glob("*.zip")):
        with zipfile.ZipFile(z) as f:
            for n in f.namelist():
                if n.endswith("conversations.json"):
                    datos = json.loads(f.read(n))
    for j in sorted(INST.rglob("conversations.json")):
        if "chats" not in j.parts:
            datos = json.loads(j.read_text())
    if datos is None:
        return []
    chats = []
    for conv in datos if isinstance(datos, list) else datos.get("conversations", []):
        msgs = []
        for m in conv.get("chat_messages", []):
            quien = "Dueño" if m.get("sender") == "human" else "Claude"
            t = m.get("text") or texto_bloques(m.get("content"))
            adj = []
            for a in (m.get("attachments") or []):
                nombre = a.get("file_name") or "adjunto"
                cont = a.get("extracted_content") or ""
                adj.append(f"[Adjunto: {nombre}]\n{cont}".rstrip())
            for f in (m.get("files") or []):
                if isinstance(f, dict) and f.get("file_name"):
                    adj.append(f"[Archivo: {f['file_name']} (sin texto en la exportación)]")
            cuerpo = "\n\n".join(x for x in [t.strip()] + adj if x)
            if cuerpo:
                msgs.append((quien, m.get("created_at", ""), cuerpo))
        fecha = (conv.get("created_at") or (msgs[0][1] if msgs else ""))[:10]
        titulo = conv.get("name") or (msgs[0][2][:60] if msgs else "chat")
        chats.append({"origen": "claude.ai", "id": (conv.get("uuid") or "")[:8], "fecha": fecha,
                      "titulo": titulo, "mensajes": msgs})
    return chats


# ---------- pestaña Code (transcripciones locales) ----------
def carpetas_code():
    yo = str(CEREBRO).replace("/", "-")
    out = []
    if PROYECTOS.is_dir():
        for d in sorted(PROYECTOS.iterdir()):
            if d.is_dir() and d.name != yo:
                n = len(list(d.glob("*.jsonl")))
                if n:
                    out.append((d, n))
    return out


def limpio(t):
    t = re.sub(r"<system-reminder>.*?</system-reminder>", "", t, flags=re.S)
    t = re.sub(r"<(command-[a-z-]+|local-command-[a-z-]+)>.*?</\1>", "", t, flags=re.S)
    return t.strip()


def leer_code(carpetas):
    chats = []
    for d in carpetas:
        for f in sorted(d.glob("*.jsonl")):
            msgs, fecha, titulo = [], "", ""
            for l in f.read_text(errors="replace").splitlines():
                try:
                    o = json.loads(l)
                except Exception:
                    continue
                if o.get("isSidechain") or o.get("type") not in ("user", "assistant"):
                    continue
                c = (o.get("message") or {}).get("content")
                if o["type"] == "user" and isinstance(c, list) and all(
                        isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                    continue
                t = limpio(texto_bloques(c))
                if not t:
                    continue
                fecha = fecha or (o.get("timestamp") or "")[:10]
                quien = "Dueño" if o["type"] == "user" else "Claude"
                if quien == "Dueño" and not titulo:
                    titulo = t[:60]
                msgs.append((quien, o.get("timestamp", ""), t))
            chats.append({"origen": f"Code · {d.name[-40:]}", "id": f.stem[:8], "fecha": fecha,
                          "titulo": titulo or "chat", "mensajes": msgs})
    return chats


def escribir(chats):
    CHATS.mkdir(parents=True, exist_ok=True)
    ya = hechos()
    nuevos, cortos = 0, 0
    chats = [c for c in chats if c["fecha"]]
    chats.sort(key=lambda c: (c["fecha"], c["id"]))
    for c in chats:
        if len(c["mensajes"]) < MIN_MENSAJES:
            cortos += 1
            continue
        base = f"{c['fecha']}-{slug(c['titulo'])}-{c['id']}"
        cuerpo = "\n\n".join(f"## {q}\n\n{t}" for q, _, t in c["mensajes"])
        partes = [cuerpo[i:i + MAX_CARACTERES] for i in range(0, len(cuerpo), MAX_CARACTERES)] or [""]
        for i, p in enumerate(partes, 1):
            nombre = base + (f"-parte{i}" if len(partes) > 1 else "") + ".md"
            if nombre in ya or (CHATS / nombre).exists():
                continue
            cab = f"# {c['titulo']}\nFecha: {c['fecha']} · Origen: {c['origen']} · Mensajes: {len(c['mensajes'])}"
            if len(partes) > 1:
                cab += f" · Parte {i} de {len(partes)}"
            (CHATS / nombre).write_text(cab + "\n\n" + p + "\n")
            nuevos += 1
    pend = sorted(x.name for x in CHATS.glob("*.md") if x.name not in ya)
    print(f"Chats por leer: {len(pend)} (nuevos ahora: {nuevos}; ya hechos antes: {len(ya)}; "
          f"descartados por cortos: {cortos})")
    for n in pend:
        print("  " + n)


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--listar-code" in a:
        cs = carpetas_code()
        if not cs:
            print("No hay chats de la pestaña Code en este ordenador.")
        for d, n in cs:
            print(f"{n:>4} chats · {d}")
        sys.exit(0)
    INST.mkdir(exist_ok=True)
    elegidas = []
    if "--code-todas" in a:
        elegidas = [d for d, _ in carpetas_code()]
    for i, x in enumerate(a):
        if x == "--code" and i + 1 < len(a):
            elegidas.append(Path(a[i + 1]).expanduser())
    escribir(leer_export() + leer_code(elegidas))
