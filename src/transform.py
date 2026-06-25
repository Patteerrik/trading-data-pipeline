import pandas as pd


def add_daily_returns(data):
    data["Daily_Return"] = (
        data["Close"].pct_change()
    )

    return data


def add_moving_averages(data):
    data["20MA"] = (
        data["Close"]
        .rolling(20)
        .mean()
    )

    data["50MA"] = (
        data["Close"]
        .rolling(50)
        .mean()
    )

    data["200MA"] = (
        data["Close"]
        .rolling(200)
        .mean()
    )

    return data


def add_volatility(data):
    data["Volatility_20D"] = (
        data["Daily_Return"]
        .rolling(20)
        .std()
    )

    return data


def add_atr(data):
    previous_close = data["Close"].shift(1)

    high_low = data["High"] - data["Low"]
    high_close = (data["High"] - previous_close).abs()
    low_close = (data["Low"] - previous_close).abs()

    data["True_Range"] = pd.concat(
        [
            high_low,
            high_close,
            low_close,
        ],
        axis=1,
    ).max(axis=1)

    data["ATR_20D"] = (
        data["True_Range"]
        .rolling(20)
        .mean()
    )

    return data