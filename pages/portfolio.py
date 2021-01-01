import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import descriptor

from main import app


def create_layout():
    tabs = html.Div(
        [
            dbc.Tabs(
                [
                    dbc.Tab(label="Tab 1", tab_id="tab-1"),
                    dbc.Tab(label="Tab 2", tab_id="tab-2"),
                ],
                id="tabs",
                active_tab="tab-1",
            ),
            html.Div(id="content"),
        ], style={"padding-top": "1%"}
    )

    return tabs


tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return descriptor.create_layout()
    elif at == "tab-2":
        return tab2_content
    return html.P("This shouldn't ever be displayed...")