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

### Próximos passos planejados

- Etapa 3: Dashboard em Streamlit (gráficos de pizza, nuvem de palavras e tabela interativa).  
- Etapas 4–6: Versionamento, ética, transparência e documentação final.

**Observação:**  
Esta documentação será atualizada conforme novas decisões forem tomadas nas próximas etapas do projeto.