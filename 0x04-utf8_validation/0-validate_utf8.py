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
            # Determine how many bytes
            if (byte & mask1) == 0:
                # 1-byte character (ASCII)
                continue
            elif (byte & (mask1 >> 1)) == 0:
                return False
            while (byte & mask1):
                num_bytes += 1
                mask1 >>= 1

            # The first byte of a UTF-8 character
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining
        num_bytes -= 1

    # If there are leftover bytes, return False
    return num_bytes == 0
