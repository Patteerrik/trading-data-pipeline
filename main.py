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

        data = add_volatility(data)

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

    df = add_20ma(df)
    
    df = add_daily_return(df)

    df = add_spark_volatility(df)

    df.select(
        "Price",
        "Close",
        "20MA_Spark",
        "Previous_Close",
        "Daily_Return_Spark",
        "Volatility_20D_Spark",
    ).show(10)

    save_spark_data(
    df,
    "data/spark/spy_spark_processed.parquet",
    )

    df.printSchema()