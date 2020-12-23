layout = open('input.txt').read().split('\n')


def occupied(x, y, layout):
    if seat(x, y, layout) and layout[y][x] == '#':
        return True
    return False


def seat(x, y, layout):
    maxrow = len(layout) - 1
    maxcol = len(layout[0]) - 1
    if (x > maxcol) or (x < 0):
        return False
    if (y > maxrow) or (y < 0):
        return False
    if layout[y][x] in ['#', 'L']:
        return True
    return False


def adjecent_occupied(x, y, layout):
    seats_occupied = 0
    for x_offset in range(x-1,x+2):
        for y_offset in range(y-1, y+2):
            if not (x == x_offset and y == y_offset):
                if occupied(x_offset, y_offset, layout):
                    seats_occupied = seats_occupied + 1
    return seats_occupied


def visible_occupied(x, y, layout, direction):
    xmax = len(layout[0])
    ymax = len(layout)
    x_offset = x
    y_offset = y
    x_delta = 0
    y_delta = 0
    if 'left' in direction: x_delta = -1
    if 'right' in direction: x_delta = 1
    if 'up' in direction: y_delta = -1
    if 'down' in direction: y_delta = 1
    occ_dir = False

    while (y_offset >= 0) and (x_offset <= xmax) and (y_offset <= ymax) and (x_offset >= 0):
        x_offset = x_offset + x_delta
        y_offset = y_offset + y_delta
        if seat(x_offset, y_offset, layout):
            if occupied(x_offset, y_offset, layout):
                occ_dir = True
            break

    return occ_dir



def count_visible_occupied(x, y, layout):
    seats_occupied = 0
    if visible_occupied(x, y, layout, 'left'): seats_occupied = seats_occupied + 1
    if visible_occupied(x, y, layout, 'left up'): seats_occupied = seats_occupied + 1
    if visible_occupied(x, y, layout, 'up'): seats_occupied = seats_occupied + 1
    if visible_occupied(x, y, layout, 'right up'): seats_occupied = seats_occupied + 1
    if visible_occupied(x, y, layout, 'right'): seats_occupied = seats_occupied + 1
    if visible_occupied(x, y, layout, 'right down'): seats_occupied = seats_occupied + 1
    if visible_occupied(x, y, layout, 'down'): seats_occupied = seats_occupied + 1
    if visible_occupied(x, y, layout, 'left down'): seats_occupied = seats_occupied + 1
    return seats_occupied


def display_floor(layout):
    for row in layout:
        print(row)


def tick(layout, lookaround, max_occupied):
    new_layout = []
    i = 0
    for y, row in enumerate(layout):
        newrow = ''
        for x, col in enumerate(row):
            if (not occupied(x, y, layout)) and (lookaround(x, y, layout) == 0) and (seat(x, y, layout)):
                newcol = '#'
            elif occupied(x, y, layout) and lookaround(x, y, layout) >= max_occupied:
                newcol = 'L'
            else:
                newcol = col
            newrow = newrow + newcol
        new_layout.append(newrow)
    return new_layout


def count_occupied(layout):
    occupied = 0
    for row in layout:
        for col in row:
            if col=='#':
                occupied = occupied + 1
    return occupied


def part_one(layout):
    ticks = 0
    while layout != tick(layout, adjecent_occupied, 4):
        ticks = ticks + 1
        print(f'Ticks: {ticks}')
        layout = tick(layout, adjecent_occupied, 4)

    print(f'Part One: Occupied seats: {count_occupied(layout)}')

#part_one(layout)

def part_two(layout):
    ticks = 0
    while layout != tick(layout, count_visible_occupied, 5):
        display_floor(layout)
        ticks = ticks + 1
        print(f'Ticks: {ticks}')
        layout = tick(layout, count_visible_occupied, 5)
    print(f'Part Two: Occupied seats: {count_occupied(layout)}')


part_two(layout)

