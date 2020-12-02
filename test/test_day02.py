import unittest

from aoc.day02.day02 import count_valid_passwords_pt1, count_valid_passwords_pt2


class TestDay02(unittest.TestCase):
    def test_02a_example(self):
        self.assertEqual(2, count_valid_passwords_pt1('../input/day02-example.txt'))

    def test_02a(self):
        self.assertEqual(625, count_valid_passwords_pt1('../input/day02.txt'))

    def test_02b_example(self):
        self.assertEqual(1, count_valid_passwords_pt2('../input/day02-example.txt'))

    def test_02b(self):
        self.assertEqual(391, count_valid_passwords_pt2('../input/day02.txt'))
