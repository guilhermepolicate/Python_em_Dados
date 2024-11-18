#ANALISE EXPLORATÓRIA DOS DADOS TRATADOS
import pandas as pd
import seaborn as sn

df = pd.read_csv('clientes-v2.csv')
print (df.head().to_string)
print (df.tail().to_string)

#Análise de dados nulos 
print (df.info())
print(df.isnull().sum()) # - Valores Inteiros
print(df.isnull().mean()*100) # - Percentual em relação ao total
print(df.isnull().sum().sum()) # - Soma o total de dados nulos
df.dropna(inplace=True)

#Análise de dados duplicados
print(df.duplicated().sum().sum()) # - Somatório do total de dados duplicados 
print(df.duplicated().sum()) # - Apresenta o total dos dados duplicados
print(df.nunique()) # - apresenta os dados não únicos

#Análise estatística
print(df.describe()) # - apresenta tabela de estatistica geral sobre o df 


#Corrigir o formato da data 
df['data'] = pd.to_datetime(df['data'])
print (df)

#Excluindo dados sensiveis
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df)

#Criando df preparado
df.to_csv('cliente-v2_preparado.csv', index=False)