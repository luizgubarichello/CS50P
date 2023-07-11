from project import moving_average, price_action, rsi
import yfinance as yf
import pandas as pd
import random

data = yf.download(['NU', 'PBR', 'VALE'], period='5y', back_adjust=True, auto_adjust=True)

closes = data['Close'].copy()
opens = data['Open'].copy()
highs = data['High'].copy()
lows = data['Low'].copy()


def test_moving_average():
    assert moving_average(closes, 200, 'abc') == None
    for _ in range(100):
        assert isinstance(moving_average(closes, random.randrange(2, 500), 'SMA'), pd.DataFrame)
        assert isinstance(moving_average(closes, random.randrange(2, 500), 'EMA'), pd.DataFrame)


def test_price_action():
    assert price_action(closes, opens, highs, lows, 'abc') == None
    for pattern in ['inside bar', 'outside bar', 'candle of force', 'upper shadow', 'lower shadow']:
        assert isinstance(price_action(closes, opens, highs, lows, pattern), pd.DataFrame)


def test_rsi():
    for _ in range(10):
        assert isinstance(rsi(closes, random.randrange(2, 200)), pd.DataFrame)
