"""Example of Min, Max and Sorting for Dictionaries"""

# The main function defines a dictionary and uses the zip function
# to convert to a list of tupples. Then we use the min, max and
# sorted functions to display min, max and sorted values.

# Define main:
def main():
    """The main function"""

    emp_wages = {
        'John': 50.00,
        'Brian': 75.00,
        'Craig': 85.00,
        'Hank': 95.00,
        'Doug': 45.00
    }

    # Zip the dictionary and convert to list of tupples:
    wages = list(zip(emp_wages.values(), emp_wages.keys()))

    # Display list of tupples:
    print(wages)

    # Display first value of each tupple:
    for tup in wages:
        print(tup[0])

    # The following functions operate according to first value
    # in tupple. We can also use min, max and sort on alphabetical
    # data by switching the position of keys and values above
    # during zip.

    # Display min value:
    print(min(wages))

    # Display max value:
    print(max(wages))

    # Display sorted values:
    print(sorted(wages))


# Call main:
main()
