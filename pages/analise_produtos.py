import streamlit as st
import pandas as pd
import plotly.express as px

def carregar_dados():
    df = pd.read_csv('dados/vendas.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    return df

df = carregar_dados()

st.title("📦 Análise de Produtos")

# Seleção de produto
produto_selecionado = st.selectbox("Selecione um Produto:", sorted(df['Produto'].unique()))
df_produto = df[df['Produto'] == produto_selecionado]

# Métricas do produto
col1, col2, col3, col4 = st.columns(4)
col1.metric("Receita", f"R$ {df_produto['Vendas'].sum():,.0f}")
col2.metric("Lucro", f"R$ {df_produto['Lucro'].sum():,.0f}")
col3.metric("Qtd. Vendida", f"{df_produto['Quantidade'].sum():,}")
col4.metric("Preço Médio", f"R$ {df_produto['Vendas'].sum() / df_produto['Quantidade'].sum():,.2f}")

# Vendas por região do produto
col_a, col_b = st.columns(2)
with col_a:
    regiao_prod = df_produto.groupby('Região')['Vendas'].sum().reset_index()
    fig = px.bar(regiao_prod, x='Região', y='Vendas', title=f'{produto_selecionado}: Vendas por Região',
                 color='Vendas', color_continuous_scale='Greens')
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    vendedor_prod = df_produto.groupby('Vendedor')['Vendas'].sum().reset_index()
    fig = px.pie(vendedor_prod, values='Vendas', names='Vendedor',
                 title=f'{produto_selecionado}: Vendas por Vendedor')
    st.plotly_chart(fig, use_container_width=True)

# Evolução temporal do produto
df_produto['Mês'] = df_produto['Data'].dt.to_period('M').astype(str)
mensal_prod = df_produto.groupby('Mês')['Vendas'].sum().reset_index()
fig = px.area(mensal_prod, x='Mês', y='Vendas', 
              title=f'Evolução Mensal de {produto_selecionado}')
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)
