import dash
from dash import callback
from dash.dependencies import Input, Output, State


# Show the modal on landing, UNLESS the user already entered demo mode this session
@callback(
    Output("landing-modal", "is_open"),
    Input("url", "pathname"),
    State("demo-session", "data"),
    prevent_initial_call=False
)
def sync_modal_on_load(pathname, demo_entered):
    if pathname == "/":
        return not demo_entered
    return dash.no_update


@callback(
    Output("login-message", "children"),
    Input("login-button", "n_clicks"),
    State("login-username", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def handle_login_attempt(n_clicks, username, password):
    return "Click 'Enter Demo' below to explore the dashboard."


# Clicking Enter Demo closes the modal AND marks the session as "entered"
@callback(
    Output("landing-modal", "is_open", allow_duplicate=True),
    Output("demo-session", "data"),
    Input("enter-demo-button", "n_clicks"),
    prevent_initial_call=True
)
def enter_demo(n_clicks):
    return False, True

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