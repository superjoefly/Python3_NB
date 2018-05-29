"""Zip list example"""

# The main function:
def main():
    """The main function"""
    first_names = ['John', 'Chris', 'Kyle']
    last_names = ['Goodman', 'Rock', 'Evans']

    # Zip lists can only be iterated one time:
    # full_names = zip(first_names, last_names)

    # To iterate more than once, convert to list:
    full_names = list(zip(first_names, last_names))

    for name in full_names:
        print(name)

    print("----------")

    for a, b in full_names:
        print(a, b)

# Call main:
main()
