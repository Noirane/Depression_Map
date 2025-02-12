import json
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do JSON
with open('resultados_validacao_cruzada.json', 'r') as file:
    dados = json.load(file)

# Calcular a média das métricas para cada modelo
modelos = list(dados.keys())
media_acuracia = [np.mean(dados[modelo]["acuracia"]) for modelo in modelos]
media_f1 = [np.mean(dados[modelo]["f1_score"]) for modelo in modelos]

# Ordenar os modelos com base na acurácia média em ordem crescente
modelos_ordenados, media_acuracia_ordenada, media_f1_ordenada = zip(*sorted(
    zip(modelos, media_acuracia, media_f1), key=lambda x: x[1]))

# Criar gráfico de barras horizontais com figura mais larga
fig, ax = plt.subplots(figsize=(10, 6))  # Aumentei a largura para 14

bar_width = 0.4
indices = np.arange(len(modelos_ordenados))

bars1 = ax.barh(indices - bar_width/2, media_acuracia_ordenada, bar_width, label='Acurácia', color='blue')
bars2 = ax.barh(indices + bar_width/2, media_f1_ordenada, bar_width, label='F1-Score', color='orange')

# Adicionar valores ao lado das barras
for bar in bars1:
    ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.4f}', va='center', fontsize=12)
for bar in bars2:
    ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.4f}', va='center', fontsize=12)

# Ajustar os rótulos e título
ax.set_yticks(indices)
ax.set_yticklabels(modelos_ordenados)
ax.set_xlabel("Média das Métricas")
ax.set_title("Comparação de Modelos - Acurácia vs F1-Score")
ax.legend()

# Ajustar o limite do eixo x para ir de 0 a 1.2
ax.set_xlim(0, 1.2)

# Adicionar grade no eixo x
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.show()
