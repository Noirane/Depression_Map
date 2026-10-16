🧠 DepressionMap
Um sistema para indicadores de depressão e análise de dados sociodemográficos
Dissertação de Mestrado · PROCC/UFS · 2025

Dashboard online Python 3.10 scikit-learn Streamlit Folium

🔗 Acessar o dashboard · O aplicativo · Como executar · A dissertação · Como citar

O DepressionMap é um dashboard web que gera indicadores de depressão a partir do questionário DASS-42, relaciona esses indicadores a variáveis sociodemográficas em 34 países e compara o desempenho de 7 algoritmos de Aprendizado de Máquina na classificação dos níveis de severidade da depressão.

⚠️ O DASS-42 é um instrumento de triagem, não de diagnóstico. Este projeto tem finalidade acadêmica e não substitui a avaliação de um profissional de saúde mental.

📱 O aplicativo
O dashboard tem duas páginas: Home, com os indicadores sociodemográficos, e Inteligência Artificial, com o desempenho dos modelos.

🗺️ Mapa de calor mundial
A página Home abre com o mapa de calor da média dos níveis de depressão (DASS-42) por país. Tons mais claros indicam médias menores e tons mais escuros, médias maiores. Países em cinza tiveram menos de 30 participantes.

Mapa de calor

🌎 Seleção de país
É possível visualizar os dados de todos os países ou de um país específico.

Seleção de país

📊 Indicadores sociodemográficos
Após a seleção, o dashboard mostra a proporção de participantes em cada grupo (gráficos de pizza) e a distribuição dos níveis de depressão em cada um deles (gráficos de barras), para gênero, idade, estado civil e escolaridade. Exemplo com gênero e idade, considerando todos os países:

Gráficos sociodemográficos

📋 Tabela-resumo
Ao final da página Home, uma tabela resume a distribuição dos níveis de depressão e a média de cada grupo:

Tabela-resumo

🤖 Inteligência Artificial
A segunda página compara a acurácia de cada algoritmo na classificação dos cinco níveis de severidade da depressão:

Acurácia dos modelos

🚀 Como executar
# 1. Clone o repositório
git clone https://github.com/Noirane/Depression_Map.git
cd Depression_Map

# 2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o dashboard
streamlit run app.py
O dashboard abrirá em http://localhost:8501. Ou acesse a versão online: depressionmap.streamlit.app.

📁 Estrutura do repositório
├── app.py                            # Ponto de entrada do Streamlit
├── menu.py                           # Navegação entre páginas
├── map_fuctions.py                   # Geração do mapa de calor (Folium)
├── country_data.py                   # Dados agregados por país
├── country_details.py                # Gráficos sociodemográficos por país
├── artificial_intelligence.py        # Página de comparação dos modelos
├── tabel.py                          # Tabela-resumo
├── Depression_map.ipynb              # Pré-processamento e experimentos
├── dataset.csv                       # Dataset pré-processado
├── dataset_one_hot_encoded.csv       # Dataset codificado para ML
├── originalDataset.csv               # Dataset original (Open Psychometrics)
├── resultados_validacao_cruzada.json # Resultados da validação cruzada
└── requirements.txt
🛠️ Tecnologias
Python 3.10 · Pandas · NumPy · scikit-learn · imbalanced-learn (SMOTE) · XGBoost · CatBoost · Folium · Streamlit · Google Colab

🎓 Sobre a dissertação
Contexto
Segundo a Organização Mundial da Saúde, a depressão aumentou mais de 25% após a pandemia de COVID-19 e é a condição mental mais incapacitante do mundo. Sistemas baseados em indicadores podem apoiar profissionais de saúde mental na triagem, na identificação de grupos vulneráveis e no mapeamento das regiões mais afetadas.

Metodologia
1. Mapeamento
Sistemático da
Literatura
2. Identificação
das lacunas
3. Pré-processamento
dos dados
4. Análise
sociodemográfica
5. Experimento
de classificação
com ML
6. DepressionMap
7. Proposta de
estrutura melhorada
O Mapeamento Sistemático da Literatura encontrou 105 estudos (IEEE Xplore, Scopus, PubMed e LILACS), dos quais 19 foram selecionados. A principal lacuna identificada: 17 deles não envolviam profissionais de saúde no processo.

