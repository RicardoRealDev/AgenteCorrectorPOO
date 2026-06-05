import json
import os
from datetime import datetime

CAMINHO_HISTORICO = "historico_correcoes.json"


def carregar_historico():
    if not os.path.exists(CAMINHO_HISTORICO):
        return []

    with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_no_historico(nome_arquivo, nota, erros, arquivo_original, arquivo_corrigido, resumo):
    historico = carregar_historico()

    nova_correcao = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "nome_arquivo": nome_arquivo,
        "nota": nota,
        "quantidade_erros": len(erros),
        "erros": erros,
        "arquivo_original": arquivo_original,
        "arquivo_corrigido": arquivo_corrigido,
        "resumo": resumo
    }

    historico.append(nova_correcao)

    with open(CAMINHO_HISTORICO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, indent=4, ensure_ascii=False)