import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div([
    dbc.Container([
        # SECTION 1: HERO
        dbc.Row([
            dbc.Col([
                html.H1("THE CALIFORNIA HOUSING PORTAL", 
                        className="text-white fw-bold display-3 mt-5", 
                        style={"letterSpacing": "5px"}),
                html.P("Deciphering the complexity of West Coast real estate through Advanced Machine Learning.",
                       className="text-info fs-5 mb-5"),
            ], width=12)
        ]),

        # SECTION 2: THE PROBLEM (Introduction)
        dbc.Row([
            dbc.Col([
                html.Img(src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80", 
                         className="intro-img mb-4"),
            ], lg=6),
            dbc.Col([
                html.H3("The Real Estate Challenge", className="text-white fw-bold mb-3"),
                html.P([
                    "Predicting property value is more than just counting bedrooms. In California, ",
                    html.B("location, neighborhood density, and economic shifts", className="text-info"),
                    " create a volatile market. Our AI model analyzes 20,000+ historical records to identify patterns human eyes might miss, ",
                    html.B("explaining about 82% of the variation in housing prices", className="text-info"),
                    "."
                ], className="text-white-50 fs-5")
                ,
                
                html.Div([
                    html.Span("8-Feature Analysis", className="data-badge"),
                    html.Span("Live Map Sync", className="data-badge"),
                    html.Span("RandomForest Powered", className="data-badge"),
                ], className="mt-4"),
                
                dbc.Button("START PREDICTING", href="/prediction", 
                           className="mt-5 py-3 px-5 fw-bold border-0",
                           style={"background": "linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%)", "borderRadius": "30px"})
            ], lg=6, className="ps-lg-5 d-flex flex-column justify-content-center")
        ], className="mb-5"),

        # SECTION 3: THE DATASET EXPLAINED
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H4("Understanding the Dataset", className="text-white mb-4"),
                    html.P("Derived from the 1990 U.S. Census, this dataset captures the backbone of California's geography. Each 'block' provides a snapshot of socio-economic health.", className="text-white-50"),
                    
                    dbc.Table([
                        html.Thead(html.Tr([html.Th("Feature"), html.Th("Significance")])),
                        html.Tbody([
                            html.Tr([html.Td("MedInc", className="text-info"), html.Td("Highest correlation with price. Measures purchasing power.")]),
                            html.Tr([html.Td("AveOccup", className="text-info"), html.Td("Identifies family-heavy vs. single-dweller areas.")]),
                            html.Tr([html.Td("Coordinates", className="text-info"), html.Td("Critical for proximity to coastline and urban hubs.")]),
                        ])
                    ], className="text-white mt-3", bordered=False, hover=True)
                ], className="p-5 result-display")
            ], width=12)
        ], className="mb-5 py-5")

    ], className="welcome-container", fluid=True)
])