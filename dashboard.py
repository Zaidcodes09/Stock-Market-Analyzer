import tkinter as tk


def create_dashboard(company, results, prediction, confidence):

    window = tk.Tk()

    window.title("Stock Market Analyzer")
    window.geometry("500x500")

    text = f"""
{company}

Current Price: ${results['price']}

50 Day Average: ${results['ma50']}

200 Day Average: ${results['ma200']}

Volatility: {results['volatility']}%

Market Trend: {prediction}

AI Confidence: {confidence}%
"""

    label = tk.Label(
        window,
        text=text,
        font=("Arial", 14)
    )

    label.pack(pady=50)

    window.mainloop()