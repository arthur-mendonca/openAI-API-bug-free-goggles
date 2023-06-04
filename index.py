import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def summary(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Resuma este texto: {text}",
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()


arquivo = "arquivo.txt"
texto = read_file(arquivo)
print(summary(texto))
