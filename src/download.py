"""
Download historical market data.
"""

import yfinance as yf
import pandas as pd


def download_data(start="2010-01-01", end="2025-01-01"):
    tickers = {
        "NSE": "^NSEI",
        "Gold": "GLD",
        "Bonds": "IEF"
    }

    prices = yf.download(
        list(tickers.values()),
        start=start,
        end=end,
        auto_adjust=True
    )["Close"]

    prices.columns = tickers.keys()

    return prices


if __name__ == "__main__":
    data = download_data()
    print(data.head())
