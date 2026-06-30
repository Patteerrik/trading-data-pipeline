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
````
