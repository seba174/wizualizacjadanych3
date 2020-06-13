import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import random
import pandas as pd


class ExampleApp:
    """Example Dash App"""
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    def __init__(self, name):
        random.seed(1234)
        df = px.data.iris()
        fig_1 = px.scatter(df, x="sepal_length", y="sepal_width", color="species")
        fig_1.update_layout(
            title="Dobry wykres",
            xaxis_title="sepal length",
            yaxis_title="sepal width",
        )

        fig_2 = px.scatter(df, x="species", y="sepal_width", color="sepal_length")
        fig_2.update_layout(
            title="Zły wykres",
            xaxis_title="sepal length",
            yaxis_title="sepal width",
        )
        self.app = dash.Dash(name, external_stylesheets=ExampleApp.external_stylesheets)
        self.app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),
            html.Div(children='''
                Dash: A web application framework for Python.
            '''),
            dcc.Graph(
                id='dobry',
                figure=fig_1
            ),
            dcc.Graph(
                id='zły',
                figure=fig_2
            )
        ])

    def run(self):
        self.app.run_server(debug=True)


if __name__ == '__main__':
    server = ExampleApp("A")
    server.run()
