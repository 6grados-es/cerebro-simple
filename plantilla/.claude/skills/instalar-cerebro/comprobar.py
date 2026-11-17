#!/usr/bin/env python3
"""Comprobaciones de la instalación del cerebro que no gastan uso: no llaman a ningún modelo.

Uso (desde la carpeta del cerebro):
  python3 .claude/skills/instalar-cerebro/comprobar.py copia     guarda cómo están las fichas (antes de escribir)
  python3 .claude/skills/instalar-cerebro/comprobar.py citas     quita las «» a las frases que el dueño no escribió tal cual
  python3 .claude/skills/instalar-cerebro/comprobar.py reten     aparta fuentes y resultados con listas de teléfonos o correos, y tapa claves
  python3 .claude/skills/instalar-cerebro/comprobar.py fichas    ¿se ha perdido alguna línea de antes? ¿enlaces rotos? ¿secciones de más de 12?
"""
import difflib, re, shutil, sys
from pathlib import Path

C = Path.cwd()
I = C / "instalacion"
TURNO = re.compile(r"(?m)^## ((?:Dueño|Claude) \[\d+\](?: · \d{4}-\d\d-\d\d)?|Sistema)[ \t]*$")
TEL = re.compile(r"(?<![\d.,/-])(?:\+34[ .-]?)?[6789]\d{2}(?:[ .-]?\d{3}){2}(?![\d.,/-])")
CORREO = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
CLAVE = re.compile(r"gh[opsu]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{24,}|sbp_[a-f0-9]{30,}|xox[abp]-[A-Za-z0-9-]{20,}|AKIA[A-Z0-9]{16}|eyJhbGciOi[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_.-]{20,}|(?i:(?:contraseña|password|passwd|clave|token|secret|api[_-]?key)\s*(?:es|:|=)\s*)\S{6,}")
IBAN = re.compile(r"\b[A-Z]{2}\d{2}(?:[ -]?\d{4}){4,5}(?:[ -]?\d{1,4})?\b")
DNI = re.compile(r"\b\d{8}[- ]?[A-HJ-NP-TV-Z]\b|\b[XYZ][- ]?\d{7}[- ]?[A-Z]\b")


def norm(s):
    s = re.sub(r"[“”\"'`´‘’«»*_]", "", s.lower().replace(" ", " "))
    return re.sub(r"\s+", " ", s).strip()


def del_dueno():
    """Todo lo que el dueño escribió en los chats troceados, junto y normalizado."""
    out = []
    for f in sorted((I / "chats").glob("*.md")):
        tro = TURNO.split(f.read_text(errors="ignore"))
        out += [tro[k + 1] for k in range(1, len(tro) - 1, 2) if tro[k].startswith("Dueño")]
    return norm("\n".join(out))


def citas():
    suyo = del_dueno()
    if not suyo:
        print("No hay chats en instalacion/chats/: no se puede comprobar."); return
    total = quitadas = 0

    def una(m):
        nonlocal total, quitadas
        d = m.group(1)
        if len(d) < 12:
            return m.group(0)          # etiquetas y nombres cortos no son citas
        total += 1
        trozos = [x for x in (norm(y).strip(" .,;:¿?¡!…") for y in re.split(r"…|\.\.\.", d)) if len(x) >= 8]
        if trozos and all(x in suyo for x in trozos):
            return m.group(0)
        quitadas += 1
        return d

    for f in sorted((I / "notas").glob("*.md")):
        t = f.read_text()
        n = re.sub(r"«([^«»]+)»", una, t)
        if n != t:
            f.write_text(n)
    print(f"citas entre «»: {total} · sin comillas por no ser literales del dueño: {quitadas}")


