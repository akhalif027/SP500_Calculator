import yfinance as yf
import pandas as pd
from datetime import datetime   

sp500 = pd.read_csv("sp500_constituents.csv")
tickers = sp500["Symbol"].tolist()

for ticker in tickers:
    if "." in ticker:
        tickers[tickers.index(ticker)] = ticker.replace(".", "-")

start_2025 = datetime(year=2025, month=1, day=2)
end_2025 = datetime(year=2025, month=1, day=3)

start_2026 = datetime(year=2025, month=12, day=31) 
end_2026 = datetime(year=2026, month=1, day=1)


def sp500_prices(tickers, start, end, year=None):
    if year is None:
        year = []

    for symbol in tickers:
        data = yf.Ticker(symbol).history(interval="1d", start=start, end=end)

        if data.empty:
            print(f"No data for {symbol} in range {start} to {end}")
            year.append(None)
            continue

        start_price = float(round((data.iloc[0]["Close"]),2))
        year.append(start_price)

    return year


price_2025 = list(sp500_prices(tickers, start_2025, end_2025, year=[]))
price_2026 = list(sp500_prices(tickers, start_2026, end_2026, year=[]))

sp500['2025 Price'] = price_2025
sp500['2026 Price'] = price_2026

sp500.to_csv("sp500_prices.csv", index=True)