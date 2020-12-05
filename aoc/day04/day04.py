import re

validations = {
    'hcl': lambda x: re.compile("^#[0-9a-f]{6}$").match(x),
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'hgt': lambda x: validate_hgt(x),
    'pid': lambda x: re.compile("^[0-9]{9}$").match(x),
}


def process_input(filename: str) -> tuple:
    with open(filename) as f:
        return tuple(
            [dict([tuple(key_value_pair.split(':')) for key_value_pair in record.split()])
             for record in f.read().split('\n\n')]
        )


def has_required_keys(passport: dict) -> bool:
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    present_keys = set(list(passport.keys()))
    return required_keys.issubset(present_keys)


def validate_hgt(hgt: str) -> bool:
    match_hgt = re.compile("^([0-9]{2,3})(cm|in)$").match(hgt)
    valid_cm = match_hgt and match_hgt.group(2) == 'cm' and 150 <= int(match_hgt.group(1)) <= 193
    valid_in = match_hgt and match_hgt.group(2) == 'in' and 59 <= int(match_hgt.group(1)) <= 76
    return valid_cm or valid_in


def has_required_keys_and_valid_values(passport: dict) -> bool:
    if not has_required_keys(passport):
        return False

    for key, validation in validations.items():
        if not validation(passport[key]):
            return False

    return True


def count_passports_with_required_keys(filename: str) -> int:
    passports = process_input(filename)
    return sum(1 if has_required_keys(passport) else 0 for passport in passports)


def count_passports_with_required_keys_and_valid_values(filename: str) -> int:
    passports = process_input(filename)
    return sum(1 if has_required_keys_and_valid_values(passport) else 0 for passport in passports)


if __name__ == '__main__':
    part1 = count_passports_with_required_keys('input/day04.txt')
    print(f"Part 1: {part1}")

    part2 = count_passports_with_required_keys_and_valid_values('input/day04.txt')
    print(f"Part 2: {part2}")
