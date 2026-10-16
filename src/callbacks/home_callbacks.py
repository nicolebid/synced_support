import dash
from dash import callback
from dash.dependencies import Input, Output, State
from src.config import DEMO_MODE 


# Show the modal on landing, UNLESS the user already entered demo mode this session
@callback(
    Output("landing-modal", "is_open"),
    Input("url", "pathname"),
    Input("demo-session", "data"),
)
def sync_modal(pathname, demo_entered):
    if not DEMO_MODE:
        return False
    return pathname == "/" and not demo_entered


# Upon attempt to log in during demo mode 
@callback(
    Output("login-message", "children"),
    Input("login-button", "n_clicks"),
    State("login-username", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def handle_login_attempt(n_clicks, username, password):
    return "Click 'Enter Demo' below to explore the dashboard."

# Enter demo mode 
@callback(
    Output("demo-session", "data"),
    Input("enter-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def enter_demo(n_clicks):
    return True

# Collapsible card for Student View info 
@callback(
    Output("card-collapse-studentview", "is_open"),
    Input("collapse-button-studentview", "n_clicks"),
    State("card-collapse-studentview", "is_open"),
)
def toggle_card(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# Collapsible card for Task View info 
@callback(
    Output("card-collapse-taskview", "is_open"),
    Input("collapse-button-taskview", "n_clicks"),
    State("card-collapse-taskview", "is_open"),
)
def toggle_card(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open