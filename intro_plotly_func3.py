import pandas as pd 
import plotly.express as px
from dash import Dash, html, dcc

#print(df)

def cria_grafico(df):
    
    # Gráfico Histograma
    fig1=px.histogram(df, x='salario', nbins=30, title='Distribuição de Salário')

    # Gráfico de Pizza 
    fig2 = px.pie(df, names='area_atuacao', color='area_atuacao', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)

    # Gráfico de Bolhas
    fig3=px.scatter(df, x='idade', y='salario', size='anos_experiencia', color='area_atuacao', hover_name='estado', size_max=60)
    # hover_name = permite colocar lista de informações a serem mostradas com o mouse sobre o ponto, co caso o estado
    fig3.update_layout(title='Salário por idade e anos de experiência')

    # Gráfico de Linhas 
    fig4=px.line(df, x='idade', y='salario', color='area_atuacao', facet_col='nivel_educacao')
    # divide pelas colunas do nivel de educação
    fig4.update_layout(
        title='Dalário por idade e area de atuação para cada nível de educação',
        xaxis_title='idade',
        yaxis_title='salario'
    )

    # Gráfico 3D
    fig5=px.scatter_3d(df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')

    # Gráfico de Barras
    fig6=px.bar(df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group', color_discrete_sequence=px.colors.qualitative.Set1)
    # Barmode = separa as barras em grupos
    fig6.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='rgba(222, 255, 253, 1)', # Fundo Interno 
        paper_bgcolor='rgba(186, 245, 241, 1)' # Fundo Externo
    )
    return fig1, fig2,fig3, fig4, fig5, fig6

def cria_app(df):
    # Criar App
    app = Dash(__name__)

    fig1, fig2,fig3, fig4, fig5, fig6 = cria_grafico(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)    
    ])
    return app

df = pd.read_csv('clientes-v3-preparado.csv')

if __name__ == '__main__':
    app = cria_app(df)
    # Execurtar App
    app.run_server(debug=True, port=8051) # Defaul 8051