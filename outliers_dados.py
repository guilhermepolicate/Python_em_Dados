import pandas as pd
from scipy import stats

df = pd.read_csv('cliente_limpeza.csv')
#print(df)

# 1 - filtro booleano básico
df_filtro_basico = df[(df['idade']>100) | (df['idade']<0)]
print(df_filtro_basico[['nome', 'idade']])

#2 - identificando outliers com Zscore (desvio padrão)
z_score = stats.zscore(df['idade'].dropna())#O '.dropna' no final remove os valores nulos
outliers = df[z_score >= 3] #criando variavel para print
print(outliers)

#aplicando outliers com Zcore (desvio padrão)
df_zscore = [(stats.zscore(df['idade'])< 1)]

#3 - identificando outliers com IQR
q1 = df['idade'].quantile(0.25)
q3 = df['idade'].quantile(0.56)
iqr = q3 - q1

#defini o limite_baixo = q1 - 1.5 * iqr
#defini o limite_alto = q3 + 1.5 * iqr

print(limite_alto, limite_baixo)

#aplicando o IQR e mostrando os outliers
outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade']> limite_alto)]
print (outliers_iqr)

#aplicando o IQR e mostrando que esta dentro do ideal
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]
print (df_iqr)

#4 - filtro manual 
limite_alto = 100
limite_baixo = 1 

#mostrando os outliers
outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade']> limite_alto)]
print (outliers_iqr)

#mostrando quem esta dentro da media
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]
print (df)

#filtrando endereco invalido
df['endereco'] = df['endereco'].apply(lambda x: 'endereço invalido' if not isinstance(x, str) or len(x.split('\n')) < 3 else x)
print('estão fora do padrão: ', (df['endereco'] == 'endereço invalido').sum())

#Tratar compos de texte 
df['nome'] = df['nome'].apply(lambda x: 'nome invalido' if not isinstance(x, str) or len(x) > 50 else x)
print('estão fora do padrão: ', (df['nome'] == 'nome invalido').sum())

print (df)

#salvando df alterado e corrigido
df.to_csv('cliente_padrao.csv', index = False)
print (df)