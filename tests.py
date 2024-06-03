import unittest
import datetime
import random
from task import my_datetime, conv_num


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
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_given_examples(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')
        self.assertEqual(my_datetime(9876543210), '12-22-2282')
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

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


if __name__ == '__main__':
    unittest.main()
