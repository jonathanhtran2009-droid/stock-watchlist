# Stock Watchlist Tracker

A Python tool that pulls live stock market data and monitors a personal watchlist for buy and sell opportunities.

## Features
- Live price, daily high/low, and volume for any stock
- Custom buy and sell price alerts per ticker
- Automatic CSV logging with date and price history
- Invalid ticker detection

## Technologies Used
- Python
- yfinance API
- datetime

## How to Use
1. Clone the repository
2. Install dependencies: `pip install yfinance`
3. Edit the `watchlist` dictionary in `project1.py` with your tickers and target prices
4. Run `python project1.py`

## Sample Output
```
--- AAPL ---
Price: $264.58
Day High: $266.75
Day Low: $262.45
Volume: 36,884,993
```

