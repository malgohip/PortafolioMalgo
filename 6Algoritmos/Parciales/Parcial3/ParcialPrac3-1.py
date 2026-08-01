def enlistador(linea: str):
    linea = linea.strip()
    if not linea:
        return []
    return [int(x) for x in linea.replace('\t', ' ').split()]


def auditorio():
    preinicios=input()
    prefinales=input()
    inicios=enlistador(preinicios)
    finales=enlistador(prefinales)
    if not inicios or not finales:
        print([])
        return
    n=min(len(inicios), len(finales))
    tiempos=[(inicios[i], finales[i]) for i in range(n)]
    orden=sorted(tiempos, key=lambda x: (x[1], x[0]))
    validas=[]
    termino=None
    for inicio, fin in orden:
        if termino is None or inicio>=termino:
            validas.append((inicio,fin))
            termino=fin
    if not validas:
        print([])
        return
    resultado=", ".join(f"[{inicio},{fin})" for inicio, fin in validas)
    print(resultado)

auditorio()