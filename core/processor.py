from core.models import Strategy, Signal
from core.indicators import calculate_rsi
from datetime import datetime

class RSIStrategy(Strategy):
    def __init__(self, name="RSI Strategy", rsi_period=14):
        super().__init__(name)
        self.rsi_period = rsi_period

    def generate_signals(self, token):
        prices = token.prices
        rsi = calculate_rsi(prices, window=self.rsi_period)

        latest_rsi = rsi.iloc[-1]
        latest_price = prices.iloc[-1]

        if latest_rsi < 30:
            signal_type = "BUY"
        elif latest_rsi > 70:
            signal_type = "SELL"
        else:
            signal_type = "HOLD"

        return Signal(
            token_symbol=token.symbol,
            signal_type=signal_type,
            price=latest_price
        )

def log_signal(signal, log_path="logs/signal_log.txt"):
    with open(log_path, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - "
                f"{signal.token_symbol}: {signal.signal_type} at ${signal.price:.2f}\n")
