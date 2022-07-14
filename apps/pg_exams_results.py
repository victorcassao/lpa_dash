from dash import dcc
from dash import html
import plotly.express as px
import pathlib
import pandas as pd

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
print(DATA_PATH.joinpath("LPA.csv"))
df = pd.read_csv(DATA_PATH.joinpath("LPA.csv"))

def positive_lpa1(df):

    amostra1 = df[df.nro_amostra=='1_amostra']

    desired_columns = ['sensivel', 'resistente', 'resistencia_inferida', 'indeterminado', 'heterorressistente']

    filtered = amostra1[amostra1.rif_resistencia_lpa1.isin(desired_columns)]

    fig = px.histogram(filtered,
                    x="redcap_data_access_group",
                    color="rif_resistencia_lpa1",
                    barmode="group",
                    text_auto=True)

    return fig

layout = html.Div([
    dcc.Graph(
        id='graph-one',
        figure=positive_lpa1(df)
    )
])

