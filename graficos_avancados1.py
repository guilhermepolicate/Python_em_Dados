import pandas as pd 
import plotly.express as px

df = pd.read_csv('clientes-v3-preparado.csv')

print(df)

#grafico de Dispersão
fig =px.scatter(df, x='idade', y='salario', color='nivel_educacao', hover_data=['estado_civil']) 
# hover_data = permite colocar lista de informações a serem mostradas com o mouse sobre o ponto 
# color = legenda de cores baseada no nivel educacional

# atualizar o layout tem varias possibilidades 
fig.update_layout(
    title = 'Idade vs Salário par Nivel de Educação',
    xaxis_title = 'Idade',
    yaxis_title = 'Salário'
)
fig.show(renderer="browser")