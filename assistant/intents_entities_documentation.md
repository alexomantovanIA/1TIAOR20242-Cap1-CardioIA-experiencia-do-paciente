# Documentação de Intents e Entities

## Visão geral
Este documento descreve a modelagem mínima do CardioIA para a Fase 5 com base na lógica de um assistente IBM Watson Assistant. O objetivo é sustentar um protótipo acadêmico de triagem inicial simulada e apoio educacional, sem realizar diagnóstico médico.

## Intents

| Intent | Finalidade | Exemplos de utterances |
|---|---|---|
| `#saudacao` | Iniciar a conversa e apresentar o assistente | "oi", "olá", "bom dia" |
| `#despedida` | Encerrar a interação com segurança | "tchau", "obrigado" |
| `#informar_sintoma` | Relato geral de sintomas | "estou sentindo algo no peito" |
| `#informar_dor_toracica` | Dor, pressão ou aperto no tórax | "estou com dor no peito" |
| `#informar_falta_de_ar` | Falta de ar ou dispneia | "estou com falta de ar" |
| `#informar_palpitacao` | Coração acelerado ou irregular | "estou com palpitação" |
| `#informar_tontura` | Tontura ou pré-síncope | "fiquei tonto" |
| `#pedir_orientacao` | Solicitar orientação ampla | "o que devo fazer?" |
| `#pedir_explicacao_exame` | Pedir explicação sobre exames | "o que é ECG?" |
| `#urgencia` | Reconhecer sinais de alerta | "dor intensa no peito e desmaio" |
| `#fallback` | Lidar com fora de escopo, ambiguidade ou insistência em diagnóstico | "pode me diagnosticar?" |

## Entities

| Entity | Finalidade | Exemplos |
|---|---|---|
| `@sintoma` | Identificar sintomas principais | dor no peito, falta de ar, palpitação |
| `@duracao` | Entender há quanto tempo ocorre | minutos, horas, dias |
| `@intensidade` | Capturar gravidade percebida | leve, moderada, intensa |
| `@frequencia` | Observar padrão temporal | contínua, intermitente |
| `@exame` | Reconhecer exames cardiovasculares | ECG, ecocardiograma, Holter |
| `@sinal_alarme` | Identificar urgência | desmaio, suor frio, irradiação para braço |

## Regras de modelagem
- O fluxo sempre deve reforçar o caráter educacional do assistente.
- Intents de urgência têm prioridade sobre orientações comuns.
- Mensagens ambíguas devem gerar perguntas objetivas para desambiguar.
- Pedidos de diagnóstico devem ser redirecionados para o limite de escopo.
- Perguntas fora do tema cardiovascular devem usar `#fallback`.

## Tratamento de exceções

### Entrada vazia
Resposta: solicitar que o usuário informe uma mensagem válida.

### Mensagem ambígua
Resposta: pedir sintoma principal, duração e intensidade.

### Múltiplos sintomas na mesma frase
Resposta: priorizar sinais de alerta e depois seguir para coleta estruturada.

### Pergunta fora do escopo
Resposta: explicar que o assistente cobre apenas sintomas cardiovasculares, sinais de alerta e exames comuns.

### Insistência em diagnóstico
Resposta: negar o diagnóstico e orientar avaliação profissional.
