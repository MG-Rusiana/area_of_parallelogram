#!/usr/bin/env python3

import unittest




def area_parallelogram(b, h):
    return b * h



class Test(unittest.TestCase):

    # test for positive
    def test_positive_numbers(self):
        result = area_parallelogram(2, 3)
        self.assertEqual(result, 6)

    # test for negative
    def test_negative_numbers(self):
        result = area_parallelogram(-4, 5)
        self.assertEqual(result, -20)

    # test for zero
    def test_zero(self):
        result = area_parallelogram(10, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()