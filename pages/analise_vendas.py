import streamlit as st
import pandas as pd
import plotly.express as px

def carregar_dados():
    # Carregar os dados de vendas
    df = pd.read_csv('dados/vendas.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# utiliza a função para carregar os dados
# e armazena em uma variável para uso posterior
# Dataframe do pandas que contém os dados de vendas
dados_vendas = carregar_dados()

st.title(':moneybag: Análise Detalhada de Vendas')

# Filtros para análise
st.sidebar.header("Filtros de Vendas")