import matplotlib.pyplot as plt


def create_graph(data, ticker):

    plt.figure(figsize=(10, 5))

    plt.plot(data["Close"], label="Price")
    plt.plot(data["MA50"], label="MA50")
    plt.plot(data["MA200"], label="MA200")

    plt.title(ticker + " Stock Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()

    plt.show()