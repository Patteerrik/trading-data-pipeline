import yfinance as yf


REQUIRED_COLUMNS = [
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
]


def validate_market_data(data, ticker):
    if data.empty:
        raise ValueError(f"No data returned for {ticker}")

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns for {ticker}: {missing_columns}"
        )


def extract_market_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
    )

    if data.columns.nlevels > 1:
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()
    data.columns.name = None

    validate_market_data(data, ticker)

    return data