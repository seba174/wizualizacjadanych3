import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# data

# wykres 1.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_of_day = ['Morning', 'Afternoon', 'Evening']
data = [[1, 25, 30, 50, 1], [18, 3, 60, 80, 30], [30, 60, 7, 3, 20]]

bad_fig = px.imshow(data,
                labels=dict(x="Day of week", y="Time of day", color="Average productivity"),
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
        'xaxis': {
            'title': "Day of week"
        },
        'yaxis': {
            'title': "Average productivity",
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

# wykres 2.
data = {
    'Avengers: Endgame': 2_797_800_564,
    'Avatar': 2_790_439_000,
    'Titanic': 2_194_439_542,
    'Star Wars: The Force Awakens': 2_068_223_624,
    'Avengers: Infinity War': 2_048_359_754
}

labels = [x for x, y in data.items()]
values = [y for x, y in data.items()]


# wykres 3.
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
bad_fig_3 = px.pie(data, values="area", names="city")
good_fig_3 = px.bar(data, x="city", y="area")

questions = ["1. What is a second biggest city in Poland",
             "2. What is the area (in hectares) of third biggest city in Poland?"]
correct_answers_3 = ["Kraków", areas["Szczecin"]]


# wykres 4.
germany = [  
    3.002446368084,
    3.439953462907,
    3.752365607148,
    3.418005001389,
    3.417094562649,
    3.757698281118,
    3.543983909148,
    3.752513503278,
    3.898726503841,
    3.381389338659,
    3.495162856297,
    3.693204332230
]

japan = [
    4.530377224970,
    4.515264514431,
    5.037908465114,
    5.231382674594,
    5.700098114744,
    6.157459594824,
    6.203213121334,
    5.155717056271,
    4.850413536038,
    4.394977752878,
    4.949273341994,
    4.872415104315,
]

years = list(range(2006, 2018))

textposition = [
    'top center',
    'middle right',
    'top center',
    'middle left',
    'middle left',
    'top center',
    'middle left',
    'middle right',
    'middle right',
    'bottom center',
    'top left',
    'middle right'
]

japan_title = 'Japan GDP (in current USD trillions)'
germany_title = 'Germany GDP (in current USD trillions)'

bad_fig_4 = go.Figure()

bad_fig_4.add_trace(go.Scatter(
        x=germany, 
        y=japan, 
        text=years,
        textposition = textposition,
        mode='lines+markers+text'))

bad_fig_4.update_layout(
    autosize=False,
    width=800,
    height=600,
    xaxis_title=germany_title,
    yaxis_title=japan_title,
) 

good_fig_4 = go.Figure()

good_fig_4.add_trace(
    go.Scatter(x=years, y=germany, mode='lines+markers', name="Germany"),
)

good_fig_4.add_trace(
    go.Scatter(x=years, y=japan, mode='lines+markers', name="Japan")
)
    
good_fig_4.update_layout(
    autosize=False,
    width=700,
    height=400,
    yaxis_title="GDP in current USD trillions",
    # showlegend=False
) 

# wykres 5.

df = px.data.iris()
good_fig_5 = px.scatter(df, x="sepal_length", y="sepal_width", color="species")
good_fig_5.update_layout(
    xaxis_title="sepal length",
    yaxis_title="sepal width",
)

bad_fig_5 = px.scatter(df, x="species", y="sepal_width", color="sepal_length")
bad_fig_5.update_layout(
    xaxis_title="sepal length",
    yaxis_title="sepal width",
)


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        html.H1("Tricky charts - QUIZ", className='m-5'),
        html.Hr(),
        dbc.Row([
        dbc.Button(
            "Start",
            color="primary",
            block=True,
            id="start-quiz-button",
            className="mb-3 col-4",
            
        )]),

        dbc.Row(id='test-div', children=[
                    dbc.FormGroup(
                [
                    dbc.Label('1. What is an average productivity at Thursday evening?'),
                    dbc.Input(id='input_1', type='number'),
                    dbc.Label('2. What is an average productivity at Monday afternoon?'),
                    dbc.Input(id='input_2', type='number'),

                    dbc.Button('Check results', id='submit-button', color="primary", className="mt-3")
            ], className="mt-5"),
            html.Div([dcc.Graph(figure=bad_fig, config={'staticPlot': True})], style=plot_styles),
        ]),


        html.Div(id='proper-div', children=[
            dbc.Button('Next >>', id='go-to-second-chart', color="primary", className="mt-3 float-right"),
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
        ]),

        html.Div(id='test-div-2', children=[
        html.Div(id='panel', children=[
            dcc.Graph(
                id='truncated-axis',
                figure={
                    'data': [
                        {'x': labels, 'y': values, 'type': 'bar', 'name': 'SF'},
                    ],
                    'layout': {
                        'title': 'Zestawienie pięciu najlepiej zarabiających filmów w historii',
                        'yaxis': {
                            'range': [2_000_000_000, 3_000_000_000],
                            'color': '#E1E1E1',
                        },
                    }
                }
            ),
            html.H4(children="Na podstawie wykresu oszacuj, ile razy więcej zarobił Avengers: Endgame niż Star Wars: The Force Awakens"),
            dcc.Input(id='truncated-axis-input', className='centered', type='range', min=1, max=10, step=0.1,
                        value=5),
            html.H4(id='result', children="2"),
            html.Button(id='check-button', children="Sprawdź")
        ])
        ]),

            html.Div(id='proper-div-2', children=[
            html.Div(children=[
            dbc.Button('Next >>', id='go-to-third-chart', color="primary", className="mt-3 float-right"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H3(children="Prawidłowa odpowiedź to 1,4. Ucięte osie potrafią znacznie utrudnić wyciągnięcie" + \
                              " z wykresu prawidłowych wniosków. Poniżej możesz obejrzeć poprawny wykres z którego" + \
                              " łatwiej odczytać prawidłowe informacje."),
            dcc.Graph(
                id='normal-axis',
                figure={
                    'data': [
                        {'x': labels, 'y': values, 'type': 'bar', 'name': 'SF'},
                    ],
                    'layout': {
                        'title': 'Zestawienie pięciu najlepiej zarabiających filmów w historii',
                    }
                }
            ),
        ])
        ]),

        html.Div(id='test-div-3', children=[
            html.Div([dcc.Graph(figure=bad_fig_3, config={'staticPlot': True})]),

            html.Label(questions[0]),
            html.Br(),
            dcc.Dropdown(options=city_options, id="input_1-3"),
            html.Br(),
            html.Label(questions[1]),
            html.Br(),
            dcc.Input(id='input_2-3', type='number'),
            html.Br(),
            html.Button('Check results', id='submit-button-3')
        ]),


        html.Div(id='proper-div-3', children=[
            dbc.Button('Next >>', id='go-to-fourth-chart', color="primary", className="mt-3 float-right"),
            html.Label('Results:'),
            html.Br(),
            html.Label(questions[0]),
            html.Br(),
            html.Div(id='input_1_out-3'),

            html.Label(questions[1]),
            html.Br(),
            html.Div(id='input_2_out-3'),

            html.H2('Bad plot'),
            html.Div([dcc.Graph(figure=bad_fig_3)]),

            html.H2('Better plot'),
            html.Div([dcc.Graph(figure=good_fig_3)])
        ]),


        html.Div(id='test-div-4', children=[
        html.Div([dcc.Graph(figure=bad_fig_4, config={'staticPlot': True})], style=plot_styles),

        html.Label('GDP of which country has fluctuated more?'),
        html.Br(),
        dcc.RadioItems(
            id='input-4',
            options=[
                {'label': 'Japan', 'value': 'Japan'},
                {'label': 'Germany', 'value': 'Germany'},
            ],
            value='Japan'
        ),
        html.Br(),
        html.Button('Check results', id='submit-button-4')
    ]),


        html.Div(id='proper-div-4', children=[
            dbc.Button('Next >>', id='go-to-fifth-chart', color="primary", className="mt-3 float-right"),
            html.Label('Results:'),
            html.Br(),
            html.Label('GDP of which country has fluctuated more?'),
            html.Br(),
            html.Div(id='input_out-4'),
            html.H2('Bad plot'),
            html.Div([dcc.Graph(figure=bad_fig_4)], style=plot_styles),
            html.H2('Better plot'),
            html.Div([dcc.Graph(figure=good_fig_4)], style=plot_styles)
        ]),

        dbc.Row(id='test-div-5', children=[
                    dbc.FormGroup(
                [
                    dbc.Label('What is the biggest sepal length for versicolor?'),
                    dbc.Input(id='input-5', type='number'),

                    dbc.Button('Check result', id='submit-button-5', color="primary", className="mt-3")
            ], className="mt-5"),
            html.Div([dcc.Graph(figure=bad_fig_5, config={'staticPlot': True})], style=plot_styles),
        ]),


        html.Div(id='proper-div-5', children=[
            html.Label('Results:'),
            html.Br(),
            html.Label('What is the biggest sepal length for versicolor?'),
            html.Br(),
            html.Div(id='input_out-5'),

            html.H2('Bad plot'),
            html.Div([dcc.Graph(figure=bad_fig_5)], style=plot_styles),

            html.H2('Better plot'),
            html.Div([dcc.Graph(figure=good_fig_5)], style=plot_styles)
        ]),

]
)



# pierwszy wykres
@app.callback(
   Output(component_id='start-quiz-button', component_property='style'),
   [Input('start-quiz-button','n_clicks')]
)
def hide_start_quiz_on_start_quiz(n_clicks):
   if n_clicks and n_clicks > 0:
       return {'marginLeft':-9999, 'position': 'absolute'}
   else: return {}


@app.callback(
   Output(component_id='test-div', component_property='style'),
   [Input('submit-button','n_clicks'), Input('start-quiz-button','n_clicks')]
)
def hide_test_on_submit_show_on_start_quiz(n_clicks, start_quiz_clicks):
    if n_clicks and n_clicks > 0:
       return {'marginLeft':-9999, 'position': 'absolute'}
    elif start_quiz_clicks and start_quiz_clicks > 0:
        return {}
    else: return {'marginLeft':-9999, 'position': 'absolute'}


@app.callback(
   Output(component_id='proper-div', component_property='style'),
   [Input('submit-button','n_clicks'),Input('go-to-second-chart','n_clicks')]
)
def show_proper_on_submit_hide_on_go_to_second_chart(n_clicks, next_chart_n_clicks):
    if next_chart_n_clicks and next_chart_n_clicks > 0:
        return {'marginLeft':-9999, 'position': 'absolute'}
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



# drugi wykres

@app.callback(
   Output(component_id='test-div-2', component_property='style'),
   [Input('go-to-second-chart','n_clicks'), Input('check-button','n_clicks')]
)
def show_second_chart_on_go_to_second_chart_hide_on_check(next_chart_n_clicks, check_n_clicks):
    if check_n_clicks and check_n_clicks > 0:
        return {'marginLeft':-9999, 'position': 'absolute'}
    if next_chart_n_clicks and next_chart_n_clicks > 0:
        return {}
    else: return {'marginLeft':-9999, 'position': 'absolute'}

@app.callback(
    Output('proper-div-2', component_property='style'),
    [Input('check-button', 'n_clicks'), Input('go-to-third-chart', 'n_clicks')]
)
def show_2nd_proper_on_check_hide_on_go_to_third(n_clicks, go_to_third_n_clicks):
    if go_to_third_n_clicks and go_to_third_n_clicks > 0:
        return {'marginLeft':-9999, 'position': 'absolute'}    
    if n_clicks and n_clicks > 0:
        return {}
    return {'marginLeft':-9999, 'position': 'absolute'}


@app.callback(
    Output('result', 'children'),
    [Input('truncated-axis-input', 'value')]
)
def result(value):
    return value


# trzeci wykres

@app.callback(
   Output(component_id='test-div-3', component_property='style'),
   [Input('submit-button-3', 'n_clicks'), Input('go-to-third-chart', 'n_clicks')]
)
def hide_test_on_submit_show_on_go_to_third_chart_3(n_clicks, next_chart_n_clicks):
    if n_clicks and n_clicks > 0:
        return {'marginLeft': -9999, 'position': 'absolute'}
    if next_chart_n_clicks and next_chart_n_clicks > 0:
        return {}
    else:
        return {'marginLeft': -9999, 'position': 'absolute'}


@app.callback(
   Output(component_id='proper-div-3', component_property='style'),
   [Input('submit-button-3', 'n_clicks'), Input('go-to-fourth-chart', 'n_clicks')]
)
def show_proper_on_submit_hide_on_go_to_next3(n_clicks, go_to_fourth_chart_n_clicks):
    if go_to_fourth_chart_n_clicks and go_to_fourth_chart_n_clicks > 0:
        return {'marginLeft': -9999, 'position': 'absolute'}
    if n_clicks and n_clicks > 0:
        return {}
    else:
        return {'marginLeft': -9999, 'position': 'absolute'}


@app.callback(
    Output("input_1_out-3", "children"),
    [Input("input_1-3", "value")],
)
def number_render_3(input_1):
    return "Your answer: {}, correct answer: {}".format(input_1, correct_answers_3[0])


@app.callback(
    Output("input_2_out-3", "children"),
    [Input("input_2-3", "value")],
)
def number_render_3(input_2):
    return "Your answer: {}, correct answer: {}".format(input_2, correct_answers_3[1])


# czwarty wykres

@app.callback(
   Output(component_id='test-div-4', component_property='style'),
   [Input('submit-button-4','n_clicks'), Input('go-to-fourth-chart', 'n_clicks')]
)

def hide_test_on_submit_show_on_go_to_fourth_chart(n_clicks, go_to_fourth_chart_n_clicks):
    if n_clicks and n_clicks > 0:
       return {'marginLeft':-9999, 'position': 'absolute'}
    if go_to_fourth_chart_n_clicks and go_to_fourth_chart_n_clicks > 0:
        return {}
    else: return {'marginLeft':-9999, 'position': 'absolute'}

@app.callback(
   Output(component_id='proper-div-4', component_property='style'),
   [Input('submit-button-4','n_clicks'), Input('go-to-fifth-chart', 'n_clicks')]
)

def show_proper_on_submit_hide_on_go_to_fifth(n_clicks, go_to_fifth_chart_n_clicks):
    if go_to_fifth_chart_n_clicks and go_to_fifth_chart_n_clicks > 0:
        return {'marginLeft':-9999, 'position': 'absolute'}
    if n_clicks and n_clicks > 0:
       return {}
    return {'marginLeft':-9999, 'position': 'absolute'}

@app.callback(
    Output("input_out-4", "children"),
    [Input("input-4", "value")],
)

def number_render(input):
    return "Your answer: {}, correct answer: {}".format(input, 'Germany')

# piąty wykres

@app.callback(
   Output(component_id='test-div-5', component_property='style'),
   [Input('submit-button-5','n_clicks'), Input('go-to-fifth-chart', 'n_clicks')]
)

def hide_test_on_submit_show_on_go_to_fifth_chart(n_clicks, go_to_fifth_chart_n_clicks):
    if n_clicks and n_clicks > 0:
       return {'marginLeft':-9999, 'position': 'absolute'}
    if go_to_fifth_chart_n_clicks and go_to_fifth_chart_n_clicks > 0:
        return {}
    else: return {'marginLeft':-9999, 'position': 'absolute'}

@app.callback(
   Output(component_id='proper-div-5', component_property='style'),
   [Input('submit-button-5','n_clicks')]
)

def show_proper_on_submit(n_clicks):
   if n_clicks and n_clicks > 0:
       return {}
   else: return {'marginLeft':-9999, 'position': 'absolute'}

@app.callback(
    Output("input_out-5", "children"),
    [Input("input-5", "value")],
)

def render_sepal_length(input):
    return "Your answer: {}, correct answer: 7".format(input)


if __name__ == '__main__':
    app.run_server(debug=True)