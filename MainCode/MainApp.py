import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# visualizations from other files
from ResearchQ1 import graph_1_1, graph_1_2, graph_1_3, graph_1_4
from ResearchQ2 import graph_2_1
from ResearchQ3 import graph_3_1
# other dependencies: statsmodels

# creating the dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# initial figure value
fig = graph_1_1()

# updating layout with the figure
app.layout = html.Div([
    dcc.Dropdown(
        id='chosenViz',
        options=[
            # add your graphs to the dropdown menu here, value rq1g1 stands for
            # research question 1 graph 1, etc, add elif statement in the callback
            # after adding a graph
            {'label': '2019 Avg PM2.5 Concentration in NYC', 'value': 'rq3g1'},
            {'label': 'NYC Air Quality vs Prosperity (2017)',
             'value': 'rq1g1'},
            {'label': 'NYC Air Quality vs Income (2017)', 'value': 'rq1g2'},
            {'label': 'NYC Air Quality vs Population (2017)',
             'value': 'rq1g3'},
            {'label': 'NYC Air Quality vs Borough (2017)', 'value': 'rq1g4'},


        ],
        value='rq3g1'
    ),
    dcc.Graph(id='graph-with-slider', figure=fig, style={'height': '90vh'})
])

# handling a change in dropdown selection


@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('chosenViz', 'value')])
def update_output(value):
    if value == "rq1g1":
        return graph_1_1()
    elif value == "rq1g2":
        return graph_1_2()
    elif value == "rq1g3":
        return graph_1_3()
    elif value == "rq1g4":
        return graph_1_4()
    elif value == "rq2g1":
        return graph_2_1()
    elif value == "rq3g1":
        return graph_3_1()


if __name__ == '__main__':
    app.run_server(debug=True)
