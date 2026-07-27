"""
features.py

Creates machine learning features for HMM.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def create_features():

    prices = pd.read_csv(
        RAW_DIR / "market_prices.csv",
        index_col=0,
        parse_dates=True,
    )

    # ---------- Feature Engineering ----------

    features = pd.DataFrame(index=prices.index)

    # NSE Log Returns
    features["Return"] = np.log(prices["NSE"]).diff()

    # Rolling Volatility
    features["Volatility"] = features["Return"].rolling(20).std()

    # Momentum
    features["Momentum"] = prices["NSE"].pct_change(20)

    # Moving Average Ratio
    ma50 = prices["NSE"].rolling(50).mean()

    features["MA_Ratio"] = prices["NSE"] / ma50

    features = features.dropna()

    scaler = StandardScaler()

    scaled = scaler.fit_transform(features)

    features = pd.DataFrame(
        scaled,
        columns=features.columns,
        index=features.index,
    )

    output = PROCESSED_DIR / "feature_matrix.csv"

    features.to_csv(output)

    print("Saved feature matrix to:", output)

    print(features.head())

    return features


if __name__ == "__main__":

    create_features()