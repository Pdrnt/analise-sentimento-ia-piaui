## Projeto: Painel de Monitoramento de Notícias sobre Inteligência Artificial no Piauí

### Etapa 1 – Coleta de Dados

**Decisão 1: Escolha do feed RSS do Google Notícias**  
- Optamos por utilizar o feed RSS do Google Notícias porque é **público, confiável e atualizado**.  
- Permite buscar notícias de forma automatizada sem necessidade de APIs pagas.  
- A busca foi realizada com os termos: `"Inteligência Artificial Piauí"` e `"SIA Piauí"`, usando operador `OR` para consolidar resultados em uma única requisição.

**Decisão 2: Campos coletados**  
- Foram extraídos: **título, link, descrição, data de publicação e fonte**.  
- A escolha desses campos garante informações suficientes para análises posteriores, como **classificação de sentimento e identificação de temas recorrentes**.

**Decisão 3: Armazenamento dos dados**  
- As notícias coletadas foram salvas em `data/noticias_coletadas.csv`.  
- A pasta `data/` é criada automaticamente caso não exista, garantindo **organização e reprodutibilidade** do projeto.  
- Evitamos versionar o CSV no GitHub para não inflar o repositório; o código permite gerar os dados localmente.

**Decisão 4: Tratamento de erros**  
- Implementamos tratamento de exceções para:  
  - Problemas de rede ou requisição HTTP (`requests.exceptions.RequestException`).  
  - Erros de parsing do XML (`xml.etree.ElementTree.ParseError`).  
- Caso algum item do RSS não contenha fonte (`<source>`), o código atribui `"Desconhecida"`.  
- Isso garante que o script **não quebre** mesmo com feeds incompletos ou indisponíveis.

### Etapa 2 – Processamento e Análise de Sentimento ✅

**Decisão 1: Limpeza de texto**  
- Combinação de título + descrição para análise mais completa.  
- Remoção de tags HTML, caracteres especiais e padronização para minúsculas.

**Decisão 2: Análise de sentimento baseada em regras**  
- Listas de palavras positivas e negativas definidas manualmente.  
- Score simples (+1 para positivo, -1 para negativo).  
- Classificação final: Positivo, Negativo ou Neutro.  
- Escolha baseada em simplicidade, explicabilidade e transparência para o case.

**Decisão 3: Armazenamento dos dados processados**  
- Salvos em `data/noticias_processadas.csv`.  
- Permite integração direta com visualização futura no Streamlit.

**Decisão 4: Tratamento de erros**  
- Arquivo de entrada não encontrado → instrução clara para executar a Etapa 1.  
- CSV vazio → evita processamento desnecessário.  
- Erro ao salvar → captura exceção.

---

### Etapa 3 – Dashboard Streamlit

**Decisão 1: Criação do dashboard**  
- Arquivo criado: `app.py`.  
- Optamos por Streamlit por ser **rápido, interativo e fácil de compartilhar**.  
- Permite exibir gráficos e tabelas diretamente no navegador sem front-end complexo.

**Decisão 2: Métricas principais (KPIs)**  
- Total de notícias coletadas.  
- Contagem e percentual de sentimentos: Positivo, Negativo e Neutro.  
- Escolha dessas métricas para fornecer uma **visão rápida e clara** do cenário de notícias.

**Decisão 3: Visualizações**  
- **Gráfico de pizza/roça** mostrando a distribuição de sentimentos.  
- **Nuvem de palavras** gerada a partir do texto limpo das notícias, destacando os termos mais frequentes.  
- **Tabela interativa** com: título, fonte, data de publicação, sentimento e link.  
- Objetivo: permitir análise detalhada e visualização intuitiva dos dados.

**Decisão 4: Cache de dados**  
- Uso de `@st.cache_data` para evitar recarregar o CSV a cada interação, melhorando **performance** do dashboard.  

**Decisão 5: Tratamento de erros e limitações**  
- Arquivo de entrada não encontrado → mensagem de erro clara no dashboard.  
- CSV vazio → aviso ao usuário e interrupção do dashboard para evitar erros.  
- Limitação: análise de sentimento ainda **baseada em regras simples**, pode não capturar sarcasmo ou contextos complexos.

**Decisão 6: Rodando o dashboard**  
- Comando: `streamlit run app.py`.  
- Estrutura de pastas mantém os CSVs na pasta `data/` para **organização e reprodutibilidade**.

---
### Próximos passos planejados
- Etapas 4–6: Versionamento, ética, transparência e documentação final.

**Observação:**  
Esta documentação será atualizada conforme novas decisões forem tomadas nas próximas etapas do projeto.