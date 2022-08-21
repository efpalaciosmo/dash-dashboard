import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids
from src.data.loader import Dataschema
from src.data.loader import load_transaction_data


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_months = data[Dataschema.MONTH].tolist()
    unique_months = sorted(set(all_months), key=int)

    @app.callback(
        Output(ids.MONTHS_DROPDOWN, "value"),
        [
            Input(ids.YEARS_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks")
        ]
    )
    def select_all_months(years: list[str], _: int) -> list[str]:
        filtered_data = data.query("year in @years")
        return sorted(set(filtered_data[Dataschema.MONTH].tolist()))

    return html.Div(
        children=[
            html.H6("month"),
            dcc.Dropdown(
                id=ids.MONTHS_DROPDOWN,
                options=[{"label": month, "value": month} for month in unique_months],
                value=unique_months,
                multi=True
            ),
            html.Button(
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                className="dropdown-button",
                children=["Select All"],
                n_clicks=0
            )
        ]
    )
