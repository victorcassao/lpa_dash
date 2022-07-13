from dash import dcc
from dash import html
from dash import Input, Output

from app import app

from apps import pg_descriptive_analysis, pg_exams_results_analysis

app.layout = html.Div([
    html.Div([
        dcc.Link('Estatística Descritiva ', href="/apps/pg_descriptive_analysis"),
        dcc.Link('Análises Resultados Exames', href="/apps/pg_exams_results_analysis.py")
    ], className="row"),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[]),
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/apps/pg_descriptive_analysis":
        return pg_descriptive_analysis.layout
    elif pathname == "/apps/pg_exams_results_analysis.py":
        return pg_exams_results_analysis.layout

if __name__ == '__main__':
    app.run_server(debug=True)