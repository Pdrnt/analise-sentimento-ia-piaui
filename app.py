import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Análise de Sentimento",
    page_icon="📊", # ALTERADO: Ícone mais genérico de dashboard
    layout="wide"
)

# --- Funções Auxiliares ---
@st.cache_data
def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:
    """Carrega os dados processados de um arquivo CSV."""
    try:
        df = pd.read_csv(caminho_arquivo)
        # Converte a coluna de data para o formato datetime, essencial para filtros
        df['data_publicacao'] = pd.to_datetime(df['data_publicacao'], errors='coerce')
        return df
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado em '{caminho_arquivo}'. Por favor, execute os scripts `coleta_dados.py` e `processamento_sentimento.py` primeiro.")
        return pd.DataFrame()

# --- Início do Dashboard ---
def main():
    # ALTERADO: Título com ícone
    st.title("📊 Análise de Sentimento sobre IA no Piauí")
    st.markdown(f"Dashboard para monitoramento de notícias sobre Inteligência Artificial no Piauí. (Dados atualizados em: {pd.Timestamp.now('America/Sao_Paulo').strftime('%d/%m/%Y às %H:%M')})")

    caminho_dados = os.path.join('data', 'noticias_processadas.csv')
    df = carregar_dados(caminho_dados)

    if df.empty:
        st.warning("Nenhum dado para exibir. Execute os scripts de coleta e processamento.")
        return

    # --- Métricas Principais (KPIs) ---
    total_noticias = len(df)
    positivas = df['sentimento'].value_counts().get('Positivo', 0)
    negativas = df['sentimento'].value_counts().get('Negativo', 0)
    neutras = df['sentimento'].value_counts().get('Neutro', 0)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Notícias", total_noticias)
    col2.metric("Sentimento Positivo", f"{positivas} ({positivas/total_noticias:.1%})")
    col3.metric("Sentimento Negativo", f"{negativas} ({negativas/total_noticias:.1%})")
    col4.metric("Sentimento Neutro", f"{neutras} ({neutras/total_noticias:.1%})")
    
    st.markdown("---")

    # --- Visualizações Principais ---
    col_grafico, col_nuvem = st.columns(2)

    with col_grafico:
        # ALTERADO: Subheader com ícone
        st.subheader("📊 Distribuição de Sentimentos")
        df_sentimento = df['sentimento'].value_counts().reset_index()
        df_sentimento.columns = ['sentimento', 'contagem']
        
        fig_pizza = px.pie(df_sentimento, names='sentimento', values='contagem', 
                           color='sentimento',
                           color_discrete_map={'Positivo':'#2ca02c', 'Negativo':'#d62728', 'Neutro':'#1f77b4'},
                           hole=.3)
        fig_pizza.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pizza, use_container_width=True)

    with col_nuvem:
        # ALTERADO: Subheader com ícone
        st.subheader("☁️ Termos Mais Frequentes")
        texto_completo = " ".join(df['texto_limpo'].dropna())
        
        if texto_completo:
            wordcloud = WordCloud(width=800, height=400, background_color='white',
                                  stopwords=None, collocations=True).generate(texto_completo)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.write("Não há texto suficiente para gerar a nuvem de palavras.")

    # NOVO: Gráfico de barras com as fontes das notícias
    st.markdown("---")
    st.subheader("📰 Notícias por Fonte")
    df_fontes = df['fonte'].value_counts().nlargest(10).reset_index() # Pega as 10 maiores fontes
    df_fontes.columns = ['fonte', 'contagem']
    
    fig_barras = px.bar(df_fontes, x='contagem', y='fonte', orientation='h', 
                        title="Top 10 Fontes de Notícias",
                        text='contagem')
    fig_barras.update_layout(yaxis={'categoryorder':'total ascending'}) # Ordena do menor para o maior
    st.plotly_chart(fig_barras, use_container_width=True)


    # ALTERADO: Tabela de dados dentro de um expander
    with st.expander("Clique para ver os detalhes das notícias coletadas"):
        df_exibicao = df[['titulo', 'fonte', 'data_publicacao', 'sentimento', 'link']]
        st.dataframe(df_exibicao, use_container_width=True, height=300)

    # --- Rodapé (Etapa 5) ---
    st.markdown("---")
    st.caption("Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.")

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    main()