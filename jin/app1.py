import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# app = dash.Dash(__name__)

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG],
                requests_pathname_prefix='/dashboard1/'
                )

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: ウェブアプリケーションのフレームワーク
    '''),

    # グラフやコンポーネントを追加することもできます
])

# サーバーを起動
if __name__ == '__main__':
    app.run_server(debug=True)
