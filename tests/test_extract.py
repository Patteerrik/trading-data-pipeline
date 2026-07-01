import pandas as pd
import pytest

from src.extract import validate_market_data


def test_validate_market_data_accepts_valid_data():
    data = pd.DataFrame(
        {
            "Date": ["2025-01-01"],
            "Open": [100],
            "High": [110],
            "Low": [95],
            "Close": [105],
            "Volume": [1000000],
        }
    )

    validate_market_data(data, "SPY")


def test_validate_market_data_raises_error_for_empty_data():
    data = pd.DataFrame()

    with pytest.raises(ValueError, match="No data returned for SPY"):
        validate_market_data(data, "SPY")


def test_validate_market_data_raises_error_for_missing_columns():
    data = pd.DataFrame(
        {
            "Date": ["2025-01-01"],
            "Open": [100],
            "High": [110],
            "Low": [95],
            "Close": [105],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_market_data(data, "SPY")