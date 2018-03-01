# unittest for euler013.py

import unittest
import re
from euler013 import *



class Test_BNBlock(unittest.TestCase):
    def test_init(self):
        for value in (0, 111, 99999, 5725, 13, 74):
            t = BNBlock(value)
            self.assertEqual(value, t.value)
            self.assertIs(t.zero, True)
        
        for value in (-1, -150, BNBlock(0), 'string'):
            with self.assertRaises(ValueError):
                t = BNBlock(value)
    
    def test_str(self):
        for val, xstr, xbool in [(1, '00001', True), (900, '00900', True),
                                 (98765, '98765', True),
                                 (1, '1', False), (900, '900', False),
                                 (98765, '98765', False)]:
            t = BNBlock(val)
            t.zero = xbool
            self.assertEqual(str(t), xstr)
    
    def test_adder(self):
        for val1, val2, balance, result in [(90000, 10500, 1, 500), 
                                         (99999, 1, 1, 0),
                                         (99999, 99999, 1, 99998),
                                         (500, 1500, 0, 2000)]:
            b1 = BNBlock(val1)
            b2 = BNBlock(val2)
            bal = b1.adder(b2, 0)
            self.assertEqual(bal, balance)
            self.assertEqual(b1.value, result)
            b1 = BNBlock(val1)
            b1.adder(b2, 1)
            self.assertEqual(b1.value, result +1)



class Test_BigNumber(unittest.TestCase):
    def test_init_and_str(self):
        for val in ('1234567890', '123456', '1234567890987654321', 
                    '12345678909', '98766543210'):
            val2 = BigNumber(val)
            self.assertEqual(val, str(val2))
    
    def test_adder(self):
        for val1, val2, result in [('111111', '222222', '333333'),
                                   ('99999', '1', '100000'),
                                   ('90000', '9990010', '10080010')]:
            val3 = BigNumber(val1) + BigNumber(val2)
            self.assertEqual(str(val3), result)



if __name__ == '__main__':
    unittest.main()