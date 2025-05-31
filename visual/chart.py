import matplotlib.pyplot as plt
import os

def plot_rsi(prices, rsi, token_symbol="ETH", save_path="visual/rsi_chart.png"):
    plt.figure(figsize=(12, 6))

    # 🔹 Panel 1: Price
    plt.subplot(2, 1, 1)
    plt.plot(prices.index, prices, label=f'{token_symbol} Price', color='blue')
    plt.title(f'{token_symbol} Price Chart')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()

    # 🔹 Panel 2: RSI
    plt.subplot(2, 1, 2)
    plt.plot(rsi.index, rsi, label='RSI', color='orange')
    plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    
    # Save the chart
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    print(f"✅ Chart saved to {save_path}")
    
    plt.close()  # Avoid showing plot in test mode
