import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids
from src.data.loader import Dataschema
from src.data.loader import load_transaction_data


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_years = data[Dataschema.YEAR].tolist()
    unique_years = sorted(set(all_years), key=int)

    @app.callback(
        Output(ids.YEARS_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks")
    )
    def select_all_years(_: int) -> list[str]:
        return unique_years

    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEARS_DROPDOWN,
                options=[{"label": year, "value": year} for year in unique_years],
                value=unique_years,
                multi=True
            ),
            html.Button(
                id=ids.SELECT_ALL_YEARS_BUTTON,
                className="dropdown-button",
                children=["Select All"],
                n_clicks=0
            )
        ]
    )
