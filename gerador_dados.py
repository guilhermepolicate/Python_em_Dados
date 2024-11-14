#GERADORO DE DADOS FAKE PARA TREINO#
from faker import Faker
import pandas as pd
import random

faker = Faker('pt_BR')

dados_pessoas = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%y")
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'
    pessoa = {
        'nome' : nome,
        'cpf' : cpf,
        'idade' : idade,
        'data' : data,
        'endereco' : endereco,
        'estado' : estado,
        'pais' : pais
    }

    dados_pessoas.append(pessoa)
df_pessoas = pd.DataFrame(dados_pessoas)
print(df_pessoas)

#POSSIBILIDADE DE FORMATACAO 1# 
pd.set_option('display.max_colwidth', None)    # Mostra o maximo da largura de coluna 
pd.set_option('display.max_rows', None)        # Mostra todas as linhas
pd.set_option('display.max_columns', None)     # Mostra todas as colunas
pd.set_option('display.width', None)           # Expande a largura para mostrar todas as colunas no console(display)
pd.set_option('display.colheader_justify', 'left')  # Justifica à esquerda o cabeçalho da coluna

#POSSIBILIDADE DE FORMATACAO ALTOMATICA 2
#print(df_pessoas.to_string()) # head() taiL()

df_pessoas.to_excel('clientes3.xlsx')