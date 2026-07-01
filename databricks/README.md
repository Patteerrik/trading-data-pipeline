# Databricks Integration

This folder contains the Databricks part of the Trading Data Pipeline project.

The goal is to extend the local PySpark pipeline by analyzing processed market data in Databricks as part of a cloud-based data engineering workflow.

Databricks is currently used to analyze processed Parquet data after it has been imported into a Delta table. The next planned step is to connect Databricks directly to Azure Blob Storage using a production-style authentication setup.

## Current Workflow

```text
Processed Parquet Files
        ↓
Manual Upload
        ↓
Delta Table
        ↓
Databricks Notebook
        ↓
PySpark Analysis
```

## Planned Workflow

```text
Processed Parquet Files
        ↓
Azure Blob Storage
        ↓
Databricks
        ↓
PySpark Analysis
```

## Current Progress

The Databricks notebook currently demonstrates:

- Loading processed market data
- Creating a Delta table
- Reading data with Apache Spark
- Selecting and filtering data
- Creating new columns with `withColumn()`
- Sorting data with `orderBy()`
- Aggregating data with `groupBy()`
- Calculating yearly average ATR values

## Notebook

```text
databricks/notebooks/trading_data_pipeline_databricks.py
```