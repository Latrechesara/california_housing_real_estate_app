import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from sklearn.datasets import fetch_california_housing
import pandas as pd

dash.register_page(__name__, path='/analysis')

# Load raw data for exploration
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Price'] = data.target

# Create a sample map for the background
fig_map = px.scatter_mapbox(df.sample(2000), lat="Latitude", lon="Longitude", color="Price",
                            color_continuous_scale="Viridis", zoom=5, height=500)
fig_map.update_layout(mapbox_style="carto-darkmatter", margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#121212")

layout = html.Div([
    dbc.Container([
        html.H2("EXPLORATORY DATA ANALYSIS", className="text-white fw-bold mb-5 text-center pt-5"),
        
        dbc.Row([
            # Data Trends Card
            dbc.Col([
                html.Div([
                    html.H5("Price vs. Income Correlation", className="text-info"),
                    dcc.Graph(
                        figure=px.scatter(df.sample(1000), x="MedInc", y="Price", 
                                          template="plotly_dark", 
                                          color_discrete_sequence=["#00d2ff"]).update_layout(
                                              paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                    )
                ], className="result-display p-4 mb-4")
            ], lg=6),

            # Geographical Distribution Card
            dbc.Col([
                html.Div([
                    html.H5("Geographical Heatmap", className="text-info"),
                    dcc.Graph(figure=fig_map, className="rounded-4")
                ], className="result-display p-4")
            ], lg=6)
        ]),

    ], className="welcome-container", fluid=True)
])