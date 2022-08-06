from dash import Dash, html
from . import nation_dropdown, bar_chart


def create_layout(app: Dash) -> html.Div:
    """
    This function is used to set the layout if the dashboard
    :param app: Dash instance
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
                    nation_dropdown.render(app)
                ]
            ),
            bar_chart.render(app)
        ]
    )