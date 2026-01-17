import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import joblib
import pandas as pd
import json # Added to handle the shape map

dash.register_page(__name__)

# 1. CONSTANTS FOR CONSTRAINTS
# California bounding box (Approximate)
LAT_LIMITS = [32.5, 42.0]
LON_LIMITS = [-124.5, -114.1]

# Load Model
import os
import joblib

# Get the path of the current directory (pages folder)
curr_path = os.path.dirname(__file__)
# Go up one level to the root folder and find the model
model_path = os.path.join(curr_path, '..', 'california_housing_model.pkl')

# Load Model using the safe path
model = joblib.load(model_path)
#model = joblib.load('california_housing_model.pkl')
features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

layout = html.Div([
    dbc.Row([
        # SIDEBAR
        dbc.Col([
            html.Div([
                html.H4("PROPERTY INPUTS", className="text-white mb-4 fw-bold", style={"letterSpacing":"2px"}),
                
                html.Div([
                    html.Label("Median Income ($10k)", className="text-info small fw-bold"),
                    dbc.Input(id="p-inc", type="number", value=4.5, step="any", className="mb-3 bg-dark-glass"),
                    
                    dbc.Row([
                        dbc.Col([
                            html.Label("House Age", className="text-info small"),
                            dbc.Input(id="p-age", type="number", value=15, step="any", className="mb-3 bg-dark-glass"),
                        ]),
                        dbc.Col([
                            html.Label("Avg Occupancy", className="text-info small"),
                            dbc.Input(id="p-occ", type="number", value=3.0, step="any", className="mb-3 bg-dark-glass"),
                        ]),
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.Label("Avg Rooms", className="text-info small"),
                            dbc.Input(id="p-rms", type="number", value=5.0, step="any", className="mb-3 bg-dark-glass"),
                        ]),
                        dbc.Col([
                            html.Label("Avg Beds", className="text-info small"),
                            dbc.Input(id="p-bed", type="number", value=1.0, step="any", className="mb-3 bg-dark-glass"),
                        ]),
                    ]),

                    html.Label("Local Population", className="text-info small"),
                    dbc.Input(id="p-pop", type="number", value=1200, step="any", className="mb-3 bg-dark-glass"),
                    
                    dbc.Row([
                        dbc.Col([
                            html.Label("Latitude", className="text-info small"),
                            dbc.Input(id="p-lat", type="number", value=34.05, step="any", className="mb-3 bg-dark-glass"),
                        ]),
                        dbc.Col([
                            html.Label("Longitude", className="text-info small"),
                            dbc.Input(id="p-lon", type="number", value=-118.24, step="any", className="mb-3 bg-dark-glass"),
                        ]),
                    ]),
                    
                    dbc.Button("CALCULATE VALUE", id="p-btn", className="w-100 py-3 mt-2 fw-bold border-0 shadow-sm",
                               style={"background": "linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%)"})
                ]),

                html.Div(id="p-output", className="mt-5 p-4 result-display text-center")

            ], className="div-user-controls h-100")
        ], width=12, lg=4, md=5),

        # MAP AREA
        dbc.Col([
            dcc.Graph(
                id="p-map", 
                style={"height": "90vh"}, 
                config={'displayModeBar': False},
                # Initial View shows California
                figure=px.scatter_mapbox(lat=[36.7], lon=[-119.4], zoom=5).update_layout(
                    mapbox_style="carto-darkmatter", margin={"r":0,"t":0,"l":0,"b":0}
                )
            )
        ], width=12, lg=8, md=7)
    ], className="g-0")
])

@callback(
    [Output("p-output", "children"),
     Output("p-map", "figure")],
    [Input("p-btn", "n_clicks")],
    [State("p-inc", "value"), State("p-age", "value"), State("p-rms", "value"), 
     State("p-bed", "value"), State("p-pop", "value"), State("p-occ", "value"),
     State("p-lat", "value"), State("p-lon", "value")]
)
def run_all(n, inc, age, rms, bed, pop, occ, lat, lon):
    if n is None:
        return "", dash.no_update

    # 1. BOUNDARY CONSTRAINT CHECK
    is_inside = (LAT_LIMITS[0] <= lat <= LAT_LIMITS[1]) and (LON_LIMITS[0] <= lon <= LON_LIMITS[1])
    
    if not is_inside:
        error_msg = html.Div([
            html.H5("OUTSIDE SERVICE AREA", className="text-warning fw-bold"),
            html.P(f"Please use coordinates within California.", className="text-white-50 small"),
            html.P(f"Lat: {LAT_LIMITS[0]} to {LAT_LIMITS[1]} | Lon: {LON_LIMITS[0]} to {LON_LIMITS[1]}", className="x-small text-info")
        ])
        # Return map zoomed out to California with no prediction point
        fig = px.scatter_mapbox(lat=[36.7], lon=[-119.4], zoom=5)
        fig.update_layout(mapbox_style="carto-darkmatter", margin={"r":0,"t":0,"l":0,"b":0}, uirevision='constant')
        return error_msg, fig

    # 2. PREDICTION LOGIC (Only runs if inside California)
    df = pd.DataFrame([[inc, age, rms, bed, pop, occ, lat, lon]], columns=features)
    pred = model.predict(df)[0] * 100000

    # 3. MAP LOGIC
    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        color_discrete_sequence=["#00d2ff"],
        size_max=20,
    )

    fig.update_layout(
        mapbox={
            "style": "carto-darkmatter",
            "center": {"lat": lat, "lon": lon},
            "zoom": 12,
            "pitch": 45,
            # ADDING THE SHAPE MAP (LAYER)
            "layers": [{
                "source": "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/california.geojson",
                "type": "line",
                "color": "#00d2ff",
                "opacity": 0.5,
                "line": {"width": 2}
            }]
        },
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor="#121212",
        uirevision='constant'
    )

    fig.update_traces(marker=dict(size=25, opacity=0.9))

    result = html.Div([
        html.H6("ESTIMATED MARKET VALUE", className="text-info opacity-75 mb-1 small"),
        html.H2(f"${pred:,.0f}", className="text-white fw-bold mb-0", style={"textShadow": "0 0 15px rgba(0, 210, 255, 0.4)"})
    ])

    return result, fig