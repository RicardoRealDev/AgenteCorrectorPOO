from pathlib import Path
from datetime import datetime


def save_annotated_java_file(annotated_code, student_name="aluno"):
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    safe_name = student_name.strip().replace(" ", "_")

    if not safe_name:
        safe_name = "aluno"

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"projeto_comentado_{safe_name}_{current_time}.java"

    file_path = output_dir / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(annotated_code)

    return file_path