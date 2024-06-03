import unittest
from task import my_datetime, conv_num, conv_endian


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
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_given_examples(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')
        self.assertEqual(my_datetime(9876543210), '12-22-2282')
        self.assertEqual(my_datetime(201653971200), '02-29-8360')


if __name__ == '__main__':
    unittest.main()
