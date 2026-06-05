from pathlib import Path
from datetime import datetime


def generate_report_content(
    student_name,
    file_name,
    correction_params,
    automatic_checks,
    correction_result
):
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    report = f"""
# Relatório de Correção de Prova de POO em Java

## Dados da correção

Aluno ou identificação: {student_name}

Arquivo corrigido: {file_name}

Data e hora da correção: {current_time}

---

## Parâmetros usados na correção

{correction_params}

---

## Análise automática inicial

{automatic_checks}

---

## Resultado da correção

{correction_result}
"""

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