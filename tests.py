import unittest
from task import my_datetime


class TestMyDatetime(unittest.TestCase):
    def test_epoch(self):
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_given_examples(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')
        self.assertEqual(my_datetime(9876543210), '12-22-2282')
        self.assertEqual(my_datetime(201653971200), '02-29-8360')


if __name__ == '__main__':
    unittest.main()
