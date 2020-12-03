import math
terrain = open('input.txt').read().split()


def extend_terrain(terrain, ratio):
    width = len(terrain[0])
    height = len(terrain)
    required_width = ratio*height
    extension_factor = math.ceil(required_width / width)

    extended_terrain = []
    for line in terrain:
        extended_terrain.append(extension_factor*line)

    return extended_terrain


def find_tree(terrain, x, y):
    if terrain[y][x] == '#':
        return True
    else:
        return False


def run_slope(terrain, direction):
    terrain = extend_terrain(terrain, direction[0])
    position = (0, 0)
    trees = 0

    while position[1] <= len(terrain)-1:
        if find_tree(terrain, *position):
            trees = trees + 1
        position = tuple(map(sum, zip(position, direction)))

    return trees


directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []

for direction in directions:
    trees.append(run_slope(terrain, direction))

print(f'Part 1: {run_slope(terrain, directions[1])}')
print(f'Part 2: {math.prod(trees)}')

