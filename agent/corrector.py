from agent.llm import OllamaLLM
from agent.prompts import CORRECTION_SYSTEM_PROMPT


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

Antes de atribuir a nota, verifique:

Se o código atende ao enunciado.
Se os critérios obrigatórios foram cumpridos.
Se há erros de sintaxe relevantes.
Se os conceitos de POO foram aplicados corretamente.
Se as penalidades informadas pelo professor devem ser aplicadas.

Responda seguindo exatamente o formato obrigatório definido no sistema.
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

        return self.llm.generate(messages)

