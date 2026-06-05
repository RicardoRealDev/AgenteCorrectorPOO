from pathlib import Path


def validate_java_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("Arquivo Java não encontrado.")

    if not path.is_file():
        raise ValueError("O caminho informado não é um arquivo.")

    if path.suffix.lower() != ".java":
        raise ValueError("O arquivo precisa ter a extensão .java.")

    if path.stat().st_size == 0:
        raise ValueError("O arquivo Java está vazio.")

    return True


def read_java_file(file_path):
    validate_java_file(file_path)

    path = Path(file_path)

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            raise ValueError("O arquivo Java não possui conteúdo válido.")

        return content

    except UnicodeDecodeError:
        raise ValueError("Não foi possível ler o arquivo. Verifique se ele está em UTF-8.")


def basic_java_checks(java_code):
    checks = {
        "tem_classe": "class " in java_code,
        "tem_main": "public static void main" in java_code,
        "tem_atributo_private": "private " in java_code,
        "tem_atributo_public": "public String" in java_code or "public int" in java_code or "public double" in java_code,
        "tem_getter": "get" in java_code,
        "tem_setter": "set" in java_code,
        "tem_construtor_possivel": False,
        "usa_heranca": "extends " in java_code,
        "usa_interface": "implements " in java_code,
    }

    return checks