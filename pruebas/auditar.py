#!/usr/bin/env python3
"""Audita una carpeta-cerebro contra su guion con verdad. Uso: auditar.py <carpeta> <guion.json> [--detalle]
Mide por palabras clave (aproximado: los fallos hay que mirarlos a mano) y por estructura (exacto)."""
import sys, json, re, unicodedata
from pathlib import Path
D=Path(sys.argv[1]); G=json.loads(Path(sys.argv[2]).read_text()); DET="--detalle" in sys.argv
def norm(t):
    t=unicodedata.normalize("NFD",t.lower()); t="".join(c for c in t if unicodedata.category(c)!="Mn")
    t=re.sub(r"(?<=\d)[.  ](?=\d{3}\b)","",t)      # 1.850 -> 1850
    t=re.sub(r"(\d),00\b",r"\1",t)                       # 45,00 -> 45
    return re.sub(r"\s+"," ",t)
def texto(dirp, sub):
    p=dirp/sub
    if p.is_file(): return p.read_text(errors="replace")
    return "\n".join(f.read_text(errors="replace") for f in sorted(p.rglob("*")) if f.is_file()) if p.is_dir() else ""
L=D.parent/"_logs"/D.name
if not L.is_dir(): L=D/"_log"
# respuestas por n
resp={}
for m in re.finditer(r"^## (\d+) \(chat [^)]*\) · .*?\n\n(.*?)\n\n_\(pasos:.*?tocó: (.*?)\)_", (L/"respuestas.md").read_text(), re.S|re.M):
    resp[int(m.group(1))]=(m.group(2), m.group(3))
tot={}; fallos=[]
def cuenta(k,ok,info):
    a=tot.setdefault(k,[0,0]); a[1]+=1; a[0]+=1 if ok else 0
    if not ok: fallos.append((k,info))
serie=[]
for ch in G["chats"]:
    snap=L/f"chat-{ch['id']}"
    def sinhist(sub):
        p=snap/sub
        return "\n".join(f.read_text(errors="replace") for f in sorted(p.rglob("*")) if f.is_file() and "historial" not in f.name) if p.is_dir() else ""
    fich=norm(texto(snap,"fichas")+sinhist("memoria")+sinhist("nativa")); todo=norm(texto(snap,"fichas")+texto(snap,"historial")+texto(snap,"resultados")+texto(snap,"INDICE.md")+texto(snap,"memoria")+texto(snap,"nativa"))
    for m in ch["mensajes"]:
        n=m["n"]; tipo=m.get("tipo",""); r,toco=resp.get(n,("","?"))
        tocó_ficha = any(k in toco for k in ("fichas/","memoria/","nativa/"))
        if tipo in("dato","correccion","cambio","descubre"):
            cl=[c for c in m.get("claves",[])]
            falt=[c for c in cl if norm(c) not in fich]
            cuenta("guardado (claves en fichas)", not falt and bool(cl), f"n{n} faltan {falt} · {m['texto'][:70]}")
            viej=[c for c in m.get("ya_no",[]) if norm(c) in fich]
            if m.get("ya_no"): cuenta("dato viejo retirado", not viej, f"n{n} siguen {viej} · {m['texto'][:70]}")
            cuenta("escrito en el mismo mensaje", tocó_ficha, f"n{n} no tocó fichas · {m['texto'][:70]}")
        elif tipo=="repetido":
            cuenta("repetido sin duplicar (no tocó o no creció)", True, "")
        elif tipo=="deshacer":
            viej=[c for c in m.get("ya_no",[]) if norm(c) in fich]
            cuenta("deshecho", not viej and bool(m.get("ya_no")), f"n{n} siguen {viej} · {m['texto'][:70]}")
        elif tipo in("sensible","clave"):
            mal=[c for c in m.get("ya_no",[])+m.get("no_debe",[]) if norm(c) in todo]
            cuenta("sensible sin guardar", not mal, f"n{n} guardó {mal} · {m['texto'][:70]}")
        elif tipo in("trabajo","charla"):
            cuenta("sin guardar de más", not tocó_ficha, f"n{n} tocó {toco} · {m['texto'][:70]}")
        elif tipo=="sonda":
            rn=norm(r); falt=[c for c in m.get("respuesta",[]) if norm(c) not in rn]; mal=[c for c in m.get("no_debe",[]) if norm(c) in rn]
            cuenta("sonda correcta", not falt and not mal, f"n{n} faltan {falt} sobran {mal} · {m['texto'][:70]}")
    # salud estructural de la foto
    fs=[f for d in ("fichas","memoria","nativa") if (snap/d).is_dir() for f in sorted((snap/d).glob("*.md")) if f.name not in ("MEMORY.md",) and "historial" not in f.name]
    maxsec=0; sobre=0; lineas=0; maxf=0
    for f in fs:
        t=f.read_text(errors="replace"); ls=[l for l in t.splitlines() if l.strip()]; lineas+=len(ls); maxf=max(maxf,len(ls))
        for sec in re.split(r"^## .*$",t,flags=re.M)[1:]:
            k=len([l for l in sec.splitlines() if l.strip().startswith("-")]); maxsec=max(maxsec,k); sobre+= k>12
    ind="".join(q.read_text(errors="replace") for q in (snap/"INDICE.md",snap/"memoria"/"MEMORY.md",snap/"nativa"/"MEMORY.md") if q.is_file())
    sinind=[f.name for f in fs if f.name not in ind]
    hist=len([l for l in texto(snap,"historial").splitlines() if l.strip()])
    serie.append((ch["id"],ch.get("fecha",""),len(fs),lineas,maxf,maxsec,sobre,len(sinind),hist))
print(f"# {D.name}")
for k,(a,b) in tot.items(): print(f"{k}: {a} de {b}")
vf=G.get("verdad_final",[]); ult=L/f"chat-{G['chats'][-1]['id']}"
fin=norm(texto(ult,"fichas")+"\n".join(f.read_text(errors="replace") for d in ("memoria","nativa") if (ult/d).is_dir() for f in sorted((ult/d).rglob("*")) if f.is_file() and "historial" not in f.name))
okv=[v for v in vf if v.get("claves") and all(norm(c) in fin for c in v["claves"])]
print(f"verdad final presente (por claves): {len(okv)} de {len(vf)}")
print("\nchat · fecha · fichas · líneas · ficha más larga · sección más larga · secciones >12 · fichas fuera del índice · líneas de historial")
paso=max(1,len(serie)//8)
for i,s in enumerate(serie):
    if i%paso==0 or i==len(serie)-1: print(" · ".join(str(x) for x in s))
if DET:
    print("\nFALLOS (por claves; revisar a mano):")
    for k,i in fallos: print(f"- [{k}] {i}")
    print("\nVERDAD FINAL que no aparece por claves:")
    for v in vf:
        if v not in okv: print(f"- {v.get('tema')}: {v.get('hecho')} {v.get('claves')}")
