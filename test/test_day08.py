import os
import unittest

from aoc.day08.day08 import fix_bug_get_acc, detect_inf_loop_get_acc

file_input = 'input/day08.txt'
file_example = 'input/day08-example.txt'


class TestDay08(unittest.TestCase):
    def test_08a_example(self):
        self.assertEqual(5, detect_inf_loop_get_acc(file_example))

    def test_08a(self):
        self.assertEqual(1614, detect_inf_loop_get_acc(file_input))

    def test_08b_example(self):
        self.assertEqual(8, fix_bug_get_acc(file_example))

    def test_08b(self):
        self.assertEqual(1260, fix_bug_get_acc(file_input))

    def test_08_main(self):
        self.assertEqual(0, os.system("python -m aoc.day08.day08"))
