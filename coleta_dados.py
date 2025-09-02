import requests
import xml.etree.ElementTree as ET
import pandas as pd
from urllib.parse import quote
import os

# Etapa 1: Coleta de Dados

def buscar_noticias_google_news(termos_de_busca: list, max_resultados=15):
    """
    Busca notícias no Google News usando RSS para uma lista de termos de busca.
    Este script é robusto contra campos ausentes no feed RSS.

    Args:
        termos_de_busca (list): Uma lista de strings para buscar.
        max_resultados (int): O número máximo de notícias para retornar.

    Returns:
        pandas.DataFrame: Um DataFrame com as notícias encontradas ou None se ocorrer um erro.
    """
    query_formatada = " OR ".join([f'"{termo}"' for termo in termos_de_busca])
    query_encodada = quote(query_formatada)
    url_rss = f"https://news.google.com/rss/search?q={query_encodada}&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    print(f"Buscando notícias com os termos: {query_formatada}...")

    try:
        resposta = requests.get(url_rss, timeout=10)
        resposta.raise_for_status()
        root = ET.fromstring(resposta.content)
        lista_noticias = []

        for item in root.findall('.//channel/item')[:max_resultados]:
            # Aplicando sua sugestão de verificação para TODOS os campos
            # Isso torna o script resiliente a dados incompletos no feed RSS
            
            titulo_find = item.find('title')
            titulo = titulo_find.text if titulo_find is not None else "Título não encontrado"

            link_find = item.find('link')
            link = link_find.text if link_find is not None else "Link não encontrado"

            data_find = item.find('pubDate')
            data_publicacao = data_find.text if data_find is not None else "Data não encontrada"
            
            desc_find = item.find('description')
            descricao = desc_find.text if desc_find is not None else "Descrição não encontrada"
            
            fonte_find = item.find('source')
            fonte = fonte_find.text if fonte_find is not None else "Fonte desconhecida"

            noticia = {
                'titulo': titulo,
                'link': link,
                'data_publicacao': data_publicacao,
                'fonte': fonte,
                'descricao': descricao,
            }
            lista_noticias.append(noticia)
        
        if not lista_noticias:
            print("Nenhuma notícia encontrada para os termos de busca.")
            return pd.DataFrame()

        df_noticias = pd.DataFrame(lista_noticias)
        print(f"Coleta concluída! {len(df_noticias)} notícias encontradas.")
        return df_noticias

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição HTTP: {e}")
        return None
    except ET.ParseError as e:
        print(f"Erro ao processar o XML: {e}")
        return None

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    termos = ["Inteligência Artificial Piauí", "SIA Piauí"]
    df_resultado = buscar_noticias_google_news(termos)

    if df_resultado is not None and not df_resultado.empty:
        print("\n--- Amostra das Notícias Coletadas ---")
        print(df_resultado[['titulo', 'fonte', 'data_publicacao']].head())

        nome_da_pasta = 'data'
        nome_do_arquivo = 'noticias_coletadas.csv'
        os.makedirs(nome_da_pasta, exist_ok=True)
        caminho_do_arquivo = os.path.join(nome_da_pasta, nome_do_arquivo)
        
        df_resultado.to_csv(caminho_do_arquivo, index=False, encoding='utf-8')
        print(f"\nDados salvos com sucesso em '{caminho_do_arquivo}'")