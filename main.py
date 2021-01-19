import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

color = {
    "main": "#C9C8BF",
    "modify": "#1B2B3C",
    "accent": "#C09B64"
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])
app.title = "Dong-Hyun's Homepage"
server = app.server


header = dbc.Row(
    [
        dbc.Col([],
            #html.Img(
            #    src=app.get_asset_url('logo_transparent.png'),
            #    height='auto',
            #    width='50 px'
            #),
        md=3, style={
                'align-items': 'center',
                'padding-top': '1%',
                'height': 'auto'}
        ),
        dbc.Col(
            html.H1(
                children="Dong-Hyun's Homepage",
                style={'textAlign': 'center', "color": color["modify"]}
            ), md=6, style={'padding-top': '1%'}
        ),
        dbc.Col(
            [], md=3
        )
    ], style={'height': '4%',
              'background-color': color["main"]}
)

navbar_sales = dbc.Row(
    [
        dbc.Col(
            [], md=3
        ),
        dbc.Col(
            dcc.Link(
                html.H4(children='Home', style={'textAlign': 'center', "color": color["main"]}),
                href='/'
            ), md=2
        ),
        dbc.Col(
            dcc.Link(
                html.H4(children='Portfolio', style={'textAlign': 'center', "color": color["main"]}),
                href='/portfolio'
            ), md=2
        ),
        dbc.Col(
            dcc.Link(
                html.H4(children='Resource', style={'textAlign': 'center', "color": color["main"]}),
                href='/resource'
            ), md=2
        ),
        dbc.Col(
            [], md=3
        ),
    ], style={
        'background-color': color["modify"],
        'box-shadow': f'2px 5px 5px 1px {color["accent"]}'
    }
)
