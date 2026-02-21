import yfinance as yf

from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")

# Get Stock information from yfinance API
def stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info

# Stores and Prints certain stock information
def get_stock_info(ticker, info):
    if info.get('regularMarketPrice') == None:
        print("Invalid Ticker")
    else:
        print(f"--- {ticker} ---")
        Price = info.get('regularMarketPrice')
        print(f"Price: ${Price:,}")
        Day_High = info.get('dayHigh')
        print(f"Day High: ${Day_High:,}")
        Day_Low = info.get('dayLow')
        print(f"Day Low: ${Day_Low:,}")
        Volume = info.get('volume')
        print(f"Volume: {Volume:,}")
        with open('watchlist_log.csv', 'a') as file:
            file.write(
                f"{today}, {ticker}, {Price}, {Day_High}, {Day_Low}, {Volume}\n")

# Alerts user when a stock on there watchlist crosses a certain price to either buy/sell
def alert_stock(ticker, info):
    Price = info.get('regularMarketPrice')
    if Price < watchlist[ticker]["buy"]:
        print("Buy Stock")
    elif Price > watchlist[ticker]["sell"]:
        print("Sell Stock")


watchlist = {
    "AAPL": {"buy": 250.00, "sell": 300.00},
    "NVDA": {"buy": 380.00, "sell": 450.00},
    "MSFT": {"buy": 380.00, "sell": 450.00},
    "TSLA": {"buy": 380.00, "sell": 450.00},
}


for tickers in watchlist:
    info = stock_info(tickers)
    get_stock_info(tickers, info)
    alert_stock(tickers, info)
