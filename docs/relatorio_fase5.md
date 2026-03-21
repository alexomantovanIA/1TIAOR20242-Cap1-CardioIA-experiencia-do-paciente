# Relatório da Fase 5 - CardioIA

## Objetivo
Esta fase do projeto CardioIA teve como objetivo construir um protótipo funcional de assistente cardiológico inteligente e conversacional, com foco em uso educacional e triagem inicial simulada. A proposta foi integrar um backend simples em Python com Flask, uma interface web direta e uma modelagem compatível com IBM Watson Assistant, preservando clareza arquitetural e responsabilidade ética.

## Funcionamento do fluxo conversacional
O fluxo foi desenhado para iniciar com saudação, apresentação do escopo e coleta da queixa principal. Em seguida, o assistente solicita elementos básicos da narrativa clínica, como duração, intensidade, frequência e sintomas associados. Essa coleta organiza a interação e prepara uma classificação simplificada em três possibilidades: orientação educacional, recomendação de acompanhamento médico e alerta de urgência.

Quando o usuário relata sinais compatíveis com maior gravidade, como dor intensa no peito, desmaio, suor frio, irradiação para braço ou falta de ar severa, o sistema interrompe a resposta convencional e emite orientação de segurança. Essa escolha foi incluída para reforçar o caráter responsável do protótipo e evitar respostas que possam ser interpretadas como aconselhamento médico definitivo.

## Arquitetura implementada
A arquitetura foi dividida em três camadas principais. A primeira é o frontend em HTML, CSS e JavaScript puro, responsável pela experiência de chat. A segunda é o backend Flask, que expõe os endpoints `/health` e `/api/chat`, valida as mensagens recebidas e normaliza as respostas. A terceira é a camada de integração com IBM Watson Assistant, encapsulada em uma classe de serviço que cria sessão, autentica na API v2 e busca respostas do assistente modelado.

Como o uso real da API depende de credenciais externas, foi incluído um fallback local funcional. Esse modo permite executar o protótipo em ambiente acadêmico mesmo sem acesso configurado ao Watson, o que melhora a reprodutibilidade da entrega e facilita demonstrações.

## Integração com IBM Watson
A integração foi planejada com as variáveis `WATSON_API_KEY`, `WATSON_URL`, `WATSON_ASSISTANT_ID` e `WATSON_ASSISTANT_VERSION`. Quando essas credenciais estão presentes, o backend abre sessão no assistente e envia mensagens usando a API v2. Quando não estão disponíveis, o sistema opera em modo offline com um conjunto de respostas controladas e identificação simplificada de intenções e entidades.

## Limitações
Por ser um protótipo acadêmico, a solução não cobre linguagem natural complexa, contexto clínico aprofundado ou persistência robusta de conversas. Não há banco de dados, autenticação ou histórico permanente. A interpretação semântica do modo offline é intencionalmente simples e baseada em palavras-chave. Além disso, as respostas não devem ser interpretadas como orientação diagnóstica ou terapêutica.

## Ética, governança e LGPD
O projeto foi elaborado com ênfase em segurança, transparência e responsabilidade. O CardioIA informa explicitamente seus limites, evita emitir diagnósticos e direciona o usuário a procurar atendimento profissional quando necessário. Como não há uso de dados sensíveis reais nem armazenamento persistente de informações pessoais, o risco relacionado à privacidade foi reduzido. Ainda assim, a documentação reforça que qualquer evolução futura precisará considerar consentimento, finalidade, minimização de dados, trilhas de auditoria e aderência à LGPD.
