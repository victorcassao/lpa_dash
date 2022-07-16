from numpy import spacing
import pandas as pd
import pathlib
from textwrap import wrap
import plotly.express as px
from copy import copy

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
print(DATA_PATH.joinpath("LPA.csv"))
df = pd.read_csv(DATA_PATH.joinpath("LPA.csv"))

df_form3 = df[((df.incluso_complete == 0.0) | 
                        (df.incluso_complete == 1.0) | 
                        (df.incluso_complete == 2.0)) &
                        (df.record_id.str.contains("-"))][['record_id', 'redcap_data_access_group', 'cor_pele', 'incluso_complete', 'genero', 'peso', 
              'altura', 'escolaridade']]

def histogram_plot_function(df, x_label, filter_option="Todos"):

    filter_option = "Todos" if filter_option == None else filter_option

    if "Todos" not in filter_option:

        filtered_df = copy(df[df.redcap_data_access_group==filter_option])
    else:

        filtered_df = df
    
    fig = px.histogram(filtered_df,
                        x=x_label,
                        color="redcap_data_access_group",
                        barmode="group",
                        text_auto=True)
    
    return fig

def weight_histogram_plot_function(df, x_label, filter_option="Todos"):

    filter_option = "Todos" if filter_option == None else filter_option

    df2 = df.dropna()
    df2.drop(df_form3[(df_form3['peso']=='UNK') | 
        (df_form3['peso']=='ASKU') | 
        (df_form3['peso']=='NI')].index, inplace=True)
    
    for idx in df2.index:
        df2.loc[idx, 'peso'] = pd.to_numeric(df.loc[idx, 'peso'])

    if "Todos" not in filter_option:

        filtered_df = copy(df2[df2.redcap_data_access_group==filter_option])
    else:
                        
        filtered_df = df2
        
        
    
    fig = px.histogram(filtered_df[filtered_df['peso'] <= 200],
                        x=x_label,
                        color="redcap_data_access_group",
                        barmode="group",
                        text_auto=True)
    
    return fig