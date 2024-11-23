import pandas as pd

df = pd.read_csv('C:/Users/Rose Claudino/Desktop/EBAC/3 - Analista de Dados/05 - Manipulação de Dados com Python/VSCode/Aula3/clientes3.csv')

#verificar todo o registro 
print (df)

#verificar os primeiros registros 
print(df.head().to_string)

#verificar os ultimo registros 
print(df.tail().to_string)

#verifica os indices 
print(df.index)

#verificar quantas linhas e colunas 
print(df.shape)

#verificar a tipagem dos dados
print(df.dtypes)

#verificar valores nulos
print(df.isnull().sum())

#verifica a tipagem e a existencia de nulidades
print(df.info())