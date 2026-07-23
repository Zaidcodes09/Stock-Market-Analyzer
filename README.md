Stock Market Analyzer

A Python application that analyzes real-world stock market data using technical indicators and machine learning.

The program downloads historical stock data from Yahoo Finance, calculates moving averages and volatility, predicts short-term market direction with a Random Forest machine learning model, and displays the results in a graphical dashboard.

---

## Features

- Download live stock market data
- Technical analysis
  - Current stock price
  - 50-day moving average
  - 200-day moving average
  - Daily volatility
- Machine learning market prediction
- AI confidence score
- Interactive stock price graph
- Simple graphical dashboard

---

## Technologies Used

- Python
- yfinance
- pandas
- matplotlib
- scikit-learn
- NumPy
- Tkinter

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Stock-Market-Analyzer.git
```

Go into the project:

```bash
cd Stock-Market-Analyzer
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it.

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Program

Run:

```bash
python main.py
```

Enter a stock ticker when prompted.

Example:

```
AAPL
```

Other examples:

- MSFT
- NVDA
- TSLA
- GOOGL
- AMZN

---

## Project Structure

```
Stock-Market-Analyzer/
│
├── main.py
├── stock_data.py
├── analysis.py
├── ml_model.py
├── dashboard.py
├── graphs.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Example Output

The application displays:

- Company name
- Current stock price
- 50-day moving average
- 200-day moving average
- Volatility
- AI market prediction
- AI confidence score
- Stock price graph

---

## License

This project is licensed under the MIT License.
