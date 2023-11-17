import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# app = dash.Dash(__name__)

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY],
                requests_pathname_prefix='/dashboard2/'
                )

app.layout = html.Div(children=[

    html.Div(className='main', children=[
        html.Div(
            className='bg-primary',
            id='sidebar',
            children=[
                html.H3(children='Sidebar'),
                html.Div(children=[html.A('dashboard1', href='/dashboard1')]),
                html.Div(children=[html.A('dashboard2', href='/dashboard2')]),
                ]
            ),
        html.H2(children='Hello Dash 2'),
        # html.Div(children='''
        #     Dash: ウェブアプリケーションのフレームワーク
        # '''),
    ])



    # グラフやコンポーネントを追加することもできます
])

# サーバーを起動
if __name__ == '__main__':
    app.run_server(debug=True)
