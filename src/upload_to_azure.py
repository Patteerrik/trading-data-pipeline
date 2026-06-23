import os
from pathlib import Path

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


load_dotenv()


def upload_file(file_path, container_name):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    if not connection_string:
        raise ValueError("Missing AZURE_STORAGE_CONNECTION_STRING")

    file_path = Path(file_path)

    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string
    )

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=file_path.name,
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"Uploaded {file_path.name} to {container_name}")


if __name__ == "__main__":
    upload_file(
        "data/processed/spy_processed.parquet",
        "processed-data",
    )