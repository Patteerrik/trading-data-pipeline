# Databricks notebook source
# MAGIC %md
# MAGIC ## Trading Data Pipeline
# MAGIC
# MAGIC ### Databricks Analysis
# MAGIC
# MAGIC This notebook demonstrates an end-to-end PySpark workflow in Databricks.
# MAGIC
# MAGIC Starting from processed market data, the notebook performs:
# MAGIC
# MAGIC - **Loading** processed market data
# MAGIC - **Exploring** the dataset
# MAGIC - **Applying** Spark transformations
# MAGIC - **Calculating** yearly ATR statistics
# MAGIC - **Saving** the results as a Delta table

# COMMAND ----------

# Verify that the Databricks SparkSession is available
spark

# COMMAND ----------

# Load the processed SPY dataset from Unity Catalog
df = spark.table("workspace.default.spy_processed")

# Display the first 10 rows
df.show(10)

# COMMAND ----------

# Select the columns used in the analysis
df.select(
    "Date",
    "Close",
    "ATR_20D"
).show(10)

# COMMAND ----------

# Filter days where the closing price is above 500
df.filter(
    df.Close > 500
).show()

# COMMAND ----------

# Import the round function
from pyspark.sql.functions import round

# COMMAND ----------

# Create a rounded version of the closing price
df.withColumn(
    "Close_Rounded",
    round(df.Close, 0)
).select(
    "Close",
    "Close_Rounded"
).show(10)

# COMMAND ----------

# Count the number of rows
df.count()

# COMMAND ----------

# Display the DataFrame schema
df.printSchema()

# COMMAND ----------

# Generate descriptive statistics
df.describe().show()

# COMMAND ----------

# Import descending sort
from pyspark.sql.functions import desc

# COMMAND ----------

# Identify the periods with the highest market volatility
df.select(
    "Date",
    "Close",
    "ATR_20D"
).orderBy(
    desc("ATR_20D")
).show(10)

# COMMAND ----------

# Calculate the average ATR for each year
from pyspark.sql.functions import year, avg

yearly_atr_summary = (
    df.withColumn(
        "Year",
        year("Date")
    )
    .groupBy("Year")
    .agg(
        avg("ATR_20D").alias("Average_ATR")
    )
    .orderBy("Year")
)

yearly_atr_summary.show()

# COMMAND ----------

# Save the yearly summary as a Delta table
yearly_atr_summary.write.mode("overwrite").saveAsTable(
    "workspace.default.yearly_atr_summary"
)

# COMMAND ----------

# Verify the saved Delta table
spark.table(
    "workspace.default.yearly_atr_summary"
).show()