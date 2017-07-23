"""
Unit testing module for AKS.py
"""

import unittest
from AKS import gcd, perfect_power

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

if __name__ == "__main__":
    unittest.main()
