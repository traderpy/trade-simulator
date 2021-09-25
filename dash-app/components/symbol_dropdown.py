from dash import html, dcc

symbol_dropdown = dcc.Dropdown(
    id='symbol-dropdown',
    options=[{'label': 'EURUSD_D1.csv', 'value': 'EURUSD_D1.csv'},
             {'label': 'BTCUSD', 'value': 'BTCUSD'}]
)