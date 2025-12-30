import unittest
import hesapla

class TestCalculate(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(hesapla.topla(3, 5), 8)

    def test_multiple(self):
        self.assertEqual(hesapla.carp(2, 4), 8)
    
    #code changes for jenkins
if __name__ == '__main__':
    unittest.main()