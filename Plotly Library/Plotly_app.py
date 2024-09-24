import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import yfinance as yf

# Baixar dados
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')
data.reset_index(inplace=True)

# Inicializar o app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(f'Análise Financeira: {ticker}'),
    dcc.Graph(id='grafico-precos',
              figure={
                  'data': [
                      go.Scatter(x=data['Date'],
                                 y=data['Close'],
                                 mode='lines',
                                 name='Preço de Fechamento')
                  ],
                  'layout':
                  go.Layout(
                      title='Preço de Fechamento ao Longo do Tempo',
                      xaxis={'title': 'Data'},
                      yaxis={'title': 'Preço (USD)'},
                  )
              }),
    dcc.Graph(id='grafico-volume',
              figure={
                  'data': [
                      go.Bar(x=data['Date'],
                             y=data['Volume'],
                             name='Volume de Negócios')
                  ],
                  'layout':
                  go.Layout(
                      title='Volume de Negócios ao Longo do Tempo',
                      xaxis={'title': 'Data'},
                      yaxis={'title': 'Volume'},
                  )
              })
])

if __name__ == '__main__':
    app.run_server(debug=True)
