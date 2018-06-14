"""Calculation using Dictionary Values"""

# Define main:
def main():
    """The main function"""

    # Define dictionary:
    stocks = {
        'GOOG': 434,
        'AAPL': 325,
        'FB': 54,
        'AMZN': 623,
        'F': 32,
        'MSFT': 549
    }

    min_value = get_min_value(stocks)

    print(min_value)


def get_min_value(stocks):

    # # Get minimum value by key:
    # min_value = min(zip(stocks.keys(), stocks.values()))

    # Get minimum value by value:
    min_value = min(zip(stocks.values(), stocks.keys()))

    # Return minimum value:
    return min_value


# Call main:
main()
