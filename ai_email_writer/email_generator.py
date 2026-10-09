import os
import requests


def generate_email(purpose, recipient, tone, details):
    api_key = os.getenv("OLLAMA_API_KEY")

    if not api_key:
        return "Error: Ollama API key not found."

    prompt = f"""
    Write a well-structured email based on the information below.

    Purpose: {purpose}
    Recipient: {recipient}
    Tone: {tone}
    Important details: {details}

    Requirements:
    - Include a suitable subject line.
    - Write a complete email.
    - Keep it clear and concise.
    - Do not invent information.
    - Do not add explanations outside the email.
    """

    try:
        response = requests.post(
            "https://ollama.com/api/chat",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-oss:20b",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "stream": False
            },
            timeout=60
        )

        if response.status_code == 200:
            return response.json()["message"]["content"]

        return f"API Error: {response.status_code}"

    except requests.exceptions.RequestException:
        return "Error: Unable to connect to Ollama API."