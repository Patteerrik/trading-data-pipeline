def save_raw_data(data, filepath):
    data.to_csv(filepath)

def save_processed_data(data, filepath):
    data.to_parquet(filepath)