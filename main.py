from src.extract import extract_market_data
from src.load import save_raw_data, save_processed_data
from src.transform import add_daily_returns
from src.transform import add_moving_averages
from src.transform import add_volatility
from src.spark_transform import (
    create_spark_session,
    read_market_data,
    add_20ma,
    save_spark_data,
    add_daily_return,
    add_spark_volatility,
)


TICKERS = [
    "SPY",
    "QQQ",
    "GLD",
    "TLT",
]

START_DATE = "2020-01-01"
END_DATE = "2025-12-31"


def run_pandas_pipeline(tickers, start_date, end_date):
    for ticker in tickers:
        data = extract_market_data(
            ticker,
            start_date,
            end_date,
        )

        raw_data = data.copy()

        data = add_daily_returns(data)
        data = add_volatility(data)
        data = add_moving_averages(data)

        save_raw_data(
            raw_data,
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


def run_spark_pipeline(tickers):
    spark = create_spark_session()
    spark.sparkContext.setLogLevel("ERROR")

    for ticker in tickers:
        df = read_market_data(
            spark,
            f"data/raw/{ticker.lower()}_raw.csv",
        )

        df = add_20ma(df)
        df = add_daily_return(df)
        df = add_spark_volatility(df)

        save_spark_data(
            df,
            f"data/spark/{ticker.lower()}_spark_processed.parquet",
        )

    spark.stop()


def main():
    run_pandas_pipeline(
        TICKERS,
        START_DATE,
        END_DATE,
    )
    run_spark_pipeline(TICKERS)


if __name__ == "__main__":
    main()