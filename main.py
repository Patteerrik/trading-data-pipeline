import logging
from pathlib import Path
from src.extract import extract_market_data
from src.load import save_raw_data, save_processed_data
from src.transform import add_daily_returns, add_moving_averages, add_volatility, add_atr 
from src.config import (
    TICKERS,
    START_DATE,
    END_DATE,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    SPARK_DATA_DIR,
)
from src.spark_transform import (
    create_spark_session,
    read_market_data,
    add_20ma,
    save_spark_data,
    add_daily_return,
    add_spark_volatility,
    add_spark_atr,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def create_output_directories():
    for directory in [
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        SPARK_DATA_DIR,  
    ]:
        Path(directory).mkdir(parents=True, exist_ok=True)


def run_pandas_pipeline(tickers, start_date, end_date):
    for ticker in tickers:
        logging.info(f"Running Pandas pipeline for {ticker}")
        data = extract_market_data(
            ticker,
            start_date,
            end_date,
        )

        raw_data = data.copy()

        data = add_daily_returns(data)
        data = add_volatility(data)
        data = add_moving_averages(data)
        data = add_atr(data)

        save_raw_data(
            raw_data,
            f"{RAW_DATA_DIR}/{ticker.lower()}_raw.csv",
        )

        save_raw_data(
            data,
            f"{PROCESSED_DATA_DIR}/{ticker.lower()}_processed.csv",
        )

        save_processed_data(
            data,
            f"{PROCESSED_DATA_DIR}/{ticker.lower()}_processed.parquet",
        )


def run_spark_pipeline(tickers):
    spark = create_spark_session()
    spark.sparkContext.setLogLevel("ERROR")

    for ticker in tickers:
        logging.info(f"Running Spark pipeline for {ticker}")
        df = read_market_data(
            spark,
            f"{RAW_DATA_DIR}/{ticker.lower()}_raw.csv",
        )

        df = add_20ma(df)
        df = add_daily_return(df)
        df = add_spark_volatility(df)
        df = add_spark_atr(df)

        save_spark_data(
            df,
            f"{SPARK_DATA_DIR}/{ticker.lower()}_spark_processed.parquet",
        )

    spark.stop()


def main():
    logging.info("Starting trading data pipeline")

    create_output_directories()

    run_pandas_pipeline(
        TICKERS,
        START_DATE,
        END_DATE,
    )
    run_spark_pipeline(TICKERS)

    logging.info("Trading data pipeline finished")


if __name__ == "__main__":
    main()