from typing import List


def process_input(filename: str) -> List[List[str]]:
    with open(filename) as f:
        contained_bags_by_bag = {}
        for bag_line in f.read().splitlines():
            bag, contained_bags = bag_line.split(' bags contain ')
            contained_bags_by_bag[bag] = contained_bags_str_to_dict(contained_bags)

        return contained_bags_by_bag


def contained_bags_str_to_dict(contained_bags_str: str) -> dict:
    bag_count_by_color = {}
    contained_bags = contained_bags_str.split(', ')
    for bag_color_with_count in contained_bags:
        if bag_color_with_count == 'no other bags.':
            continue
        bag_color_with_count_split = bag_color_with_count.split()
        count = bag_color_with_count_split[0]
        color = ' '.join(bag_color_with_count_split[1:len(bag_color_with_count_split) - 1])
        bag_count_by_color[color] = count
    return bag_count_by_color


def bag_fits_in_bags_from_file(color: str, filename: str):
    rules = process_input(filename)
    return len(bag_fits_in_bags(color, rules))


def bag_fits_in_bags(color: str, rules: dict):
    compatible_colors = set()

    for rule_color, rule in rules.items():
        if color in rule:
            compatible_colors.add(rule_color)

    compatible_colors_copy = compatible_colors.copy()
    for color in compatible_colors_copy:
        mre_colors = bag_fits_in_bags(color, rules)
        compatible_colors.update(mre_colors)

    return compatible_colors


def count_bags_from_file(color: str, filename: str) -> int:
    rules = process_input(filename)
    return count_bags(color, rules)


def count_bags(color: str, rules: dict) -> int:
    more_bags = rules[color]

    count = 0
    for bag_color, bag_count in more_bags.items():
        inner_count = count_bags(bag_color, rules)
        count = count + int(bag_count) + int(bag_count) * inner_count
    return count


if __name__ == '__main__':
    part1 = bag_fits_in_bags_from_file('shiny gold', 'input/day07.txt')
    print(f"Part 1: {part1}")

    part2 = count_bags_from_file('shiny gold', 'input/day07.txt')
    print(f"Part 2: {part2}")
