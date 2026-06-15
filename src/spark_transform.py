from pyspark.sql import SparkSession
from pyspark.sql.functions import col 


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


def add_test_column(df):
    df = df.withColumn(
        "Close_x2",
        col("Close") * 2,
    )

    return df


def save_spark_data(df, filepath):
    df.write.mode("overwrite").parquet(filepath)