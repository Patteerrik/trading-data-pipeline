import os
from pathlib import Path

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


load_dotenv()


def upload_directory(directory_path, container_name):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    if not connection_string:
        raise ValueError("Missing AZURE_STORAGE_CONNECTION_STRING")

    directory_path = Path(directory_path)

    if not directory_path.exists():
        raise FileNotFoundError(
            f"Directory not found: {directory_path}"
        )

    parquet_files = list(directory_path.glob("*.parquet"))

    if not parquet_files:
        raise FileNotFoundError(
            f"No parquet files found in {directory_path}"
        )

    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string
    )

    for file_path in parquet_files:
        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob=file_path.name,
        )

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Uploaded {file_path.name} to {container_name}")


if __name__ == "__main__":
    upload_directory(
        "data/processed",
        "processed-data",
    )