from src.extract import extract_market_data
from src.load import save_raw_data
from src.transform import add_daily_returns
from src.transform import add_moving_averages


def main():
    tickers = [
        "SPY",
        "QQQ",
        "GLD",
        "TLT",
    ]

    start_date = "2020-01-01"
    end_date = "2025-12-31"

    for ticker in tickers:
        data = extract_market_data(
            ticker, 
            start_date, 
            end_date
        )

        data = add_daily_returns(data)

        data = add_moving_averages(data)

        save_raw_data(
            data,
            f"data/raw/{ticker.lower()}_raw.csv",
        )

        save_raw_data(
            data,
            f"data/processed/{ticker.lower()}_processed.csv",
        )

if __name__ == "__main__":
    main()