import pandas as pd
import re
import os
import html

# Etapa 2: Processamento e Análise de Sentimento

# Listas de palavras-chave para uma análise de sentimento baseada em regras.
# Estas listas podem ser melhoradas para análises mais complexas.
PALAVRAS_POSITIVAS = [
  'crescimento', 'avanço', 'oportunidade', 'inova', 'melhora', 'positivo', 
    'sucesso', 'desenvolvimento', 'investimento', 'beneficia', 'impulsiona',
    'qualidade', 'aumento', 'expansão', 'fortalece', 'otimista', 'solução',
    'parceria', 'capacitação', 'moderniza', 'amplia', 'incentivo'
]

PALAVRAS_NEGATIVAS = [
    'risco', 'desafio', 'problema', 'crise', 'negativo', 'dificuldade', 
    'ameaça', 'preocupação', 'impacto negativo', 'barreira', 'lento', 
    'queda', 'redução', 'insegurança', 'pessimista', 'fraude', 'golpe', 'alerta'
]

def limpar_texto(texto: str) -> str:
    """
    Limpa o texto removendo tags HTML, caracteres especiais e convertendo para minúsculas.
    """
    if not isinstance(texto, str):
        return ""
    
    # Decodifica entidades HTML (ex: &amp; -> &)
    texto = html.unescape(texto)
    # Remove tags HTML
    texto = re.sub(r'<.*?>', '', texto)
    # Converte para minúsculas para a análise de palavras-chave
    texto = texto.lower()
    # Remove caracteres que não são letras ou espaços (mantendo acentos)
    texto = re.sub(r'[^a-záéíóúâêôãõç\s]', '', texto)
    # Remove espaços extras que podem ter sido criados
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def analisar_sentimento(texto: str) -> str:
    """
    Analisa o sentimento de um texto com base na contagem de palavras positivas e negativas.
    """
    score = 0
    # Adiciona um ponto para cada palavra positiva encontrada
    for palavra in PALAVRAS_POSITIVAS:
        if palavra in texto:
            score += 1
    # Subtrai um ponto para cada palavra negativa encontrada
    for palavra in PALAVRAS_NEGATIVAS:
        if palavra in texto:
            score -= 1
            
    # Classifica o sentimento com base no score final
    if score > 0:
        return 'Positivo'
    elif score < 0:
        return 'Negativo'
    else:
        return 'Neutro'

def processar_dados(caminho_entrada: str, caminho_saida: str):
    """
    Função principal que carrega os dados, os processa e salva o resultado.
    """
    print(f"Iniciando o processamento do arquivo: {caminho_entrada}")
    try:
        # Carrega os dados coletados na Etapa 1
        df = pd.read_csv(caminho_entrada)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{caminho_entrada}'.")
        print("Por favor, execute o script 'coleta_dados.py' primeiro.")
        return

    if df.empty:
        print("O arquivo de dados está vazio. Nenhum processamento a ser feito.")
        return

    # 1. Combina o título e a descrição para uma análise mais completa
    # O .fillna('') garante que, se um campo for nulo (vazio), não causará erro
    df['texto_completo'] = df['titulo'].fillna('') + ' ' + df['descricao'].fillna('')

    # 2. Limpa o texto combinado, criando uma nova coluna 'texto_limpo'
    print("Limpando os textos das notícias...")
    df['texto_limpo'] = df['texto_completo'].apply(limpar_texto)

    # 3. Aplica a análise de sentimento no texto limpo, criando a coluna 'sentimento'
    print("Analisando o sentimento de cada notícia...")
    df['sentimento'] = df['texto_limpo'].apply(analisar_sentimento)
    
    # 4. Salva o novo DataFrame com as colunas adicionais
    try:
        df.to_csv(caminho_saida, index=False, encoding='utf-8')
        print(f"Processamento concluído! Resultados salvos em: {caminho_saida}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo processado: {e}")

    # Exibe um resumo dos resultados no terminal
   # CÓDIGO MELHORADO PARA UMA SAÍDA MAIS LIMPA
    print("\n--- Resumo da Análise de Sentimento ---")
    resumo_sentimento = df['sentimento'].value_counts()
    print(resumo_sentimento.to_string())


# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    # Define os caminhos de entrada e saída
    caminho_dados_brutos = os.path.join('data', 'noticias_coletadas.csv')
    caminho_dados_processados = os.path.join('data', 'noticias_processadas.csv')
    
    # Chama a função principal de processamento
    processar_dados(caminho_dados_brutos, caminho_dados_processados)