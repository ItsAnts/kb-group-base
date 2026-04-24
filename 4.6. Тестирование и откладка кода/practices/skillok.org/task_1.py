import unittest

def multiply(a, b):
    result = a * b 
    return result

class MultiplyTest(unittest.TestCase):
    def test_mulit(self):
        self.assertEqual(multiply(6, 2), 12)
    

