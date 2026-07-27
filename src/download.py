"""
download.py
------------

Downloads historical data for:
1. NSE Nifty 50
2. Gold ETF
3. Bond ETF

Saves the cleaned price data in data/raw/.
"""

from pathlib import Path

import pandas as pd
import yfinance as yf


DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)


TICKERS = {
    "NSE": "^NSEI",
    "Gold": "GLD",
    "Bonds": "IEF",
}


def download_market_data(
    start="2010-01-01",
    end="2025-01-01",
):

    print("Downloading data...")

    raw = yf.download(
        list(TICKERS.values()),
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
    )

    prices = raw["Close"].copy()

    prices.columns = list(TICKERS.keys())

    prices = prices.dropna()

    output_file = DATA_DIR / "market_prices.csv"

    prices.to_csv(output_file)

    print(f"Saved data to {output_file}")

    return prices


if __name__ == "__main__":

    df = download_market_data()

    print(df.head())

    print(df.tail())