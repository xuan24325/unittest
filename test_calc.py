import unittest
import calc

class TestCalc(unittest.TestCase):
    '''Test calc.py'''
    def test_add(self):
        '''Test method add(x,y)'''
        result = calc.add(10, 5)
        self.assertEqual(result,15)
        

if __name__ == '__main__':
    unittest.main()
