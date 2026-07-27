from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

REGIME_FILE = BASE_DIR / "data" / "processed" / "regimes.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "weights.csv"


def optimize():

    print("Loading regimes...")

    df = pd.read_csv(REGIME_FILE, index_col=0)

    weights = {
        0: {"NSE": 0.70, "Gold": 0.20, "Bonds": 0.10},
        1: {"NSE": 0.30, "Gold": 0.30, "Bonds": 0.40},
        2: {"NSE": 0.10, "Gold": 0.40, "Bonds": 0.50},
    }

    portfolio = []

    for regime in df["Regime"]:
        portfolio.append(weights[int(regime)])

    portfolio = pd.DataFrame(portfolio, index=df.index)

    portfolio.to_csv(OUTPUT_FILE)

    print("Saved weights to:", OUTPUT_FILE)

    print(portfolio.head())


if __name__ == "__main__":
    optimize()