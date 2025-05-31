import streamlit as st
from core.price_source import fetch_token_price_history
from core.indicators import calculate_rsi
import matplotlib.pyplot as plt

# Streamlit UI
st.set_page_config(layout="wide")
st.title("📊 Multi-Token RSI Signal Dashboard")

tokens = {
    "ETH": "ethereum",
    "BTC": "bitcoin",
    "SOL": "solana"
}

selected_tokens = st.multiselect("Select tokens to visualize:", list(tokens.keys()), default=["ETH", "BTC", "SOL"])
rsi_period = st.slider("RSI Window", min_value=5, max_value=21, value=14)

for symbol in selected_tokens:
    try:
        st.subheader(f"{symbol} RSI Chart")
        coingecko_id = tokens[symbol]
        prices = fetch_token_price_history(coingecko_id)
        rsi = calculate_rsi(prices, window=rsi_period)

        fig, ax = plt.subplots()
        ax.plot(prices.index, prices, label="Price", color="blue", alpha=0.4)
        ax2 = ax.twinx()
        ax2.plot(rsi.index, rsi, label="RSI", color="orange")
        ax2.axhline(70, linestyle="--", color="red", label="Overbought")
        ax2.axhline(30, linestyle="--", color="green", label="Oversold")
        ax.set_title(f"{symbol} - Price & RSI")
        ax.legend(loc="upper left")
        ax2.legend(loc="upper right")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Failed to load {symbol}: {e}")
