import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids
from src.data.loader import Dataschema
from src.data.loader import load_transaction_data


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_categories = data[Dataschema.CATEGORY].tolist()
    unique_categories = sorted(set(all_categories), key=str)

    @app.callback(
        Output(ids.CATEGORIES_DROPDOWN, "value"),
        [
            Input(ids.YEARS_DROPDOWN, "value"),
            Input(ids.MONTHS_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks")
        ]
    )
    def select_all_categories(years: list[str], months: list[str], _: int) -> list[str]:
        filtered_data = data.query("year in @years and month in @months")
        return sorted(set(filtered_data[Dataschema.CATEGORY].tolist()))

    return html.Div(
        children=[
            html.H6("category"),
            dcc.Dropdown(
                id=ids.CATEGORIES_DROPDOWN,
                options=[{"label": category, "value": category} for category in unique_categories],
                value=unique_categories,
                multi=True
            ),
            html.Button(
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                className="dropdown-button",
                children=["Select All"],
                n_clicks=0
            )
        ]
    )
