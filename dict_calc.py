"""Perform Calculation on Dictionary Values"""


def main():
    """Performs Calculation on Dictionary Values"""

    # Assign stocks dictionary:
    stocks = {
        'GOOG': 434,
        'AAPL': 325,
        'FB': 54,
        'AMZN': 623,
        'F': 32,
        'MSFT': 549
    }


    # Get minimum stock by value:
    min_price = min(zip(stocks.values(), stocks.keys()))

    # Display minimum stock:
    print(min_price)

main()
