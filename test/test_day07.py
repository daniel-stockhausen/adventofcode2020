import os
import unittest

from aoc.day07.day07 import count_bags_from_file, bag_fits_in_bags_from_file

file_input = 'input/day07.txt'
file_example = 'input/day07-example.txt'
file_example2 = 'input/day07-example2.txt'


class TestDay07(unittest.TestCase):
    def test_07a_example(self):
        self.assertEqual(11, bag_fits_in_bags_from_file('shiny gold', file_example))

    def test_07a(self):
        self.assertEqual(7283, bag_fits_in_bags_from_file('shiny gold', file_input))

    def test_07b_example(self):
        self.assertEqual(126, count_bags_from_file('shiny gold', file_example2))

    def test_07b(self):
        self.assertEqual(6260, count_bags_from_file('shiny gold', file_input))

    # def test_07_main(self):
    #     self.assertEqual(0, os.system("python -m aoc.day07.day07"))
