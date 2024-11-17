#Criação de Features (Variaveis) - permite utilizar o campo criado para realizar análise
import pandas as pd
import numpy as np
from scipy import stats 
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.colheader_justify', 'left')

df = pd.read_csv('cliente_v2_preparado.csv')

# Transformação Logarítmica (bom para valores discrepantes pois traz mais uniforme.)
df['salario_log'] = np.log1p(df['salario']) # O Log1p é usado para evitar problemas com valores zero

# Transformacao Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1) # O '+ 1' é para evitar eventuais valores negativos

# Codificação a frequencia para 'estado' que numera de acordo com o numero de repetição (permite criar prioridade)
estado_frequencia = df['estado'].value_counts() /len(df)
df['estado_frequencia'] = df ['estado'].map(estado_frequencia) # resultado em porcentual em decimal 
df['estado_frequencia'] = (df ['estado'].map(estado_frequencia)) * 100 #resultado em percentual corrigido

# Interação
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print (df)
