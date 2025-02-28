import unittest
from number_representations import to_roman_numeral


class TestToRomanNumeral(unittest.TestCase):
    def test_to_roman_numeral_1(self):
        self.assertTrue(to_roman_numeral("I"))
        self.assertFalse(to_roman_numeral("1"))

if __name__ == '__main__':
    unittest.main()

        