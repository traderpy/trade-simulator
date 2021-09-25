from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go

from components.symbol_dropdown import symbol_dropdown
from components.strategy_dropdown import strategy_dropdown

app = Dash(__name__)

STYLE = {'margin-left': '5%', 'margin-right': '5%'}
app.layout = html.Div([
    html.H1('PyAlgo Trading - Backtest'),
    html.Hr(),

    html.H2('Select Data'),
    symbol_dropdown,
    html.Div(id='symbol-chart'),

    html.Hr(),
    html.H2('Backtest'),
    strategy_dropdown

], style=STYLE)


@app.callback(
    Output('symbol-chart', 'children'),
    Input('symbol-dropdown', 'value')
)
def return_ohlc_chart(value):
    print(value)
    if value:
        df = pd.read_csv(f'history/{value}')

        fig = go.Figure(data=[go.Candlestick(x=df['time'],
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])

        fig.update_layout(xaxis_rangeslider_visible=False)

        return [
            html.H3(value),
            dcc.Graph(figure=fig),
        ]


if __name__ == '__main__':
    app.run_server()
