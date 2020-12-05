import os
import unittest

from aoc.day04.day04 import count_passports_with_required_keys, count_passports_with_required_keys_and_valid_values, \
    validate_hgt

file_input = 'input/day04.txt'
file_example = 'input/day04-example.txt'
file_passport_values_invalid = 'input/day04-values-invalid.txt'
file_passport_values_valid = 'input/day04-values-valid.txt'


class TestDay04(unittest.TestCase):
    def test_04a_example(self):
        self.assertEqual(2, count_passports_with_required_keys(file_example))

    def test_04a(self):
        self.assertEqual(213, count_passports_with_required_keys(file_input))

    def test_04b_values_invalid(self):
        self.assertEqual(0, count_passports_with_required_keys_and_valid_values(file_passport_values_invalid))

    def test_04b_values_valid(self):
        self.assertEqual(4, count_passports_with_required_keys_and_valid_values(file_passport_values_valid))

    def test_04b(self):
        self.assertEqual(147, count_passports_with_required_keys_and_valid_values(file_input))

    def test_04_main(self):
        self.assertEqual(0, os.system("python -m aoc.day04.day04"))

    def test_04_validate_hgt(self):
        self.assertTrue(validate_hgt('60in'))
        self.assertTrue(validate_hgt('190cm'))
        self.assertFalse(validate_hgt('190in'))
        self.assertFalse(validate_hgt('190'))
