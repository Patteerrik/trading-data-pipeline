# Trading Data Pipeline

A Data Engineering project that extracts financial market data,
processes it with Pandas and PySpark, stores the results in
CSV and Parquet formats, and uploads processed Parquet output
to Azure Blob Storage.

## Project Workflow

```text
Yahoo Finance
    ↓
Extract Data
    ↓
Raw CSV Files
    ↓
Pandas Transformations
    ↓
Processed CSV / Parquet
    ↓
PySpark Transformations
    ↓
Spark Parquet Output
    ↓
Azure Blob Storage
```

## Example Output

The PySpark pipeline processes multiple market datasets and
calculates indicators such as moving averages, daily returns
and 20-day volatility before storing the results as Parquet files.

![PySpark Output](assets/pyspark_output.png)

## Sample Dataset

Tickers:
- SPY (S&P 500 ETF)
- QQQ (Nasdaq 100 ETF)
- GLD (Gold ETF)
- TLT (20+ Year Treasury Bond ETF)

Period:
- 2020-01-01 to 2025-12-31

## Features

- Extract market data from Yahoo Finance
- Process multiple market tickers using both Pandas and PySpark
- Calculate daily returns using Pandas
- Calculate daily returns using PySpark
- Calculate moving averages using Pandas
- Calculate moving averages using PySpark
- Calculate 20-day volatility using Pandas
- Calculate 20-day volatility using PySpark
- Store datasets in CSV format
- Store datasets in Parquet format
- Structured ETL pipeline
- Upload processed Parquet files to Azure Blob Storage

## PySpark Output

The PySpark pipeline currently processes the following tickers:

- SPY
- QQQ
- GLD
- TLT

Each ticker is stored as a separate Parquet output in:

```text
data/spark/
├── spy_spark_processed.parquet
├── qqq_spark_processed.parquet
├── gld_spark_processed.parquet
└── tlt_spark_processed.parquet

## Technologies

- Python
- Pandas
- PySpark
- PyArrow
- yfinance
- Azure Blob Storage
- python-dotenv
- azure-storage-blob
- GitHub Codespaces

## Project Structure

```text
trading-data-pipeline/
│
├── assets/
│   └── pyspark_output.png
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── spark/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── spark_transform.py
│   └── upload_to_azure.py
│
├── main.py
└── README.md
```

## Planned Improvements

- Support uploading multiple processed files to Azure Blob Storage
- Make the upload step reusable for different file types and containers
- Add basic validation and logging to the transformation and upload steps
- Add more market indicators, such as ATR and rolling volume
- Expand the PySpark pipeline with additional transformations
- Explore a Databricks-based version of the pipeline