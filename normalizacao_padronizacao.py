import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.colheader_justify', 'left')

df = pd.read_csv('cliente_v2_preparado.csv')

df = df.drop(['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)
# ou 
#df = df[['idade', 'salario']]

# - METODOS DE NORMALIZAÇÃO
# - MinMaxScaler (normaliza todos entre '0' e '1') - (so muda a escala)
scaler = MinMaxScaler()
df ['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df ['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])


# - MinMaxScaler (normaliza todos por criterios proprios) - (so muda a escala)
scaler = MinMaxScaler(feature_range=(-1, 1))
df ['idadeMinMaxScaler_mm'] = scaler.fit_transform(df[['idade']])
df ['salarioMinMaxScaler_mm'] = scaler.fit_transform(df[['salario']])

# - METODO DE PADRONIZAÇÃO
# - Padronização - StandardScaler (muda a escala e o padrao dos dados) - (média = 0 e desvio = 1) 
scaler = StandardScaler()
df ['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df ['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# - Padronização - RobustScaler (muda a escala e o padrao dos dados) - (medida e iqr)
# - Bom para valores discrepantes pois traz mais uniforme
scaler = RobustScaler()
df ['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df ['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print('MinMaxScaler (De 0 a 1):')
print('idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print('\nMinMaxScaler (De -1 a 1):')
print('idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler_mm'].min(), df['idadeMinMaxScaler_mm'].max(), df['idadeMinMaxScaler_mm'].mean(), df['idadeMinMaxScaler_mm'].std()))
print('salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler_mm'].min(), df['salarioMinMaxScaler_mm'].max(), df['salarioMinMaxScaler_mm'].mean(), df['salarioMinMaxScaler_mm'].std()))

print('\nStandardScaler( media = 0 e desvio = 1):')
print('idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}'.format(df['idadeStandardScaler'].min(), df['idadeStandardScaler'].max(), df['idadeStandardScaler'].mean(), df['idadeStandardScaler'].std()))
print('salario - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}'.format(df['salarioStandardScaler'].min(), df['salarioStandardScaler'].max(), df['salarioStandardScaler'].mean(), df['salarioStandardScaler'].std()))

print('\nRobustScaler( mediana e iqr - ignora outliers):')
print('idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeRobustScaler'].min(), df['idadeRobustScaler'].max(), df['idadeRobustScaler'].mean(), df['idadeRobustScaler'].std()))
print('salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['salarioRobustScaler'].min(), df['salarioRobustScaler'].max(), df['salarioRobustScaler'].mean(), df['salarioRobustScaler'].std()))





