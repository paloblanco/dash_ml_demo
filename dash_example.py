from dash import Dash, html, dcc, callback, Output, Input, State
import pickle
import pandas as pd

external_stylesheets = [
    'https://unpkg.com/simpledotcss/simple.min.css',
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Demo for getting info from Dash'),
    html.P(children='Enter your information to get a prediction'),
    html.Br(),
    dcc.Dropdown(
        ["Cleveland","New York","Philadelphia","Allentown"],
        id='dropdown-selection',
        placeholder="Select a city"
        ),
    html.Br(),
    dcc.Input(
        id='input-age',
        type='number',
        placeholder="Enter your age"
    ),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Br(),
    html.Br(),
    html.H3(children="Results"),
    html.P(children="", id="p-result")
])

@callback(
    Output('p-result', 'children'),
    Input('submit-val', "n_clicks"),
    State('dropdown-selection', 'value'),
    State('input-age', 'value'),
    prevent_initial_call=True
)
def update_result(clicks, city, age):
    result = ""
    if not age: result += "You need to enter an age!    "
    if not city: result += "You need to enter a city!"
    if result: return result
    return f"You are {str(age)} years old and live in {city}"

if __name__ == '__main__':
    app.run(debug=True)