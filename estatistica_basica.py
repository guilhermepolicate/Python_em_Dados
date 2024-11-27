import numpy as np
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

print(df)

# Estatistica com PANDAS

print('média', df['salario'].mean())
print('mediana', df['salario'].median())
print('variância', df['salario'].var())
print('desv.pad', df['salario'].std())
print('moda', df['salario'].mode()[0])
print('minimo', df['salario'].min())
print('quartis', df['salario'].quantile([0, 0.25, 0.5, 0.75, 1]))
print('máximo', df['salario'].max())
print('cont_valor_não_nulos', df['salario'].value_counts().sum())
print('soma', df['salario'].sum())

# Estrutura de Dados
print('coluna', df['salario'])
print('array do campo', df['salario'].values)# O '.values'transforma em array

# Estatística com NUMPY
print('Média com coluna', np.mean(df['salario']))
print('Média com Array', np.mean(df['salario'].values))
#ou
array_campo = df['salario'].values
print('média', np.mean(array_campo))
print('mediana', np.median(array_campo))
print('variancia', np.var(array_campo))
print('desv.pad', np.std(array_campo))
print('minimo', np.min(array_campo))
print('quartis', np.quantile(array_campo,[0.25, 0.5, 0.75]))
print('porcentagem', np.percentile(array_campo,[25, 50, 75]))
print('máximo', np.max(array_campo))
print('cont_valor_nao_nulo', np.count_nonzero(array_campo))
print('soms', np.sum(array_campo))