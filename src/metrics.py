from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

PORTFOLIO_FILE = BASE_DIR / "results" / "portfolio_returns.csv"
BENCHMARK_FILE = BASE_DIR / "results" / "benchmark_returns.csv"


def calculate_metrics(returns):

    annual_return = (1 + returns).prod() ** (252 / len(returns)) - 1

    annual_volatility = returns.std() * np.sqrt(252)

    sharpe = annual_return / annual_volatility

    cumulative = (1 + returns).cumprod()

    drawdown = cumulative / cumulative.cummax() - 1

    max_drawdown = drawdown.min()

    return annual_return, annual_volatility, sharpe, max_drawdown


def main():

    portfolio = pd.read_csv(PORTFOLIO_FILE, index_col=0)

    benchmark = pd.read_csv(BENCHMARK_FILE, index_col=0)

    p = portfolio["Portfolio_Return"]

    b = benchmark["Benchmark_Return"]

    print("\n========== PORTFOLIO ==========")

    ar, vol, sharpe, mdd = calculate_metrics(p)

    print(f"Annual Return     : {ar:.2%}")
    print(f"Volatility        : {vol:.2%}")
    print(f"Sharpe Ratio      : {sharpe:.2f}")
    print(f"Maximum Drawdown  : {mdd:.2%}")

    print("\n========== BENCHMARK ==========")

    ar, vol, sharpe, mdd = calculate_metrics(b)

    print(f"Annual Return     : {ar:.2%}")
    print(f"Volatility        : {vol:.2%}")
    print(f"Sharpe Ratio      : {sharpe:.2f}")
    print(f"Maximum Drawdown  : {mdd:.2%}")


if __name__ == "__main__":
    main()