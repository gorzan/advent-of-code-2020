import time
from collections import defaultdict, deque
input_data = [14,1,17,0,3,20]


def next_number(numbers):
    numbers = numbers[::-1]
    prev = numbers[0]
    numbers = numbers[1:]
    if prev not in numbers:
        return 0
    else:
        last_occurence = numbers.index(prev)
        return last_occurence + 1


def find_number_n_old(numbers, n):
    turns = len(numbers)
    start = time.time()
    while turns != n:
        turns = turns + 1
        #if turns % 1000 == 0: print(f'Turns: {turns}')
        numbers.append(next_number(numbers))
    end = time.time()
    print(f'The {turns}th number is {numbers[-1]} (in {round(end-start,2)}s)')


def find_number_n(starting, n):
    numbers = defaultdict(deque)
    last = None
    turn = 0
    for current in starting:
        turn = turn + 1
        numbers[current].append(turn)
        last = current
    while turn < n:
        turn = turn + 1
        prev_occurences = numbers[last]
        if len(prev_occurences) == 1:
            number = 0
        else:
            number = prev_occurences[-1] - prev_occurences[-2]
        numbers[number].append(turn)
        if len(numbers[number])>2:
            numbers[number].popleft()
        last = number
    print(f'The {turn}th number is {number}')

# Part One
start = time.time()
find_number_n(input_data, 2020)
end = time.time()

print(f'Time: {round(end-start,2)}s')


# Part Two
start = time.time()
find_number_n(input_data, 30000000)
end = time.time()

print(f'Time: {round(end-start,2)}s')

