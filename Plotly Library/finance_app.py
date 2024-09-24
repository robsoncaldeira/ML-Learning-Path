from logging import getLogger
from pathlib import Path

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from pages.archive import create_archive_layout

# Criar um objeto de caminho
path = Path("/user/home/myfile.txt")

# Verificar se o arquivo existe
print(path.exists())

# Verificar se é um arquivo
print(path.is_file())

# Obter o diretório pai
print(path.parent)

# Juntar um novo caminho
new_path = path / "newfile.txt"
print(new_path)

# Inicializar o app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do aplicativo
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dbc.NavbarSimple(
            brand="Análise de Tickers",
            brand_href="/",
            color="primary",
            dark=True,
        ),
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Analytics", href="/analytics")),
        dbc.NavItem(dbc.NavLink("Archive", href="/archive")),
    ]
)


# Callback para renderizar as páginas
# Callback para renderizar as páginas
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/analytics":
        from pages.analytics import layout

        return layout
    elif pathname == "/archive":
        return create_archive_layout(app)  # Chame a função para obter o layout
    else:
        from pages.home import layout

        return layout


if __name__ == "__main__":
    app.run_server(debug=True)
