
import os
import sys

import httpx
from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors
from google.genai import types

DEFAULT_MODEL = "gemini-3.5-flash"
EXIT_COMMANDS = {"exit", "quit"}

# Instrução de sistema: define o comportamento padrão do assistente.
SYSTEM_INSTRUCTION = (
    "Você é um assistente de IA integrado a um chatbot de terminal. "
    "Responda de forma clara, objetiva e educada, utilizando o mesmo "
    "idioma em que o usuário escreveu a mensagem."
)


def carregar_api_key() -> str:
    """Carrega a GEMINI_API_KEY a partir do arquivo .env / ambiente.

    Encerra o programa com uma mensagem explicativa caso a chave
    não tenha sido configurada.
    """
    load_dotenv()  

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print(" Erro: a variável de ambiente GEMINI_API_KEY não foi encontrada.\n")
        sys.exit(1)

    return api_key


def criar_chat(api_key: str):
    """Cria o cliente do Gemini e inicia uma sessão de chat.

    O objeto de chat retornado por `client.chats.create` mantém
    automaticamente o histórico da conversa a cada `send_message`,
    o que garante que o modelo entenda o contexto das mensagens
    anteriores.

    """
    model_name = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)

    client = genai.Client(api_key=api_key)
    chat = client.chats.create(
        model=model_name,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
        ),
    )
    return chat, model_name, client


def exibir_boas_vindas(model_name: str) -> None:
    """Mostra o cabeçalho inicial com instruções básicas de uso."""
    print("=" * 60)
    print("Chatbot")
    print("=" * 60)
    print(f"Modelo em uso: {model_name}")
    print("Digite sua mensagem e pressione Enter para conversar.")
    print("Digite 'exit' ou 'quit' para encerrar o chatbot.")
    print("=" * 60 + "\n")


def obter_resposta(chat, mensagem: str) -> str | None:
    """Envia a mensagem ao Gemini e trata os possíveis erros.

    Retorna o texto da resposta em caso de sucesso, ou None se algum
    erro ocorreu (a mensagem de erro já é exibida dentro da função).
    """
    print("Gemini está processando sua resposta...", end="\r")

    try:
        resposta = chat.send_message(mensagem)
        print(" " * 45, end="\r")  

        if not resposta.text:
            print(" O Gemini não retornou nenhum texto para essa mensagem.")
            return None

        return resposta.text

    except httpx.TransportError:
        # Erros de rede
        print(" " * 45, end="\r")
        print("Erro de conexão: não foi possível acessar a API do Gemini.")

    except genai_errors.APIError as e:
        # Erros retornados pela própria API 
        print(" " * 45, end="\r")
        print(f" Erro da API do Gemini (código {e.code}): {e.message}")

    except Exception as e:  # rede de segurança para erros inesperados
        print(" " * 45, end="\r")
        print(f" Erro inesperado: {e}")

    return None


def main() -> None:
    api_key = carregar_api_key()
    chat, model_name, client = criar_chat(api_key)
    exibir_boas_vindas(model_name)

    while True:
        try:
            mensagem = input("Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n Até logo!")
            break

        # Entrada vazia: pede para o usuário digitar algo e continua.
        if not mensagem:
            print(" Digite uma mensagem antes de enviar.\n")
            continue

        # Comandos de saída.
        if mensagem.lower() in EXIT_COMMANDS:
            print("\n Até logo!")
            break

        resposta = obter_resposta(chat, mensagem)
        if resposta is not None:
            print(f"Gemini: {resposta}\n")


if __name__ == "__main__":
    main()
