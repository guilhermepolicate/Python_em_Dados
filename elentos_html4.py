import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Carregar dados
df = pd.read_csv('clientes-v3-preparado.csv')
lista_nivel_educacao = df['nivel_educacao'].unique()
options = [{'label': nivel, 'value': nivel} for nivel in lista_nivel_educacao]

# Função para criar gráficos
def cria_grafico(df_filtrado):
    # Gráfico de Barras
    fig1 = px.bar(
        df_filtrado,
        x='estado_civil',
        y='salario',
        color='nivel_educacao',
        barmode='group',
        color_discrete_sequence=px.colors.qualitative.Blues
    )
    fig1.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='rgba(245, 245, 250, 1)',  # Fundo Interno
        paper_bgcolor='rgba(220, 230, 240, 1)'  # Fundo Externo
    )

    # Gráfico 3D
    fig2 = px.scatter_3d(
        df_filtrado,
        x='idade',
        y='salario',
        z='anos_experiencia',
        color='nivel_educacao',
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    fig2.update_layout(
        title='Salário vs Idade e Anos de Experiência',
        scene=dict(
            xaxis_title='Idade',
            yaxis_title='Salário',
            zaxis_title='Anos de Experiência'
        ),
        paper_bgcolor='rgba(220, 230, 240, 1)',
    )
    return fig1, fig2

# Função para criar o aplicativo
def cria_app(df):
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dash Board Interativo'),
        html.Div('Interatividade entre os dados'),
        html.Br(),  # Pular linha
        html.H2('Gráfico de Salário por Estado Civil'),
        dcc.Checklist(
            id='id_selecao_nivel_educacao',
            options=options,
            value=[lista_nivel_educacao[0]],  # Valor padrão
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d')
    ])

    # Callback para atualizar os gráficos
    @app.callback(
        [Output('id_grafico_barra', 'figure'),
         Output('id_grafico_3d', 'figure')],
        [Input('id_selecao_nivel_educacao', 'value')]
    )
    def atualiza_graficos(selecao_niveis):
        df_filtrado = df[df['nivel_educacao'].isin(selecao_niveis)]
        return cria_grafico(df_filtrado)

    return app

# Executar o aplicativo
if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)