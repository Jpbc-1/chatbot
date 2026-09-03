#  Chatbot

Chatbot de terminal (CLI) desenvolvido em **Python**, integrado à **API do Google Gemini**, capaz de manter uma conversa contínua e contextualizada diretamente no terminal.

Projeto criado como exercício prático de integração com LLMs (Large Language Models), cobrindo desde o consumo de uma API de IA generativa até boas práticas de organização de código, segurança de credenciais e tratamento de erros.

---

##  Descrição

O **Chatbot** é uma aplicação de linha de comando que permite conversar com o modelo **Gemini**, da Google, sem sair do terminal. Cada mensagem enviada leva em conta o histórico da conversa, para que o modelo entenda o contexto e gere respostas coerentes ao longo do diálogo — assim como em um chat comum.

O projeto foi pensado para ser simples de ler, simples de rodar e fácil de estender, servindo tanto como ferramenta de estudo de APIs de IA generativa quanto como base para projetos maiores.

---

## Funcionalidades

- Conversa contínua e interativa via terminal
- Histórico de conversa mantido automaticamente (o Gemini "lembra" do que foi dito antes)
- Chave de API carregada com segurança via variável de ambiente (nunca fica no código)
- Tratamento de erros para:
  - chave de API ausente
  - falha de conexão com a internet
  - erros retornados pela API do Gemini
  - entrada vazia do usuário
- Comandos `exit` / `quit` para encerrar o chatbot a qualquer momento
- Indicador simples de "processando..." enquanto o Gemini gera a resposta
- Código modular, comentado e fácil de entender

---

##  Tecnologias utilizadas

Python 3.11+
google-genai
python-dotenv
httpx
---

##  Requisitos

Antes de começar, você precisa ter:

- **Python 3.11 ou superior** 
- Uma **chave de API do Google Gemini** 
- Conexão com a internet

---



## Como instalar as dependências

Clone o repositório e crie um ambiente virtual :

```bash
git clone https://github.com/seu-usuario/chatbot.git
cd gemini-cli-chatbot

# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Linux / macOS:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1

# Instalar as dependências
pip install -r requirements.txt
```

---

##  Como configurar o `.env`

O projeto usa um arquivo `.env` para armazenar sua chave de API com segurança (esse arquivo nunca deve ser enviado ao Git — ele já está listado no `.gitignore`).

```bash
# 1. Copie o arquivo de exemplo
cp .env.example .env       # Linux/macOS
copy .env.example .env     # Windows

# 2. Abra o .env e cole sua chave
GEMINI_API_KEY=sua_chave_aqui
```

Opcionalmente, você pode definir também qual modelo do Gemini usar (por padrão o projeto usa `gemini-3.5-flash`):

```bash
GEMINI_MODEL=gemini-3.5-flash
```

---

##  Como executar o projeto

Com o ambiente virtual ativado e o `.env` configurado, basta rodar:

```bash
python main.py
```

---

##  Exemplo de uso

```text
============================================================
Chatbot
============================================================
Modelo em uso: gemini-3.5-flash
Digite sua mensagem e pressione Enter para conversar.
Digite 'exit' ou 'quit' para encerrar o chatbot.
============================================================

Você: Olá! Quem é você?
Gemini: Olá! Sou um assistente baseado no modelo Gemini, do Google, e estou
aqui para ajudar com o que você precisar. Como posso te ajudar hoje?

Você: Me dê uma dica rápida de produtividade
Gemini: Claro! Uma técnica simples e eficaz é a "regra dos 2 minutos": se uma
tarefa leva menos de 2 minutos para ser feita, faça-a imediatamente em vez
de adiar para depois.

Você: exit

 Até logo!
```

---

##  Estrutura do projeto

```text
gemini-cli-chatbot/
├── main.py            # Código principal do chatbot
├── requirements.txt    # Dependências do projeto
├── .env.example        # Modelo de configuração das variáveis de ambiente
├── .gitignore           # Arquivos e pastas ignorados pelo Git
└── README.md            # Este arquivo
```

---

##  Licença

Este projeto está licenciado sob a licença MIT — sinta-se livre para usá-lo, estudá-lo e modificá-lo.
