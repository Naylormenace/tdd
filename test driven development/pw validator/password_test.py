import unittest
from password_validator import *


class test_Password(unittest.TestCase):
    def test_min_lent(self): 
        self.assertTrue(min_lent("Qwerty17!"))
        self.assertFalse(min_lent("123"))

    def test_uppercase(self): 
        self.assertTrue(uppercase("Q"))
        self.assertFalse(uppercase("q"))

    def test_lowercase(self): 
        self.assertTrue(lowercase("q"))
        self.assertFalse(lowercase("Q"))

    def test_number(self): 
        self.assertTrue(number("5"))
        self.assertFalse(number("g"))

    def test_special(self): 
        self.assertTrue(special("!"))
        self.assertFalse(special("xj "))