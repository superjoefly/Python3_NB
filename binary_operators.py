"""Binary Operator Examples"""

# Define main:
def main():
    """The main function"""

    # Binary Number Explanation:
    # Each bit represents a number: 32, 16, 8, 4, 2, 1

    # 0 = bit is off
    # 1 = bit is on

    # 25 = 011001 (From right to left: 1 is on, 2 is off, 4 is off
    # 8 is on, 16 is on, 32 is off ) (8 + 16 + 1 = 25)

    ##############################

    # Binary AND Operator
    a = 50      # 110010
    b = 25      # 011001
    c = a & b   # 010000
    print(c)    # 16



    # Binary RIGHT SHIFT Operator (shift two places to right)
    x = 240     # 11110000
    y = x >> 2  # 00111100
    print(y)    # 60



    # Binary LEFT SHIFT Operator (shift two places to left)
    x = 240     # 11110000
    y = x << 2  # 1111000000
    print(y)    # 960


# Call main:
main()
