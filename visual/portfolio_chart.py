import matplotlib.pyplot as plt

def plot_multi_rsi(rsi_dict, save_path="visual/portfolio_rsi_comparison.png"):
    plt.figure(figsize=(12, 6))
    for symbol, rsi_series in rsi_dict.items():
        plt.plot(rsi_series.index, rsi_series, label=symbol)

    plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')
    plt.title("RSI Comparison: ETH vs BTC vs SOL")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"✅ Portfolio RSI chart saved to {save_path}")
