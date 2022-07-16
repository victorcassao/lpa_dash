from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import plotly.express as px
import pathlib
import pandas as pd

from apps.plot_functions import *
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
print(DATA_PATH.joinpath("LPA.csv"))
df = pd.read_csv(DATA_PATH.joinpath("LPA.csv"))

df_form3 = df[((df.incluso_complete == 0.0) | 
                        (df.incluso_complete == 1.0) | 
                        (df.incluso_complete == 2.0)) &
                        (df.record_id.str.contains("-"))][['record_id', 'redcap_data_access_group', 'cor_pele', 'incluso_complete', 'genero', 'peso', 
              'altura', 'escolaridade']]

dropdown_centros = df_form3.redcap_data_access_group.unique().tolist()
dropdown_centros.insert(0, "Todos")

layout = html.Div([
    html.Div([
        html.H1(children='Gênero'),
        dcc.Dropdown(
            dropdown_centros,
            id='selected-centers'
        ),
        dcc.Graph(
            id='gender-graph',
        )
    ]),
    html.Div([
        html.H1(children='Cor da Pele'),
        dcc.Dropdown(
            dropdown_centros,
            id='selected-centers-skin-color'
        ),
        dcc.Graph(
            id='skin-color'
        )
    ]),
    html.Div([
        html.H1(children='Altura'),
        dcc.Dropdown(
            dropdown_centros,
            id='selected-centers-height'
        ),
        dcc.Graph(
            id='height'
        )
    ]),
    html.Div([
        html.H1(children='Peso'),
        dcc.Dropdown(
            dropdown_centros,
            id='selected-centers-weight'
        ),
        dcc.Graph(
            id='weight'
        )
    ])
])

@app.callback(
    Output('gender-graph', 'figure'),
    Input('selected-centers', 'value'))
def update_graph_genders(selected_centers):

    return histogram_plot_function(df_form3, "genero", filter_option=selected_centers)

@app.callback(
    Output('skin-color', 'figure'),
    Input('selected-centers-skin-color', 'value'))
def update_skin_color_graph(selected_centers):

    return histogram_plot_function(df_form3, "cor_pele", filter_option=selected_centers)

@app.callback(
    Output('height', 'figure'),
    Input('selected-centers-height', 'value'))
def update_skin_color_graph(selected_centers):

    return histogram_plot_function(df_form3, "altura", filter_option=selected_centers)

@app.callback(
    Output('weight', 'figure'),
    Input('selected-centers-weight', 'value'))
def update_skin_color_graph(selected_centers):

    return weight_histogram_plot_function(df_form3, "peso", filter_option=selected_centers) 