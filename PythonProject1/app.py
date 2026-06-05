from agent.corrector import JavaPOOCorrector
from agent.java_analyzer import read_java_file, basic_java_checks
from agent.correction_params import get_default_correction_params, format_correction_params


def main():
    file_path = "uploads/projetoDoAluno.java"

    try:
        java_code = read_java_file(file_path)

        automatic_checks = basic_java_checks(java_code)

        params = get_default_correction_params()

        correction_params = format_correction_params(
            params=params,
            automatic_checks=automatic_checks
        )

        corrector = JavaPOOCorrector()

        print("Arquivo Java lido com sucesso.")
        print("Parâmetros de correção carregados com sucesso.")
        print("Análise automática inicial:")
        print(automatic_checks)
        print("\nCorrigindo prova...\n")

        result = corrector.correct(
            java_code=java_code,
            correction_params=correction_params
        )

        print(result)

    except Exception as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()