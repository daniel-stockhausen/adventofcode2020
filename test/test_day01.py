import unittest

from aoc.day01.day01 import product_of_2_summands_of_sum, product_of_3_summands_of_sum

file_input = 'input/day01.txt'
file_example = 'input/day01-example.txt'


class TestDay01(unittest.TestCase):
    def test_01a_example(self):
        self.assertEqual(514579, product_of_2_summands_of_sum(file_example, 2020))

    def test_01a(self):
        self.assertEqual(691771, product_of_2_summands_of_sum(file_input, 2020))

    def test_01b_example(self):
        self.assertEqual(241861950, product_of_3_summands_of_sum(file_example, 2020))

    def test_01b(self):
        self.assertEqual(232508760, product_of_3_summands_of_sum(file_input, 2020))
