def process_input(filename: str) -> tuple:
    with open(filename) as f:
        return tuple([tuple(line.strip()) for line in f])


def count_trees_on_slope(filename: str, slope: tuple) -> int:
    area_map = process_input(filename)
    max_x, max_y = len(area_map[0]), len(area_map)

    x, y = 0, 0
    tree_count = 0
    while y < max_y - 1:
        x, y = (x + slope[0]) % max_x, y + slope[1]
        if area_map[y][x] == '#':
            tree_count = tree_count + 1

    return tree_count


def multiply_trees_on_slopes(filename: str, slopes: tuple) -> int:
    product = 1
    for slope in slopes:
        product = product * count_trees_on_slope(filename, slope)

    return product


if __name__ == '__main__':
    part1 = count_trees_on_slope('../../input/day03.txt', (3, 1))
    print(f"Part 1: {part1}")

    part2 = multiply_trees_on_slopes('../../input/day03.txt', ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))
    print(f"Part 2: {part2}")
