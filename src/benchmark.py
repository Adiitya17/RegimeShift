from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

PRICE_FILE = BASE_DIR / "data" / "raw" / "market_prices.csv"
OUTPUT_FILE = BASE_DIR / "results" / "benchmark_returns.csv"


def benchmark():

    print("Creating benchmark...")

    prices = pd.read_csv(PRICE_FILE, index_col=0)

    benchmark_returns = prices["NSE"].pct_change().dropna()

    benchmark = pd.DataFrame({
        "Benchmark_Return": benchmark_returns
    })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    benchmark.to_csv(OUTPUT_FILE)

    print("Saved benchmark to:", OUTPUT_FILE)

    print(benchmark.head())


if __name__ == "__main__":
    benchmark()