# Arquitetura da Solução

## Visão geral
O CardioIA Fase 5 foi estruturado como um protótipo acadêmico de arquitetura leve, com frontend simples em HTML, CSS e JavaScript puro, backend em Flask e camada de integração com IBM Watson Assistant.

## Componentes principais

### Frontend
- Página única para interação com o usuário.
- Formulário de envio de mensagens.
- Área de renderização de respostas do assistente.
- Tratamento visual para alertas de urgência.

### Backend Flask
- `GET /health`: verifica disponibilidade da aplicação.
- `POST /api/chat`: recebe mensagem, valida dados, consulta o serviço do assistente e aplica regras de segurança.

### Serviço Watson
- Usa a API v2 do IBM Watson Assistant quando as credenciais estão configuradas.
- Cria e reutiliza sessão por `conversation_id`.
- Possui modo fallback local para demonstração offline acadêmica.

### Camada de segurança
- Detecta sinais de urgência por palavras-chave.
- Sobrescreve respostas comuns quando o caso sugere risco.
- Inclui disclaimer institucional em todas as respostas relevantes.

## Fluxo técnico resumido
1. O usuário envia uma mensagem pelo frontend.
2. O frontend realiza `POST /api/chat`.
3. O backend valida o payload.
4. O `WatsonService` consulta a API do Watson ou usa fallback local.
5. As regras de segurança avaliam urgência e limites de uso.
6. O backend responde com JSON padronizado.
7. O frontend exibe a orientação ao usuário.

## Decisões arquiteturais
- Sem banco de dados: a persistência de sessão é mantida em memória apenas para simplificar a demonstração.
- Sem framework frontend: a interface foi mantida enxuta para aderência ao escopo acadêmico.
- Sem autenticação: foco na prova de conceito de experiência conversacional.
- Sem diagnóstico automatizado: a lógica privilegia segurança e uso educacional.

## Considerações de governança
- O projeto não usa dados pessoais reais.
- O assistente não toma decisão clínica.
- O fluxo foi desenhado para reduzir risco de interpretação como consulta médica.
