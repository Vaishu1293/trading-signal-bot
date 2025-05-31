import pandas as pd
import os
from core.indicators import calculate_rsi
from core.models import Token
from core.price_source import fetch_eth_price_history
from core.processor import RSIStrategy, log_signal
from visual.chart import plot_rsi
from core.telegram import send_telegram_message

# === Load live price data ===
def load_eth_prices():
    return fetch_eth_price_history(days=30)

# === Main Runner ===
prices = load_eth_prices()
token = Token("ETH", prices)
rsi = calculate_rsi(prices)
strategy = RSIStrategy()
signal = strategy.generate_signals(token)

# === Output ===
print(signal.to_dict())
log_signal(signal)
plot_rsi(prices, rsi, token_symbol=token.symbol)

# === Telegram Integration ===
bot_token = "7533358664:AAF8BIYVAN_hP1WfM6NwAgYLe-0IPL7ieVw"
chat_id = "7548797867"  # Replace this with your actual Telegram user ID

message = f"📊 *Trading Signal Alert*\n" \
          f"Token: `{signal.token_symbol}`\n" \
          f"Action: *{signal.signal_type}*\n" \
          f"Price: `${signal.price:.2f}`\n" \
          f"Time: `{signal.timestamp.strftime('%Y-%m-%d %H:%M:%S')}`"

sent = send_telegram_message(bot_token, chat_id, message)

if sent:
    print("✅ Signal sent to Telegram.")
else:
    print("❌ Failed to send Telegram message.")
