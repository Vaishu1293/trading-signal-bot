import os
from core.indicators import calculate_rsi
from core.models import Token
from core.price_source import fetch_token_price_history
from core.processor import RSIStrategy, log_signal
from visual.chart import plot_rsi
from core.telegram import send_telegram_image

# === Configuration ===
bot_token = os.getenv("BOT_TOKEN", "7533358664:AAF8BIYVAN_hP1WfM6NwAgYLe-0IPL7ieVw")
chat_id = os.getenv("CHAT_ID", "7548797867")  # Replace with your real chat ID if needed

# Tokens to track (symbol → CoinGecko ID)
tokens_to_track = {
    "ETH": "ethereum",
    "BTC": "bitcoin",
    "SOL": "solana"
}

# === Main Execution Loop ===
for symbol, coingecko_id in tokens_to_track.items():
    try:
        print(f"📥 Fetching data for {symbol}...")
        prices = fetch_token_price_history(coingecko_id)
        token = Token(symbol, prices)
        rsi = calculate_rsi(prices)

        strategy = RSIStrategy()
        signal = strategy.generate_signals(token)

        # Log + save chart
        log_signal(signal)
        chart_path = f"visual/{symbol.lower()}_rsi_chart.png"
        plot_rsi(prices, rsi, token_symbol=symbol, save_path=chart_path)

        # Prepare caption
        caption = f"📊 *{symbol} Trading Signal*\n" \
                  f"Action: *{signal.signal_type}*\n" \
                  f"Price: `${signal.price:.2f}`\n" \
                  f"Time: `{signal.timestamp.strftime('%Y-%m-%d %H:%M:%S')}`"

        # Send chart + caption to Telegram
        sent = send_telegram_image(bot_token, chat_id, image_path=chart_path, caption=caption)

        if sent:
            print(f"✅ {symbol} signal sent to Telegram.")
        else:
            print(f"❌ Failed to send {symbol} signal.")

    except Exception as e:
        print(f"🚨 Error processing {symbol}: {e}")
