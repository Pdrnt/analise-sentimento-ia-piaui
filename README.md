# analise-sentimento-ia-piaui
Dashboard para monitorar menções sobre Inteligência Artificial no Piauí, projeto de case para processo seletivo.
# Painel de Monitoramento de Notícias sobre Inteligência Artificial no Piauí

## Descrição do Projeto
Este projeto tem como objetivo criar um **painel simplificado** para monitorar menções sobre **"Inteligência Artificial no Piauí"** em fontes de notícias públicas, com foco em análise de sentimento e identificação de temas recorrentes.  

O projeto segue boas práticas de **Python, Git e Streamlit**, garantindo **organização, reprodutibilidade e transparência**.

---

## Etapas do Projeto

### Etapa 1 – Coleta de Dados ✅
- Coleta de notícias utilizando o **feed RSS do Google Notícias**.  
- Termos de busca: `"Inteligência Artificial Piauí"` e `"SIA Piauí"`.  
- Campos extraídos: título, link, descrição, data de publicação e fonte.  
- Dados salvos em **`data/noticias_coletadas.csv`**.

### Etapa 2 – Processamento de Dados e Análise de Sentimento ✅
- Limpeza de textos: remoção de tags HTML, caracteres especiais e padronização de minúsculas.  
- Combinação de título + descrição para análise mais completa.  
- Classificação de sentimento usando **abordagem baseada em regras**.  
- Resultados salvos em **`data/noticias_processadas.csv`**.  
- Resumo da análise exibido no terminal.

### Etapa 3 – Dashboard Streamlit ✅
- Arquivo: `app.py`.
- Métricas principais (KPIs): total de notícias, contagem e percentual por sentimento.  
- Gráfico de pizza/roça mostrando a distribuição de sentimentos.  
- Nuvem de palavras com termos mais frequentes.  
- Tabela interativa com título, fonte, data, sentimento e link.  
- Rodar com: `streamlit run app.py`.  
- Dashboard atualizado em tempo real com data e hora da execução.

### Etapa 4 – Versionamento 🔜
- Repositório organizado no GitHub com commits claros e frequentes.  
- Arquivos: `README.md`, `requirements.txt`, `main.py`, `DECISIONS.md`.

### Etapa 5 – Ética e Transparência 🔜
- Aviso sobre limitações da análise de sentimento (ex.: sarcasmo, contexto complexo).  
- Explicação de quais códigos/etapas foram desenvolvidos com apoio de IA.

### Etapa 6 – Documentação de Decisões 🔜
- Arquivo `DECISIONS.md` explicando escolhas de abordagem e tratamento de erros.

---

## Como Executar

1. **Clonar o repositório**
```bash
git clone https://github.com/seuusuario/case2-painel-ia-piaui.git
cd case2-painel-ia-piaui

2 - Criar e ativar ambiente virtual

python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

3 - Instalar dependências

pip install -r requirements.txt

4 - Executar Scripts

# Etapa 1 – Coleta
python main.py

# Etapa 2 – Processamento e análise de sentimento
python processamento.py

# Etapa 3 – Dashboard
streamlit run app.py


Contato

Pedro Lima – Estudante/Desenvolvedor

Teresina, Piauí – Brasil