from dash import Dash, html, dcc
import plotly.express as px
from plotly.graph_objs.table import header

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
def layout():
    return html.Div([
        html.Div([])
    ])
def generate_table(df, max_rows=10):
    return html.Table
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
app.layout = html.Div([
    html.H4(children='Souls Foods Sales'),
])


