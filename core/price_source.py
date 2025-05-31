import requests
import pandas as pd
from datetime import datetime

def fetch_eth_price_history(days=30):
    url = f"https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from CoinGecko")

    data = response.json()
    prices = data.get("prices", [])  # List of [timestamp, price]

    # Convert to DataFrame
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["Date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("Date", inplace=True)

    return pd.Series(df["price"].values, index=df.index)
