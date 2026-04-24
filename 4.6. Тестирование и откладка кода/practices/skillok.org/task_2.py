"""
Запустите следующий код и исправьте его:
def sum_list(lst): 
    total = 0;
    for i in range(len(lst) + 1): 
        total += lst[i]; return total. 
    Ожидается результат 6
"""
import unittest

def sum_list(lst: list) -> int:
    total: int = 0
    for i in range(len(lst)):
        total += lst[i]
    return total
    
class SumListTest(unittest.TestCase):
    
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)


unittest.main()