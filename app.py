import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
import os

st.set_page_config(page_title="Analisador de Logs com IA (Gemini)", layout="wide")

load_dotenv()

# Pega a chave da variável de ambiente ou do Streamlit Secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", None)

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.warning("Informe sua chave de API Gemini nas Secrets do Streamlit ou no .env")

st.title("🔍 Analisador Inteligente de Logs com IA (Google Gemini)")

log_file = st.file_uploader("Envie um arquivo de log (.log ou .txt) para ser analiado por nosso analista de segurança cibernética virtual.", type=["log", "txt"])

def analisar_linha_com_gemini(linha):
    prompt = f"""
Você é um analista de segurança cibernética.
Analise tecnicamente esta linha de log e diga:
1. O que aconteceu.
2. É suspeito ou legítimo?
3. Qual o nível de risco? (baixo, médio, alto)
4. Se for malicioso, sugira uma mitigação.

Linha do log:
{linha}
"""
    try:
        resposta = model.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"[Erro na API Gemini]: {e}"

if log_file and GEMINI_API_KEY:
    log_lines = log_file.read().decode("utf-8").splitlines()
    st.success(f"{len(log_lines)} linhas carregadas.")
    linhas_exibidas = st.slider("Quantidade de linhas a analisar", 1, min(50, len(log_lines)), 10)

    if st.button("🚀 Analisar com IA"):
        resultados = []
        with st.spinner("Analisando..."):
            for linha in log_lines[:linhas_exibidas]:
                if linha.strip():
                    analise = analisar_linha_com_gemini(linha)
                    resultados.append({"Log": linha, "Análise da IA": analise})

        df = pd.DataFrame(resultados)
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Baixar resultado CSV", csv, "analise_logs.csv", "text/csv")

elif not GEMINI_API_KEY:
    st.warning("Informe sua chave de API Gemini para continuar.")
