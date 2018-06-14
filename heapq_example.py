"""heapq Example"""


# Description: the following program uses the heapq module
# to determine the highest grades in a list:


# Import modules:
import heapq


# Define main:
def main():
    """Main Function"""

    print("The following program will determine the highest grades\n" \
    "in a list of grades according to the user's specifications:")

    print()

    level = int(input("How many highest grades would you like to view? "))

    # Get a list of grades from the user:



    # Get 3 highest grades:
    three_highest_grades = heapq.nlargest(level, grades)

    # Display 3 highest grades:
    print(three_highest_grades)

    print("--------------------------")




    # ## Iterate through list of dictionaries:
    # # Assign stocks:
    # stocks = [
    #     {'ticker': 'AAPL', 'price': 201},
    #     {'ticker': 'GOOG', 'price': 800},
    #     {'ticker': 'F', 'price': 54},
    #     {'ticker': 'MSFT', 'price': 313},
    #     {'ticker': 'TUNA', 'price': 68}
    # ]
    #
    # # Get 2 cheapest stocks:
    # two_cheapest_stocks = heapq.nsmallest(2, stocks, key=lambda stock: stock['price'])
    #
    # # Display 2 cheapest stocks:
    # print(two_cheapest_stocks)


# Call main:
main()
