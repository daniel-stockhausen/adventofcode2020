from typing import List


def process_input(filename: str) -> List[List[str]]:
    with open(filename) as f:
        return [group.split() for group in f.read().split('\n\n')]


def count_questions_answered_yes(filename: str, require_yes_from_whole_group: bool = False) -> int:
    groups = process_input(filename)
    yes_question_count = 0

    for group in groups:
        count_by_question = {}
        for person in group:
            for question in person:
                count_by_question[question] = 1 if question not in count_by_question else \
                    count_by_question[question] + 1

        for count in count_by_question.values():
            min_yes_answers = 1 if not require_yes_from_whole_group else len(group)
            if count >= min_yes_answers:
                yes_question_count = yes_question_count + 1

    return yes_question_count


if __name__ == '__main__':
    part1 = count_questions_answered_yes('input/day06.txt')
    print(f"Part 1: {part1}")

    part2 = count_questions_answered_yes('input/day06.txt', True)
    print(f"Part 2: {part2}")
