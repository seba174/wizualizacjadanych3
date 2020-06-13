# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = {
    'Avengers: Endgame': 2_797_800_564,
    'Avatar': 2_790_439_000,
    'Titanic': 2_194_439_542,
    'Star Wars: The Force Awakens': 2_068_223_624,
    'Avengers: Infinity War': 2_048_359_754
}

labels = [x for x, y in data.items()]
values = [y for x, y in data.items()]

app.layout = html.Div(children=[
    html.Div(children=[
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
    ])
])

@app.callback(
    Output('panel', 'children'),
    [Input('check-button', 'n_clicks')],
    [dash.dependencies.State('truncated-axis-input', 'value')]
)
def update_panels(n_clicks, value):
    if n_clicks is None:
        return [
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
                          value=5.5),
                html.H4(id='result', children="2"),
                html.Button(id='check-button', children="Sprawdź")
            ])
        ]

    else:
        value = float(value)
        if value == 1.4:
            div = html.H3("Odpowiedziałeś poprawnie!")
        elif abs(value - 1.4) <= 0.5:
            div = html.H3("Byłeś blisko!")
        else:
            div = html.H3("Zupełnie nie!")
        return [
            div,
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
        ]


@app.callback(
    Output('result', 'children'),
    [Input('truncated-axis-input', 'value')]
)
def result(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)