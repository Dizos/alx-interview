#!/usr/bin/python3

def validUTF8(data):
    bytes_remaining = 0
    for num in data:
        byte = num & 0xFF
        if bytes_remaining == 0:
            if (byte & 0x80) == 0:
                # 1-byte character
                pass
            elif (byte & 0xE0) == 0xC0:
                # 2-byte character
                bytes_remaining = 1
            elif (byte & 0xF0) == 0xE0:
                # 3-byte character
                bytes_remaining = 2
            elif (byte & 0xF8) == 0xF0:
                # 4-byte character
                bytes_remaining = 3
            else:
                # Invalid start byte
                return False
        else:
            # Check for continuation byte
            if (byte & 0xC0) != 0x80:
                return False
            bytes_remaining -= 1
    # Valid only if all characters are complete
    return bytes_remaining == 0
