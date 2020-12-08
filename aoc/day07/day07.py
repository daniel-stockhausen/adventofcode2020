from typing import List


def process_input(filename: str) -> List[List[str]]:
    with open(filename) as f:
        contained_bags_by_bag = {}
        for bag_line in f.read().splitlines():
            bag, contained_bags = bag_line.split(' bags contain ')
            contained_bags_by_bag[bag] = contained_bags_list_to_dict(contained_bags.split(', '))

        return contained_bags_by_bag


def contained_bags_list_to_dict(contained_bags: list) -> dict:
    contained_bag_count_by_bag = {}
    for bag_with_count in contained_bags:
        if bag_with_count == 'no other bags.':
            continue
        bag_with_count_split = bag_with_count.split()
        count = int(bag_with_count_split[0])
        bag = ' '.join(bag_with_count_split[1:-1])
        contained_bag_count_by_bag[bag] = count
    return contained_bag_count_by_bag


def count_possible_container_bags(bag: str, filename: str):
    contained_bags_by_bag = process_input(filename)
    return len(bag_fits_in_bags(bag, contained_bags_by_bag))


def bag_fits_in_bags(bag_to_fit: str, contained_bags_by_bag: dict):
    container_bags = set()

    for bag, contained_bags in contained_bags_by_bag.items():
        if bag_to_fit in contained_bags:
            container_bags.add(bag)

    for bag_to_fit in set(container_bags):
        parent_container_bags = bag_fits_in_bags(bag_to_fit, contained_bags_by_bag)
        container_bags.update(parent_container_bags)

    return container_bags


def bag_count_inside_bag_from_file(bag: str, filename: str) -> int:
    contained_bags_by_bag = process_input(filename)
    return bag_count_inside_bag(bag, contained_bags_by_bag)


def bag_count_inside_bag(bag: str, contained_bags_by_bag: dict) -> int:
    child_bags = contained_bags_by_bag[bag]

    total_bags = 0
    for bag, bag_count in child_bags.items():
        inside_total_bags = bag_count_inside_bag(bag, contained_bags_by_bag)
        total_bags = total_bags + bag_count * (inside_total_bags + 1)
    return total_bags


if __name__ == '__main__':
    part1 = count_possible_container_bags('shiny gold', 'input/day07.txt')
    print(f"Part 1: {part1}")

    part2 = bag_count_inside_bag_from_file('shiny gold', 'input/day07.txt')
    print(f"Part 2: {part2}")
