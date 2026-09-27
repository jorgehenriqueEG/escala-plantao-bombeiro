# escala-plantao-bombeiro
## Descrição do Problema
Gerar a escala de plantão dos bombeiros de uma cidade pequena para a próxima semana, considerando a disponibilidade de cada um e a regra de que ninguém pode ficar mais de 2 dias seguidos de plantão.
## Requisitos
- Receber uma lista de bombeiros com seus dias de folga.
- Distribuir o plantão de segunda a domingo.
- Garantir que cada dia tenha exatamente 1 bombeiro de plantão.
- Evitar que um bombeiro fique 2 dias seguidos de plantão.
## Exemplo de Uso
Bombeiros: João (folga: seg, ter), Maria (folga: qua), Carlos (sem folga)
Saída: Seg: Carlos, Ter: Maria, Qua: João, Qui: Carlos, Sex: Maria, Sáb: João, Dom: Carlos