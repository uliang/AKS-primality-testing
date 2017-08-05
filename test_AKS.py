"""
Unit testing module for AKS.py
"""

import unittest
from AKS import gcd, perfect_power, order, get_r, totient


class TestPerfectPower(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(6, 4), 2)
        self.assertEqual(gcd(13, 51), 1)
        self.assertEqual(gcd(121, 15), 1)

    def test_perfect_power(self):
        self.assertTrue(perfect_power(125))
        self.assertFalse(perfect_power(10))
        self.assertTrue(perfect_power(50**60))
        self.assertTrue(perfect_power(6**7))
        self.assertFalse(perfect_power(137))

    def test_order(self):
        self.assertEqual(order(8, 3), 2)
        self.assertEqual(order(15, 2), 4)
        self.assertEqual(order(8, 65), 1)
        self.assertEqual(order(3, 5), 2)
        self.assertFalse(order(6, 4))

    def test_get_r(self):
        self.assertEqual(get_r(31), 29)

    def test_totient(self):
        self.assertEqual(totient(1), 1)
        self.assertEqual(totient(6), 2)
        self.assertEqual(totient(8), 4)
        self.assertEqual(totient(31), 30)


if __name__ == "__main__":
    print(__doc__)
    unittest.main()
