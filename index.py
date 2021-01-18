import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from main import app, header, navbar_sales, server
from pages import resource, home
from pages.portfolio import portfolio

content = html.Div(id="page-content")


app.layout = html.Div(
        [
            dcc.Location(id="url"),
            header,
            navbar_sales,
            content,
        ],
        style={'padding-top': '1%', "background-color": "#1B2B3C",}
    )


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.create_layout()
    elif pathname == "/portfolio":
        return portfolio.create_layout()
    elif pathname == "/resource":
        return resource.create_layout()
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=False)