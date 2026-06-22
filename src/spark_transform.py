from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, lag, stddev
from pyspark.sql.window import Window


def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("TradingPipeline")
        .getOrCreate()
    )

    return spark


def read_market_data(spark, filepath):
    df = spark.read.csv(
        filepath,
        header=True,
        inferSchema=True,
    )

    return df


def save_spark_data(df, filepath):
    df.write.mode("overwrite").parquet(filepath)


def add_20ma(df):
    window_spec = (
        Window
        .orderBy("Price")
        .rowsBetween(-19, 0)
    )

    df = df.withColumn(
        "20MA_Spark",
        avg("Close").over(window_spec),
    )

    return df


def add_daily_return(df):
    window_spec = (
        Window
        .orderBy("Price")
    )

    df = df.withColumn(
        "Previous_Close",
        lag("Close").over(window_spec),
    )

    df = df.withColumn(
        "Daily_Return_Spark",
        (
            (col("Close") - col("Previous_Close"))
            / col("Previous_Close")
        ),
    )

    return df


def add_spark_volatility(df):
    window_spec = (
        Window
        .orderBy("price")
        .rowsBetween(-19, 0)
    )

    df = df.withColumn(
        "Volatility_20D_Spark",
        stddev("Daily_Return_Spark").over(window_spec),
    )

    return df