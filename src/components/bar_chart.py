import pandas as pd
from dash import Dash, html,dcc
import plotly.express as px
from dash.dependencies import Input, Output
from . import ids
from src.data.loader import Dataschema


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.YEARS_DROPDOWN, "value"),
            Input(ids.MONTHS_DROPDOWN, "value"),
            Input(ids.CATEGORIES_DROPDOWN, "value")
        ]
    )
    def update_bar_chart(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        filtered_data = data.query("year in @years and month in @months and category in @categories")

        if filtered_data.shape[0] == 0:
            return html.Div(
                html.H3("No data selected")
            )

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=Dataschema.AMOUNT,
                index=Dataschema.CATEGORY,
                aggfunc="sum",
                fill_value=0
            )
            return pt.reset_index().sort_values(Dataschema.AMOUNT, ascending=False)

        pt = create_pivot_table()
        fig_yaar = px.bar(filtered_data, x=pt[Dataschema.CATEGORY], y=pt[Dataschema.AMOUNT], color=pt[Dataschema.CATEGORY], text=pt[Dataschema.CATEGORY])
        return html.Div(
            dcc.Graph(figure=fig_yaar),
            id=ids.BAR_CHART
        )

    return html.Div(
        id=ids.BAR_CHART
    )
