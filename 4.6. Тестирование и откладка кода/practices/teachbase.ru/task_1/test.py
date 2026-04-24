import unittest
from main import divide


class TestDivide(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(4.0, divide(16, 4))
        self.assertEqual(2.0, divide(4.0, 2.0))

    def test_zero_divined(self):
        self.assertEqual(0.0, divide(0, 30))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(15, 0)


unittest.main()
