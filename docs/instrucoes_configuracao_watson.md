# Instruções de Configuração do IBM Watson Assistant

## Objetivo
Configurar o CardioIA para utilizar a API v2 do IBM Watson Assistant em ambiente local.

## Pré-requisitos
- Conta IBM Cloud com serviço Watson Assistant criado.
- Assistente configurado com intents, entities e fluxo equivalente ao arquivo `assistant/cardioia_assistant_export.json`.
- Python 3.10+ instalado.

## Passo a passo

### 1. Criar o assistente
No IBM Watson Assistant, crie um novo assistente e use a modelagem documentada na pasta `assistant/` como referência para intents, entities e nós de diálogo.

### 2. Obter credenciais
No painel do serviço, copie:
- `API Key`
- `Service URL`
- `Assistant ID`

### 3. Configurar o `.env`
Crie um arquivo `.env` com base no `.env.example`:

```env
FLASK_ENV=development
FLASK_DEBUG=true
PORT=5000
WATSON_API_KEY=sua_chave
WATSON_URL=https://api.us-south.assistant.watson.cloud.ibm.com/instances/xxxx
WATSON_ASSISTANT_ID=seu_assistant_id
WATSON_ASSISTANT_VERSION=2021-11-27
```

### 4. Executar a aplicação
Instale as dependências e inicie o backend:

```bash
pip install -r requirements.txt
python -m backend.app
```

### 5. Testar integração
- Acesse `http://localhost:5000/`
- Envie uma mensagem de saudação
- Verifique se a resposta vem com `source: "watson"` no retorno JSON

## Observação
Se as credenciais não forem configuradas, o projeto continua funcional em modo demonstrativo offline com respostas locais controladas.
