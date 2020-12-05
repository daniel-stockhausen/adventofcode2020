import math
from typing import Tuple


class Seat:
    row: int
    col: int
    id: int

    def __init__(self, row: int, col: int, id: int):
        self.row = row
        self.col = col
        self.id = id

    def __eq__(self, other):
        return (self.row, self.col, self.id) == (other.row, other.col, other.id)


def process_input(filename: str) -> Tuple[str]:
    with open(filename) as f:
        return tuple(f.read().splitlines())


def binary_search(down_cmd: chr, up_cmd: chr, commands: str) -> int:
    min = 0
    max = pow(2, len(commands))
    for cmd in commands:
        if cmd == down_cmd:
            max = (min + max) / 2
        elif cmd == up_cmd:
            min = min + math.ceil((max - min) / 2)
        else:
            print(f'Error: invalid command character \'{cmd}\' in "{commands}"')
            exit(1)

    return min


def extract_seats(filename: str) -> Tuple[Seat]:
    seat_strings = process_input(filename)

    seats = []
    for seat_string in seat_strings:
        row = binary_search('F', 'B', seat_string[0:7])
        col = binary_search('L', 'R', seat_string[7:10])

        id = row * 8 + col
        seats.append(Seat(row, col, id))

    return tuple(seats)


def highest_seat_id(seats: Tuple[Seat]) -> int:
    return max(seat.id for seat in seats)


def find_missing_seat_id_with_neighbors(seats: Tuple[Seat]) -> int:
    seat_ids = [seat.id for seat in seats]
    seat_ids.sort()

    for idx, seat_id in enumerate(seat_ids):
        if seat_ids[idx + 1] == seat_id + 2:
            return seat_id + 1


if __name__ == '__main__':
    part1 = highest_seat_id(extract_seats('input/day05.txt'))
    print(f"Part 1: {part1}")

    part2 = find_missing_seat_id_with_neighbors(extract_seats('input/day05.txt'))
    print(f"Part 2: {part2}")
