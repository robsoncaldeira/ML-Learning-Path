# pages /analytics.py
from dash import html, dcc

layout = html.Div([
    html.H1('Análise Financeira de Tickers'),
    dcc.Input(id='ticker-input', value='AAPL', type='text'),
    dcc.Graph(id='grafico-precos'),
    dcc.Graph(id='grafico-volume')
])
