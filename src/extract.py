import yfinance as yf


def extract_market_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
    )

    if isinstance(data.columns, type(data.columns)) and data.columns.nlevels > 1:
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()
    data.columns.name = None

    return data