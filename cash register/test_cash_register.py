import unittest
from cash_register import *


class test_Change(unittest.TestCase):
    def test_min_lent(self): 
        self.assertTrue(change("R50.50"))
        self.assertFalse(change("-3"))