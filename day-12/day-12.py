instructions = open('input.txt').read().split('\n')


def rotate_ship(original_direction, rotation, clockwise=True):
    directions = ['N', 'E', 'S', 'W']
    original_direction_index = directions.index(original_direction)
    delta = rotation/90 if clockwise else -rotation/90
    new_direction_index = original_direction_index + delta
    if new_direction_index >= 4:
        new_direction_index = new_direction_index - 4
    new_direction = directions[int(new_direction_index)]
    return new_direction


def rotate_wp(wp, rotation, clockwise=True):
    rotation = rotation if clockwise else -rotation
    if (rotation == 90) or (rotation == -270):
        y = wp['x']
        x = -wp['y']
    elif (rotation == -90) or (rotation == 270):
        y = -wp['x']
        x = wp['y']
    elif (rotation == 180) or (rotation == -180):
        x = -wp['x']
        y = -wp['y']
    return dict(x=x, y=y)


def move(state, direction, distance):
    if direction == 'N': state['y'] = state['y'] - distance
    if direction == 'S': state['y'] = state['y'] + distance
    if direction == 'E': state['x'] = state['x'] + distance
    if direction == 'W': state['x'] = state['x'] - distance
    return state


def move_ship_to_wp(ship, wp, distance):
    ship['x'] = ship['x'] + (wp['x'] * distance)
    ship['y'] = ship['y'] + (wp['y'] * distance)
    return ship


def execute_simple(instruction, state):
    operation = instruction[0:1]
    argument = int(instruction[1:])
    if operation == 'R': state['direction'] = rotate_ship(state['direction'], argument, True)
    if operation == 'L': state['direction'] = rotate_ship(state['direction'], argument, False)
    if operation in ('N', 'S', 'W', 'E'): state = move(state, operation, argument)
    if operation == 'F': state = move(state, state['direction'], argument)
    return state


def execute(instruction, wp, ship):
    operation = instruction[0:1]
    argument = int(instruction[1:])
    if operation in ('N', 'S', 'W', 'E'): wp = move(wp, operation, argument)
    if operation == 'R': wp = rotate_wp(wp, argument, True)
    if operation == 'L': wp = rotate_wp(wp, argument, False)
    if operation == 'F': ship = move_ship_to_wp(ship, wp, argument)
    return [wp, ship]


def manhattan(state):
    x = abs(state['x'])
    y = abs(state['y'])
    return x + y


def part_one(instructions):
    state = dict(x=0, y=0, direction='E')
    for instruction in instructions:
        state = execute_simple(instruction, state)

    result = manhattan(state)
    print(f'Part 1: Final location: [{state["x"]}, {state["y"]}] facing {state["direction"]} at manhattan distance {result}')


part_one(instructions)


def part_two(instructions):
    ship = dict(x=0, y=0)
    wp = dict(x=10, y=-1)
    for instruction in instructions:
        state = execute(instruction, wp, ship)
        wp = state[0]
        ship = state[1]
    result = manhattan(ship)
    print(f'Part 2: Final location: [{ship["x"]}, {ship["y"]}] at manhattan distance {result}')


part_two(instructions)