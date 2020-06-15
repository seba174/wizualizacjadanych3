import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

bad_fig = go.Figure()

bad_fig.add_trace(go.Scatter(
        x=germany, 
        y=japan, 
        text=years,
        textposition = textposition,
        mode='lines+markers+text'))

bad_fig.update_layout(
    autosize=False,
    width=800,
    height=600,
    xaxis_title=germany_title,
    yaxis_title=japan_title,
) 

good_fig = go.Figure()

good_fig.add_trace(
    go.Scatter(x=years, y=germany, mode='lines+markers', name="Germany"),
)

good_fig.add_trace(
    go.Scatter(x=years, y=japan, mode='lines+markers', name="Japan")
)
    
good_fig.update_layout(
    autosize=False,
    width=700,
    height=400,
    yaxis_title="GDP in current USD trillions",
    # showlegend=False
) 


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
    html.H1(children='Time wiggles through plot space'),


    html.Div(id='test-div', children=[
        html.Div([dcc.Graph(figure=bad_fig, config={'staticPlot': True})], style=plot_styles),

        html.Label('GDP of which country has fluctuated more?'),
        html.Br(),
        dcc.RadioItems(
            id='input',
            options=[
                {'label': 'Japan', 'value': 'Japan'},
                {'label': 'Germany', 'value': 'Germany'},
            ],
            value='Japan'
        ),
        html.Br(),
        html.Button('Check results', id='submit-button')
    ]),


    html.Div(id='proper-div', children=[
        html.Label('Results:'),
        html.Br(),
        html.Label('GDP of which country has fluctuated more?'),
        html.Br(),
        html.Div(id='input_out'),
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
    Output("input_out", "children"),
    [Input("input", "value")],
)

def number_render(input):
    return "Your answer: {}, correct answer: {}".format(input, 'Germany')

app.run_server(debug=True, use_reloader=True)