import plotly.express as px
import pathlib
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_interactive_graphviz
import pandas as pd
from dash.dependencies import Input, Output

from main import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()

a = pd.read_csv(DATA_PATH / "treemap.csv", index_col=0)


def create_layout():
    fig = px.treemap(a, path=['industry', "company"], values='mkt_cap', color="return", color_continuous_scale="RdBu")
    fig.update_layout(height=800, title="2021-01-28")
    return html.Div([
        dcc.Graph(figure=fig)
    ])



"""from pathlib import Path
BASE_DIR = Path(r"G:\공유 드라이브\research_data\dataguide")


import pandas as pd
mkt_cap = pd.read_csv(BASE_DIR / "company" / "mkt_cap" / "data.csv", index_col=0, parse_dates=True)
industry = pd.read_csv(BASE_DIR / "company" / "industry" / "data.csv", index_col=0, parse_dates=True)
rtn = pd.read_csv(BASE_DIR / "price_volume" / "price_close" / "data.csv", index_col=0, parse_dates=True)
rtn = rtn.pct_change(fill_method=None)


a = pd.concat([
    mkt_cap.iloc[-2], industry.iloc[-2], rtn.iloc[-2]
    ], axis=1).dropna().reset_index()


a.columns = ("company", "mkt_cap", "industry", "return")

a = a.loc[a.groupby("industry")["mkt_cap"].nlargest().index.get_level_values(level=1)]
a.to_csv("treemap.csv")"""