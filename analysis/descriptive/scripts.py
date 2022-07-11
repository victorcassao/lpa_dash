import plotly.express as px
import pandas as pd

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
