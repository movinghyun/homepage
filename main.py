import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

color = {
    "main": "#C9C8BF",
    "modify": "#1B2B3C",
    "accent": "#C09B64"
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])
server = app.server

header = html.Div([
    html.Div([], className='col-2'),
    html.Div([
        html.H1(children="Dong-Hyun's Homepage",
                style={'textAlign': 'center', "color": color["modify"]}
                )], className='col-8', style={'padding-top': '1%'}
    ),
    html.Div([
        html.Img(
            src=app.get_asset_url('logo_.png'),
            height='43 px',
            width='auto')
    ],
        className='col-2',
        style={
            'align-items': 'center',
            'padding-top': '1%',
            'height': 'auto'})
],
    className='row',
    style={'height': '4%',
           'background-color': color["main"]}
)

navbar_sales = html.Div([
    html.Div([], className='col-3'),
    html.Div([
        dcc.Link(
            html.H4(children='Home', style={'textAlign': 'center', "color": color["main"]}),
            href='/'
        )
    ],
        className='col-2'),
    html.Div([
        dcc.Link(
            html.H4(children='Portfolio', style={'textAlign': 'center', "color": color["main"]}),
            href='/portfolio'
        )
    ],
        className='col-2'),
    html.Div([
        dcc.Link(
            html.H4(children='About Me', style={'textAlign': 'center', "color": color["main"]}),
            href='/about'
        )
    ],
        className='col-2'),
    html.Div([], className='col-3')
],
    className='row',
    style={'background-color': color["modify"],
           'box-shadow': f'2px 5px 5px 1px {color["accent"]}'}
)

