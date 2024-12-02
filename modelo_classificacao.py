import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score

df = pd.read_csv('clientes-v3-preparado.csv')
#print(df)

# Categorizar Salário: 1 = acima ou 0 = igual ou abaixo da media 
df['salario_categoria'] = (df['salario'] > df['salario'].median()).astype(int)
print (df['salario_categoria'])

# x = df[['anos_experiencia']] # preditor (variavel independente)
# devemos usar o maximo de campos possiveis
x = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']]  # preditor (variavel independente)
y = df[['salario_categoria']] # prever (variavel dependente)

# 1 - dividir os dados para treinamento e teste (20% para teste e 80 % para treino / salva em 42)
# o numero randomico sempre deve ser derterminado para manter um padrao
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# 2.A - criando o modelo de regressão logística
modelo_lr = LogisticRegression() 
# 3.A - treinando o modelo de regressão logística 
modelo_lr.fit(x_train, y_train)
# 4.A - prever os valores de teste 
y_prev_lr = modelo_lr.predict(x_test)
# 5.A - métricas de avaliação de performance de regressão logística
accuracy_lr = accuracy_score(y_test, y_prev_lr)
precision_lr = precision_score(y_test, y_prev_lr)
recall_lr = recall_score(y_test, y_prev_lr)
# 6.A - imprimindo as metricas de avaliação de regressão lpgística 
print (f'\nacurácia de regressão logística: {accuracy_lr:.2f}')
print (f'precisão de regressão logística: {precision_lr:.2f}')
print (f'sensibilidade de regressão logística: {recall_lr:.2f}')
# 7.A - salvando modelo treinado 
joblib.dump(modelo_lr, 'modelo_regressao_logistica.pkl')

# 2.B - criando modelo de árvore de decisão 
modelo_dt = DecisionTreeClassifier() 
# 3.B - treinando modelo de árvode de decisão 
modelo_dt.fit(x_train, y_train)
# 4.B prever os valores de teste 
y_prev_dt = modelo_dt.predict(x_test)
# 5.A - métricas de avaliação de performance da árvore de decisão 
accuracy_dt = accuracy_score(y_test, y_prev_dt)
precision_dt = precision_score(y_test, y_prev_dt)
recall_dt = recall_score(y_test, y_prev_dt)
# 6.A - imprimindo as metricas de avaliação de árvore de decisão 
print (f'\nacurácia de árvore de decisão: {accuracy_dt:.2f}')
print (f'precisão de árvore de decisão: {precision_dt:.2f}')
print (f'sensibilidade de árvore de decisão: {recall_dt:.2f}')
# 7.B - salvando modelo treinado 
joblib.dump(modelo_dt, 'modelo_arvore_decisao.pkl')