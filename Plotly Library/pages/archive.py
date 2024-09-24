from dash import dcc, html, Input, Output
import pandas as pd
import yfinance as yf
import dash.dash_table
def update_table(n_clicks, ticker, start_date, end_date):
    if n_clicks > 0:
        # Baixar dados
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        data.reset_index(inplace=True)
        return data.to_dict('records')  # Retorna os dados em formato de dicionário para a tabela
    return []  # Retorna vazio se n_clicks for 0

def create_archive_layout(app):
    # Layout da página de arquivo
    layout = html.Div([
        html.H1("Arquivo de Tickers"),
        html.P("Aqui você pode acessar dados históricos de tickers."),
        
        dcc.Input(id='ticker-input', value='AAPL', type='text', placeholder='Digite o ticker'),
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date='2020-01-01',
            end_date='2023-01-01',
            display_format='YYYY-MM-DD'
        ),
        html.Button('Baixar Dados', id='download-button', n_clicks=0),
        
        dash.dash_table.DataTable(
            id='data-table',
            columns=[{"name": "Data", "id": "Date"},
                     {"name": "Abertura", "id": "Open"},
                     {"name": "Máxima", "id": "High"},
                     {"name": "Mínima", "id": "Low"},
                     {"name": "Preço de Fechamento", "id": "Close"},
                     {"name": "Volume", "id": "Volume"}],
            data=[],
            page_size=10,
            style_cell={'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': 0},
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)',
                }
            ],
        )
    ])

    # Callback para baixar os dados e atualizar a tabela
    @app.callback(
        Output('data-table', 'data'),
        Input('download-button', 'n_clicks'),
        Input('ticker-input', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')
    )
    def update_table(n_clicks, ticker, start_date, end_date):
        if n_clicks > 0:
            # Baixar dados
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)
            data.reset_index(inplace=True)
            return data.to_dict('records')  # Retorna os dados em formato de dicionário para a tabela
        return []  # Retorna vazio se n_clicks for 0

    return layout
