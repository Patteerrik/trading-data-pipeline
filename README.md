# Trading Data Pipeline

A Data Engineering project that extracts financial market data,
processes it using Pandas and PySpark, and stores the results in
CSV and Parquet formats.

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
│   └── spark_transform.py
│
├── main.py
└── README.md
```

## Planned Improvements

- Add additional market indicators such as ATR or rolling volume metrics
- Expand the PySpark pipeline with more transformations and output validation
- Explore a cloud-based version of the pipeline using Azure or Databricks