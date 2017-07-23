"""
Unit testing module for AKS.py
"""

import unittest
from AKS import gcd, perfect_power, ord, get_r

class TestPerfectPower(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(6,4), 2)
        self.assertEqual(gcd(13,51), 1)
        self.assertEqual(gcd(121,15), 1)

    def test_perfect_power(self):
        self.assertTrue(perfect_power(125))
        self.assertFalse(perfect_power(10))
        self.assertTrue(perfect_power(50**60))
        self.assertTrue(perfect_power(6**7))
        self.assertFalse(perfect_power(137))

    def test_ord(self):
        self.assertEqual(ord(8,3), 2)
        self.assertEqual(ord(15,2), 4)
        self.assertEqual(ord(8, 65), 1)
        self.assertEqual(ord(3, 5), 2)
        self.assertFalse(ord(6, 4))

    def test_get_r(self):
        self.assertEqual(get_r(31), 29)


if __name__ == "__main__":
    unittest.main()
