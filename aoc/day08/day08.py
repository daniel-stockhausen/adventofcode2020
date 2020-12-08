from copy import deepcopy
from typing import List


def process_input(filename: str) -> List[List[str]]:
    with open(filename) as f:
        code = []
        for operation_with_operand in f.read().splitlines():
            operation, operand = operation_with_operand.split(' ')
            code.append([operation, int(operand)])

        return code


def detect_inf_loop_get_acc(filename: str) -> int:
    code = process_input(filename)
    exit_code, acc = execute(code)
    return acc


def execute(code: list) -> (int, int):
    executed_lines = []
    accumulator = 0
    line = 0

    while True:
        if line in executed_lines:
            return 1, accumulator
        executed_lines.append(line)

        operation = code[line][0]
        operand = code[line][1]

        if operation == 'nop':
            line = line + 1
        elif operation == 'acc':
            accumulator = accumulator + operand
            line = line + 1
        elif operation == 'jmp':
            line = line + operand

        if line == len(code):
            return 0, accumulator


def fix_bug_get_acc(filename: str) -> int:
    original_code = process_input(filename)
    code = original_code
    next_line_to_change = 0

    while True:
        if next_line_to_change == len(code):
            break

        exit_code, accumulator = execute(code)
        if exit_code != 0:
            code = deepcopy(original_code)
            for line in range(next_line_to_change, len(code)):
                operation = code[line][0]
                if operation == 'nop':
                    code[line][0] = 'jmp'
                    next_line_to_change = next_line_to_change + 1
                elif operation == 'jmp':
                    code[line][0] = 'nop'
                    next_line_to_change = next_line_to_change + 1
                else:
                    continue
                break
            continue
        return accumulator


if __name__ == '__main__':
    part1 = detect_inf_loop_get_acc('input/day08.txt')
    print(f"Part 1: {part1}")

    part2 = fix_bug_get_acc('input/day08.txt')
    print(f"Part 2: {part2}")
