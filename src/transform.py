def add_daily_returns(data):
    data["Daily Return"] = (
        data["Close"].pct_change()
    )

    return data