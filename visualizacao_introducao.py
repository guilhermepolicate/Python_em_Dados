import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
#print (df)

# Histograma / matplotlib - paramentros 
plt.figure(figsize=(10, 6)) # tamanha da caixa
plt.hist(df['salario'], bins = 100, alpha = 0.8, color = 'green') #coluna, frequência, Transparência e cor
plt.title('histograma - Distribuição de Salário') # título 
plt.xlabel('salario') # nome eixo 'x'
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))  # intervalo do eixo 'x'
plt.ylabel('frequencia') # nome eixo 'y'
plt.grid(True) # linhas do gráfico

# Mapa de Calor
corr = df[['salario', 'anos_experiencia']].corr()
sns.heatmap (corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e idade')

# Tamanha da apresentação
plt.figure(figsize=(12, 6)) # tamanha da caixa

# Multiplos Gráficos 
# Gráfico de correlação(dispersão) / matplotlib
plt.subplot(2, 2, 1) #2 linhas, 2 colunas, 1º grafico
plt.scatter(df['salario'], df['salario'], alpha = 0.8, color = 'blue') # colunas, transparência e cor
plt.title('Dispersão - Salário por Salário') # título 
plt.xlabel('Salário') # nome eixo 'x'
plt.ylabel('Salário') # nome eixo 'y'

# '+'

# Gráfico de correlação(dispersão) / matplotlib
plt.subplot(2, 2, 2) #2 linhas, 2 colunas, 2º grafico
plt.scatter(df['salario'], df['anos_experiencia'], alpha = 0.5 ,color = 'yellow') # colunas, transparência e cor
plt.title('Dispersão - Salário e Anos de Experiência') # título 
plt.xlabel('Salário') # nome eixo 'x'
plt.ylabel('Anos de Experiência') # nome eixo 'y'

# '+'

# Histograma / matplotlib - paramentros 
plt.subplot(2, 2, 3) #2 linhas, 2 colunas, 3º grafico
plt.hist(df['salario'], bins = 100, alpha = 0.8, color = 'green') #coluna, frequência, Transparência e cor
plt.title('histograma - Distribuição de Salário') # título 
plt.xlabel('salario') # nome eixo 'x'
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))  # intervalo do eixo 'x'
plt.ylabel('frequencia') # nome eixo 'y'
plt.grid(True) # linhas do gráfico

# '+'

# Mapa de Calor - Seaborn
plt.subplot(2, 2, 4) #2 linhas, 2 colunas, 4º grafico
corr = df[['salario', 'anos_experiencia']].corr()
sns.heatmap (corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e idade')

plt.tight_layout() # evita a sobreposição
plt.show()