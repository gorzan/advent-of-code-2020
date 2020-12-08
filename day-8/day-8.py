from copy import deepcopy
input_text = open('input.txt').read().split('\n')


def structure_instructions(instructions):
    output = []
    for instruction in instructions:
        instruction = instruction.split(' ')
        output.append(dict(
            operation=instruction[0],
            argument=int(instruction[1])
        ))
    return output


def execute(instruction, state):
    if instruction['operation'] == 'acc':
        state['accumulator'] = state['accumulator'] + instruction['argument']

    if instruction['operation'] == 'jmp':
        state['pointer'] = state['pointer'] + instruction['argument']
    else:
        state['pointer'] = state['pointer'] + 1

    return state


def run(instructions):
    lines_executed = []
    state = dict(pointer=0, accumulator=0, termination='')
    while (state['pointer'] not in lines_executed) and (state['pointer'] < len(instructions)):
        lines_executed.append(state['pointer'])
        state = execute(instructions[state['pointer']], state)

    state['termination'] = 'completed' if state['pointer'] == len(instructions) else 'infinite loop'

    return state


def substitute_instructions(operation, pointer, instructions):
    modified_instructions = deepcopy(instructions)
    modified_instructions[pointer]['operation'] = operation
    return modified_instructions


instructions = structure_instructions(input_text)


# Part one
def part_one(instructions):
    endstate = run(instructions)
    print(f'''Part One: Terminated at pointer {endstate['pointer']}. Reason: {endstate['termination']}. Accumulator: {endstate['accumulator']}.''')


part_one(instructions)


# Part two
def part_two(instructions):
    for pointer, instruction in enumerate(instructions):
        if instruction['operation'] == 'nop':
            substituted_operation = 'jmp'
        elif instruction['operation'] == 'jmp':
            substituted_operation = 'nop'
        else:
            continue

        modified_instructions = substitute_instructions(substituted_operation, pointer, instructions)
        endstate = run(modified_instructions)

        if endstate['termination'] == 'completed':
            print(f'''Part Two: Terminated at pointer {endstate['pointer']}. Reason: {endstate['termination']}. Accumulator: {endstate['accumulator']}. Substitution: {substituted_operation} at {pointer}.''')


part_two(instructions)
