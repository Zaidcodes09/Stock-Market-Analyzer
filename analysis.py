def analyze_stock(data):

    data["MA50"] = data["Close"].rolling(50).mean()
    data["MA200"] = data["Close"].rolling(200).mean()

    data["Daily Return"] = data["Close"].pct_change()

    result = {
        "price": round(data["Close"].iloc[-1], 2),
        "ma50": round(data["MA50"].iloc[-1], 2),
        "ma200": round(data["MA200"].iloc[-1], 2),
        "volatility": round(data["Daily Return"].std() * 100, 2)
    }

    return data, result