from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

PRICE_FILE = BASE_DIR / "data" / "raw" / "market_prices.csv"
WEIGHTS_FILE = BASE_DIR / "data" / "processed" / "weights.csv"

OUTPUT_FILE = BASE_DIR / "results" / "portfolio_returns.csv"


def backtest():

    print("Loading data...")

    prices = pd.read_csv(PRICE_FILE, index_col=0)

    weights = pd.read_csv(WEIGHTS_FILE, index_col=0)

    returns = prices.pct_change().dropna()

    # Keep only dates present in both files
    common = returns.index.intersection(weights.index)

    returns = returns.loc[common]
    weights = weights.loc[common]

    portfolio_return = (
        returns["NSE"] * weights["NSE"]
        + returns["Gold"] * weights["Gold"]
        + returns["Bonds"] * weights["Bonds"]
    )

    portfolio = pd.DataFrame({
        "Portfolio_Return": portfolio_return
    })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    portfolio.to_csv(OUTPUT_FILE)

    print("Saved portfolio returns to:", OUTPUT_FILE)

    print(portfolio.head())


if __name__ == "__main__":
    backtest()