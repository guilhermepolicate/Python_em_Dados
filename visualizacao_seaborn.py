import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
print (df)

# Tamanho da apresentação

# Grafico de Dispersão / Seaborn
# jointplot = mostra a dispersão e a concentracao das variaveis
plt.figure(figsize=(12, 6)) # tamanha da caixa
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') # 'scatter' , 'hist' , 'hex' , 'kde' , 'reg' , 'resid'

# Gráfico de Densidade (Suaviza o Histograma) / Seaborn
plt.figure(figsize=(12, 6)) # tamanha da caixa
sns.kdeplot(df['salario'], fill=True, color='black')
plt.title('Densidade - Salário por Salário') # título 
plt.xlabel('Salário') # nome eixo 'x'

# Gráfico de Pairplot - Dispersão e Histograma / Seaborn
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao_cod']])

# Gráfico de regressão / Seaborm
sns.regplot (x='idade', y='salario', data=df, color='black', scatter_kws={'alpha':0.5, 'color': 'blue', 's':30})
plt.title ('Regressão de salário por idade')
plt.xlabel ('idade')
plt.ylabel ('salario')

# Gráfico countplot com hue / Seaborn
# hue = agrupamento de quantidade de pessoas em cada nivel de educação em cada estado civil
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel ('Estado Civil')
plt.ylabel ('Quantidade de Clientes')
plt.legend (title='Nível de Educação')

plt.show()