from download import download_market_data
from features import create_features
from hmm_model import train_hmm
from optimizer import optimize
from backtest import backtest
from benchmark import benchmark
from metrics import main as metrics
from plots import main as plots


def main():

    print("=" * 60)
    print("RegimeShift")
    print("=" * 60)

    download_market_data()

    create_features()

    train_hmm()

    optimize()

    backtest()

    benchmark()

    metrics()

    plots()

    print("\nProject Completed Successfully!")


if __name__ == "__main__":
    main()