def my_func():
    return "Hello World"


def conv_hex(num) -> str:
    """Takes input integer and returns a string containing it's
    hexadecimal value"""

    hex = ''
    hex_digits = "0123456789ABCDEF"
    dividend = abs(num)
    remainder = 0
    count = 0

    # Do some math
    while dividend > 16:
        remainder = int(((dividend / 16) - int(dividend / 16)) * 16)
        dividend = int(dividend / 16)

        hex = hex_digits[remainder] + hex
        count += 1

        # Add spaces between each byte
        if count % 2 == 0:
            hex = " " + hex

    hex = hex_digits[dividend] + hex

    # Add leading zero if needed
    if len(hex) % 2 != 0:
        hex = "0" + hex
    return hex


def conv_endian(num, endian="big"):
    """Takes an integer and endian (either 'big' or 'little') and
    returns a string with the hexadecimal value in the correct endian order"""
    result = ''

    # If endian isn't 'big' or 'little', return None
    if endian != 'big' and endian != 'little':
        return None

    # If num is less then 0, add negative sign to result
    if num < 0:
        result += "-"

    # Convert from int to hex string
    hex_num = conv_hex(num)

    # Put hex into result with correct endian-ness
    if endian == "little":
        hex_array = hex_num.split(" ")
        hex_num = ""
        hex_array.reverse()
        for i in range(len(hex_array) - 1):
            hex_num += hex_array[i] + " "
        hex_num += hex_array[i + 1]

    result += hex_num
    return result
