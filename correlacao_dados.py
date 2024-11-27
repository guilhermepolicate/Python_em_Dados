import numpy as np
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

print(df)

# Estatistica com PANDAS

print(df.describe()) # faz a estatidtica descritiva os dados
# ou
print(df[['salario', 'idade']].describe()) # faz a estatistica so das colunas selecionadas

# Correlação de dados numéricos
print(df[['salario', 'idade']].corr())

# Correlação de dados normalizados e padronizados
print('correlacao com normalizacao', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('correlacao com padronizacao', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('correlacao com padronizacao', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

# Exemplo Prático 
df_idade_ativo = df[df['idade'] < 60]
print('clientes menores de 60', df_idade_ativo[['salario', 'idade']].corr())

# Variavel Espúria - Varia de acordo com o tempo 
df['variavel_espúria'] = np.arange(len(df))
print('variavel_espúria', df['variavel_espúria'].values)

pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod','area_atuacao_cod', 'estado_cod']].corr()
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod','area_atuacao_cod', 'estado_cod']].corr()

print (pearson_corr)
print (spearman_corr)


