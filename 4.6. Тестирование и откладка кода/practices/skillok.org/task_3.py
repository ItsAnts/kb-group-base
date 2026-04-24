"""
Напишите функцию, которая возвращает длину строки, и протестируйте её на строках разной длины
"""
import unittest

def len_string(string: str) -> int:
    return len(string)


class LenStringTest(unittest.TestCase):
    
    def test_len_string(self):
        self.assertEqual(len_string("Hello"), 5)
        self.assertEqual(len_string("message"), 7)

