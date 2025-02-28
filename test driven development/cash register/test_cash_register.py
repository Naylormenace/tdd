import unittest
from cash_register import *


class test_Change(unittest.TestCase):
    def test_change(self): 
        self.assertTrue(change({50 : 1,}))
        self.assertFalse(change("-3"))