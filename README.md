# Analisador Inteligente de Logs de Segurança com IA

![Streamlit](https://img.shields.io/badge/streamlit-application-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Google Gemini](https://img.shields.io/badge/Google-Gemini--1.5--flash-brightgreen)

## Descrição

Este projeto é um Software as a Service (SaaS) desenvolvido em Streamlit que permite a análise automática e inteligente de arquivos de logs de segurança usando inteligência artificial (IA). A aplicação utiliza a API Google Gemini (modelo `gemini-1.5-flash`) para interpretar linhas de logs, identificar eventos suspeitos, classificar o nível de risco e sugerir ações de mitigação.

## Funcionalidades

- Upload de arquivos de log (.log ou .txt)
- Análise linha a linha com IA (Google Gemini `gemini-1.5-flash`)
- Classificação do evento, risco e sugestões de mitigação
- Exibição dos resultados em tabela interativa
- Download dos resultados em CSV

## Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- Google Gemini API (`gemini-1.5-flash`)
- Pandas
- python-dotenv

## Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/sanmiir/log-analyzer-ia.git
   cd log-analyzer-ia
2. Crie e ative um ambiente virtual:
   ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
4. Configure sua chave da API Gemini no arquivo .env:
   ```bash
    GEMINI_API_KEY=sua_chave_aqui

5. Rode a aplicação:
   ```bash
    streamlit run app.py

6. Como usar:

  - Faça upload do arquivo de log pelo botão na página.

  - Defina quantas linhas deseja analisar.

  - Clique em "Analisar linhas com IA".

  - Veja os resultados e baixe em CSV, se desejar.

  - Código exemplo para chamada da API Gemini:
  ```python
from google.ai import generativelanguage as glm
      client = glm.GenerationServiceClient()

def analisar_linha_com_ia(linha):
    prompt = f"""
Você é um analista de segurança. Analise tecnicamente esta linha de log e diga:
- Qual evento ocorreu
- Se é uma atividade suspeita ou legítima
- Qual o nível de risco (baixo, médio, alto)
- Se for malicioso, dê sugestões de mitigação.

Linha do log:
{linha}
"""
    response = client.generate_text(
        model="gemini-1.5-flash",
        prompt=prompt,
        temperature=0.2,
        max_tokens=300,
    )
    return response.candidates[0].output
````
7. Hospedagem
A aplicação está hospedada no Streamlit Cloud e pode ser acessada em:
https://seu-link-do-streamlit-app.streamlit.app


    
