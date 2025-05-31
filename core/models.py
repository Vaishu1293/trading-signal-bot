from datetime import datetime

class Token:
    def __init__(self, symbol, prices):
        self.symbol = symbol.upper()
        self.prices = prices  # This should be a Pandas Series or DataFrame

    def latest_price(self):
        return self.prices.iloc[-1] if not self.prices.empty else None

class Strategy:
    def __init__(self, name):
        self.name = name

    def generate_signals(self, token):
        raise NotImplementedError("You must implement generate_signals()")

class Signal:
    def __init__(self, token_symbol, signal_type, price, timestamp=None):
        self.token_symbol = token_symbol.upper()
        self.signal_type = signal_type.upper()  # BUY, SELL, HOLD
        self.price = price
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        return {
            "token": self.token_symbol,
            "signal": self.signal_type,
            "price": round(self.price, 2),
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
