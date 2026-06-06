from pathlib import Path
from datetime import datetime
import json


def format_correction_result(correction_result):
    if isinstance(correction_result, dict):
        if "erro" in correction_result:
            return f"""
Erro ao estruturar resposta:

{correction_result.get("erro")}

Resposta original:

{correction_result.get("resposta_original")}
"""

        pontos_positivos = "\n".join(
            f"- {item}" for item in correction_result.get("pontos_positivos", [])
        )

        problemas = "\n".join(
            f"- {item}" for item in correction_result.get("problemas_encontrados", [])
        )

        sugestoes = "\n".join(
            f"- {item}" for item in correction_result.get("sugestoes_de_melhoria", [])
        )

        avaliacao = json.dumps(
            correction_result.get("avaliacao_por_criterio", []),
            ensure_ascii=False,
            indent=2
        )

        penalidades = json.dumps(
            correction_result.get("penalidades_aplicadas", []),
            ensure_ascii=False,
            indent=2
        )

        return f"""
## Resumo geral

{correction_result.get("resumo_geral", "")}

## Nota final

Nota final: {correction_result.get("nota_final", 0)} / {correction_result.get("nota_maxima", 0)}

## Pontos positivos

{pontos_positivos}

## Problemas encontrados

{problemas}

## Avaliação por critério

```json
{avaliacao}
## Penalidades Aplicadas
    {penalidades}
##Justificativa da Nota
{correction_result.get("justificativa_da_nota", "")}
##Sugestões de melhoria
{sugestoes}
"""
    return str(correction_result)
def generate_report_content(
student_name,
file_name,
correction_params,
automatic_checks,
correction_result
):
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    formatted_result = format_correction_result(correction_result)

    report = f"""
##Relatório de Correção de Prova de POO em Java
    ##Dados da correção
    Aluno ou identificação: {student_name}
    Arquivo corrigido: {file_name}
    Data e hora da correção: {current_time}
##Parâmetros usados na correção
{correction_params}
##Análise automática inicial
    {automatic_checks}
##Resultado da correção
    {formatted_result}"""
    return report
def save_report(report_content, student_name="aluno"):
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    safe_name = student_name.strip().replace(" ", "_")

    if not safe_name:
        safe_name = "aluno"

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"relatorio_{safe_name}_{current_time}.md"

    file_path = output_dir / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report_content)

    return file_path