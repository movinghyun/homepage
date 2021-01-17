import pathlib

import dash_core_components as dcc
import dash_html_components as html
import dash_interactive_graphviz
import pandas as pd
from dash.dependencies import Input, Output

from main import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()

a = pd.read_csv(DATA_PATH / "a.csv")


def create_layout():
    return html.Div([
        html.Div([
            html.Div([], className="col-3"),
            html.Div(
                dcc.Dropdown(
                    id='a',
                    options=[{'label': i, 'value': i} for i in a.iloc[:, 0].unique()],
                ), className='col-3'
            ),
            html.Div(id='my-output', className='col-3'),
            html.Div([], className="col-3"),
        ], className="row"),
        html.Br(),
        html.Div([
            html.Div([], className='col-3'),
            html.Div(id='b', className='col-6'),
            html.Div([], className='col-3'),
        ], className='row')

    ], style={'align-items': 'center',
              'padding-top': '1%',
              'height': 'auto'})


@app.callback(
            Output(component_id='my-output', component_property='children'),
            [Input(component_id='a', component_property='value')]
        )
def update_output_div(input_value):
    return dcc.Dropdown(
        id='c',
        options=[{'label': i, 'value': i} for i in a[a.iloc[:, 0] == input_value].iloc[:, 1]],
    )


@app.callback(
            Output(component_id='b', component_property='children'),
            [Input(component_id='c', component_property='value')]
        )
def update_output_divi(asdf):
    b = a[a.iloc[:, 1] == asdf]['1'].values[0]
    c = f"digraph {b}"

    return dash_interactive_graphviz.DashInteractiveGraphviz(
    id="graph",
    dot_source=c, style={'display': 'inline-block', 'height': '600px'}
)

