import json, uuid
def conv(fecha, nombre, pares):
    msgs=[]; 
    for i,(s,t) in enumerate(pares):
        msgs.append({"uuid":str(uuid.uuid4()),"sender":s,"text":t,"created_at":f"{fecha}T10:{i:02d}:00Z","attachments":[],"files":[]})
    return {"uuid":str(uuid.uuid4()),"name":nombre,"created_at":f"{fecha}T10:00:00Z","updated_at":f"{fecha}T11:00:00Z","chat_messages":msgs}
H,A="human","assistant"
c=[]
c.append(conv("2026-01-08","Presentación",[(H,"Hola. Soy Laura Mena, arquitecta técnica autónoma en Málaga. Dirijo reformas de viviendas y locales. Trabajo sola."),(A,"Encantado, Laura. ¿En qué te ayudo?"),(H,"Mi gestoría es Arjona y Asociados; me lleva Nuria Arjona. Les paso los papeles del trimestre antes del día 10 del mes siguiente."),(A,"Entendido.")]))
c.append(conv("2026-01-15","Correo a Marta Quintero",[(H,"Escríbele un correo a Marta Quintero, mi clienta de la obra de Larios, diciéndole que la licencia ya está pedida."),(A,"Estimada Sra. Quintero:\n\nPor la presente le comunico que la licencia de obra menor ha sido solicitada...\n\nAtentamente,\nLaura Mena"),(H,"Muy de notario. A los clientes les escribo de tú, empiezo con «Hola Marta,», firmo solo «Laura» y no paso de seis líneas."),(A,"Hola Marta,\n\nYa he pedido la licencia de obra menor de Larios. Te aviso en cuanto la concedan.\n\nLaura")]))
c.append(conv("2026-01-20","Tiempo",[(H,"¿Qué tiempo hace mañana en Málaga?"),(A,"No tengo datos en tiempo real.")]))
c.append(conv("2026-02-02","Reunión con Hernán",[(H,"Te pego la transcripción de Plaud de la reunión con Hernán Ortuño, del Café Alameda: «Laura: Hernán, repasamos la barra. Hernán: La quiero en roble macizo, no en chapa, aunque suba. Laura: Son unos 900 euros más según Ebanor. Hernán: Adelante. Y la campana que sea la de 1,8 metros, que la de 1,5 se queda corta. Laura: Apuntado. ¿Inauguración? Hernán: El 1 de marzo, sí o sí.» ¿Qué tengo que encargar?"),(A,"Encargar: barra en roble macizo a Ebanor (+900 €) y campana de 1,8 m. Inauguración el 1 de marzo."),(H,"Perfecto, gracias.")]))
pres="# Presupuesto · Reforma integral calle Larios\nCliente: Marta Quintero Ruiz · Fecha: 10-feb-2026\n\n| Capítulo | Importe |\n|---|---|\n| 02 Albañilería y alicatados | 13.440 € |\n| 05 Carpintería | 8.420 € |\n| 01 Demolición y residuos | 6.430 € |\n| 06 Pintura | 4.921 € |\n| 04 Electricidad | 3.450 € |\n| 03 Fontanería | 3.323 € |\n\nBase imponible: 39.984 €\nIVA (10 %): 3.998 €\nTotal: 43.982 €\n\nForma de pago: 30 % a la firma, 40 % a mitad de obra, 30 % a la recepción.\nPlazo: 16 semanas desde el inicio."
c.append(conv("2026-02-10","Presupuesto Larios para Marta",[(H,"Prepárame el presupuesto de Larios para mandárselo a Marta: por capítulos, sin precios unitarios ni gremios, y debajo base, IVA y total."),(A,pres),(H,"Perfecto, este es el que le mando.")]))
c.append(conv("2026-02-18","Pimentel y portal",[(H,"Para Teatinos cuento con Anselmo Pimentel, el fontanero: solo trabaja de lunes a jueves, los viernes no va a ninguna obra. Cobra 36 € la hora."),(A,"Anotado: Pimentel, de lunes a jueves, 36 €/h."),(H,"Y la clave del portal de licencias del Ayuntamiento es Mlg#2026, guárdala tú que yo me olvido."),(A,"Prefiero no guardar contraseñas; mejor en un gestor de contraseñas.")]))
c.append(conv("2026-03-01","Visita Teatinos",[(H,"Teodoro Cabello, el cliente de Teatinos, tiene una hernia discal y no puede cargar peso; me ha pedido aplazar la visita de obra al 10 de marzo."),(A,"Entendido: visita de Teatinos aplazada al 10 de marzo."),(H,"Gracias.")]))
c.append(conv("2026-03-12","Cambios",[(H,"Hernán me ha llamado: retrasa la inauguración del Café Alameda al 15 de marzo."),(A,"Entendido, 15 de marzo."),(H,"Y en la gestoría ya no está Nuria: ahora me lleva Íñigo Bravo. Lo demás igual."),(A,"Entendido.")]))
c.append(conv("2026-04-05","Correos más largos",[(H,"He cambiado de idea con los correos a clientes: ahora quiero que sean de 8 a 10 líneas, con el detalle de lo hecho y lo que viene. El «Hola Nombre,» y la firma «Laura» se quedan."),(A,"Entendido."),(H,"Escríbele uno a Teodoro con el avance de esta semana: alicatado del baño terminado, la semana que viene fontanería.")]))
c.append(conv("2026-04-20","Estrategia",[(H,"Te cuento mi estrategia, quiero que la tengas: «Quiero dejar de hacer obras pequeñas de baño suelto, porque me comen el tiempo y dejan poco margen. A partir de enero de 2027 solo acepto reformas integrales o locales de más de 25.000 euros, salvo clientes de siempre como Teodoro. Máximo cuatro obras grandes a la vez.»"),(A,"Entendido, lo tendré presente."),(H,"Eso es.")]))
c.append(conv("2026-05-03","Feedback presupuestos",[(H,"Un feedback del presupuesto que me hiciste ayer, para siempre: «Me sobra la introducción, a los clientes no les interesa quién soy. Lo que quieren ver primero es el total, arriba y grande, y luego el desglose. Y nunca pongas \"aproximadamente\": o es un precio o no lo es.»"),(A,"Entendido."),(H,"Gracias.")]))
c.append(conv("2026-05-20","Series",[(H,"Recomiéndame una serie para el fin de semana."),(A,"Prueba «The Bear»."),(H,"Ya la he visto, otra."),(A,"Entonces «Slow Horses».")]))
json.dump(c,open("conversations.json","w"),ensure_ascii=False,indent=1)
def ses(fecha, pares, nombre):
    L=[]
    for i,(t,x) in enumerate(pares):
        ts=f"{fecha}T09:{i:02d}:00Z"
        if t=="u": L.append({"type":"user","timestamp":ts,"message":{"role":"user","content":x}})
        elif t=="a": L.append({"type":"assistant","timestamp":ts,"message":{"role":"assistant","content":[{"type":"text","text":x}]}})
        elif t=="tool": L.append({"type":"assistant","timestamp":ts,"message":{"role":"assistant","content":[{"type":"tool_use","name":"Bash","input":{"command":"cat facturas.csv"}}]}})
        elif t=="res": L.append({"type":"user","timestamp":ts,"message":{"role":"user","content":[{"type":"tool_result","content":"numero;estado\nF1;cobrada"}]}})
        elif t=="side": L.append({"type":"user","isSidechain":True,"timestamp":ts,"message":{"role":"user","content":"SUBAGENTE: no debe aparecer"}})
    open(f"code-prueba/{nombre}.jsonl","w").write("\n".join(json.dumps(o,ensure_ascii=False) for o in L)+"\n")
ses("2026-03-20",[("u","<system-reminder>ruido</system-reminder>Suma las facturas emitidas de marzo del CSV de facturas."),("tool",None),("res",None),("side",None),("a","Suman 4.320 € con IVA, contando las anuladas."),("u","Las anuladas no cuentan nunca, quítalas siempre."),("a","Entendido: sin las anuladas son 3.910 €.")],"sesion-facturas")
ses("2026-05-10",[("u","Pimentel me ha dicho que desde junio cobra 38 € la hora."),("a","Entendido."),("u","Hazme la tabla de horas de Pimentel en Teatinos para mayo."),("a","Aquí tienes la tabla.")],"sesion-pimentel")
print("ok", len(c), "chats")
