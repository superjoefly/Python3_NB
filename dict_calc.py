"""Calculation using Dictionary Values"""


# Description: The following program uses the zip and min
# functions to determine the minimum value in a dictionary:


# Assigns a dictionary and determines the minimum value
# in the dictionary:
def main():
    """The main function"""

    # Assign dictionary:
    stocks = {
        'GOOG': 434,
        'AAPL': 325,
        'FB': 54,
        'AMZN': 623,
        'F': 32,
        'MSFT': 549
    }

    # Get the minimum value:
    min_value = get_min_value(stocks)

    # Display the minimum value:
    print(min_value)


# Takes the stocks dictionary and returns
# the minimum value:
def get_min_value(stocks):

    # # Get minimum value by key:
    # min_value = min(zip(stocks.keys(), stocks.values()))

    # Get minimum value by value:
    min_value = min(zip(stocks.values(), stocks.keys()))

    # Return minimum value:
    return min_value


# Call main:
main()
