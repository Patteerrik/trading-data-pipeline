import pandas as pd

from src.transform import (
    add_daily_returns,
    add_moving_averages,
)


def test_add_daily_returns_creates_column():
    data = pd.DataFrame(
        {
            "Close": [100, 110, 121],
        }
    )

    result = add_daily_returns(data)

    assert "Daily_Return" in result.columns


def test_add_moving_averages_creates_columns():
    data = pd.DataFrame(
        {
            "Close": range(1, 250),
        }
    )

    result = add_moving_averages(data)

    assert "20MA" in result.columns
    assert "50MA" in result.columns
    assert "200MA" in result.columns