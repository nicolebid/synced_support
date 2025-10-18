from dash import html, register_page

register_page(__name__, path="/student-view", name="Student View")

layout = html.Div(
    [
        html.H2("Student View"),
        html.P("CONTENT")
    ]
)