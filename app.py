# app.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Painel de Reclamações - ANS", layout="wide")

st.title("📊 Painel de Reclamações com Regras da ANS")

uploaded_file = st.file_uploader("Envie o arquivo CSV com os dados validados", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Filtros")
    col1, col2, col3 = st.columns(3)
    with col1:
        status = st.multiselect("Status da Reclamação", options=df['Status da Reclamação'].unique())
    with col2:
        prazo = st.multiselect("Validação de Prazo", options=df['Validação de Prazo'].unique())
    with col3:
        erro = st.selectbox("Erro de Cobertura", ['Todos', 'Sim', 'Não'])

    if status:
        df = df[df['Status da Reclamação'].isin(status)]
    if prazo:
        df = df[df['Validação de Prazo'].isin(prazo)]
    if erro != 'Todos':
        df = df[df['Erro de Cobertura'] == erro]

    st.subheader("📢 Alertas")
    st.metric("❗ Fora do Prazo", len(df[df['Validação de Prazo'] == 'Fora do prazo']))
    st.metric("🚫 Erros de Cobertura", len(df[df['Erro de Cobertura'] == 'Sim']))

    st.subheader("📋 Tabela")
    st.dataframe(df, use_container_width=True)
