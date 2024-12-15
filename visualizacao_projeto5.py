import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

df = pd.read_csv('clientes-v3-preparado.csv')

# mapa de calor interativo de corelação
df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'estado_cod']].corr()
fig = px.imshow(df_corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Mapa de Calor de Correlação')
fig.show()

# area plot do salário ao longo da idade 
fig=px.area(df, x='idade', y='salario', line_group='estado_civil', color='estado_civil', title='Mapa do Salário por Idade e Estado')
fig.show()

# visualização dos resultados nos modelos de classificação e regressão

# gráficos para a classificação 

# matriz de confusão para regressão logística
cm_lr = confusion_matrix(y_test, y_prev_lr)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Matriz de Confusão: Regressão Logística')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()

# matriz de confusão para árvore de decisão 
cm_lr = confusion_matrix(y_teste, y_prev-lr)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_lr, annot=True, fat='d', cmap='Greens', cbar=False)
plt.title('Matrix de Confusão: Árvore de Decisão')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()

# gráfico de regressão linear
plt.figure(figsize=(8, 6))
plt.scatter(y_test, Y_prev, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.title('Valores Reais vc Predições: Regressão Linear')
plt.xlabel('Real')
plt.ylabel('Previsto')
plt.show()

# visualização de correlação 
# heatmap de correlação de pearson
plt.figure(figsize=(8, 6))
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação de Pearson entre Variáveis')
plt.show()

# heatmap de correlacao de spearman 
plt.figure(figsize=(8, 6))
sns.heatmap(spearman_corr, annot=True, cmap='viridis', fmt='.2f')
plt.title('Correlação de Spearman entre Variáveis')
plt.show()

# visualização interativa usando plotly para a correlação Pearson
fig = px.imshow(pearson_corr, teste_auto=True, aspect='auto', color_continuous_scale='RdBu', title='Correlação de Pearson Interativa')
fig.show()

# visualização interativa usando plotly para a correlação Spearman
fig = px.imshow(pearson_corr, teste_auto=True, aspect='auto', color_continuous_scale='RdBu', title='Correlação de Spearman Interativa')
fig.show()

