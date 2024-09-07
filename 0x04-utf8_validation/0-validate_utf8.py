#!/usr/bin/python3
"""
Module to validate UTF-8 encoding
"""

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to identify the leading bits of a byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Loop through each integer in the data list
    for num in data:
        # Mask to get only the 8 least significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine how many bytes are in the current UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check that the byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
        num_bytes -= 1

    # If there are leftover bytes, return False
    return num_bytes == 0
