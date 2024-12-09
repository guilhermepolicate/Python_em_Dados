import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
#print (df)

df_corr=df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
sns.set(style='whitegrid')

# Heatmap de correlação (muito bom para analises iniciais)
plt.figure(figsize=(10, 5))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title ('Mapa de Calor de Correlação entre Variáveis')

# Exemplo aleatório de grafico de dispersão 
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)

plt.scatter(x, y, c=colors, cmap='viridis') # mapa de cores
plt.colorbar()  # Adiciona uma barra de cores para referência
plt.title('Gráfico de Dispersão com cmap')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Sobreposição de gráficos (colocar um 'plt.show' no final)
# Countplot sem legenda
sns.countplot(x = 'estado_civil', data = df, color = 'Black')
plt.title('Distribuição de Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')

# Countplot com legenda
sns.countplot(x = 'estado_civil', hue = 'nivel_educacao', data = df)
plt.title('Distribuição de Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')

# Salvando o Gráfico 
plt.savefig('Distrubição - Estado Civil vs Nivel Escolar')


plt.tight_layout() # evita a sobreposição
plt.show()