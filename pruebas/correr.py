#!/usr/bin/env python3
"""Pasa un guion por una carpeta-cerebro con Claude Code sin ventana.
Uso: correr.py <carpeta> <guion.json|guion.txt> [modelo]
Guion txt: líneas "chat|n|mensaje". Guion json: {"chats":[{"id":1,"fecha":"2027-01-12","mensajes":[{"n":1,"texto":"..."}]}]}
Deja en <carpeta>/_log: respuestas.md, turnos.jsonl (qué archivos cambió cada mensaje) y una copia de las fichas tras cada chat."""
import sys, json, subprocess, hashlib, shutil, time, os
from pathlib import Path
B="/Users/usuario/Library/Application Support/Claude/claude-code/2.1.325/485fdac4332e/claude.app/Contents/MacOS/claude"
D=Path(sys.argv[1]).resolve(); G=Path(sys.argv[2]); M=sys.argv[3] if len(sys.argv)>3 else "sonnet"
if G.suffix==".json":
    chats=json.loads(G.read_text())["chats"]
else:
    chats=[]; 
    for l in G.read_text().strip().splitlines():
        c,n,t=l.split("|",2)
        if not chats or chats[-1]["id"]!=c: chats.append({"id":c,"mensajes":[]})
        chats[-1]["mensajes"].append({"n":n,"texto":t})
L=D.parent/"_logs"/D.name; L.mkdir(parents=True,exist_ok=True)
VIG=["fichas","historial","resultados","INDICE.md","memoria"]
NAT=Path.home()/".claude/projects"/str(D).replace("/","-")/"memory"
def foto():
    h={}
    for v in VIG:
        p=D/v
        fs=[p] if p.is_file() else (sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else [])
        for f in fs: h[str(f.relative_to(D))]=hashlib.md5(f.read_bytes()).hexdigest()
    if NAT.is_dir():
        for f in sorted(x for x in NAT.rglob("*") if x.is_file()): h["nativa/"+str(f.relative_to(NAT))]=hashlib.md5(f.read_bytes()).hexdigest()
    return h
resp=open(L/"respuestas.md","a"); tj=open(L/"turnos.jsonl","a")
for ch in chats:
    sid=None
    for m in ch["mensajes"]:
        antes=foto()
        a=[B,"-p",m["texto"],"--model",M,"--setting-sources","project","--strict-mcp-config","--permission-mode","bypassPermissions","--output-format","json"]
        if ch.get("fecha"): a+=["--append-system-prompt",f"A todos los efectos, hoy es {ch['fecha']}. Usa esa fecha y ninguna otra."]
        if sid: a+=["--resume",sid]
        t0=time.time(); d={}; intentos=0; aborta=False
        while True:
            intentos+=1; err=""
            try:
                out=subprocess.run(a,cwd=D,capture_output=True,text=True,timeout=600,stdin=subprocess.DEVNULL).stdout
                d=json.loads(out)
                if not d.get("is_error"): break
                err=str(d.get("result"))
            except Exception as e:
                err=type(e).__name__; d={"is_error":True}
            limite="limit" in err.lower()
            if intentos>=(60 if limite else 4):
                d["result"]="[ERROR: "+err[:200]+"]"; aborta=True; break
            time.sleep(420 if limite else 40*intentos)
        if aborta:
            resp.write("ABORTADO en "+str(m["n"])+": "+str(d["result"])+chr(10)); resp.close(); sys.exit(1)
        sid=d.get("session_id") or sid
        despues=foto()
        cambios=sorted(k for k in set(antes)|set(despues) if antes.get(k)!=despues.get(k))
        resp.write(f"## {m['n']} (chat {ch['id']}{' · '+ch['fecha'] if ch.get('fecha') else ''}) · {m['texto']}\n\n{d.get('result','')}\n\n_(pasos: {d.get('num_turns')} · {round(time.time()-t0,1)} s · tocó: {', '.join(cambios) or 'nada'})_\n\n"); resp.flush()
        u=d.get("usage") or {}
        tj.write(json.dumps({"n":m["n"],"chat":ch["id"],"cambios":cambios,"pasos":d.get("num_turns"),"s":round(time.time()-t0,1),"entrada":(u.get("input_tokens",0)+u.get("cache_read_input_tokens",0)+u.get("cache_creation_input_tokens",0)),"coste":d.get("total_cost_usd"),"error":bool(d.get("is_error")),"intentos":intentos},ensure_ascii=False)+"\n"); tj.flush()
    snap=L/f"chat-{ch['id']}"; 
    if snap.exists(): shutil.rmtree(snap)
    snap.mkdir()
    for v in VIG:
        p=D/v
        if p.is_dir(): shutil.copytree(p,snap/v)
        elif p.is_file(): shutil.copy(p,snap/v)
    if NAT.is_dir(): shutil.copytree(NAT,snap/"nativa")
resp.write("FIN\n"); resp.close()
