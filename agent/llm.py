import os
from dotenv import load_dotenv
from ollama import chat


load_dotenv()


class OllamaLLM:
    def __init__(self, model=None):
        self.model = model or os.getenv("OLLAMA_MODEL", "qwen2.5-coder")

    def generate(self, messages):
        try:
            response = chat(
                model=self.model,
                messages=messages
            )

            return response["message"]["content"]

        except Exception as error:
            return f"Erro ao conectar com o Ollama: {error}"
