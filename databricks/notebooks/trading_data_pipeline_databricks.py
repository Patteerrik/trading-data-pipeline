# Verify that the Databricks SparkSession is available
spark

# COMMAND ----------

data = [
    ("SPY", 610.25),
    ("QQQ", 545.18),
    ("GLD", 312.40),
]

columns = ["Ticker", "Close"]

df = spark.createDataFrame(data, columns)

df.show()

# COMMAND ----------

# Load the processed SPY dataset from Databricks Unity Catalog
df = spark.table("workspace.default.spy_processed")

df.show(10)

# COMMAND ----------

df.select(
    "Date",
    "Close",
    "ATR_20D"
).show(10)

# COMMAND ----------

df.filter(
    df.Close > 500
).show()

# COMMAND ----------

from pyspark.sql.functions import round

# COMMAND ----------

df.withColumn(
    "Close_Rounded",
    round(df.Close, 0)
).select(
    "Close",
    "Close_Rounded"
).show(10)

# COMMAND ----------

df.count()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.describe().show()

# COMMAND ----------

from pyspark.sql.functions import desc

# COMMAND ----------

df.select(
    "Date",
    "Close",
    "ATR_20D"
).orderBy(
    desc("ATR_20D")
).show(10)

# COMMAND ----------

from pyspark.sql.functions import year, avg

# COMMAND ----------

df.withColumn(
    "Year",
    year("Date")
).groupBy(
    "Year"
).agg(
    avg("ATR_20D").alias("Average_ATR")
).orderBy(
    "Year"
).show()