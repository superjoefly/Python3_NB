"""Examples of Exceptions and Error Handling"""


# Description: The following program uses exceptions and error
# handling to validate user input for an integer:


# Validates user input as an integer:
def main():
    """The main function"""

    # Get a valid number from the user:
    number = validate_number()

    # Display message that number is valid:
    print("The number", number, "is valid!")


# Validates and returns an integer:
def validate_number():
    """Validate number"""

    # Loop to validate number:
    while True:
        try:
            # Convert value to integer:
            number = int(input("Enter a number: "))
            print(18 / number)
            # Break out of the loop:
            break
        # Handle value error:
        except ValueError:
            # Display a message:
            print()
            print("That's not a number! Try again...")
            # Continue to loop:
            # continue
        # Handle zero division error:
        except ZeroDivisionError:
            print()
            print("You cannot divide a number by zero!")
            # continue
        # Handle any unknown error:
        except:
            print()
            print("Handling unknown error...")
            break
        # Display message no matter what:
        finally:
            print()
            print("I will display no matter what!")

    return number


# Call main:
main()
