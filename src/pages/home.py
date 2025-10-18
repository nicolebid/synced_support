from dash import html, register_page

# Register the page at path "/"
register_page(__name__, path="/", name="Home")

layout = html.Div(
    [
        html.H2("Welcome to Synced Support!"),
        html.P("This is the landing page."),
    ],
    className="text-center text-light mt-5"
)