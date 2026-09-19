import ollama

def ask_llm(diagnosis):
    prompt = f"""
You are an AI healthcare assistant for DiagnosAI.

The machine learning model has predicted the following health condition:

{diagnosis}

Explain what this condition means in simple language.

Rules:
- Keep the explanation to 2-4 sentences.
- Explain only what the condition is.
- Do not provide treatment or medical advice.
- Do not recommend medicines, lifestyle changes, or tests.
- Do not claim that the user definitely has the condition.
- Do not mention that you are an AI unless necessary.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]