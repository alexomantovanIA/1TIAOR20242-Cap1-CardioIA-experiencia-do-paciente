# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

---

# CardioIA - Assistente Cardiológico Inteligente e Conversacional

### Fase 5

---

## 👨‍🎓 Integrantes:

- [Alexandre Oliveira Mantovani](https://www.linkedin.com/in/alexomantovani)
- [Edmar Ferreira Souza](https://www.linkedin.com/in/)
- [Ricardo Lourenço Coube](https://www.linkedin.com/in/ricardolcoube/)
- [Jose Andre Filho](https://www.linkedin.com/in/joseandrefilho)

## 👩‍🏫 Professores:

- Tutor: [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona)
- Coordenador: [André Godoi](https://www.linkedin.com/in/profandregodoi)

---

## 📌 Descrição do Projeto

Este repositório apresenta a **Fase 5 - Assistente Cardiológico Inteligente e Conversacional** do projeto **CardioIA**, com foco no desenvolvimento de um protótipo funcional de chatbot cardiológico educacional. A solução foi construída com **Python 3.10+**, **Flask**, **IBM Watson Assistant** e uma interface web simples em **HTML, CSS e JavaScript puro**.

O objetivo é simular uma experiência de **triagem inicial cardiovascular** e **apoio educacional**, permitindo que o usuário relate sintomas, receba orientações iniciais seguras, compreenda exames comuns e seja alertado em cenários compatíveis com urgência.

> **Aviso Acadêmico, Médico e de Governança**: este projeto tem **uso estritamente acadêmico**. O assistente **não realiza diagnóstico**, **não prescreve medicamentos**, **não substitui o médico** e **não deve ser utilizado para decisões clínicas reais**. A arquitetura foi planejada com ênfase em **ética, segurança, transparência e aderência conceitual à LGPD**.

---

## 📦 Entregáveis

### Parte 1 - Assistente Conversacional com NLP
- Modelagem de intents, entities e fluxo no padrão IBM Watson Assistant.
- Integração com API v2 do Watson Assistant.
- Modo fallback local para demonstração offline.
- Regras de segurança para sinais de alerta cardiovasculares.

### Parte 2 - Interface de Interação com o Usuário
- Interface web simples e responsiva.
- Comunicação com backend Flask via `POST /api/chat`.
- Renderização de respostas, estados de carregamento e alerta de urgência.

---

## 🧪 Metodologia

1. **Fase A - Planejamento e arquitetura**: definição de objetivo, escopo, restrições, estrutura de diretórios e arquivos de configuração.
2. **Fase B - Modelagem do assistente**: construção de intents, entities, respostas e fluxo conversacional compatível com Watson Assistant.
3. **Fase C - Backend Flask**: implementação dos endpoints, validação, normalização de respostas e organização por camadas.
4. **Fase D - Integração Watson**: criação da classe de serviço com autenticação, sessão e fallback offline.
5. **Fase E - Regras de segurança e ética**: detecção de urgência, sobrescrita de respostas inseguras e inclusão de disclaimer.
6. **Fase F - Frontend simples**: desenvolvimento da interface de chat responsiva com JavaScript puro.
7. **Fase G - Testes**: criação de testes básicos com `pytest` para saúde da aplicação, endpoint de chat, payload inválido e urgência.
8. **Fase H/I - Documentação acadêmica**: relatório, roteiro de vídeo, documentação Watson e README final em padrão FIAP.

---

## 🔄 Fluxo Conversacional Resumido

1. Saudação e apresentação do escopo educacional.
2. Coleta da queixa principal, duração, intensidade e sintomas associados.
3. Classificação em orientação educacional, recomendação de acompanhamento ou alerta de urgência.
4. Encerramento com mensagem segura e reforço do limite do assistente.

---

## 📊 Métricas e Critérios de Avaliação

- **Cobertura funcional**: presença dos endpoints, frontend integrado e fluxo conversacional mínimo.
- **Segurança**: capacidade de detectar urgência e bloquear diagnóstico.
- **Qualidade técnica**: organização modular, clareza do código e facilidade de execução local.
- **Documentação**: README acadêmico, relatório, instruções de configuração e amostras.
- **Testabilidade**: execução simples dos testes automatizados com `pytest`.

---

## 🗂️ Estrutura do Projeto

```text
cardioia-fase5-assistente-cardiologico/
│
├─ assets/
│  └─ logo-fiap.png
├─ assistant/
│  ├─ cardioia_assistant_export.json
│  ├─ fluxo_conversacional.md
│  └─ intents_entities_documentation.md
├─ backend/
│  ├─ __init__.py
│  ├─ app.py
│  ├─ config.py
│  ├─ models/
│  │  └─ message_models.py
│  ├─ prompts/
│  │  └─ response_guidelines.md
│  ├─ routes/
│  │  └─ chat_routes.py
│  ├─ services/
│  │  └─ watson_service.py
│  ├─ tests/
│  │  ├─ test_chat_endpoint.py
│  │  ├─ test_healthcheck.py
│  │  └─ test_safety_rules.py
│  └─ utils/
│     ├─ safety_rules.py
│     └─ validators.py
├─ docs/
│  ├─ arquitetura_solucao.md
│  ├─ instrucoes_configuracao_watson.md
│  ├─ relatorio_fase5.md
│  └─ roteiro_video.md
├─ frontend/
│  ├─ index.html
│  ├─ script.js
│  └─ style.css
├─ samples/
│  ├─ conversas_exemplo.md
│  ├─ json_examples/
│  │  ├─ request_exemplo.json
│  │  └─ response_exemplo.json
│  └─ screenshots/
│     ├─ fluxo_assistente.png
│     └─ tela_chat.png
├─ .env.example
├─ .gitignore
├─ LICENSE
├─ README.md
└─ requirements.txt
```

---

## ✅ Requisitos para Execução

- Python **3.10+**
- `pip` disponível no ambiente
- Conta IBM Cloud com Watson Assistant configurado, caso deseje usar integração real

Instalação das dependências:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Como Configurar IBM Watson Assistant

1. Criar um assistente no IBM Watson Assistant.
2. Replicar a modelagem descrita em `assistant/cardioia_assistant_export.json`.
3. Copiar `API Key`, `Service URL` e `Assistant ID`.
4. Criar um arquivo `.env` com base no `.env.example`.

Exemplo:

```env
FLASK_ENV=development
FLASK_DEBUG=true
PORT=5000
WATSON_API_KEY=sua_chave
WATSON_URL=https://api.us-south.assistant.watson.cloud.ibm.com/instances/xxxx
WATSON_ASSISTANT_ID=seu_assistant_id
WATSON_ASSISTANT_VERSION=2021-11-27
```

Sem essas variáveis, o projeto continua funcional em modo demonstrativo offline.

---

## ▶️ Como Rodar o Backend

```bash
python -m backend.app
```

Aplicação disponível em:

```text
http://localhost:5000
```

Endpoint de healthcheck:

```text
GET /health
```

Endpoint principal:

```text
POST /api/chat
```

---

## 💻 Como Rodar o Frontend

O frontend é servido pelo próprio Flask. Basta iniciar o backend e abrir:

```text
http://localhost:5000
```

---

## 🧪 Como Executar os Testes

```bash
pytest backend/tests -q
```

---

## ⚠️ Limitações

- O fallback local usa regras simples por palavras-chave.
- Não há banco de dados nem histórico persistente.
- Não existe autenticação de usuários.
- O assistente não processa prontuários ou dados clínicos reais.
- O protótipo não substitui avaliação profissional.

---

## 📝 Licença

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
Este projeto segue o modelo FIAP e está licenciado sob
<a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer">Attribution 4.0 International (CC BY 4.0)</a>.
</p>
