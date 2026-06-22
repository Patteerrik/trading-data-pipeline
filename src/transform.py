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