Base de dados
Dataset público da Open Psychometrics, com respostas anônimas de 39.775 participantes coletadas entre 2017 e 2019. Foram usadas as 14 questões da subescala de depressão do DASS-42 e cinco variáveis sociodemográficas: país, idade, gênero, estado civil e escolaridade.

Etapa do pré-processamento	Descrição
Ajuste de escala	Respostas convertidas de 1–4 para 0–3, conforme o DASS-42
Representatividade	Remoção de países com menos de 30 participantes
Valores ausentes	Remoção de linhas incompletas
Faixas válidas	Gênero (1–3), estado civil (1–3), escolaridade (1–4), idade (18–100)
Resultado	24.927 respostas válidas de 34 países
O nível de depressão é a soma das questões 3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38 e 42 (cada uma de 0 a 3):

🟢 Normal	🟡 Leve	🟠 Moderado	🔴 Severo	🟣 Extremamente severo
0 – 9	10 – 13	14 – 20	21 – 27	28+
Resultados
Análise sociodemográfica — média do nível de depressão (0 = normal, 4 = extremamente severo):

Variável	Maior média	Menor média
Gênero	Outro (2,56)	Masculino (2,04)
Idade	18–34 anos (2,19)	55+ anos (1,66)
Estado civil	Nunca casado (2,22)	Casado (1,60)
Escolaridade	Ensino médio (2,28)	Pós-graduação (1,91)
Região	África (2,36)	Austrália/Nova Zelândia (2,16)
Os resultados descrevem esta amostra, que é desbalanceada (maioria de participantes asiáticos, mulheres e jovens), e não devem ser generalizados para populações.

Classificação — One-Hot Encoding, normalização Min-Max, balanceamento com SMOTE e validação cruzada 10-fold, sem ajuste de hiperparâmetros:

Modelo	Acurácia
🥇 Regressão Logística	99,69%
🥈 SVM	99,66%
🥉 Random Forest	95,84%
KNN	91,87%
Árvore de Decisão	84,55%
Gaussian Naive Bayes	68,54%
AdaBoost	49,36%
Proposta de estrutura melhorada
A dissertação propõe uma evolução do DepressionMap que inclui profissionais de saúde mental no fluxo:

responde DASS-42
com consentimento
contato, triagem
e consultas
👤 Participante
Base segura
criptografada
📊 Dashboard
💻 Equipe de TI
🩺 Equipe de saúde
Coleta online com termo de consentimento e retorno ao participante, dados protegidos com criptografia e controle de acesso, painel com lista de espera e mapa de calor em nível de bairro, município ou estado, e acompanhamento pela equipe de saúde.

Limitações e trabalhos futuros
Dataset público, sem controle sobre a qualidade da coleta, e amostra demograficamente desbalanceada;
Avaliação dos modelos baseada apenas em acurácia; trabalhos futuros incluem Precision, Recall e F1-Score;
A estrutura melhorada é conceitual e precisa ser detalhada e validada com profissionais de saúde em um contexto real.
Ética
Conforme a Resolução CNS nº 510/2016, pesquisas com bancos de dados públicos, anônimos e sem possibilidade de identificação individual dispensam registro no sistema CEP/CONEP.

📚 Como citar
@mastersthesis{sa2025depressionmap,
  author  = {Noirane Getirana de Sá},
  title   = {DepressionMap: Um Sistema Para Indicadores de Depressão e Análise de Dados Sociodemográficos},
  school  = {Universidade Federal de Sergipe},
  address = {São Cristóvão, SE},
  year    = {2025},
  type    = {Dissertação de Mestrado},
  note    = {Programa de Pós-Graduação em Ciência da Computação}
}
👩‍💻 Autoria
Noirane Getirana de Sá — Mestre em Ciência da Computação (PROCC/UFS) Orientador: Prof. Dr. Gilton José Ferreira da Silva

Pesquisa financiada com bolsa da FAPITEC-SE.

💙 Se você está passando por um momento difícil, procure ajuda.
No Brasil, o CVV atende 24h pelo telefone 188 ou em cvv.org.br.

INFORMAÇÕES SOBRE O DEPRESSIONMAP 

Link para o dashboard: https://depression-map.streamlit.app/


Apresenta duas páginas: Home, com informações sociodemográficas e sua relação com a depressão e a página com as métricas sobre Inteligência Artificial (com informações sobre o desempenho dos algoritmos na classificação de níveis de severidade da depressão).



