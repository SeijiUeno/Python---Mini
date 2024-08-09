from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"  # Pode ser qualquer string, já que Ollama não requer autenticação local
)

def get_chat_response(messages):
    try:
        response = client.chat.completions.create(
            model="qwen2:0.5b",
            messages=messages
        )
        
        assistant_message = response.choices[0].message.content
        
        return assistant_message, messages
    except AttributeError as e:
        print("Erro ao acessar a resposta:", e)
        return "Erro: Não foi possível obter a resposta.", messages

def save_conversation_history(messages, filename="conversation_history.txt"):
    try:
        with open(filename, 'w') as file:
            for message in messages:
                role = message['role']
                content = message['content']
                file.write(f"{role}: {content}\n")
        print(f"Histórico da conversa salvo em '{filename}'.")
    except IOError as e:
        print(f"Erro ao salvar o histórico: {e}")

def print_help():
    help_text = """
    Comandos disponíveis:
    /ajuda - Lista todos os comandos disponíveis.
    /salvar - Salva o histórico da conversa em um arquivo de texto.
    /sair - Encerra o chat.
    """
    print(help_text)


def main():
    message_history = []
    
    while True:
        user_input = input("> ")
        
        if user_input == "/ajuda":
            print_help()
            continue
        
        if user_input == "/salvar":
            save_conversation_history(message_history)
            continue
        
        if user_input == "/sair":
            print("Encerrando o chat...")
            break

        message_history.append({"role": "user", "content": user_input})
        assistant_response, updated_message_history = get_chat_response(message_history)
        message_history = updated_message_history
        message_history.append({"role": "assistant", "content": assistant_response})
        print(assistant_response)

if __name__ == "__main__":
    main()
