import pandas as pd
from scipy import stats
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.colheader_justify', 'rigth')

df = pd.read_csv('cliente_padrao.csv')

#mascarando dados do CPF em outra coluna
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***{cpf[-2:]}' if pd.notnull(cpf) else '')
#mascarando dados do CPF na mesma coluna
df['cpf'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***{cpf[-2:]}' if pd.notnull(cpf) else '')

#corrigindo cpf nulo se tiver menos que 14 digitos
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'cpf invalido')

#corrigindo datas
df['data'] = pd.to_datetime(df['data'], format='%Y/%m/%d', errors='coerce')

#corrigindo e atualizando datas 
data_atual = pd.to_datetime('today')
df['data'] = pd.to_datetime(df['data'], errors='coerce')

#corrigindo as datas erradas para um data especifica
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1990-01-01'))
#corrigindo as datas erradas para campo nulo
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.NaT)

#atualizar a data (se o mês fo posterio ao atualizado e necessario subitari 1 do ano)
df['idade_ajustada'] = data_atual.yaer - df['data_atualizada'].dt.year

#para verificar a necessidade desse ajuste 
df['idade_ajustada'] = ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)

#substituindo as idades ajustadas que estao fora do padrao por nulo 
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

#verificando o formato do endereço
df['endereco'] = df['endereco'].apply(lambda x: 'invalido' if len(x) > 50 or len(x) < 3 else x)

#corrigindo o endereço
df['endereco'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip() if isinstance(x, str) else '')
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'desconhecido')
df['estado'] = df['endereco'].apply(lambda x: x.split('\n')[-1].strip() if len(x.split('\n')) > 1 else 'desconhecido')

#verificando o formato do endereço
df['endereco'] = df['endereco'].apply(lambda x: 'invalido' if len(x) > 50 or len(x) < 3 else x)

#corrigindo a sigla dos estados 
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 
        'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estado'] = df['estado'].str.upper().apply(lambda x: x if x in estados else 'desconhecido')

print(df)