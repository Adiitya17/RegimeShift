# RegimeShift: Hidden Markov Model Based Dynamic Portfolio Allocation

## Overview

RegimeShift is a quantitative finance project that identifies hidden market regimes using a Hidden Markov Model (HMM) and dynamically adjusts portfolio allocations based on the detected market state. The project demonstrates an end-to-end workflow including financial data collection, feature engineering, regime detection, portfolio construction, backtesting, benchmarking, performance evaluation, and visualization.

This project was developed as part of the **Summer of Quant (SOQ)** program at **IIT Bombay**.

---

## Project Objectives

- Detect hidden market regimes using statistical learning.
- Engineer financial indicators from historical market data.
- Allocate portfolio weights based on detected market conditions.
- Compare strategy performance against a benchmark.
- Evaluate performance using standard portfolio metrics.

---

## Project Structure

```
RegimeShift/
│
├── data/
│   ├── raw/
│   │   └── market_prices.csv
│   └── processed/
│       ├── feature_matrix.csv
│       ├── regimes.csv
│       └── weights.csv
│
├── results/
│   ├── portfolio_returns.csv
│   ├── benchmark_returns.csv
│   └── equity_curve.png
│
├── notebooks/
│   └── RegimeShift.ipynb
│
├── src/
│   ├── download.py
│   ├── features.py
│   ├── hmm_model.py
│   ├── optimizer.py
│   ├── backtest.py
│   ├── benchmark.py
│   ├── metrics.py
│   ├── plots.py
│   ├── config.py
│   └── main.py
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Methodology

### 1. Data Collection

Historical daily prices for:

- NSE Index
- Gold
- Bond ETF

are downloaded and stored for further processing.

---

### 2. Feature Engineering

Several market indicators are computed, including:

- Daily Returns
- Rolling Volatility
- Moving Average
- Momentum

The features are standardized before model training.

---

### 3. Hidden Markov Model

A Gaussian Hidden Markov Model is trained on the engineered features to classify market behavior into hidden regimes.

The detected regimes are used as signals for portfolio allocation.

---

### 4. Portfolio Construction

Portfolio weights are assigned according to the detected market regime.

The generated weights are stored and later used during backtesting.

---

### 5. Backtesting

The strategy is evaluated using historical data by calculating the portfolio returns over time.

---

### 6. Benchmark

The strategy performance is compared against a Buy-and-Hold NSE benchmark.

---

### 7. Performance Metrics

The following metrics are computed:

- Annual Return
- Annual Volatility
- Sharpe Ratio
- Maximum Drawdown

---

### 8. Visualization

The project generates an equity curve comparing:

- Dynamic Regime Strategy
- Buy-and-Hold Benchmark

---

## Results

The project automatically generates:

- Portfolio Returns
- Benchmark Returns
- Equity Curve
- Performance Metrics

Example output:

```
Annual Return

Volatility

Sharpe Ratio

Maximum Drawdown
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Aditya17/RegimeShift.git
cd RegimeShift
```

Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the complete pipeline

```bash
python3 src/main.py
```

The pipeline automatically performs:

1. Download data
2. Feature engineering
3. Hidden Markov Model training
4. Portfolio allocation
5. Backtesting
6. Benchmark generation
7. Performance evaluation
8. Visualization

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- hmmlearn
- yfinance

---

## Future Improvements

Potential extensions include:

- Walk-forward validation
- Dynamic mean-variance optimization
- Transaction cost modeling
- Multiple benchmark portfolios
- Additional financial features
- Regime probability visualization
- Risk-adjusted portfolio optimization

---

## Author

**Aditya Mishra**

Summer of Quant (SOQ)  
Indian Institute of Technology Bombay

---

## License

This project is released under the MIT License.
