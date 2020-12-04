import re


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


def has_required_keys_and_valid_values(passport: dict) -> bool:
    if not has_required_keys(passport):
        return False

    if not re.compile("^#[0-9a-f]{6}$").match(passport['hcl']):
        return False

    if not 1920 <= int(passport['byr']) <= 2002:
        return False

    if not 2010 <= int(passport['iyr']) <= 2020:
        return False

    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    match_hgt_cm = re.compile("^([0-9]{3})cm$").match(passport['hgt'])
    match_hgt_in = re.compile("^([0-9]{2})in$").match(passport['hgt'])
    if match_hgt_cm:
        if not 150 <= int(match_hgt_cm.group(1)) <= 193:
            return False
    elif match_hgt_in:
        if not 59 <= int(match_hgt_in.group(1)) <= 76:
            return False
    else:
        return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not re.compile("^[0-9]{9}$").match(passport['pid']):
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
