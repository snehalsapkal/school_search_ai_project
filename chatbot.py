import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who helps parents find schools."},
            {"role": "user", "content": message}
        ]
    )
    return response["choices"][0]["message"]["content"]
