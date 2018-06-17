"""heapq Example"""


# Description: The following program uses the heapq module:


# Import modules:
import heapq

# Constants:
LEVEL = 3


# Define main:
def main():
    """Main Function"""

    # Get highest grades in list of grades:
    get_highest_grades()

    # Get cheapest stocks in dictionary of stocks:
    get_cheapest_stocks()



def get_highest_grades():
    """Gets highest grades in list of grades"""

    print("Determine the highest", LEVEL, \
    "grades in a list of grades.")

    print()

    # Get a list of grades from the user:
    grades = []

    # Loop to collect grades:
    keep_going = True
    while keep_going:
        # Get valid user input:
        grade = validate_grade()
        if grade == 'exit':
            keep_going = False
        else:
            # Append grades to list:
            grades.append(grade)

    # Get 3 highest grades:
    three_highest_grades = heapq.nlargest(LEVEL, grades)

    # Display 3 highest grades:
    print(three_highest_grades)

    print("--------------------------")



# Validates user input for grades:
def validate_grade():
    """Validates user input for grades"""

    # Checks if number is from 0 to 100:
    is_valid_score = lambda n: 0 <= n <= 100

    # Get user input for grade:
    grade = input("Enter a grade or 'exit' to see result: ")

    # Loop to validate input:
    while True:
        try:
            # Check if input is a number:
            grade = float(grade)
            # Check if number is from 0 to 100:
            if is_valid_score(grade):
                # If it's a valid number, return it:
                return grade
            # If it's not a valid number:
            else:
                print("The score has to be from 0 to 100...")
                grade = input("Enter a grade: ")
        # If it's not a number:
        except ValueError:
            if grade == 'exit':
                return grade
            else:
                print("Please enter a valid grade or 'exit' to continue...")
                grade = input("Enter a grade: ")



# Get cheapest stocks:
def get_cheapest_stocks():
    """Gets cheapest stocks in dictionary of stocks"""

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
