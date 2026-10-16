import dash 
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import base64
from src.utils.init_check import is_initialized
import os 
# Initialize app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    title="Synced Support",
    use_pages=True,
    pages_folder=os.path.join(os.path.dirname(__file__), "pages"),
    suppress_callback_exceptions=True,
)

server = app.server
from src.universal_callbacks import register_universal_callbacks
register_universal_callbacks(app)


LOGO = "img/icon.png"
with open(LOGO, "rb") as f:
    encoded_img = base64.b64encode(f.read()).decode("utf-8")

GITHUB_LOGO = "img/github_logo.png"
with open(GITHUB_LOGO, "rb") as f:
    encoded_github_logo = base64.b64encode(f.read()).decode("utf-8")


# Components -- Navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                                html.Img(
                                src=f"data:image/png;base64,{encoded_img}",
                                height="40px"
                            )
                        ),
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
                        dbc.NavItem(dbc.NavLink("Logout", id="logout-button", href="#", n_clicks=0)),

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
                dbc.Col(
                    html.P("© 2026 Nicole Bidwell", className="mb-0"),
                    xs=12, md="auto"
                ),
                dbc.Col(
                    html.P(
                        [
                            "Source Code: ",
                                    html.A(
                                        html.Img(
                                            src=f"data:image/png;base64,{encoded_github_logo}",
                                            height="20px",
                                            style={"verticalAlign": "middle"}
                                        ),
                                        href="https://github.com/nicolebid/synced_support",
                                        target="_blank",
                                    ), 
                        ],
                        className="mb-0"
                    ),
                    xs=12, md="auto"
                ),
                dbc.Col(
                    html.P("Last Update: 28/09/2026", className="mb-0"),
                    xs=12, md="auto"
                )
            ],
            justify="between", 
            className="text-center text-md-start g-2"
        ),
        fluid=True,
        className="py-3"
    ),
    className="bg-light border-top mt-5"
)

# Main Layout 
app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Location(id="url"), 
                dcc.Store(id="demo-session", storage_type="session", data=False), 
                navbar,
                dash.page_container
            ],
            style={'flex': '1 0 auto'}
        ),
            footer
    ],
    style={
        'display':'flex',
        'flexDirection':'column',
        "minHeight": "100vh", 
    }
)
if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

