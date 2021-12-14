"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 13

def getData(file):
    data_parts = open(file).read().split("\n\n")
    coords = [list(map(int, pair.split(','))) for pair in data_parts[0].strip().split()]
    folds = list()
    for line in data_parts[1].split('\n'):
        line_parts = line.split('=')
        folds.append((line_parts[0][-1], int(line_parts[1])))
    return coords, folds


def fold(coords, axis, point):
    for i in range(len(coords)):
        if axis == 'x':
            if coords[i][0] == 2 * point:
                coords[i][0] = 0
            else:
                coords[i][0] = coords[i][0] - 2 * (coords[i][0] % point) if coords[i][0] > point else coords[i][0]
        elif axis == 'y':
            if coords[i][1] == 2 * point:
                coords[i][1] = 0
            coords[i][1] = coords[i][1] - 2 * (coords[i][1] % point) if coords[i][1] > point else coords[i][1]


def count_points(coords):
    single_coords = {(pair[0], pair[1]) for pair in coords}
    return len(single_coords)


def print_grid(coords):
    print()
    max_x = max(pair[0] for pair in coords) + 1
    max_y = max(pair[1] for pair in coords) + 1
    grid = [['.' for j in range(max_x)] for i in range(max_y)]
    for x, y in coords:
        grid[y][x] = '#'
    for line in grid:
        print(''.join(line))
    print()


def part1(file):
    coords, folds = getData(file)
    fold(coords, folds[0][0], folds[0][1])
    return count_points(coords)


def part2(file):
    coords, folds = getData(file)
    for action in folds:
        axis, point = action
        fold(coords, axis, point)
    print_grid(coords)


print("Solution 1: " + str(part1("input.txt")))
part2("input.txt")  # Read output and watch closely :)
