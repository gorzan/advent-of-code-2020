answers = open('input.txt').read().split('\n\n')


def part_one(answers):
    answers = [answer.replace('\n', '') for answer in answers]
    n = 0
    for answer in answers:
        n = n + len(set(answer))
    print(f'Part one: Sum of counts: {n}')


def common_letters(group):
    common_letters = []
    for answer in group:
        for letter in answer:
            common = True
            for other_answers in group:
                if letter not in other_answers:
                    common = False
            if common and (letter not in common_letters):
                common_letters.append(letter)
    return common_letters


def part_two(answers):
    answers = [group.split() for group in answers]
    count = 0
    for group in answers:
        count = count + len(common_letters(group))
    print(f'Part two: Sum of counts: {count}')


part_one(answers)
part_two(answers)