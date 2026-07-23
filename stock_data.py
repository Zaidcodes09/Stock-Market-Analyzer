import yfinance as yf


def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="2y")


def get_company_name(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info.get("longName", ticker)