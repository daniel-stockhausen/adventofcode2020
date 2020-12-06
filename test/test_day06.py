import os
import unittest

from aoc.day06.day06 import count_questions_answered_yes

file_input = 'input/day06.txt'
file_example = 'input/day06-example.txt'


class TestDay06(unittest.TestCase):
    def test_06a_example(self):
        self.assertEqual(11, count_questions_answered_yes(file_example))

    def test_06a(self):
        self.assertEqual(7283, count_questions_answered_yes(file_input))

    def test_06b_example(self):
        self.assertEqual(6, count_questions_answered_yes(file_example, True))

    def test_06b(self):
        self.assertEqual(3520, count_questions_answered_yes(file_input, True))

    def test_06_main(self):
        self.assertEqual(0, os.system("python -m aoc.day06.day06"))
