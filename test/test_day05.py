import os
import unittest

from aoc.day05.day05 import Seat, extract_seats, highest_seat_id, find_missing_seat_id_with_neighbors

file_input = 'input/day05.txt'
file_example = 'input/day05-example.txt'
file_invalid_cmd = 'input/day05-invalid-cmd.txt'


class TestDay05(unittest.TestCase):
    def test_05a_example_compare_seats(self):
        expected_seats = (
            Seat(44, 5, 357),
            Seat(70, 7, 567),
            Seat(14, 7, 119),
            Seat(102, 4, 820),
        )

        self.assertEqual(expected_seats, extract_seats(file_example))

    def test_05a_example(self):
        self.assertEqual(820, highest_seat_id(extract_seats(file_example)))

    def test_05a(self):
        self.assertEqual(826, highest_seat_id(extract_seats(file_input)))

    def test_05b(self):
        self.assertEqual(678, find_missing_seat_id_with_neighbors(extract_seats(file_input)))

    def test_05_main(self):
        self.assertEqual(0, os.system("python -m aoc.day05.day05"))

    def test_invalid_command_char(self):
        with self.assertRaises(ValueError):
            extract_seats(file_invalid_cmd)
