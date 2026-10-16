<p align="center">
  <img src="img/banner_en.svg" alt="DepressionMap" width="100%">
</p>

<p align="center">
  <a href="https://depressionmap.streamlit.app/"><img src="https://img.shields.io/badge/▶_Open_the_dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Open the dashboard"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/scikit--learn-1.6-F7931E?logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-1.41-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-2.2-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Plotly-charts-3F4F75?logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/Folium-maps-77B829?logo=leaflet&logoColor=white" alt="Folium">
  <img src="https://img.shields.io/badge/UFS-PROCC-1F4E9C" alt="UFS PROCC">
</p>

<details>
<summary><b>🇧🇷 Ler em português</b> <sub>(clique para abrir)</sub></summary>
<br>

**DepressionMap** é um dashboard web que transforma respostas ao questionário **DASS-42** em **indicadores de depressão**, cruza esses indicadores com **dados sociodemográficos** de 34 países e mostra como **7 algoritmos de Aprendizado de Máquina** se saem ao classificar os níveis de severidade da doença, com validação estatística dos resultados.

<p align="center">
  <img src="img/numeros.svg" alt="39.775 respostas, 24.927 válidas, 34 países, 7 algoritmos, 99,69% de acurácia" width="100%">
</p>

> [!IMPORTANT]
> O DASS-42 é um instrumento de **triagem**, não de diagnóstico. Este projeto tem finalidade acadêmica e **não substitui a avaliação de um profissional de saúde mental**.

---

## 📱 O aplicativo

O dashboard tem duas páginas: **Home**, com os indicadores sociodemográficos, e **Inteligência Artificial**, com o desempenho dos modelos.

### 🗺️ Mapa de calor mundial

A página Home abre com a média dos níveis de depressão por país. Amarelo claro indica médias mais baixas e vermelho escuro, médias mais altas. Países em cinza tiveram menos de 30 participantes.

<p align="center">
  <img src="https://i.ibb.co/LrJrK9M/Menu.png" alt="Mapa de calor do DepressionMap" width="95%">
</p>

### 🌎 Escolha o país, veja os gráficos

<table>
  <tr>
    <td width="50%" valign="top">
      <b>1. Selecione</b> todos os países ou um país específico.<br><br>
      <img src="https://i.ibb.co/F8gs2mW/pais.png" alt="Seleção de país" width="100%">
    </td>
    <td width="50%" valign="top">
      <b>2. Compare</b> os níveis de depressão por gênero, idade, estado civil e escolaridade.<br><br>
      <img src="https://i.ibb.co/Sd0ZxQT/graficos.png" alt="Gráficos sociodemográficos" width="100%">
    </td>
  </tr>
</table>

### 📋 Tabela-resumo

No fim da página Home, uma tabela reúne a distribuição dos níveis de depressão e a média de cada grupo.

<p align="center">
  <img src="https://i.ibb.co/CzHf8L5/dados.png" alt="Tabela-resumo" width="95%">
</p>

### 🤖 Inteligência Artificial

A segunda página compara a acurácia de cada algoritmo na classificação dos cinco níveis de severidade.

<p align="center">
  <img src="https://i.ibb.co/QFVdd7p/macLear.png" alt="Acurácia dos modelos no dashboard" width="95%">
</p>

---

## 🎓 A pesquisa

> *“Segundo a Organização Mundial da Saúde, após a pandemia de COVID-19, ocorreu um aumento da depressão em mais de 25%, sendo a condição mental mais incapacitante do mundo. Um sistema baseado em indicadores de depressão pode auxiliar profissionais de saúde mental na triagem da doença.”*
>
> — Resumo da dissertação

### 🧭 Metodologia

<p align="center">
  <img src="img/metodologia.png" alt="Etapas da metodologia" width="90%">
</p>

