"""Example of using map function"""

# Define the main function:
def main():
    """Double's values of income list:"""

    # Define income (list of dallar amounts):
    income = [25, 88, 79]

    # Use the map function to double each value in
    # the income list; convert to list:
    doubled_income = list(map(double_income, income))

    # Display doubled values:
    print(doubled_income)


# Define doubel_income function:
def double_income(dollars):
    """Doubles a value"""

    # Return value doubled:
    return dollars * 2

# Call main:
main()
