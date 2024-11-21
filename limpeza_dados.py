import pandas as pd
import numpy as np

#chamando o arquivo
df = pd.read_csv('clientes3.csv')

#mostra a coluna inteira 
pd.set_option('display.width', None)

#mostra o df
#print(df)

#Etapa 1 - remover itens desnecessarios
df.drop('pais', axis=1, inplace=True) # axis = 1 = COLUNA
df.drop(2, axis=0, inplace=True) # axis = 0 = COLUNA

#Etapa 2 - normalizando os campos
df['nome'] = df['nome'].str.title() #Primeira letra de cada palavra maiuscula
df['endereco'] = df['endereco'].str.lower() #Todas as letras em minusculo
df['estado'] = df['estado'].str.upper() #Todas as letras em MAIUSCULO

#Etapa 3 - converter os tipos de dados
df['idade'] = df['idade'].astype(int)

#Etapa 4 - primeira verificação 
print(df)
print(df.info())

#Etapa 5 - verificar quais campos tem valores nulos
print(df.isnull().sum())

#OBS - TECNICAS DE PARA AJUSTE DE VALORES NULOS
df['cpf'] = df['cpf'].replace(['', ' ', 'None'], np.nan)#conver valores vazios para 'NaN'
print(df)

#df_fillna = df.fillna(0) #Substitui todos os campos nulos pelo valor que esta dentro do parenteses
print ('qtd registros nulos com fillna: ', df_fillna.isnull().sum().sum())

df_dropna = df.dropna() #Remove todos os registros que tenham algum valor nulo 
print ('qtd registros nulos com dropna: ', df_dropna.isnull().sum().sum())

df_dropna4 = df.dropna(thresh=4) #Remove os registro que tenham no minimo 'x' registros NÃO nulos
print ('qtd registros nulos com dropna4: ', df_dropna4.isnull().sum().sum())

df = df.dropna (subset=['cpf']) #Util quando se tem um registro chave removendo as linhas que tal campo é nulo
print ('qtd registros nulos com cpf: ', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True) #Substitui o campo especificado pelo valor desejado
print ('qtd registros nulos com fillna: ', df.isnull().sum().sum())

df['endereco'] = df['endereco'].fillna('Endereço não encontrado')#Substitui o campo especificado pelo valor desejado
print ('qtd registros nulos com fillna: ', df.isnull().sum().sum())

df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean)#Subistitui o campo desejado pela media dos demais
print ('qtd registros nulos com fillna: ', df.isnull().sum().sum())

df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') #corrige data para o padrao
print(df)

#Etapa 6 - trata dados duplicados
df.drop_duplicates # remove todos os campos duplicados
df.drop_duplicates(subset='cpf', inplace=True) # remove os campos especificamente duplicados
print(df.shape) # verificar quanto registros tem de LINHAS E  COLUNA

#Etapa 7 - Segunda verificação 
print(df)
print(df.info())

#Etapa 8 - Salvando as 
df['data'] = df['data_corrigida']
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('cliente_limpeza.csv', index=False)
print('Novo DataFrame: \n', pd.read_csv('cliente_limpeza.csv'))

