def get_default_correction_params():
    params = {
        "nota_maxima": 10,
        "nivel_correcao": "Rigoroso",
        "tema": "Programação Orientada a Objetos em Java",
        "enunciado": """
Crie uma classe Aluno com atributos nome e idade.
A classe deve usar encapsulamento, construtor, getters, setters e um método para exibir os dados do aluno.
""",
        "criterios_obrigatorios": [
            "Criar corretamente a classe Aluno.",
            "Declarar os atributos nome e idade.",
            "Usar atributos privados.",
            "Criar construtor.",
            "Criar métodos getters.",
            "Criar métodos setters.",
            "Criar método para exibir os dados do aluno.",
            "Usar boas práticas de Programação Orientada a Objetos."
        ],
        "criterios_opcionais": [
            "Código organizado e legível.",
            "Nomes de variáveis claros.",
            "Uso adequado da palavra-chave this.",
            "Evitar repetição desnecessária de código."
        ],
        "penalidades": [
            "Atributos públicos: até -2 pontos.",
            "Ausência de construtor: até -2 pontos.",
            "Ausência de getters: até -1 ponto.",
            "Ausência de setters: até -1 ponto.",
            "Código que não compila: até -3 pontos.",
            "Solução incompleta: até -3 pontos.",
            "Baixa legibilidade: até -1 ponto."
        ],
        "observacoes": """
A correção deve considerar que este é um exercício introdutório de POO.
Não penalize o aluno por não usar herança, polimorfismo ou interface, pois esses conceitos não foram pedidos no enunciado.
"""
    }

    return params


def format_correction_params(params, automatic_checks=None):
    criterios_obrigatorios = "\n".join(
        f"- {criterio}" for criterio in params["criterios_obrigatorios"]
    )

    criterios_opcionais = "\n".join(
        f"- {criterio}" for criterio in params["criterios_opcionais"]
    )

    penalidades = "\n".join(
        f"- {penalidade}" for penalidade in params["penalidades"]
    )

    automatic_checks_text = ""

    if automatic_checks:
        automatic_checks_text = f"""
Análise automática inicial feita pelo sistema:
{automatic_checks}
"""

    formatted_params = f"""
Nota máxima: {params["nota_maxima"]}
Nível de correção: {params["nivel_correcao"]}
Tema: {params["tema"]}

Enunciado:
{params["enunciado"]}

Critérios obrigatórios:
{criterios_obrigatorios}

Critérios opcionais:
{criterios_opcionais}

Penalidades:
{penalidades}

Observações do professor:
{params["observacoes"]}

{automatic_checks_text}
"""

    return formatted_params