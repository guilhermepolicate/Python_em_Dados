import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
#print (df)

# Tamanho da apresentação
plt.figure(figsize=(12, 6)) # tamanha da caixa sempre deve ser definido

# Multiplos Gráfico
# Gráfico de Barras / Pandas (.plot)
plt.subplot(2, 2, 1) #2 linhas, 2 colunas, 1º grafico
df['nivel_educacao'].value_counts().plot(kind='bar', color='gray') # '.plot = plotar'
plt.title('Divisão de escolaridade 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=30) # rotação do indice do eixo 'x'
plt.yticks(rotation=30) # rotação do indice do eixo 'y'

# ou 

plt.subplot(2, 2, 2) #2 linhas, 2 colunas, 2º grafico
x=df['nivel_educacao'].value_counts().index
y=df['nivel_educacao'].value_counts().values
plt.bar(x, y, color = 'gray')
plt.title('Divisão de escolaridade 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=90) # rotação do indice do eixo 'x'
plt.yticks(rotation=90) # rotação do indice do eixo 'y'

# ou

# Gráfico de Pizza
plt.subplot(2, 2, 3) #2 linhas, 2 colunas, 3º grafico
plt.pie(y, labels=x, autopct='%.2f%%', startangle=90) # 'labels=descrição','.2F=casas decimais','ângulo de início
plt.title('Divisão de escolaridade 3')

# Grafico de Dispresao (correlação) tipo Hexbin /Matplotlib
plt.subplot(2, 2, 4) #2 linhas, 2 colunas, 4º grafico
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues') # 'gridsize=tamanho das bolinhas','cmap=profundidade de cor
plt.colorbar(label='contagem dentro do bin') # contagem acontece pela cor da bolinha
plt.xlabel('idade')
plt.xlabel('salario')
plt.title('Dispersão de Idade e Salário')

plt.tight_layout() # evita a sobreposição
plt.show()