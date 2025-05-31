from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd
import os
from core.models import Token
from core.processor import RSIStrategy
from core.indicators import calculate_rsi
from visual.chart import plot_rsi

app = FastAPI()

def load_eth_prices():
    csv_path = "data/eth_prices.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, parse_dates=["Date"])
        return pd.Series(df["Close"].values, index=df["Date"])
    else:
        # Fallback dummy prices
        dates = pd.date_range(start="2025-05-01", periods=15, freq="D")
        return pd.Series([100, 102, 101, 105, 107, 106, 109, 112, 110, 108, 111, 113, 115, 114, 116], index=dates)

@app.get("/signal")
def get_latest_signal():
    prices = load_eth_prices()
    token = Token("ETH", prices)
    strategy = RSIStrategy()
    signal = strategy.generate_signals(token)
    return signal.to_dict()


@app.get("/plot")
def get_rsi_plot():
    prices = load_eth_prices()
    rsi = calculate_rsi(prices)
    plot_path = "visual/rsi_chart.png"
    plot_rsi(prices, rsi, save_path=plot_path)
    return FileResponse(path=plot_path, media_type="image/png", filename="rsi_chart.png")