import dash 
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash import Dash
from dash.dependencies import Input, Output, State
from .components import *
from .callbacks import * 
from src.callbacks import register_callbacks


# Initialize app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    title="Synced Support",
    use_pages=True,
    suppress_callback_exceptions=True,
)
server = app.server

LOGO = "https://placehold.co/50x50"

# Components -- Navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="40px")),
                        dbc.Col(dbc.NavbarBrand("Synced Support", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),

            # Navbar toggler 
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),

            # Collapsible nav
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Student View", href="/student-view")),
                        dbc.NavItem(dbc.NavLink("Task View", href="/task-view")),
                    ],
                    className="ms-auto", 
                    navbar=True,
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="primary",
    dark=True,
    className="mb-4",
)

# Components -- Footer 
footer = html.Footer(
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(html.P("© 2025 Nicole", className="mb-0"), xs=12, md="auto"),
                dbc.Col(html.P("Source Code: GitHub", className="mb-0"), xs=12, md="auto"),
                dbc.Col(html.P("Last Update: Date", className="mb-0"), xs=12, md="auto"),
            ],
            justify="between", 
            className="text-center text-md-start g-2",
        ),
        fluid=True,
        className="py-3",
    ),
    className="bg-light border-top mt-5"
)


# Main Layout 
app.layout = dbc.Container(
    [
        dcc.Location(id="url"), 
        navbar,
        dash.page_container, 
        footer
    ],
    fluid=True,
    style={
        "minHeight": "100vh", 
    }
)

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)


