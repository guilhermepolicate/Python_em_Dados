import joblib
import pandas as pd 
from math import sqrt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('clientes-v3-preparado.csv')
#print (df)

# x = df[['anos_experiencia']] # preditor (variavel independente)
# devemos usar o maximo de campos possiveis
x = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']]  # preditor (variavel independente)
y = df[['salario']] # prever (variavel dependente)

# 1 - dividir os dados para treinamento e teste (20% para teste e 80 % para treino / salva em 42)
# o numero randomico sempre deve ser derterminado para manter um padrao
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# 2 - criando o modelo de regressão linear 
modelo_lr = LinearRegression() 

# 3 - treinando o modelo 
modelo_lr.fit(x_train, y_train)

# 4 - prever os valores de teste 
y_prev = modelo_lr.predict(x_test)

# 5 - métricas de avaliação de performance para modelo de regressão linear 
r2 = r2_score(y_test, y_prev) # test = dados // # prev = obtido no teste
print(f'coeficiente de determinação - R**2: {r2:.2f}') # mínimo de 55% considerar usar

rmse = sqrt(mean_squared_error(y_test, y_prev))
print(f'Raiz do Erro Quadrático Médio -RMSE: {rmse:.2f}') # não pode estar muito perto do desvio padrão
print(f'Desvio Padrão do Campo Salário: {df['salario'].std()}') # desvio padrao

# 6 - Salvando Modelo Treinado
joblib.dump(modelo_lr, 'modelo_regressao_linear.pkl')