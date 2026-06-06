# AgenteCorrectorPOO
# Agente Corretor de Provas de POO em Java

Projeto em Python que usa Ollama e Streamlit para corrigir provas de Programação Orientada a Objetos em Java.

O sistema permite que o professor envie um arquivo `.java`, preencha os parâmetros de correção e receba uma avaliação estruturada com nota, justificativa, penalidades, sugestões e uma cópia comentada do código do aluno.

## Objetivo do projeto

O objetivo é criar um agente de IA dedicado à correção de atividades de POO em Java.

O professor informa os critérios da prova, como enunciado, nota máxima, nível de correção, critérios obrigatórios, critérios opcionais e penalidades. A partir disso, o agente analisa o código enviado pelo aluno e gera uma devolutiva organizada.

## Funcionalidades

- Upload de arquivo `.java` pela interface.
- Preenchimento dos parâmetros de correção pelo professor.
- Correção automática usando modelo local via Ollama.
- Avaliação estruturada em JSON.
- Exibição da nota final na interface.
- Listagem de pontos positivos e problemas encontrados.
- Aplicação de penalidades conforme os critérios definidos.
- Geração de relatório em Markdown.
- Download do relatório da correção.
- Geração de uma cópia comentada do código Java.
- Download do arquivo Java comentado.
- Análise automática inicial do código, verificando elementos básicos de POO.

## Tecnologias utilizadas

- Python
- Streamlit
- Ollama
- Modelo `qwen2.5-coder`
- python-dotenv

## Estrutura do projeto

```text
PythonProject1/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── agent/
│   ├── __init__.py
│   ├── llm.py
│   ├── prompts.py
│   ├── corrector.py
│   ├── java_analyzer.py
│   ├── report_generator.py
│   ├── annotated_file_generator.py
│   ├── correction_params.py
│   └── historico.py
│
├── interface/
│   ├── __init__.py
│   └── web.py
│
├── uploads/
│   └── .gitkeep
│
└── outputs/
    └── .gitkeep
```

## Função dos principais arquivos

### `interface/web.py`

Arquivo principal da interface com Streamlit.

Nele o professor consegue:

- enviar o arquivo Java do aluno;
- informar o nome do aluno ou identificação da prova;
- definir nota máxima;
- escolher o nível de correção;
- preencher enunciado, critérios e penalidades;
- visualizar a correção;
- baixar o relatório;
- baixar o código Java comentado.

### `agent/llm.py`

Responsável pela conexão com o Ollama.

Esse arquivo envia mensagens para o modelo local configurado no `.env`.

### `agent/prompts.py`

Contém os prompts principais do agente:

- prompt para correção da prova;
- prompt para gerar a cópia comentada do código Java.

### `agent/corrector.py`

Contém a classe principal `JavaPOOCorrector`.

Ela é responsável por:

- enviar o código e os critérios para o modelo;
- receber a correção;
- tentar converter a resposta em JSON;
- gerar uma versão comentada do código Java.

### `agent/java_analyzer.py`

Faz verificações iniciais no código Java.

Exemplos:

- verifica se existe classe;
- verifica se existe `main`;
- verifica se existem atributos privados;
- verifica se existem atributos públicos;
- verifica se há indícios de getters e setters;
- verifica uso de `extends` e `implements`.

### `agent/report_generator.py`

Gera o relatório final em Markdown.

O relatório inclui:

- dados da correção;
- parâmetros usados;
- análise automática inicial;
- resultado da correção;
- nota final;
- penalidades;
- sugestões de melhoria.

### `agent/annotated_file_generator.py`

Salva a cópia comentada do arquivo Java na pasta `outputs`.

### `app.py`

Arquivo de teste via terminal.

Pode ser usado para testar a correção sem abrir a interface web.

## Pré-requisitos

Antes de executar o projeto, instale:

- Python 3.10 ou superior.
- PyCharm ou outro editor Python.
- Ollama.
- Modelo `qwen2.5-coder` no Ollama.

## Instalação do Ollama

Baixe e instale o Ollama no Windows pelo site oficial:

```text
https://ollama.com/download
```

Depois de instalar, abra o terminal e teste:

```bash
ollama --version
```

Baixe o modelo usado no projeto:

```bash
ollama pull qwen2.5-coder
```

Teste o modelo:

```bash
ollama run qwen2.5-coder
```

Para sair do chat do Ollama, digite:

```text
/bye
```

## Configuração do ambiente Python

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.\.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter:

```text
ollama
streamlit
python-dotenv
```

## Configuração do `.env`

Crie um arquivo chamado `.env` na raiz do projeto.

