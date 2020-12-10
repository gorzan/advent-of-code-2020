data = open('input.txt').read().split('\n')
data = [int(i) for i in data]
preamble = 25

def verify_sum(number, previous_numbers):
    for index, prev in enumerate(previous_numbers):
        for other_prev in previous_numbers[index+1:]:
            if prev+other_prev == number:
                return True
    return False


def find_first_invalid(data, preamble):
    for index, n in enumerate(data):
        if index >= preamble:
            if not verify_sum(data[index], data[index-preamble:index]):
                return data[index]


def find_set(data, target_sum):
    for index, number in enumerate(data):
        contiguous_set = [number]
        contiguous_sum = number
        i = index
        while contiguous_sum < target_sum:
            i = i + 1
            contiguous_set.append(data[i])
            contiguous_sum = contiguous_sum + data[i]
        if contiguous_sum == target_sum:
            return contiguous_set
    return False


# Part One
def part_one(data, preamble):
    solution = find_first_invalid(data, preamble)
    print(f'Part One: First invalid number is {solution}')


part_one(data, preamble)


# Part Two
def part_two(data, preamble):
    invalid = find_first_invalid(data, preamble)
    target_set = find_set(data, invalid)
    solution = min(target_set) + max(target_set)
    print(f'Part Two: Sum of smallest and largets numbers in target set: {solution}')


part_two(data, preamble)

