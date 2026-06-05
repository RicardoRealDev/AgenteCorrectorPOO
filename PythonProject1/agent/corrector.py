import json

from agent.llm import OllamaLLM
from agent.prompts import CORRECTION_SYSTEM_PROMPT, ANNOTATION_SYSTEM_PROMPT


class JavaPOOCorrector:
    def __init__(self, model=None):
        self.llm = OllamaLLM(model=model)

    def correct(self, java_code, correction_params):
        user_prompt = f"""
        Corrija o código Java abaixo com base nos parâmetros definidos pelo professor.

        PARÂMETROS DA CORREÇÃO:

    {correction_params}

        CÓDIGO DO ALUNO:

        ```java
    {java_code}
        Instruções para correção:

        Leia o enunciado.
        Leia os critérios obrigatórios.
        Leia os critérios opcionais.
        Leia as penalidades.
        Analise o código do aluno.
        Aplique os descontos de forma proporcional.
        Calcule a nota final.
        Responda somente no formato JSON obrigatório.

        A nota final deve seguir esta lógica:
        nota_final = nota_maxima - soma_dos_descontos

        A nota final nunca pode ser menor que zero.
        A nota final nunca pode ser maior que a nota máxima.
        """
        messages = [
            {
                "role": "system",
                "content": CORRECTION_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]

        response = self.llm.generate(messages)

        return self._parse_json_response(response)

        def annotate_code(self, java_code, correction_params):
            user_prompt = f"""
            Adicione comentários explicativos no código Java do aluno.

            PARÂMETROS DA CORREÇÃO:

            {correction_params}

            CÓDIGO ORIGINAL DO ALUNO:

            ```java
            {java_code}
            Instruções:

            Preserve o código original.
            Não corrija diretamente o código.
            Adicione comentários Java com // antes das linhas problemáticas.
            Explique o erro.
            Explique como corrigir.
            Não use markdown.
            Responda apenas com o código Java comentado.
            """
            messages = [
                {
                    "role": "system",
                    "content": ANNOTATION_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]

            response = self.llm.generate(messages)

            return self._clean_code_response(response)
    def _parse_json_response(self, response):
        try:
            return json.loads(response)

        except json.JSONDecodeError:
            cleaned_response = self._clean_json_response(response)

            try:
                return json.loads(cleaned_response)

            except json.JSONDecodeError:
                return {
                    "erro": "O modelo não retornou um JSON válido.",
                    "resposta_original": response
                }

    def _clean_json_response(self, response):
        response = response.strip()

        if response.startswith("```json"):
            response = response.replace("```json", "", 1)

        if response.startswith("```"):
            response = response.replace("```", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()

    def _clean_code_response(self, response):
        response = response.strip()

        if response.startswith("```java"):
            response = response.replace("```java", "", 1)

        if response.startswith("```"):
            response = response.replace("```", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()