Dentro dele, coloque:

```env
OLLAMA_MODEL=qwen2.5-coder
```

Esse valor define qual modelo local será usado pelo agente.

## Como executar a interface

Na raiz do projeto, rode:

```bash
python -m streamlit run interface/web.py
```

O Streamlit abrirá uma página no navegador.

Se não abrir automaticamente, copie o endereço exibido no terminal. Normalmente será:

```text
http://localhost:8501
```

## Como usar o sistema

Na interface, o professor deve preencher:

1. Nome do aluno ou identificação da prova.
2. Arquivo `.java` do aluno.
3. Nota máxima.
4. Nível de correção.
5. Tema da prova.
6. Enunciado da questão.
7. Critérios obrigatórios.
8. Critérios opcionais.
9. Penalidades.
10. Observações extras.

Depois, deve clicar em:

```text
Corrigir prova
```

O sistema irá:

1. Ler o código Java.
2. Fazer uma análise automática inicial.
3. Enviar o código e os parâmetros para o Ollama.
4. Gerar a correção estruturada.
5. Gerar uma cópia comentada do código.
6. Salvar os arquivos na pasta `outputs`.
7. Exibir os resultados na interface.

## Exemplo de arquivo Java para teste

Crie um arquivo chamado `projetoDoAluno.java` com este conteúdo:

```java
public class Aluno {
    public String nome;
    public int idade;

    public void mostrarDados() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
    }
}
```

Esse exemplo possui problemas intencionais de POO:

- atributos públicos;
- ausência de construtor;
- ausência de getters;
- ausência de setters.

## Exemplo de preenchimento dos parâmetros

### Enunciado

```text
Crie uma classe Aluno com atributos nome e idade. A classe deve usar encapsulamento, construtor, getters, setters e um método para exibir os dados do aluno.
```

### Critérios obrigatórios

```text
- Criar corretamente a classe Aluno.
- Declarar os atributos nome e idade.
- Usar atributos privados.
- Criar construtor.
- Criar getters e setters.
- Criar método para exibir os dados do aluno.
```

### Critérios opcionais

```text
- Código organizado.
- Bons nomes de variáveis.
- Uso adequado da palavra-chave this.
```

### Penalidades

```text
- Atributos públicos: até -2 pontos.
- Ausência de construtor: até -2 pontos.
- Ausência de getters: até -1 ponto.
- Ausência de setters: até -1 ponto.
- Código que não compila: até -3 pontos.
- Solução incompleta: até -3 pontos.
```

### Observações extras

```text
Não penalizar ausência de herança, polimorfismo ou interface, pois esses conceitos não foram pedidos no enunciado.
```

## Saídas geradas

Os arquivos gerados ficam na pasta:

```text
outputs/
```

O sistema pode gerar:

```text
relatorio_NomeDoAluno_DATA.md
projeto_comentado_NomeDoAluno_DATA.java
```

## Observações importantes

Este projeto usa um modelo local. A qualidade da correção depende do modelo instalado no Ollama.

Para correção de código, o modelo recomendado é:

```text
qwen2.5-coder
```

A análise automática do Java ainda é simples. Ela ajuda o agente, mas não substitui uma análise completa com compilação real.

## Melhorias futuras recomendadas

- Criar rubrica com pontuação por critério.
- Fazer o Python calcular a nota final, em vez de deixar só o modelo decidir.
- Permitir upload de vários arquivos `.java`.
- Permitir upload de projeto `.zip`.
- Compilar o código automaticamente com `javac`.
- Rodar testes automatizados.
- Criar modelos salvos de prova.
- Gerar relatório em PDF.
- Criar histórico de correções.
- Melhorar a inserção de comentários por linha no arquivo Java.

## Problemas comuns

### Erro: `No module named 'agent'`

Rode o Streamlit sempre pela raiz do projeto:

```bash
python -m streamlit run interface/web.py
```

Confirme também se o começo do `interface/web.py` contém:

```python
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
```

### Erro: `No module named 'ollama'`

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou instale diretamente:

```bash
pip install ollama
```

### Erro: modelo não encontrado

Baixe o modelo:

```bash
ollama pull qwen2.5-coder
```

### Erro: conexão com Ollama recusada

Abra o Ollama no Windows e teste:

```bash
ollama list
```

Depois execute novamente:

```bash
python -m streamlit run interface/web.py
```

## Status do projeto

Projeto em desenvolvimento.

A versão atual funciona como MVP de um agente corretor de provas de POO em Java com interface web local, parâmetros definidos pelo professor, relatório e arquivo comentado.