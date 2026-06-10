from src.extract import extract_market_data
from src.load import save_raw_data
from src.transform import add_daily_returns
def main():
    ticker = "SPY"
    start_date = "2020-01-01"
    end_date = "2025-12-31"

    data = extract_market_data(
        ticker, 
        start_date, 
        end_date
    )

    data = add_daily_returns(data)

    save_raw_data(
        data,
        "data/raw/spy_raw.csv",
    )

    print(data.head())

if __name__ == "__main__":
    main()