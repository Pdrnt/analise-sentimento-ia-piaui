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

### Etapa 2 – Processamento de Dados 🔜
- Limpeza de texto (remoção de tags HTML e caracteres especiais).  
- Classificação de sentimento usando abordagem baseada em regras.  
- Preparação de dados para visualização no dashboard.

### Etapa 3 – Visualização 🔜
- Dashboard interativo em **Streamlit** com:  
  - Gráfico de pizza (distribuição de sentimentos: positivo, negativo, neutro).  
  - Nuvem de palavras com termos mais frequentes.  
  - Tabela interativa com notícias coletadas.

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
Criar e ativar ambiente virtual

bash
Copiar código
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Instalar dependências

bash
Copiar código
pip install -r requirements.txt
Executar script de coleta de notícias

bash
Copiar código
python coleta_dados.py
Verificar CSV gerado

Local: data/noticias_coletadas.csv