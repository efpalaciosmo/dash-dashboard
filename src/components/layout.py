import pandas as pd
from dash import Dash, html
from . import year_dropdown, bar_chart, category_dropdown, month_dropdown


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    This function is used to set the layout if the dashboard
    :param app: Dash instance
    :param data: data frame to lead information on dashboard
    :return: html.Div, a div element with all the sub divs in the dashboard, one for each visual needed
    """
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data),
                    month_dropdown.render(app, data),
                    category_dropdown.render(app, data)
                ]
            ),
            bar_chart.render(app, data)
        ]
    )