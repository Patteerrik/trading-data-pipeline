import yfinance as yf

def extract_market_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
    )

    return data