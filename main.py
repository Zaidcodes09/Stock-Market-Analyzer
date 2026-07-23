from stock_data import get_stock_data, get_company_name
from analysis import analyze_stock
from ml_model import train_model, predict_market
from graphs import create_graph
from dashboard import create_dashboard


ticker = input("Enter stock ticker: ").upper()

data = get_stock_data(ticker)

if data.empty:
    print("Invalid ticker")
    exit()


company = get_company_name(ticker)

data, results = analyze_stock(data)

model = train_model(data)

prediction, confidence = predict_market(model, data)

create_dashboard(
    company,
    results,
    prediction,
    confidence
)

create_graph(
    data,
    ticker
)