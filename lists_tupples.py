"""Unpacking Lists and Tupples Example"""

# The main function:
def main():
    """The main function"""

    # Access elements of list:
    item = ["December 23, 2015", "Toy Car", 12.50]
    print(item[0])
    print(item[1])
    print(item[2])

    print("------------")


    # Unpacking list:
    date, name, price = ["December 23, 2015", "Toy Car", 12.50]
    print(date, name, price)

    print("------------")


    # Define grades:
    grades = [99, 100, 77, 85, 60, 100]

    # Drop first and last grades:
    kept_grades = drop_first_last(grades)

    # Get average of kept_grades:
    average = get_average(kept_grades)

    # Display average:
    print("The average grade is", average)



# Drop first and last grade; return middle grades:
def drop_first_last(grades):
    """Returns only the middle grades"""

    first, *middle, last = grades
    return middle


# Calculate and return average of kept grades:
def get_average(grades):
    """Returns average grade"""

    avg = sum(grades) / len(grades)
    return avg


# Call main:
main()
