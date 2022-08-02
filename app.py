#%%
# Gunicorn is a WSGI HTTP server that is used for deploying Flask apps into production.
from dash import Dash, Input, Output, State, html, dcc, dash_table, callback
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc

#%%
app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    html.H1("This text is black")
)
# run server
if __name__ == "__main__":
    app.run_server(debug=True)