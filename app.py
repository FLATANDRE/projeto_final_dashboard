import streamlit as st

# configuracao inicial da pagina
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon=":bar_chart:",
    layout="wide"
)

# Definindo as páginas
visao_geral = st.Page('./pages/visao_geral.py',
                      title='Visão Geral',
                      icon='🏠',
                      default=True
                    )

analise_vendas = st.Page('./pages/analise_vendas.py',
                         title='Análise de Vendas',
                        icon='💰')

mapa_vendas = st.Page('./pages/mapa_vendas.py',
                      title='Mapa de Vendas',
                      icon='🗺️')


#analise_produtos = st.Page('./pages/analise_produtos.py',
#                            title='Produtos',
#                            icon=':package:')

#sobre = st.Page('./pages/sobre.py',
#                 title='Sobre',
#                 icon=':information_source:')

# Configurando a navegação entre as páginas
pg = st.navigation(
    [
       visao_geral,
       analise_vendas, 
       mapa_vendas,      
    ]     
)

pg.run()