<table>
  <tr>
    <td align="center" width="25%">🔎<br><b>Mapeamento Sistemático</b><br><sub>105 estudos em 4 bases<br>19 selecionados</sub></td>
    <td align="center" width="25%">🧹<br><b>Pré-processamento</b><br><sub>39.775 → 24.927<br>respostas válidas</sub></td>
    <td align="center" width="25%">📊<br><b>Análise sociodemográfica</b><br><sub>gênero, idade, estado civil,<br>escolaridade e país</sub></td>
    <td align="center" width="25%">🤖<br><b>Classificação com ML</b><br><sub>7 algoritmos, 10-fold<br>testes estatísticos</sub></td>
  </tr>
</table>

**A lacuna encontrada:** dos 19 estudos selecionados no mapeamento, **17 não envolviam profissionais de saúde** no processo. O DASS não foi projetado para substituir uma avaliação psicológica, e sim para gerar indicadores que apoiem o diagnóstico. Daí a proposta de uma estrutura que une tecnologia e equipe clínica.

### 🗂️ Dados

Dataset público da [Open Psychometrics](https://openpsychometrics.org/) com respostas anônimas coletadas entre 2017 e 2019. Foram usadas as **14 questões da subescala de depressão** do DASS-42 e cinco variáveis sociodemográficas: **país, idade, gênero, estado civil e escolaridade**.

<details>
<summary><b>Ver etapas do pré-processamento</b></summary>
<br>

| Etapa | Descrição |
|---|---|
| Ajuste de escala | Respostas convertidas de 1–4 para 0–3, conforme o DASS-42 |
| Representatividade | Remoção de países com menos de 30 participantes (teorema do limite central) |
| Valores ausentes | Remoção de linhas incompletas |
| Faixas válidas | Gênero (1–3), estado civil (1–3), escolaridade (1–4), idade (18–100) |
| **Resultado** | **24.927 respostas válidas de 34 países** |

</details>

### 🧮 Como o nível de depressão é calculado

Soma das questões **3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38 e 42**, cada uma pontuada de 0 a 3:

<table align="center">
  <tr>
    <td align="center">⬜<br><b>Normal</b><br>0 – 9</td>
    <td align="center">🟨<br><b>Leve</b><br>10 – 13</td>
    <td align="center">🟧<br><b>Moderado</b><br>14 – 20</td>
    <td align="center">🟥<br><b>Severo</b><br>21 – 27</td>
    <td align="center">🟪<br><b>Extremamente severo</b><br>28+</td>
  </tr>
</table>

---

## 📈 Resultados

### Depressão e perfil sociodemográfico

<table>
  <tr>
    <td width="55%" valign="top">
      <img src="img/genero.png" alt="Gênero e sua relação com a depressão" width="100%">
      <p align="center"><sub>Distribuição dos níveis de depressão por gênero (todos os países)</sub></p>
    </td>
    <td width="45%" valign="top">

<table>
<tr><th>Variável</th><th>↑ Maior média</th><th>↓ Menor média</th></tr>
<tr><td>Gênero</td><td>Outro · <b>2,56</b></td><td>Masculino · <b>2,04</b></td></tr>
<tr><td>Idade</td><td>18–34 · <b>2,19</b></td><td>55+ · <b>1,66</b></td></tr>
<tr><td>Estado civil</td><td>Nunca casado · <b>2,22</b></td><td>Casado · <b>1,60</b></td></tr>
<tr><td>Escolaridade</td><td>Ensino médio · <b>2,28</b></td><td>Pós · <b>1,91</b></td></tr>
<tr><td>Região</td><td>África · <b>2,36</b></td><td>Aus./NZ · <b>2,16</b></td></tr>
</table>

<sub>Média do nível de depressão: 0 = normal, 4 = extremamente severo.</sub>

</td>
  </tr>
</table>

> [!NOTE]
> Os resultados descrevem **esta amostra**, que é desbalanceada (maioria de participantes asiáticos, mulheres e jovens), e não devem ser generalizados para populações.

### Classificação dos níveis de severidade

Sete algoritmos foram treinados com One-Hot Encoding, normalização Min-Max e balanceamento com SMOTE, avaliados por validação cruzada 10-fold e sem ajuste de hiperparâmetros.

<p align="center">
  <img src="img/acuracia.png" alt="Comparação dos modelos: acurácia e medida-F1" width="85%">
</p>

<table align="center">
<tr><th></th><th>Modelo</th><th align="right">Acurácia</th><th align="right">Precisão</th><th align="right">Sensibilidade</th><th align="right">Medida-F1</th></tr>
<tr><td align="center">🥇</td><td><b>Regressão Logística</b></td><td align="right"><b>0,9969</b></td><td align="right"><b>0,9969</b></td><td align="right"><b>0,9969</b></td><td align="right"><b>0,9969</b></td></tr>
<tr><td align="center">🥇</td><td><b>SVM</b></td><td align="right"><b>0,9966</b></td><td align="right"><b>0,9966</b></td><td align="right"><b>0,9966</b></td><td align="right"><b>0,9966</b></td></tr>
<tr><td align="center">🥉</td><td>Random Forest</td><td align="right">0,9592</td><td align="right">0,9594</td><td align="right">0,9592</td><td align="right">0,9592</td></tr>
<tr><td></td><td>KNN</td><td align="right">0,9187</td><td align="right">0,9231</td><td align="right">0,9187</td><td align="right">0,9192</td></tr>
<tr><td></td><td>Árvore de Decisão</td><td align="right">0,8463</td><td align="right">0,8462</td><td align="right">0,8463</td><td align="right">0,8461</td></tr>
<tr><td></td><td>Gaussian Naive Bayes</td><td align="right">0,6854</td><td align="right">0,7350</td><td align="right">0,6854</td><td align="right">0,6866</td></tr>
<tr><td></td><td>AdaBoost</td><td align="right">0,4936</td><td align="right">0,5946</td><td align="right">0,4936</td><td align="right">0,4359</td></tr>
</table>

> [!TIP]
> **Empate técnico confirmado estatisticamente.** Entre os modelos que atingiram a meta de 95% de acurácia, o teste de Friedman indicou diferença significativa (p = 0,00036 para acurácia e p = 0,00050 para F1). O pós-teste de Nemenyi mostrou que **Regressão Logística e SVM são estatisticamente equivalentes** (p = 0,78 e p = 0,90) e ambos superiores à Random Forest.

<details>
<summary><b>Ver validação estatística completa</b></summary>
<br>

Fluxo definido com a ferramenta [Autorank](https://github.com/sherbold/autorank), com nível de significância de 0,05:

| Teste | Objetivo | Resultado |
|---|---|---|
| Shapiro-Wilk | Normalidade | Distribuições normais (LR 0,27 · SVM 0,90 · RF 0,49) |
| Bartlett | Homogeneidade das variâncias | Variâncias não homogêneas (p = 0,00176 e 0,00172) |
| Friedman | Comparação entre algoritmos | Diferença significativa (p = 0,00036 e 0,00050) |
| Nemenyi | Comparação par a par | RF × SVM e RF × LR diferentes; **SVM × LR equivalentes** |

| Par comparado | p (Acurácia) | p (Medida-F1) |
|---|---:|---:|
| Random Forest × SVM | 0,007165 | 0,004965 |
| Random Forest × Regressão Logística | 0,000658 | 0,001010 |
| SVM × Regressão Logística | **0,780467** | **0,895638** |

</details>

<details>
<summary><b>Comparação com estudos relacionados</b></summary>
<br>

Acurácia (%) obtida neste estudo em comparação com trabalhos que usaram o mesmo dataset:

| Modelo | Este estudo | Srinath et al. (2022) | Singh et al. (2022) |
|---|---:|---:|---:|
| Regressão Logística | **99,69** | 98,15 | – |
| SVM | **99,66** | 97,35 | 94,00 |
| Random Forest | **95,92** | 84,97 | 85,00 |
| KNN | **91,87** | 75,14 | 73,00 |
| Árvore de Decisão | **84,63** | – | 75,00 |
| Gaussian Naive Bayes | **68,54** | – | 33,00 |
| AdaBoost | 49,36 | – | **80,00** |

Os estudos relacionados classificaram depressão, ansiedade e estresse ao mesmo tempo, com menos etapas de pré-processamento. Este trabalho focou somente na depressão.

</details>

### 🏥 Proposta de estrutura melhorada

A versão atual do DepressionMap envolve dataset, equipe de TI e dashboard. A dissertação propõe uma evolução que coloca **profissionais de saúde mental** no centro do fluxo: o participante responde ao questionário com consentimento, recebe um retorno inicial, seus dados ficam protegidos com criptografia e controle de acesso, e a equipe de saúde usa o painel para triagem, lista de espera e agendamento de consultas.

<p align="center">
  <img src="img/estrutura_melhorada.png" alt="DepressionMap x Estrutura melhorada" width="70%">
</p>

<details>
<summary><b>Limitações e trabalhos futuros</b></summary>
<br>

- Dataset público, sem controle sobre a qualidade da coleta, e amostra demograficamente desbalanceada;
- A remoção de dados no pré-processamento pode introduzir viés;
- Gaussian Naive Bayes e AdaBoost tiveram desempenho abaixo de 70% e podem melhorar com ajuste de parâmetros ou mais dados;
- A estrutura melhorada é conceitual e precisa ser detalhada e validada com profissionais de saúde em um contexto real.

</details>

<details>
<summary><b>Aspectos éticos</b></summary>
<br>

Conforme a Resolução CNS nº 510/2016, pesquisas com bancos de dados públicos, anônimos e sem possibilidade de identificação individual dispensam registro no sistema CEP/CONEP.

</details>

---

## 🚀 Como executar

```bash
git clone https://github.com/Noirane/Depression_Map.git
cd Depression_Map
pip install -r requirements.txt
streamlit run app.py
```

O dashboard abre em `http://localhost:8501`.

<details>
<summary><b>Estrutura do repositório</b></summary>
<br>

```
├── app.py                            # Ponto de entrada do Streamlit
├── menu.py                           # Navegação entre páginas
├── map_fuctions.py                   # Mapa de calor (Folium)
├── country_data.py                   # Dados agregados por país
├── country_details.py                # Gráficos sociodemográficos
├── artificial_intelligence.py        # Página de comparação dos modelos
├── tabel.py                          # Tabela-resumo
├── Depression_map.ipynb              # Pré-processamento e experimentos
├── dataset.csv                       # Dataset pré-processado
├── dataset_one_hot_encoded.csv       # Dataset codificado para ML
├── originalDataset.csv               # Dataset original (Open Psychometrics)
├── resultados_validacao_cruzada.json # Resultados da validação cruzada
├── img/                              # Imagens do README
└── requirements.txt
```

</details>

---

## 📚 Como citar

```bibtex
@mastersthesis{sa2025depressionmap,
  author  = {Noirane Getirana de Sá},
  title   = {DepressionMap: Um Sistema Para Indicadores de Depressão e Análise de Dados Sociodemográficos},
  school  = {Universidade Federal de Sergipe},
  address = {São Cristóvão, SE},
  year    = {2025},
  type    = {Dissertação de Mestrado},
  note    = {Programa de Pós-Graduação em Ciência da Computação}
}
```

## 👩‍💻 Autoria

<table>
  <tr>
    <td>
      <b>Noirane Getirana de Sá</b><br>
      Mestre em Ciência da Computação · PROCC/UFS<br>
      <sub>Orientador: Prof. Dr. Gilton José Ferreira da Silva · Bolsa FAPITEC-SE</sub><br>
      <sub>Dissertação defendida e <b>aprovada</b> em 27 de janeiro de 2025</sub>
    </td>
  </tr>
</table>

<details>
<summary><b>Banca examinadora</b></summary>
<br>

- Prof. Dr. Gilton José Ferreira da Silva (PROCC/UFS), presidente
- Profª. Dra. Zenith Nara Costa Delabrida (DPS/UFS), examinadora externa
- Prof. Dr. Fábio Gomes Rocha (PROCC/UFS), examinador interno

</details>

<details>
<summary><b>Artigos derivados da pesquisa</b></summary>
<br>

- *Relevância de Escalas Emocionais no Aprendizado de Máquina e em Cidades Inteligentes*, submetido à revista Abakós;
- *Saúde Mental e Inteligência Artificial, Identificação de Temas e Técnicas Relevantes: um Mapeamento Sistemático*, submetido à Revista Tecnologia e Sociedade;
- *Accessible Smart Health: Framework for Depression Indicators*, submetido ao SBSI 2025.

</details>

<!-- Adicione seus links: -->
<!-- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/SEU-PERFIL) -->

---

<p align="center">
  💙 Se você está passando por um momento difícil, procure ajuda.<br>
  No Brasil, o <b>CVV</b> atende 24h pelo telefone <b>188</b> ou em <a href="https://cvv.org.br">cvv.org.br</a>.
</p>

<p align="center"><sub>⬆️ Clique em "Ler em português" para fechar · 🇺🇸 English version below</sub></p>

</details>

---

**DepressionMap** is a web dashboard that turns responses to the **DASS-42** questionnaire into **depression indicators**, cross-references them with **sociodemographic data** from 34 countries, and shows how **7 Machine Learning algorithms** perform when classifying depression severity levels, with statistical validation of the results.

<p align="center">
  <img src="img/numeros_en.svg" alt="39,775 responses, 24,927 valid, 34 countries, 7 algorithms, 99.69% accuracy" width="100%">
</p>

> [!IMPORTANT]
> The DASS-42 is a **screening** tool, not a diagnostic one. This is an academic project and **does not replace an assessment by a mental health professional**.

<p align="center">
  <a href="#-the-app">The app</a> •
  <a href="#-the-research">The research</a> •
  <a href="#-results">Results</a> •
  <a href="#-how-to-run">How to run</a> •
  <a href="#-how-to-cite">How to cite</a>
</p>

---

## 📱 The app

The dashboard has two pages: **Home**, with sociodemographic indicators, and **Artificial Intelligence**, with model performance.

### 🗺️ World heat map

The Home page opens with the average depression level per country. Light yellow means lower averages and dark red means higher averages. Countries in gray had fewer than 30 participants.

<p align="center">
  <img src="https://i.ibb.co/LrJrK9M/Menu.png" alt="DepressionMap heat map" width="95%">
</p>

### 🌎 Pick a country, explore the charts

<table>
  <tr>
    <td width="50%" valign="top">
      <b>1. Select</b> all countries or a specific one.<br><br>
      <img src="https://i.ibb.co/F8gs2mW/pais.png" alt="Country selection" width="100%">
    </td>
    <td width="50%" valign="top">
      <b>2. Compare</b> depression levels by gender, age, marital status and education.<br><br>
      <img src="https://i.ibb.co/Sd0ZxQT/graficos.png" alt="Sociodemographic charts" width="100%">
    </td>
  </tr>
</table>

### 📋 Summary table

At the bottom of the Home page, a table brings together the distribution of depression levels and the average of each group.

<p align="center">
  <img src="https://i.ibb.co/CzHf8L5/dados.png" alt="Summary table" width="95%">
</p>

### 🤖 Artificial Intelligence

The second page compares each algorithm's accuracy in classifying the five severity levels.

<p align="center">
  <img src="https://i.ibb.co/QFVdd7p/macLear.png" alt="Model accuracy in the dashboard" width="95%">
</p>

<sub>The dashboard is in Portuguese. Figures from the dissertation below are also in Portuguese.</sub>

---

## 🎓 The research

> *"According to the World Health Organization, after the COVID-19 pandemic, there was an increase of more than 25% in depression, making it the most disabling mental condition in the world. A system based on depression indicators can assist mental health professionals in screening for the disease."*
>
> — Dissertation abstract

### 🧭 Methodology

<p align="center">
  <img src="img/metodologia.png" alt="Methodology steps" width="90%">
</p>

<table>
  <tr>
    <td align="center" width="25%">🔎<br><b>Systematic Mapping</b><br><sub>105 studies in 4 databases<br>19 selected</sub></td>
    <td align="center" width="25%">🧹<br><b>Preprocessing</b><br><sub>39,775 → 24,927<br>valid responses</sub></td>
    <td align="center" width="25%">📊<br><b>Sociodemographic analysis</b><br><sub>gender, age, marital status,<br>education and country</sub></td>
    <td align="center" width="25%">🤖<br><b>ML classification</b><br><sub>7 algorithms, 10-fold<br>statistical tests</sub></td>
  </tr>
</table>

**The gap we found:** of the 19 studies selected in the mapping, **17 did not involve health professionals** in the process. The DASS was not designed to replace a psychological assessment, but to provide indicators that support diagnosis. Hence the proposal of a structure that brings technology and clinical teams together.

### 🗂️ Data

Public dataset from [Open Psychometrics](https://openpsychometrics.org/) with anonymous responses collected between 2017 and 2019. We used the **14 items of the DASS-42 depression subscale** and five sociodemographic variables: **country, age, gender, marital status and education**.

<details>
<summary><b>See preprocessing steps</b></summary>
<br>

| Step | Description |
|---|---|
| Scale adjustment | Responses converted from 1–4 to 0–3, as defined by the DASS-42 |
| Representativeness | Countries with fewer than 30 participants removed (central limit theorem) |
| Missing values | Incomplete rows removed |
| Valid ranges | Gender (1–3), marital status (1–3), education (1–4), age (18–100) |
| **Result** | **24,927 valid responses from 34 countries** |

</details>

### 🧮 How the depression level is computed

Sum of items **3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38 and 42**, each scored from 0 to 3:

<table align="center">
  <tr>
    <td align="center">⬜<br><b>Normal</b><br>0 – 9</td>
    <td align="center">🟨<br><b>Mild</b><br>10 – 13</td>
    <td align="center">🟧<br><b>Moderate</b><br>14 – 20</td>
    <td align="center">🟥<br><b>Severe</b><br>21 – 27</td>
    <td align="center">🟪<br><b>Extremely severe</b><br>28+</td>
  </tr>
</table>

---

## 📈 Results

### Depression and sociodemographic profile

<table>
  <tr>
    <td width="55%" valign="top">
      <img src="img/genero.png" alt="Gender and depression" width="100%">
      <p align="center"><sub>Distribution of depression levels by gender (all countries)</sub></p>
    </td>
    <td width="45%" valign="top">
<table>
<tr><th>Variable</th><th>↑ Highest average</th><th>↓ Lowest average</th></tr>
<tr><td>Gender</td><td>Other · <b>2.56</b></td><td>Male · <b>2.04</b></td></tr>
<tr><td>Age</td><td>18–34 · <b>2.19</b></td><td>55+ · <b>1.66</b></td></tr>
<tr><td>Marital status</td><td>Never married · <b>2.22</b></td><td>Married · <b>1.60</b></td></tr>
<tr><td>Education</td><td>High school · <b>2.28</b></td><td>Graduate · <b>1.91</b></td></tr>
<tr><td>Region</td><td>Africa · <b>2.36</b></td><td>Aus./NZ · <b>2.16</b></td></tr>
</table>

<sub>Average depression level: 0 = normal, 4 = extremely severe.</sub>

</td>
  </tr>
</table>

> [!NOTE]
> These results describe **this sample**, which is unbalanced (mostly Asian, female and young participants), and should not be generalized to populations.

### Severity level classification

Seven algorithms were trained with One-Hot Encoding, Min-Max normalization and SMOTE balancing, evaluated with 10-fold cross-validation and no hyperparameter tuning.

<p align="center">
  <img src="img/acuracia.png" alt="Model comparison: accuracy and F1-score" width="85%">
</p>

<table align="center">
<tr><th></th><th>Model</th><th align="right">Accuracy</th><th align="right">Precision</th><th align="right">Recall</th><th align="right">F1-score</th></tr>
<tr><td align="center">🥇</td><td><b>Logistic Regression</b></td><td align="right"><b>0.9969</b></td><td align="right"><b>0.9969</b></td><td align="right"><b>0.9969</b></td><td align="right"><b>0.9969</b></td></tr>
<tr><td align="center">🥇</td><td><b>SVM</b></td><td align="right"><b>0.9966</b></td><td align="right"><b>0.9966</b></td><td align="right"><b>0.9966</b></td><td align="right"><b>0.9966</b></td></tr>
<tr><td align="center">🥉</td><td>Random Forest</td><td align="right">0.9592</td><td align="right">0.9594</td><td align="right">0.9592</td><td align="right">0.9592</td></tr>
<tr><td></td><td>KNN</td><td align="right">0.9187</td><td align="right">0.9231</td><td align="right">0.9187</td><td align="right">0.9192</td></tr>
<tr><td></td><td>Decision Tree</td><td align="right">0.8463</td><td align="right">0.8462</td><td align="right">0.8463</td><td align="right">0.8461</td></tr>
<tr><td></td><td>Gaussian Naive Bayes</td><td align="right">0.6854</td><td align="right">0.7350</td><td align="right">0.6854</td><td align="right">0.6866</td></tr>
<tr><td></td><td>AdaBoost</td><td align="right">0.4936</td><td align="right">0.5946</td><td align="right">0.4936</td><td align="right">0.4359</td></tr>
</table>

> [!TIP]
> **A statistically confirmed tie.** Among the models that reached the 95% accuracy target, the Friedman test found a significant difference (p = 0.00036 for accuracy and p = 0.00050 for F1). The Nemenyi post-hoc test showed that **Logistic Regression and SVM are statistically equivalent** (p = 0.78 and p = 0.90), and both outperform Random Forest.

<details>
<summary><b>See full statistical validation</b></summary>
<br>

Test workflow defined with [Autorank](https://github.com/sherbold/autorank), significance level 0.05:

| Test | Purpose | Result |
|---|---|---|
| Shapiro-Wilk | Normality | Normal distributions (LR 0.27 · SVM 0.90 · RF 0.49) |
| Bartlett | Homogeneity of variances | Non-homogeneous variances (p = 0.00176 and 0.00172) |
| Friedman | Comparison across algorithms | Significant difference (p = 0.00036 and 0.00050) |
| Nemenyi | Pairwise comparison | RF × SVM and RF × LR differ; **SVM × LR equivalent** |

| Pair | p (Accuracy) | p (F1-score) |
|---|---:|---:|
| Random Forest × SVM | 0.007165 | 0.004965 |
| Random Forest × Logistic Regression | 0.000658 | 0.001010 |
| SVM × Logistic Regression | **0.780467** | **0.895638** |

</details>

<details>
<summary><b>Comparison with related studies</b></summary>
<br>

Accuracy (%) in this study compared with previous work using the same dataset:

| Model | This study | Srinath et al. (2022) | Singh et al. (2022) |
|---|---:|---:|---:|
| Logistic Regression | **99.69** | 98.15 | – |
| SVM | **99.66** | 97.35 | 94.00 |
| Random Forest | **95.92** | 84.97 | 85.00 |
| KNN | **91.87** | 75.14 | 73.00 |
| Decision Tree | **84.63** | – | 75.00 |
| Gaussian Naive Bayes | **68.54** | – | 33.00 |
| AdaBoost | 49.36 | – | **80.00** |

The related studies classified depression, anxiety and stress together, with fewer preprocessing steps. This work focused on depression only.

</details>

### 🏥 Proposed improved structure

The current DepressionMap involves the dataset, an IT team and the dashboard. The dissertation proposes an evolution that puts **mental health professionals** at the center: participants answer the questionnaire with consent and receive initial feedback, their data is protected with encryption and access control, and the health team uses the dashboard for screening, waiting lists and scheduling appointments.

<p align="center">
  <img src="img/estrutura_melhorada.png" alt="DepressionMap vs improved structure" width="70%">
</p>

<details>
<summary><b>Limitations and future work</b></summary>
<br>

- Public dataset with no control over data collection quality, and a demographically unbalanced sample;
- Removing data during preprocessing may introduce bias;
- Gaussian Naive Bayes and AdaBoost scored below 70% and may improve with parameter tuning or more data;
- The improved structure is conceptual and needs to be detailed and validated with health professionals in a real-world setting.

</details>

<details>
<summary><b>Ethics</b></summary>
<br>

Under Brazilian National Health Council Resolution No. 510/2016, research using public, anonymous databases with no possibility of individual identification does not require registration with the CEP/CONEP ethics system.

</details>

---

## 🚀 How to run

```bash
git clone https://github.com/Noirane/Depression_Map.git
cd Depression_Map
pip install -r requirements.txt
streamlit run app.py
```

The dashboard opens at `http://localhost:8501`.

<details>
<summary><b>Repository structure</b></summary>
<br>

```
├── app.py                            # Streamlit entry point
├── menu.py                           # Page navigation
├── map_fuctions.py                   # Heat map (Folium)
├── country_data.py                   # Country-level aggregated data
├── country_details.py                # Sociodemographic charts
├── artificial_intelligence.py        # Model comparison page
├── tabel.py                          # Summary table
├── Depression_map.ipynb              # Preprocessing and experiments
├── dataset.csv                       # Preprocessed dataset
├── dataset_one_hot_encoded.csv       # Encoded dataset for ML
├── originalDataset.csv               # Original dataset (Open Psychometrics)
├── resultados_validacao_cruzada.json # Cross-validation results
├── img/                              # README images
└── requirements.txt
```

</details>

---

## 📚 How to cite

```bibtex
@mastersthesis{sa2025depressionmap,
  author  = {Noirane Getirana de Sá},
  title   = {DepressionMap: Um Sistema Para Indicadores de Depressão e Análise de Dados Sociodemográficos},
  school  = {Universidade Federal de Sergipe},
  address = {São Cristóvão, SE},
  year    = {2025},
  type    = {Dissertação de Mestrado},
  note    = {Programa de Pós-Graduação em Ciência da Computação}
}
```

## 👩‍💻 Author

<table>
  <tr>
    <td>
      <b>Noirane Getirana de Sá</b><br>
      M.Sc. in Computer Science · PROCC/UFS<br>
      <sub>Advisor: Prof. Dr. Gilton José Ferreira da Silva · FAPITEC-SE scholarship</sub><br>
      <sub>Dissertation defended and <b>approved</b> on January 27, 2025</sub>
    </td>
  </tr>
</table>

<details>
<summary><b>Examining committee</b></summary>
<br>

- Prof. Dr. Gilton José Ferreira da Silva (PROCC/UFS), chair
- Prof. Dr. Zenith Nara Costa Delabrida (DPS/UFS), external examiner
- Prof. Dr. Fábio Gomes Rocha (PROCC/UFS), internal examiner

</details>

<details>
<summary><b>Papers derived from this research</b></summary>
<br>

- *Relevância de Escalas Emocionais no Aprendizado de Máquina e em Cidades Inteligentes*, submitted to Abakós journal;
- *Saúde Mental e Inteligência Artificial, Identificação de Temas e Técnicas Relevantes: um Mapeamento Sistemático*, submitted to Revista Tecnologia e Sociedade;
- *Accessible Smart Health: Framework for Depression Indicators*, submitted to SBSI 2025.

</details>

<!-- Add your links: -->
<!-- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR-PROFILE) -->

---

<p align="center">
  💙 If you are going through a hard time, please reach out for help.<br>
  In Brazil, <b>CVV</b> is available 24/7 at <b>188</b> or <a href="https://cvv.org.br">cvv.org.br</a>.
</p>