def reten():
    apartadas = tapadas = 0
    (I / "retenidas").mkdir(parents=True, exist_ok=True)
    for carpeta in ("fuentes", "resultados"):
        for f in sorted((C / carpeta).rglob("*.md")):
            t = f.read_text(errors="ignore")
            tel = {re.sub(r"\D", "", x)[-9:] for x in TEL.findall(t)}
            cor = {x.lower() for x in CORREO.findall(t)}
            if len(tel) >= 3 or len(cor) >= 4:
                shutil.move(str(f), str(I / "retenidas" / f.name)); apartadas += 1
                print(f"  apartada: {carpeta}/{f.name} ({len(tel)} teléfonos, {len(cor)} correos)")
                continue
            n = CLAVE.sub("[no se guarda]", IBAN.sub("[cuenta bancaria: no se guarda]", DNI.sub("[documento de identidad: no se guarda]", t)))
            if n != t:
                f.write_text(n); tapadas += 1
    print(f"apartadas en instalacion/retenidas/: {apartadas} · archivos con algo tapado: {tapadas}")
    if apartadas:
        print("Dile al dueño que hay archivos apartados por llevar listas de contactos, y que decida él si entran.")


def datos(p):
    return [l.rstrip() for l in p.read_text().splitlines() if l.startswith("- ")]


def nucleo(l):
    l = re.sub(r"\s*·\s*[a-z]{3}-\d\d\s*$", "", l)
    return re.sub(r"\s+", " ", re.sub(r"\s*\[\[[^\]]+\]\]", "", l)).strip()


def fichas():
    F = C / "fichas"
    antes = I / "fichas-antes"
    hoy = {p.stem: datos(p) for p in F.glob("*.md")}
    perdidas = 0
    if antes.exists():
        todo = {nucleo(l) for ls in hoy.values() for l in ls}
        for p in sorted(antes.glob("*.md")):
            for l in datos(p):
                k = nucleo(l)
                if k in todo:
                    continue
                cerca = difflib.get_close_matches(k, list(todo), n=1, cutoff=0.0)
                ops = difflib.SequenceMatcher(None, k.split(), cerca[0].split(), autojunk=False).get_opcodes() if cerca else [("delete",)]
                if all(o[0] in ("equal", "insert") for o in ops):
                    continue           # solo se le ha añadido algo
                perdidas += 1
                print(f"  CAMBIADA O PERDIDA · {p.stem}\n     antes: {l[:260]}\n     hoy:   {(cerca[0] if cerca else '')[:260]}")
    rotos = largas = 0
    for n, p in sorted((x.stem, x) for x in F.glob("*.md")):
        t = p.read_text()
        for e in re.findall(r"\[\[([^\]|#]+)", t):
            e = e.strip()
            if not ((F / f"{e}.md").exists() or (C / f"{e}.md").exists() or (C / e).exists()):
                rotos += 1; print(f"  ENLACE ROTO · {n}: [[{e}]]")
        sec, cuenta = None, {}
        for l in t.splitlines():
            if l.startswith("## "):
                sec = l[3:].strip(); cuenta[sec] = 0
            elif l.startswith("- ") and sec and not re.match(r"- [^\n]*: \[\[[a-z0-9-]+\]\] · [a-z]{3}-\d\d$", l):
                cuenta[sec] += 1
        for s, c in cuenta.items():
            if c > 12 and n not in ("yo", "como-trabajo"):
                largas += 1; print(f"  LARGA · {n} · {s}: {c}")
    print(f"fichas: {len(hoy)} · líneas de antes cambiadas o perdidas: {perdidas} · enlaces rotos: {rotos} · secciones de más de 12: {largas}")


if __name__ == "__main__":
    orden = sys.argv[1] if len(sys.argv) > 1 else ""
    if orden == "copia":
        d = I / "fichas-antes"
        if d.exists():
            shutil.rmtree(d)
        shutil.copytree(C / "fichas", d); print("copia de las fichas en", d)
    elif orden == "citas": citas()
    elif orden == "reten": reten()
    elif orden == "fichas": fichas()
    else: print(__doc__)
