from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

from analysis.descriptive.scripts import *
from constants import *

df = pd.read_csv('https://redbox.technology/csv_data/LPA.csv')

df_form3 = df[((df.incluso_complete == 0.0) | 
                        (df.incluso_complete == 1.0) | 
                        (df.incluso_complete == 2.0)) &
                        (df.record_id.str.contains("-"))][cols_form3]

app = Dash(__name__)

dropdown_centros = df_form3.redcap_data_access_group.unique().tolist()
dropdown_centros.insert(0, "Todos")

app.layout = html.Div([
    dcc.Graph(
        id='graph-one',
        figure=positive_lpa1(df)
    ),
    html.Br(),
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

if __name__ == '__main__':
    app.run_server(debug=True)
