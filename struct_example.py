"""Struct - Packing and Unpacking Bytes Data"""

from struct import *


# Define main:
def main():
    """The main function"""

    # Store as bytes data (int, int, float):
    packed_data = pack('iif', 5, 4, 3.33)

    # Display bytes data:
    print(packed_data)

    # Display bytes size:
    print(calcsize('i'))
    print(calcsize('if'))
    print(calcsize('iif'))

    # Unpack to human-readable data:
    unpacked_data = unpack('iif', packed_data)
    print(unpacked_data)
    print('----------------------------')
    print(unpack('iif', b'\x05\x00\x00\x00\x04\x00\x00\x00\xb8\x1eU@'))


# Call main:
main()
