# Trading Data Pipeline

A Data Engineering project that extracts financial market data,
cleans and structures raw datasets, processes them with Pandas
and PySpark, stores the results in CSV and Parquet formats,
and uploads processed Parquet output to Azure Blob Storage.

## Project Workflow

```text
Yahoo Finance
    ↓
Extract and clean raw market data
    ↓
Raw CSV Files
    ↓
Pandas Transformations
(daily returns, moving averages, volatility, ATR)
    ↓
Processed CSV / Parquet
    ↓
PySpark Transformations
(daily returns, moving averages, volatility, ATR)
    ↓
Spark Parquet Output
    ↓
Azure Blob Storage
```

## Example Output

The PySpark pipeline processes multiple market datasets and
calculates indicators such as moving averages, daily returns,
20-day volatility and ATR before storing the results as
Parquet files.

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

## Features

- Extract market data from Yahoo Finance
- Clean and structure raw market data with a dedicated `Date` column
- Process multiple market tickers using Pandas and PySpark
- Calculate daily returns
- Calculate moving averages
- Calculate 20-day volatility
- Calculate 20-day ATR (Average True Range)
- Store processed datasets in CSV and Parquet format
- Upload processed Parquet files to Azure Blob Storage
- Use a structured ETL pipeline with configurable tickers, dates and paths

## Azure Upload

The pipeline includes a reusable upload step that scans the
`data/processed/` directory and uploads all processed
Parquet files to Azure Blob Storage.

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
```

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

- Create output directories automatically when the pipeline runs
- Make the upload step reusable for different file types and containers
- Add basic validation and logging to the transformation and upload steps
- Add more market indicators, such as rolling volume
- Explore a Databricks-based version of the pipeline