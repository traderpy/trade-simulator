from dash import html, dcc

strategy_dropdown = dcc.Dropdown(
    id='strategy-dropdown',
    options=[{'label': 'ma_strategy.py', 'value': 'ma_strategy.py'},
             {'label': 'rsi_strategy.py', 'value': 'rsi_strategy.py'}]
)