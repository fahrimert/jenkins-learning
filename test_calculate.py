import unittest
import calculate

class TestCalculate(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculate.sum(3, 5), 8)

    def test_multiple(self):
        self.assertEqual(calculate.multiple(2, 4), 8)
    
    #code changes for jenkins
if __name__ == '__main__':
    unittest.main()