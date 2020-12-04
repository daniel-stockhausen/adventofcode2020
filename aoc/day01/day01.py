def process_input(filename: str) -> list:
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def product_of_2_summands_of_sum(filename: str, sum: int) -> int:
    numbers = process_input(filename)

    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == sum:
                return num1 * num2


def product_of_3_summands_of_sum(filename: str, sum: int) -> int:
    numbers = process_input(filename)

    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 + num2 + num3 == sum:
                    return num1 * num2 * num3


if __name__ == '__main__':
    part1 = product_of_2_summands_of_sum('input/day01.txt', 2020)
    print(f"Part 1: {part1}")

    part2 = product_of_3_summands_of_sum('input/day01.txt', 2020)
    print(f"Part 2: {part2}")
