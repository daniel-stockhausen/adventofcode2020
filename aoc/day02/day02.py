def process_input_pair(pair: list) -> dict:
    policy, password = pair
    policy_nums, policy_char = policy.split(' ')
    policy_num1, policy_num2 = [int(num) for num in policy_nums.split('-')]

    return {'password': password, 'policy_char': policy_char, 'policy_num1': policy_num1, 'policy_num2': policy_num2}


def process_input(filename: str) -> list:
    with open(filename) as f:
        return [process_input_pair(line.split(': ')) for line in f]


def check_password_policy_pt1(password: str, policy_char: str, policy_min: int, policy_max: int) -> bool:
    occurrence = password.count(policy_char)
    return policy_min <= occurrence <= policy_max


def check_password_policy_pt2(password: str, policy_char: str, char_pos_1: int, char_pos_2: int) -> bool:
    return (password[char_pos_1 - 1] == policy_char) != (password[char_pos_2 - 1] == policy_char)


def count_valid_passwords_pt1(filename: str) -> int:
    entries = process_input(filename)

    return sum(
        1 if check_password_policy_pt1(e['password'], e['policy_char'], e['policy_num1'], e['policy_num2'])
        else 0 for e in entries)


def count_valid_passwords_pt2(filename: str) -> int:
    entries = process_input(filename)

    return sum(
        1 if check_password_policy_pt2(e['password'], e['policy_char'], e['policy_num1'], e['policy_num2'])
        else 0 for e in entries)


if __name__ == '__main__':
    part1 = count_valid_passwords_pt1('../../input/day02.txt')
    print(f"Part 1: {part1}")

    part2 = count_valid_passwords_pt2('../../input/day02.txt')
    print(f"Part 2: {part2}")
