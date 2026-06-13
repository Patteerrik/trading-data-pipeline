from pyspark.sql import SparkSession

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