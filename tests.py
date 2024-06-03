import unittest
import datetime
import random
from task import my_datetime, conv_num, conv_endian


def date_to_seconds(year, month, day):
    """Convert a date to the number of seconds since the epoch"""
    date = datetime.datetime(year, month, day)
    timestamp = date.timestamp()
    return int(timestamp)


def check_datetime_conversion(test_case, num_sec):
    """ Generate the expected result using datetime"""
    dt = datetime.datetime.utcfromtimestamp(num_sec)
    expected_result = f"{dt.month:02d}-{dt.day:02d}-{dt.year}"

    # Compare the result of my_datetime function to the expected result
    result = my_datetime(num_sec)
    test_case.assertEqual(
        result,
        expected_result,
        (
            f"Failed for {num_sec}: got {result}, "
            f"expected {expected_result}"
        )
    )


class TestMyDatetime(unittest.TestCase):
    def test_conv_endian_1(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_conv_endian_2(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_conv_endian_3(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_conv_endian_4(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_conv_endian_5(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_conv_endian_6(self):
        self.assertEqual(conv_endian(954786, 'other'), None)

    def test_conv_endian_7(self):
        self.assertEqual(conv_endian(0), "00")

    def test_conv_num_regular(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test_conv_num_regular_with_decimal(self):
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test_conv_num_decimal_only(self):
        self.assertEqual(conv_num('.45'), 0.45)

    def test_conv_num_regular_with_empty_decimal(self):
        self.assertEqual(conv_num('123.'), 123.0)

    def test_conv_num_working_uppercase_hex(self):
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_conv_num_working_lowercase_hex(self):
        self.assertEqual(conv_num('0Xad4'), 2772)

    def test_conv_num_working_lowercase_negative_hex(self):
        self.assertEqual(conv_num('-0Xad4'), -2772)

    def test_conv_num_incorrect_hex(self):
        self.assertEqual(conv_num('0xAZ4'), None)

    def test_conv_num_regular_with_hex(self):
        self.assertEqual(conv_num('12345A'), None)

    def test_conv_num_multiple_decimals(self):
        self.assertEqual(conv_num('12.3.45'), None)

    def test_epoch(self):
        """Tests for the epoch date"""
        check_datetime_conversion(self, 0)

    def test_given_examples_date(self):
        """ Tests for the given examples"""
        test_cases = [
            123456789,
            9876543210,
            201653971200,
        ]

        for num_sec in test_cases:
            check_datetime_conversion(self, num_sec)

    def test_random_dates(self):
        """Tests for random dates from 0 to 75 years"""
        # Total seconds in 75 years
        seconds_in_a_day = 24 * 60 * 60
        seconds_in_a_year = 365 * seconds_in_a_day
        seconds_in_leap_year = 366 * seconds_in_a_day

        num_leap_years = 75 // 4
        num_regular_years = 75 - num_leap_years

        total_seconds_in_75_years = (
            num_regular_years * seconds_in_a_year +
            num_leap_years * seconds_in_leap_year
        )

        # Generate 10 random test cases
        for _ in range(10):
            # Random seconds within 75 years
            num_sec = random.randint(0, total_seconds_in_75_years - 1)
            check_datetime_conversion(self, num_sec)

    def test_leap_dates_and_far_out_date_testing(self):
        """Tests for leap, non-leap years and leap day"""
        test_cases = [
            (1971, 1, 1),  # Non-leap year
            (1972, 1, 1),  # Leap year
            (1972, 2, 29),  # Leap day
            (2000, 1, 1),  # Leap year (Y2K)
            (2000, 2, 29),  # Leap day
            (2001, 1, 1),  # Non-leap year
            (2020, 1, 1),  # Leap year
            (2021, 1, 1),  # Non-leap year
            (2024, 1, 1),  # Leap year
            (2100, 1, 1),  # far out date
            (2500, 6, 25),  # super far out date
            (3000, 7, 26)  # extremely far out date
        ]

        for year, month, day in test_cases:
            num_sec = date_to_seconds(year, month, day)
            check_datetime_conversion(self, num_sec)

    def edge_testing(self):
        """ Tests for the edge examples"""
        test_cases = [
            1,
            59,  # last minute before first hour
            3600,  # first hour
            86399  # last second before first day ends
        ]

        for num_sec in test_cases:
            check_datetime_conversion(self, num_sec)


if __name__ == '__main__':
    unittest.main()
