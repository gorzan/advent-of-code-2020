from copy import deepcopy
from collections import defaultdict
adapters = open('input.txt').read().split('\n')
adapters = [int(i) for i in adapters]


def jump_next(current, adapters):
    if current + 1 in adapters:
        return 1
    elif current + 2 in adapters:
        return 2
    elif current + 3 in adapters:
        return 3
    else:
        print('No valid next adapter!')
        return False


# Part One
def part_one(adapters):
    current = 0
    device = max(adapters) + 3
    adapters.append(device)

    jumps = []

    while current < device:
        jump = jump_next(current, adapters)
        next_adapter = current + jump
        jumps.append(jump)
        current = next_adapter

    one_jumps = jumps.count(1)
    two_jumps = jumps.count(2)
    three_jumps = jumps.count(3)
    solution = one_jumps * three_jumps
    print(f'Part One: 1-jumps: {one_jumps}, 2-jumps: {two_jumps}, 3-jumps: {three_jumps}, solution: {solution}')


part_one(adapters)


# Part Two - more or less stolen from mortenlj
def part_two(adapters):
    adapters = list(reversed(sorted(adapters)))
    paths_from = defaultdict(int)
    paths_from[max(adapters) + 3] = 1
    for i in adapters:
        paths_from[i] = paths_from[i + 1] + paths_from[i + 2] + paths_from[i + 3]
    result = paths_from[1] + paths_from[2] + paths_from[3]
    print(f"Part 2 result: {result}")
    return result


part_two(adapters)
