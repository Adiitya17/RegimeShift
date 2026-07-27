from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]

PORTFOLIO_FILE = BASE_DIR / "results" / "portfolio_returns.csv"
BENCHMARK_FILE = BASE_DIR / "results" / "benchmark_returns.csv"

OUTPUT = BASE_DIR / "results" / "equity_curve.png"


def main():

    portfolio = pd.read_csv(PORTFOLIO_FILE, index_col=0)

    benchmark = pd.read_csv(BENCHMARK_FILE, index_col=0)

    portfolio.index = pd.to_datetime(portfolio.index)
    benchmark.index = pd.to_datetime(benchmark.index)

    portfolio_curve = (1 + portfolio["Portfolio_Return"]).cumprod()
    benchmark_curve = (1 + benchmark["Benchmark_Return"]).cumprod()

    plt.figure(figsize=(12,6))

    plt.plot(portfolio_curve, label="RegimeShift Strategy")
    plt.plot(benchmark_curve, label="Buy & Hold NSE")

    plt.title("Portfolio Value")

    plt.xlabel("Date")

    plt.ylabel("Growth of ₹1")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(OUTPUT)

    plt.show()

    print(f"Saved plot to {OUTPUT}")


if __name__ == "__main__":
    main()