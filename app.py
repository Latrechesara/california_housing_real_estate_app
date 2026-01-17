import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, 
    use_pages=True, 
    external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server
navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(html.I(className="bi bi-geo-fill text-info fs-3")),
                dbc.Col(dbc.NavbarBrand("CALIFORNIA REAL ESTATE APP", className="ms-2 fw-bold")),
            ], align="center", className="g-0"),
            href="/", style={"textDecoration": "none"}
        ),
        dbc.Nav([
            dbc.NavLink("Explore", href="/", active="exact"),
            dbc.NavLink("Predictor", href="/prediction", active="exact"),
        ], navbar=True, className="ms-auto")
    ], fluid=True),
    dark=True, color="#121212", sticky="top"
)

# Ultra-Modern Footer
footer = html.Footer(
    html.Div(
        dbc.Container([
            html.Div([
                html.Span("© ", className="me-1"),
                html.Span("Latrechhe Sara", className="text-info fw-semibold"),
                html.Span(" — All rights reserved.")
            ], className="text-center text-white-50")
        ]),
        className="modern-footer py-4"
    )
)


app.layout = html.Div([
    navbar,
    html.Div(dash.page_container, style={"minHeight": "85vh"}),
    footer
], style={"backgroundColor": "#121212", "display": "flex", "flexDirection": "column", "minHeight": "100vh"})

if __name__ == "__main__":
    app.run(debug=True)