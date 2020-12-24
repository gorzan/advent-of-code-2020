instructions = open('input.txt').read().split('\n')


def parse_allocation(instruction):
    instruction = instruction.split(' = ')
    output = dict(
        adr = int(instruction[0].split('[')[1].split(']')[0]),
        val = int(instruction[1])
    )
    return output


def parse_mask(instruction):
    return instruction.split(' = ')[1]


def mask(num, bitmask):
    bnum = '{0:036b}'.format(num)
    output = [bit for bit in bnum]
    for index, bit in enumerate(bitmask):
        if bit == 'X':
            output[index] = bnum[index]
        else:
            output[index] = bit
    return ''.join(output)


def mask_adr(bitmask, adr):
    badr = '{0:036b}'.format(adr)
    wildcard_adr = [bit for bit in badr]
    for index, bit in enumerate(bitmask):
        if bit == 'X':
            wildcard_adr[index] = 'X'
        elif bit == '1':
            wildcard_adr[index] = '1'
        elif bit == '0':
            wildcard_adr[index] = badr[index]
    return ''.join(wildcard_adr)


def find_addresses(wildcard_adr):
    output = []
    first_x = wildcard_adr.find('X')
    if first_x >= 0:
        wildcard_adr = list(wildcard_adr)

        substitute_0 = wildcard_adr.copy()
        substitute_0[first_x] = '0'
        substitute_0 = ''.join(substitute_0)
        output = output + (find_addresses(substitute_0))

        substitute_1 = wildcard_adr.copy()
        substitute_1[first_x] = '1'
        substitute_1 = ''.join(substitute_1)
        output = output + (find_addresses(substitute_1))
    else:
        output = [wildcard_adr]

    return output


def set_mem(memory, bitmask, adr, value):
    wildcard_adr = mask_adr(bitmask, adr)
    addresses = find_addresses(wildcard_adr)
    for address in addresses:
        memory[address] = value
    return memory


def part_one(instructions):
    adr = value = bitmask = ''
    memory = dict()
    for instruction in instructions:
        if instruction[0:3] == 'mas':
            bitmask = parse_mask(instruction)
        elif instruction[0:3] == 'mem':
            adr = parse_allocation(instruction)['adr']
            value = parse_allocation(instruction)['val']
            memory[adr] = int(mask(value, bitmask),2)
    result = sum(memory.values())
    print(f'Sum of values in memory: {result}')


def part_two(instructions):
    adr = value = bitmask = ''
    memory = dict()
    for instruction in instructions:
        if instruction[0:3] == 'mas':
            bitmask = parse_mask(instruction)
        elif instruction[0:3] == 'mem':
            adr = parse_allocation(instruction)['adr']
            value = parse_allocation(instruction)['val']
            memory = set_mem(memory, bitmask, adr, value)
    result = sum(memory.values())
    print(f'Part two: sum of values in memory: {result}')


part_one(instructions)

part_two(instructions)