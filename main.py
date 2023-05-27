#!/usr/bin/env python3
import unittest



def area_parallelogram(b, h):
    return b * h



class TestParallelogramArea(unittest.TestCase):

    def test_positive_values(self):
        result = area_parallelogram(5, 3)
        self.assertEqual(result, 15)

    def test_zero_base(self):
        result = area_parallelogram(0, 10)
        self.assertEqual(result, 0)

    def test_zero_height(self):
        result = area_parallelogram(7, 0)
        self.assertEqual(result, 0)

    def test_negative_values(self):
        result = area_parallelogram(-4, 6)
        self.assertEqual(result, -24)


if __name__ == '__main__':
    unittest.main()