"""Get smallest and largest values using heapq"""

# Import modules:
import heapq

# Define main:
def main():
    """heapq example"""

    ## Iterate through list:
    # Assign grades:
    grades = [99, 85, 100, 97, 98, 75]

    # Get 3 highest grades:
    three_highest_grades = heapq.nlargest(3, grades)

    # Display 3 highest grades:
    print(three_highest_grades)

    print("--------------------------")




    ## Iterate through list of dictionaries:
    # Assign stocks:
    stocks = [
        {'ticker': 'AAPL', 'price': 201},
        {'ticker': 'GOOG', 'price': 800},
        {'ticker': 'F', 'price': 54},
        {'ticker': 'MSFT', 'price': 313},
        {'ticker': 'TUNA', 'price': 68}
    ]

    # Get 2 cheapest stocks:
    two_cheapest_stocks = heapq.nsmallest(2, stocks, key=lambda stock: stock['price'])

    # Display 2 cheapest stocks:
    print(two_cheapest_stocks)


# Call main:
main()
