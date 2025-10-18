from dash import html, register_page

register_page(__name__, path="/task-view", name="Task View")

layout = html.Div(
    [
        html.H2("Task View"),
        html.P("CONTENT")
    ]
)