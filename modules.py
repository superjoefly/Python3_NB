# The following program shows how to
# implement a module into a program:
"""Import Module Example"""

# Modules:
import greetings

# Define main:
def main():
    """The main function for module example"""

    # Call say_hello function of greetings module:
    greetings.say_hello()

    print("---------")

    # Call say_goodbye function of greetings module:
    greetings.say_goodbye()

# Call main
main()
