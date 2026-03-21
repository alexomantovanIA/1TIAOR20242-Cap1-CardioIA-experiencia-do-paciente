# Fluxo Conversacional do CardioIA

## Objetivo do fluxo
Conduzir o usuário por uma interação segura, curta e educativa sobre sintomas cardiovasculares, com foco em triagem inicial simulada.

## Etapas do fluxo

### 1. Saudação
O assistente cumprimenta o usuário, apresenta o nome CardioIA e informa que a interação é acadêmica e educacional.

### 2. Apresentação do escopo
O sistema informa que pode:
- coletar sintomas iniciais;
- explicar sinais de alerta;
- explicar exames cardiovasculares comuns.

Também informa que não pode:
- diagnosticar;
- prescrever medicamentos;
- substituir o médico.

### 3. Coleta da queixa principal
O assistente pede:
- sintoma principal;
- duração;
- intensidade;
- frequência;
- sintomas associados.

### 4. Perguntas complementares
Dependendo do sintoma relatado, o assistente pergunta:
- dor no peito: há irradiação, falta de ar ou suor frio?
- palpitação: há tontura, desmaio ou gatilho conhecido?
- falta de ar: ocorre em repouso ou esforço?
- tontura: houve quase desmaio ou palpitação associada?

### 5. Classificação básica

#### Orientação educacional
Quando os sintomas são leves, sem sinais de alerta, o assistente fornece explicação breve e orienta acompanhamento profissional se houver persistência.

#### Sugestão de acompanhamento médico
Quando há recorrência, duração prolongada ou impacto funcional, o sistema recomenda avaliação clínica programada.

#### Alerta de urgência
Quando há palavras-chave como dor intensa no peito, desmaio, irradiação para braço e falta de ar severa, o assistente interrompe o fluxo comum e orienta busca imediata por atendimento.

### 6. Encerramento seguro
Toda conversa termina com lembrete de uso educacional e recomendação para procurar ajuda profissional em caso de dúvida, persistência ou piora.

## Cenários excepcionais
- Entrada vazia: solicitar texto válido.
- Múltiplos sintomas: considerar o mais grave primeiro.
- Fora de escopo: redirecionar para tema cardiovascular.
- Pedido insistente por diagnóstico: recusar e reforçar limites.
