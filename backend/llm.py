import ollama

def ask_llm(messages):
    response = ollama.chat(
        model="llama3.2:3b",
        messages=messages
    )

    return response["message"]["content"]