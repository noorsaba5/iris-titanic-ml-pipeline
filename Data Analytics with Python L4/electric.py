import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load dataset
file_path = "Electric_Vehicle_Population_Data.csv"
df = pd.read_csv(file_path)

# Data preprocessing
df.dropna(subset=["County", "City", "Legislative District", "Postal Code"], inplace=True)
df["Electric Vehicle Type"] = df["Electric Vehicle Type"].astype("category")
df["Make"] = df["Make"].astype("category")
df["Model"] = df["Model"].astype("category")

# Create plots
# Fixing ValueError by renaming columns properly
ev_type_counts = df["Electric Vehicle Type"].value_counts().reset_index()
ev_type_counts.columns = ["Electric Vehicle Type", "Count"]
ev_type_fig = px.bar(ev_type_counts, x='Count', y='Electric Vehicle Type', 
                      title='Electric Vehicle Type Distribution', labels={'Electric Vehicle Type': 'Vehicle Type', 'Count': 'Count'})

model_year_fig = px.histogram(df, x="Model Year", nbins=20, title="Model Year Distribution", 
                              labels={'Model Year': 'Year', 'count': 'Count'}, color_discrete_sequence=["blue"])

# Fixing column name issue for Make
top_makes_counts = df["Make"].value_counts().head(10).reset_index()
top_makes_counts.columns = ["Make", "Count"]
top_makes_fig = px.bar(top_makes_counts, x='Count', y='Make', 
                        title='Top 10 EV Makes', labels={'Make': 'Make', 'Count': 'Number of Vehicles'}, 
                        color_discrete_sequence=["green"])

# Fixing column name issue for Model
top_models_counts = df["Model"].value_counts().head(10).reset_index()
top_models_counts.columns = ["Model", "Count"]
top_models_fig = px.bar(top_models_counts, x='Count', y='Model', 
                         title='Top 10 EV Models', labels={'Model': 'Model', 'Count': 'Number of Vehicles'}, 
                         color_discrete_sequence=["purple"])

electric_range_fig = px.box(df, x="Electric Vehicle Type", y="Electric Range", title="Electric Range by Vehicle Type",
                             labels={'Electric Vehicle Type': 'Vehicle Type', 'Electric Range': 'Range (miles)'}, 
                             color="Electric Vehicle Type")

price_dist_fig = px.histogram(df, x="Base MSRP", nbins=50, title="Distribution of Base MSRP", 
                              labels={'Base MSRP': 'Price ($)', 'count': 'Count'}, 
                              color_discrete_sequence=["red"])

cafv_counts = df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].value_counts().reset_index()
cafv_counts.columns = ["CAFV Eligibility", "Count"]
cafv_fig = px.bar(cafv_counts, x='Count', y='CAFV Eligibility', title='CAFV Eligibility Status', 
                   labels={'CAFV Eligibility': 'CAFV Eligibility', 'Count': 'Count'}, 
                   color_discrete_sequence=["orange"])

# Fixing column name issue for County
top_county_counts = df["County"].value_counts().head(10).reset_index()
top_county_counts.columns = ["County", "Count"]
county_fig = px.bar(top_county_counts, x='Count', y='County', 
                     title='Top 10 Counties with Most EVs', labels={'County': 'County', 'Count': 'Number of Vehicles'}, 
                     color_discrete_sequence=["cyan"])

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Electric Vehicle Data Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(figure=ev_type_fig),
    dcc.Graph(figure=model_year_fig),
    dcc.Graph(figure=top_makes_fig),
    dcc.Graph(figure=top_models_fig),
    dcc.Graph(figure=electric_range_fig),
    dcc.Graph(figure=price_dist_fig),
    dcc.Graph(figure=cafv_fig),
    dcc.Graph(figure=county_fig),
])

if __name__ == '__main__':
    app.run_server(debug=True)
