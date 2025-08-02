from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html', signals=[
    {'pair': 'XAUUSD', 'direction': 'Buy', 'entry': 2321.5, 'sl': 2309.0, 'tp': 2345.0, 'rr': '1:2'},
    {'pair': 'GBPUSD', 'direction': 'Sell', 'entry': 1.2870, 'sl': 1.2910, 'tp': 1.2790, 'rr': '1:2.5'},
    {'pair': 'EURUSD', 'direction': 'Buy', 'entry': 1.1020, 'sl': 1.0980, 'tp': 1.1100, 'rr': '1:2'},
    {'pair': 'USDJPY', 'direction': 'Sell', 'entry': 144.20, 'sl': 144.80, 'tp': 143.00, 'rr': '1:2'},
    {'pair': 'AUDUSD', 'direction': 'Buy', 'entry': 0.6730, 'sl': 0.6700, 'tp': 0.6790, 'rr': '1:2'}
]
