from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import plotly.express as px
import pathlib
import pandas as pd

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
    dcc.Dropdown(
        dropdown_centros,
        id='selected-centers'
    ),
    dcc.Graph(
        id='graph-two',
    )
])

@app.callback(
    Output('graph-two', 'figure'),
    Input('selected-centers', 'value'))
def update_graph_genders(selected_centers):

    if (selected_centers == None) or ("Todos" in selected_centers):
        fig = px.histogram(df_form3,
                    x="genero",
                    color="redcap_data_access_group",
                    barmode="group",
                    text_auto=True)
        return fig
    else:
        fig = px.histogram(df_form3[df_form3.redcap_data_access_group==selected_centers],
                        x="genero",
                        color="redcap_data_access_group",
                        barmode="group",
                        text_auto=True)
        return fig