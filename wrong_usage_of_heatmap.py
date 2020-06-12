import plotly.express as px

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_of_day = ['Morning', 'Afternoon', 'Evening']
data = [[1, 25, 30, 50, 1], [18, 3, 60, 80, 30], [30, 60, 7, 3, 20]]

bad_fig = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day", color="Average productivity"),
                x=days,
                y=time_of_day
               )
bad_fig.update_xaxes(side="top")


good_fig = {
    'data': [
        {'x': days, 'y': data[0], 'type': 'bar', 'name': time_of_day[0]},
        {'x': days, 'y': data[1], 'type': 'bar', 'name': time_of_day[1]},
        {'x': days, 'y': data[2], 'type': 'bar', 'name': time_of_day[2]}
    ],
    'layout': {
        'yaxis': {
            'tickmode': "linear",
            'tick0': 0,
            'dtick': 4
        },
        'height': 700
    }
}


proper_answers = [data[2][3], data[1][0]]


plot_styles = {
    'margin': '0 auto',
    'width': '50%'
}


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Heatmap vs barplot'),


    html.Div(id='test-div', children=[
        html.Div([dcc.Graph(figure=bad_fig, config={'staticPlot': True})], style=plot_styles),

        html.Label('1. What is an average productivity at Thursday evening?'),
        html.Br(),
        dcc.Input(id='input_1', type='number'),
        html.Br(),
        html.Label('2. What is an average productivity at Monday afternoon?'),
        html.Br(),
        dcc.Input(id='input_2', type='number'),

        html.Br(),
        html.Button('Check results', id='submit-button')
    ]),


    html.Div(id='proper-div', children=[
        html.Label('Results:'),
        html.Br(),
        html.Label('1. What is an average productivity at Thursday evening?'),
        html.Br(),
        html.Div(id='input_1_out'),

        html.Label('2. What is an average productivity at Monday afternoon?'),
        html.Br(),
        html.Div(id='input_2_out'),

        html.H2('Bad plot'),
        html.Div([dcc.Graph(figure=bad_fig)], style=plot_styles),

        html.H2('Better plot'),
        html.Div([dcc.Graph(figure=good_fig)], style=plot_styles)
    ])
])


@app.callback(
   Output(component_id='test-div', component_property='style'),
   [Input('submit-button','n_clicks')]
)
def hide_test_on_submit(n_clicks):
   if n_clicks and n_clicks > 0:
       return {'marginLeft':-9999, 'position': 'absolute'}
   else: return {}


@app.callback(
   Output(component_id='proper-div', component_property='style'),
   [Input('submit-button','n_clicks')]
)
def show_proper_on_submit(n_clicks):
   if n_clicks and n_clicks > 0:
       return {}
   else: return {'marginLeft':-9999, 'position': 'absolute'}


@app.callback(
    Output("input_1_out", "children"),
    [Input("input_1", "value")],
)
def number_render(input_1):
    return "Your answer: {}, correct answer: {}".format(input_1, proper_answers[0])


@app.callback(
    Output("input_2_out", "children"),
    [Input("input_2", "value")],
)
def number_render(input_2):
    return "Your answer: {}, correct answer: {}".format(input_2, proper_answers[1])


app.run_server(debug=True, use_reloader=True)