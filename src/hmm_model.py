"""
Train Hidden Markov Model on market features.
"""

from pathlib import Path

import pandas as pd
from hmmlearn.hmm import GaussianHMM


# ----------------------------------------------------
# Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

FEATURE_FILE = BASE_DIR / "data" / "processed" / "feature_matrix.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "regimes.csv"
def train_hmm():
    """
    Train a Gaussian Hidden Markov Model on the feature matrix.
    """

    print("Loading feature matrix...")

    df = pd.read_csv(FEATURE_FILE, index_col=0)

    print(f"Loaded {len(df)} observations.")

    model = GaussianHMM(
        n_components=3,
        covariance_type="full",
        n_iter=200,
        random_state=42
    )

    model.fit(df)

    regimes = model.predict(df)

    df["Regime"] = regimes

    df.to_csv(OUTPUT_FILE)

    print(f"Saved regimes to: {OUTPUT_FILE}")

    print(df.head())




if __name__ == "__main__":
         train_hmm()