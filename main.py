dias_semana = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
bombeiros = {
    "João": ["seg", "ter"],
    "Maria": ["qua"],
    "Carlos": []
}

def gerar_escala(bombeiros, dias):
    escala = {}
    ultimo_plantao = {}
    for dia in dias:
        disponiveis = [b for b, folgas in bombeiros.items() if dia not in folgas]
        if not disponiveis:
            escala[dia] = "SEM PLANTÃO"
            continue
        
        candidatos = []
        for b in disponiveis:
            if b in ultimo_plantao:
                if ultimo_plantao[b] != "sem_plantao":
                    if dias.index(ultimo_plantao[b]) == dias.index(dia) - 1:
                        continue
            candidatos.append(b)
        
        if not candidatos:
            escala[dia] = "SEM PLANTÃO"
            ultimo_plantao["sem_plantao"] = dia
        else:
            escolhido = candidatos[0]
            escala[dia] = escolhido
            ultimo_plantao[escolhido] = dia
    return escala

resultado = gerar_escala(bombeiros, dias_semana)
for dia, bombeiro in resultado.items():
    print(f"{dia}: {bombeiro}")