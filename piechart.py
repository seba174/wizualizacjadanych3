import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


"""
Pomysł zaczerpnięty z konkursu Przemysława Biecka na najgorszy wykres roku 2017.
 http://smarterpoland.pl/index.php/2017/12/najgorszy-wykres-2017-roku/
 https://www.wroclaw.pl/biznes/finanse-wroclawia-2018-na-tle-innych-miast
"""

areas = {
    "Warszawa": 51_724,
    "Kraków": 32_685,
    "Szczecin": 30_055,
    "Łódź": 29_325,
    "Wrocław": 29_282,
    "Zielona Góra": 27_832,
    "Gdańsk": 26_196,
    "Poznań": 26_191,
    "Świnoujście": 19_723
}

city_options = [{"label": key, "value": key} for key in areas.keys()]

data = pd.DataFrame({"city": [k for k in areas.keys()], "area": [value for value in areas.values()]})
bad_fig = px.pie(data, values="area", names="city")
good_fig = px.bar(data, x="city", y="area")

questions = ["1. What is a second biggest city in Poland",
             "2. What is the area (in hectares) of third biggest city in Poland?"]
correct_answers = ["Kraków", areas["Szczecin"]]

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Pie chart vs barplot'),

    html.Div(id='test-div', children=[
        html.Div([dcc.Graph(figure=bad_fig, config={'staticPlot': True})]),

        html.Label(questions[0]),
        html.Br(),
        dcc.Dropdown(options=city_options, id="input_1"),
        html.Br(),
        html.Label(questions[1]),
        html.Br(),
        dcc.Input(id='input_2', type='number'),
        html.Br(),
        html.Button('Check results', id='submit-button')
    ]),


    html.Div(id='proper-div', children=[
        html.Label('Results:'),
        html.Br(),
        html.Label(questions[0]),
        html.Br(),
        html.Div(id='input_1_out'),

        html.Label(questions[1]),
        html.Br(),
        html.Div(id='input_2_out'),

        html.H2('Bad plot'),
        html.Div([dcc.Graph(figure=bad_fig)]),

        html.H2('Better plot'),
        html.Div([dcc.Graph(figure=good_fig)])
    ])
])


@app.callback(
   Output(component_id='test-div', component_property='style'),
   [Input('submit-button', 'n_clicks')]
)
def hide_test_on_submit(n_clicks):
    if n_clicks and n_clicks > 0:
        return {'marginLeft': -9999, 'position': 'absolute'}
    else:
        return {}


@app.callback(
   Output(component_id='proper-div', component_property='style'),
   [Input('submit-button', 'n_clicks')]
)
def show_proper_on_submit(n_clicks):
    if n_clicks and n_clicks > 0:
        return {}
    else:
        return {'marginLeft': -9999, 'position': 'absolute'}


@app.callback(
    Output("input_1_out", "children"),
    [Input("input_1", "value")],
)
def number_render(input_1):
    return "Your answer: {}, correct answer: {}".format(input_1, correct_answers[0])


@app.callback(
    Output("input_2_out", "children"),
    [Input("input_2", "value")],
)
def number_render(input_2):
    return "Your answer: {}, correct answer: {}".format(input_2, correct_answers[1])


app.run_server(debug=True, use_reloader=True)
