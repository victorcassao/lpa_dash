from dash import dcc
from dash import html
from dash import Input, Output

from app import app
from apps import pg_exams_results, pg_socioeconomics

app.layout = html.Div([
    html.Div([
        dcc.Link('Análises Socioeconômicas', href="/apps/pg_socioeconomics"),
         html.Br(),
        dcc.Link('Análises Resultados Exames', href="/apps/pg_exams_results")
    ], className="row"),
    dcc.Location(id='url', refresh=False),
    html.Br(),
    html.Div(id='page-content', children=[]),
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/apps/pg_socioeconomics":
        return pg_socioeconomics.layout
    elif pathname == "/apps/pg_exams_results":
        return pg_exams_results.layout

if __name__ == '__main__':
    app.run_server(debug=True)