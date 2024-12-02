import joblib
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
#print('\n', df)

# necessario verificar antes se existe valores nulos
# caso tenha valores nulos; tratar antes de aplicar os modelo
print('\n', df.isnull().sum().sum(), '\n')

# carregar modelos treinados 
modelo_regressao_linear = joblib.load('modelo_regressao_linear.pkl')
modelo_regressao_logistica = joblib.load('modelo_regressao_logistica.pkl')
modelo_arvore_decisao = joblib.load('modelo_arvore_decisao.pkl')

# aplicando nos dados de um novo funcionário
dados_novos_funcionarios = pd.DataFrame({
    'idade': [35, 45, 30],
    'anos_experiencia': [6, 12, 5],
    'nivel_educacao_cod': [2, 3, 4], # Ensino Médio, Ensino Superior, Pós-graduação
    'area_atuacao_cod': [1, 4, 3] # Educação, Tecnologia, Saúde
})

# Aplicando o modelo treinado de regressao linear
print('Por regressão linear')
salario_previsto = modelo_regressao_linear.predict(dados_novos_funcionarios)
# Garantir que o array de saída seja 1D
salario_previsto = salario_previsto.flatten()  # Caso seja um array 2D, transforma em 1D
# Iterar e exibir os valores formatados
for idx, salario in enumerate(salario_previsto):
    print(f"Salário previsto do {idx + 1} funcionário: R$ {float(salario):,.2f}")

# Aplicando o modelo treinado de classificação - regressão logística
print('Por regressão logística')
categoria_salario1 = modelo_regressao_logistica.predict(dados_novos_funcionarios)
# Garantir que o array de saída seja 1D
categoria_salario1 = categoria_salario1.flatten()  # Caso seja um array 2D, transforma em 1D
# Iterar e exibir os valores formatados
for idx, salario in enumerate(categoria_salario1):
    categoria = 'acima da mediana' if categoria_salario1[idx] == 1 else 'abaixo da mediana'
    print(f"Categoria Prevista do {idx + 1} funcionário: {categoria}")

# Aplicando o modelo treinado de clawssificação - árvore de decisão
print('Por árvore de decisão')
categoria_salario2 = modelo_arvore_decisao.predict(dados_novos_funcionarios)
# Garantir que o array de saída seja 1D
categoria_salario2 = categoria_salario2.flatten()  # Caso seja um array 2D, transforma em 1D
for idx, salario in enumerate(categoria_salario2):
    categoria = 'acima da mediana' if categoria_salario2[idx] == 1 else 'abaixo da mediana'
    print(f"Categoria Prevista do {idx + 1} funcionário: {categoria} e salário: R$ {float(salario):,.2f}")