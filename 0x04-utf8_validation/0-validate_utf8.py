def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        # If num_bytes is 0, then this is a new character
        if num_bytes == 0:
            # Determine the number of bytes in the character
            if (byte & mask1) == 0:
                continue  # 1-byte character
            elif (byte & (mask1 >> 1)) == 0:
                num_bytes = 1  # 2-byte character
            elif (byte & (mask1 >> 2)) == 0:
                num_bytes = 2  # 3-byte character
            elif (byte & (mask1 >> 3)) == 0:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 character
        else:
            # If num_bytes > 0, check if the current byte is a continuation byte (starts with '10')
            if (byte & mask1) == 0 or (byte & mask2) != 0:
                return False
            num_bytes -= 1

    # If all characters were valid, num_bytes should be 0 at the end
    return num_bytes == 0
