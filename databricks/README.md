# Databricks Integration

This folder documents the Databricks part of the Trading Data Pipeline project.

The goal is to extend the existing local PySpark pipeline by running Spark-based processing in Databricks and connecting the project to a cloud-based data engineering workflow.

## Planned Databricks Workflow

```text
Processed Parquet Files
        ↓
Azure Blob Storage
        ↓
Databricks Notebook
        ↓
PySpark Transformations / Validation
        ↓
Databricks Output
```

## Current Progress

The project now includes a Databricks notebook demonstrating basic Spark operations on processed market data.

Current functionality includes:

- Loading processed Parquet data into Databricks
- Creating a Delta table
- Reading data using Spark
- Selecting specific columns
- Filtering rows
- Creating new columns with `withColumn()`
- Sorting data with `orderBy()`
- Aggregating data with `groupBy()`
- Calculating yearly average ATR values

## Notebook

```text
databricks/notebooks/trading_data_pipeline_databricks.py
```
