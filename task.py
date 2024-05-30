def my_datetime(num_sec):
    """Takes an integer value that represents the number of seconds since the
    epoch and returns it as a string with the following format: MM-DD-YYYY"""

    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
    SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    DAYS_IN_LEAP_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate the total number of days since the epoch
    total_days = num_sec // SECONDS_PER_DAY

    # helper function that returns whether a year is a leap year
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # Determines the year
    year = 1970
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if total_days >= days_in_year:
            total_days -= days_in_year
            year += 1
        else:
            break

    # Determine which days we use depending on Leap Year status
    if is_leap_year(year):
        days_in_month = DAYS_IN_LEAP_MONTH
    else:
        days_in_month = DAYS_IN_MONTH

    # Determines the month
    month = 1
    for days in days_in_month:
        if total_days >= days:
            total_days -= days
            month += 1
        else:
            break

    # Determines the day
    day = total_days + 1

    # Return the result in the proper format: MM-DD-YYYY
    return f"{month:02d}-{day:02d}-{year}"


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
