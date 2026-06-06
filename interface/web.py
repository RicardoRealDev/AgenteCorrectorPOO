import sys

from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent.parent))

from agent.corrector import JavaPOOCorrector
from agent.java_analyzer import basic_java_checks
from agent.report_generator import generate_report_content, save_report
from agent.annotated_file_generator import save_annotated_java_file

def format_teacher_params(
    nota_maxima,
    nivel_correcao,
    tema,
    enunciado,
    criterios_obrigatorios,
    criterios_opcionais,
    penalidades,
    observacoes,
    automatic_checks
):
    return f"""
Nota máxima: {nota_maxima}
Nível de correção: {nivel_correcao}
Tema: {tema}

Enunciado:
{enunciado}

Critérios obrigatórios:
{criterios_obrigatorios}

Critérios opcionais:
{criterios_opcionais}

Penalidades:
{penalidades}

Observações do professor:
{observacoes}

Análise automática inicial feita pelo sistema:
{automatic_checks}
"""


def main():
    st.set_page_config(
        page_title="Agente Corretor de POO",
        layout="centered"
    )

    st.title("Agente Corretor de Provas de POO em Java")

    st.write("Preencha os parâmetros da correção e envie o arquivo Java do aluno.")

    student_name = st.text_input(
        "Nome do aluno ou identificação da prova",
        placeholder="Exemplo: João Silva, Prova 1, Turma A"
    )

    uploaded_file = st.file_uploader(
        "Envie o arquivo projetoDoAluno.java",
        type=["java"]
    )

    st.subheader("Parâmetros da correção")

    nota_maxima = st.number_input(
        "Nota máxima",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.5
    )

    nivel_correcao = st.selectbox(
        "Nível de correção",
        ["Flexível", "Médio", "Rigoroso"]
    )

    tema = st.text_input(
        "Tema da prova",
        value="Programação Orientada a Objetos em Java"
    )

    enunciado = st.text_area(
        "Enunciado da questão",
        height=130,
        placeholder="Exemplo: Crie uma classe Aluno com atributos nome e idade..."
    )

    criterios_obrigatorios = st.text_area(
        "Critérios obrigatórios",
        height=160,
        placeholder="""Exemplo:
- Criar corretamente a classe Aluno.
- Usar atributos privados.
- Criar construtor.
- Criar getters e setters.
- Criar método para exibir os dados."""
    )

    criterios_opcionais = st.text_area(
        "Critérios opcionais",
        height=120,
        placeholder="""Exemplo:
- Código organizado.
- Bons nomes de variáveis.
- Uso adequado da palavra-chave this."""
    )

    penalidades = st.text_area(
        "Penalidades",
        height=140,
        placeholder="""Exemplo:
- Atributos públicos: até -2 pontos.
- Ausência de construtor: até -2 pontos.
- Código que não compila: até -3 pontos."""
    )

    observacoes = st.text_area(
        "Observações extras",
        height=100,
        placeholder="Exemplo: Não penalizar ausência de herança, pois não foi pedida no enunciado."
    )

    if st.button("Corrigir prova"):
        if uploaded_file is None:
            st.error("Envie um arquivo .java antes de corrigir.")
            return

        if not student_name.strip():
            st.error("Preencha o nome do aluno ou uma identificação da prova.")
            return

        if not enunciado.strip():
            st.error("Preencha o enunciado da questão.")
            return

        if not criterios_obrigatorios.strip():
            st.error("Preencha os critérios obrigatórios.")
            return

        if not penalidades.strip():
            st.error("Preencha as penalidades.")
            return

        try:
            java_code = uploaded_file.read().decode("utf-8")

            if not java_code.strip():
                st.error("O arquivo Java está vazio.")
                return

            automatic_checks = basic_java_checks(java_code)

            correction_params = format_teacher_params(
                nota_maxima=nota_maxima,
                nivel_correcao=nivel_correcao,
                tema=tema,
                enunciado=enunciado,
                criterios_obrigatorios=criterios_obrigatorios,
                criterios_opcionais=criterios_opcionais,
                penalidades=penalidades,
                observacoes=observacoes,
                automatic_checks=automatic_checks
            )

            corrector = JavaPOOCorrector()

            with st.spinner("Corrigindo a prova..."):
                correction_result = corrector.correct(
                    java_code=java_code,
                    correction_params=correction_params
                )

            with st.spinner("Gerando cópia comentada do código..."):
                annotated_code = corrector.annotate_code(
                    java_code=java_code,
                    correction_params=correction_params
                )

            report_content = generate_report_content(
                student_name=student_name,
                file_name=uploaded_file.name,
                correction_params=correction_params,
                automatic_checks=automatic_checks,
                correction_result=correction_result
            )

            report_path = save_report(
                report_content=report_content,
                student_name=student_name
            )
            annotated_file_path = save_annotated_java_file(
                annotated_code=annotated_code,
                student_name=student_name
            )

            st.success("Correção concluída.")

            st.subheader("Análise automática inicial")
            st.json(automatic_checks)

            st.subheader("Resultado da correção")

            if isinstance(correction_result, dict) and "erro" not in correction_result:
                st.write("Resumo geral:")
                st.write(correction_result.get("resumo_geral", ""))

                st.write("Nota final:")
                st.metric(
                    label="Nota",
                    value=f'{correction_result.get("nota_final", 0)} / {correction_result.get("nota_maxima", nota_maxima)}'
                )

                st.write("Pontos positivos:")
                for item in correction_result.get("pontos_positivos", []):
                    st.write(f"- {item}")

                st.write("Problemas encontrados:")
                for item in correction_result.get("problemas_encontrados", []):
                    st.write(f"- {item}")

                st.write("Avaliação por critério:")
                st.json(correction_result.get("avaliacao_por_criterio", []))

                st.write("Penalidades aplicadas:")
                st.json(correction_result.get("penalidades_aplicadas", []))

                st.write("Justificativa da nota:")
                st.write(correction_result.get("justificativa_da_nota", ""))

                st.write("Sugestões de melhoria:")
                for item in correction_result.get("sugestoes_de_melhoria", []):
                    st.write(f"- {item}")

            else:
                st.warning("A correção foi gerada, mas não veio no formato estruturado esperado.")
                st.write(correction_result)

            st.subheader("Relatório gerado")
            st.write(f"Relatório salvo em: `{report_path}`")

            st.download_button(
                label="Baixar relatório em Markdown",
                data=report_content,
                file_name=report_path.name,
                mime="text/markdown"
            )
            st.subheader("Arquivo Java comentado")

            st.code(annotated_code, language="java")

            st.write(f"Arquivo comentado salvo em: `{annotated_file_path}`")

            st.download_button(
                label="Baixar arquivo Java comentado",
                data=annotated_code,
                file_name=annotated_file_path.name,
                mime="text/x-java-source"
            )


        except UnicodeDecodeError:
            st.error("Não foi possível ler o arquivo. Verifique se ele está salvo em UTF-8.")

        except Exception as error:
            st.error(f"Erro ao corrigir a prova: {error}")


if __name__ == "__main__":
    main()