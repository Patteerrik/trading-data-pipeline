from src.extract import extract_market_data
from src.load import save_raw_data, save_processed_data
from src.transform import add_daily_returns
from src.transform import add_moving_averages
from src.spark_transform import (
    create_spark_session,
    read_market_data,
    add_test_column,
    save_spark_data,
)
from src.spark_transform import add_20ma


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

        save_processed_data(
            data,
            f"data/processed/{ticker.lower()}_processed.parquet",
        )

if __name__ == "__main__":
    main()


    spark = create_spark_session()

    df = read_market_data(
        spark,
        "data/raw/spy_raw.csv",
    )

    df = add_test_column(df)
    df = add_20ma(df)

    save_spark_data(
    df,
    "data/spark/spy_spark_processed.parquet",
    )

    df.printSchema()