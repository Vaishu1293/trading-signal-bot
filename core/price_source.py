import requests
import pandas as pd

def fetch_token_price_history(token_id: str, days: int = 30):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for {token_id}")

    data = response.json()
    prices = data.get("prices", [])
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["Date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("Date", inplace=True)

    return pd.Series(df["price"].values, index=df.index)
