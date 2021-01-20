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

footer = dbc.Row([
    dbc.Col(html.A([
        html.Img(
            src=app.get_asset_url('notion_.png'),
            style={"max-width": "100%", 'height': "auto"}
        )
    ], href='https://www.notion.so/movinghyun/6a1bb55359e948a09ce24ee474ad6cd0?v=8a9a4c44d9c84232b440cb29da29b555', target='_blank'), width='auto'),
    dbc.Col(html.A([
        html.Img(
            src=app.get_asset_url('GitHub_.png'),
            style={"max-width": "100%", 'height':"auto"}
        )
    ], href='https://github.com/movinghyun', target='_blank'), width='auto'),
    dbc.Col(html.A([
        html.Img(
            src=app.get_asset_url('linkedin_.png'),
            style={"max-width": "100%", 'height':"auto"}
        )
    ], href='https://www.linkedin.com/in/movinghyun', target='_blank'),  width='auto'),
    dbc.Col(html.A([
        html.Img(
            src=app.get_asset_url('youtube_.png'),
            style={"max-width": "100%", 'height': "auto"}
        )
    ], href='https://www.youtube.com/channel/UCDtjhl3QW1IEtf0TQr9i4mQ', target='_blank'),  width='auto'),
    dbc.Col([], md=2)
], justify="end", style={
    "padding": "1%", 'align-items': 'center', 'color': '#C9C8BF'
})