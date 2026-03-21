# Roteiro de Video - CardioIA Fase 5

**Duracao total:** ate 3 minutos
**Formato:** gravacao de tela com narracao
**Resolucao recomendada:** 1920x1080 (Full HD)

---

## Preparacao Antes da Gravacao

1. Iniciar o backend: `python -m backend.app`
2. Verificar que o terminal mostra `watson_connected: True` (ou confirmar via `/health`)
3. Abrir `http://localhost:5000` no navegador
4. Limpar qualquer conversa anterior (botao "Limpar conversa")
5. Ter o terminal visivel em segundo plano para mostrar logs
6. Opcional: ter o resultado de `pytest backend/tests -q` pronto para mostrar

---

## Cena 1 - Apresentacao do Projeto (0:00 - 0:30)

**Narrador mostra a tela inicial do projeto no navegador.**

> "Este e o CardioIA, um assistente cardiologico inteligente e conversacional desenvolvido como projeto da Fase 5 na FIAP. O objetivo e demonstrar um chatbot educacional que interage com o usuario sobre saude cardiovascular, utilizando processamento de linguagem natural com IBM Watson Assistant."

**Acoes na tela:**
- Mostrar a interface do chat aberta no navegador
- Apontar o painel de boas-vindas com o titulo "CardioIA"
- Mostrar brevemente os exemplos de prompt sugeridos na interface
- Destacar que a interface e responsiva e acessivel

**Pontos tecnicos a mencionar:**
- Frontend em HTML5, CSS3 e JavaScript puro (sem frameworks)
- Backend em Flask (Python)
- Integracao com IBM Watson Assistant API v2

---

## Cena 2 - Interacao com Sintomas (0:30 - 1:15)

**Narrador demonstra uma conversa tipica de relato de sintoma.**

> "Vamos simular uma interacao real. O usuario relata palpitacoes leves ha 2 dias..."

**Acoes na tela:**
1. Digitar: `Oi, bom dia!`
2. Mostrar a resposta de saudacao do assistente
3. Apontar a tag de fonte (Watson Assistant ou Fallback local)
4. Digitar: `Estou com palpitacoes leves ha 2 dias e queria uma orientacao inicial.`
5. Mostrar a resposta educativa sobre palpitacoes
6. Destacar a nota de rodape reforçando carater educativo

> "O assistente reconheceu a intencao de palpitacao (intent: informar_palpitacao), extraiu informacoes de duracao e intensidade (entities: @duracao=dias, @intensidade=leve), e forneceu orientacao educacional adequada."

**Conceitos demonstrados:** reconhecimento de intent, extracao de entities, resposta contextualizada.

---

## Cena 3 - Pergunta sobre Exame (1:15 - 1:45)

**Narrador pergunta sobre um exame cardiaco.**

> "Agora vamos perguntar sobre um exame cardiovascular."

**Acoes na tela:**
1. Digitar: `O que e um ECG e quando ele costuma ser solicitado?`
2. Mostrar a resposta educativa sobre o eletrocardiograma
3. Destacar a qualidade e completude da resposta

> "O assistente identificou a intencao perguntar_ecg e forneceu informacao educacional clara e estruturada sobre o eletrocardiograma. O sistema suporta 5 exames especificos: ECG, ecocardiograma, Holter, teste ergometrico e cateterismo."

**Conceitos demonstrados:** intents de exames, respostas educativas estruturadas.

---

## Cena 4 - Cenario de Urgencia (1:45 - 2:15)

**Narrador demonstra a deteccao de urgencia - funcionalidade critica do sistema.**

> "Agora vamos testar o cenario mais importante: a deteccao de urgencia cardiovascular."

**Acoes na tela:**
1. Digitar: `Estou com dor intensa no peito e falta de ar.`
2. Mostrar a resposta com indicador de urgencia
3. Destacar a mensagem sobre SAMU 192
4. Apontar a tag de fonte mostrando "Regra de seguranca"

> "O sistema detectou palavras-chave de urgencia antes mesmo de consultar o Watson. Esta camada de seguranca opera de forma independente e sobrescreve qualquer resposta padrao com um alerta de urgencia, orientando o usuario a buscar atendimento medico imediato e ligando para o SAMU 192. Isso demonstra o compromisso do projeto com a seguranca do paciente."

**Conceitos demonstrados:** regras de seguranca pre-Watson, sobrescrita de resposta, SAMU 192.

---

## Cena 5 - Limite Etico (2:15 - 2:30)

**Narrador demonstra o tratamento de solicitacao de diagnostico.**

> "Vamos testar o limite etico do assistente."

**Acoes na tela:**
1. Digitar: `O que eu tenho? Me da um diagnostico.`
2. Mostrar a resposta de limite - o assistente recusa educadamente

> "O assistente reconhece a intencao de solicitar diagnostico e responde de forma etica, reforçando que nao tem capacidade de diagnosticar e orientando o usuario a consultar um profissional."

**Conceitos demonstrados:** governanca, limites eticos, recusa educada.

---

## Cena 6 - Arquitetura e Testes (2:30 - 3:00)

**Narrador mostra brevemente o codigo e os testes.**

> "A arquitetura do projeto utiliza Flask no backend, com integracao ao IBM Watson Assistant e modo fallback local para operacao offline. O frontend e simples, responsivo e acessivel."

**Acoes na tela:**
1. Mostrar rapidamente a estrutura de diretorios no explorador de arquivos
2. Alternar para o terminal
3. Mostrar o servidor rodando com indicacao de Watson conectado
4. Executar `pytest backend/tests -q` e mostrar resultado: "30 passed"

> "Os 30 testes automatizados validam o healthcheck, o endpoint de chat com diversos cenarios, e as regras de seguranca incluindo deteccao de urgencia com normalizacao de acentos. O projeto esta organizado com documentacao completa no repositorio GitHub."

**Encerramento:**
> "Obrigado pela atencao. Projeto CardioIA - Fase 5 - FIAP. Grupo: Alexandre Oliveira Mantovani, Edmar Ferreira Souza, Ricardo Lourenço Coube e Jose Andre Filho."

---

## Checklist Pre-Gravacao

- [ ] Backend iniciado e Watson conectado
- [ ] Interface carregada sem erros no console
- [ ] Conversa limpa (sem historico anterior)
- [ ] Audio de narracao testado
- [ ] Resolucao de tela adequada (1920x1080)
- [ ] Terminal visivel para demonstracao de testes
- [ ] Resultado de pytest preparado

## Plano de Contingencia

Se o Watson estiver indisponivel no momento da gravacao:
- O sistema opera automaticamente em modo fallback local
- A tag de fonte mostrara "Fallback local" ao inves de "Watson Assistant"
- Todas as funcionalidades de intents, entities e seguranca continuam operacionais
- Mencionar na narracao que o fallback esta ativo e explicar a dualidade do sistema
