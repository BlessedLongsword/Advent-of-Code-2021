"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 17

def getData(file):
    line = open(file).readline()
    line_parts = line.split()
    area = dict()
    area[line_parts[2][0]] = list(map(int, line_parts[2][2:-1].split('..')))
    area[line_parts[3][0]] = list(map(int, line_parts[3][2:].split('..')))
    return area


def in_range(coords, target):
    x, y = coords
    return target['x'][0] <= x <= target['x'][1] and target['y'][0] <= y <= target['y'][1]


def over_range(coords, target):
    x, y = coords
    return x > target['x'][1] or y < target['y'][0]


def step(coords, vel):
    coords[0] += vel[0]
    coords[1] += vel[1]
    if vel[0] != 0:
        vel[0] += -1 if vel[0] > 0 else 1
    vel[1] -= 1


def throw(start, initial_vel, target):
    coords = start.copy()
    vel = initial_vel.copy()
    while not in_range(coords, target):
        step(coords, vel)
        if over_range(coords, target):
            return False
    return True


def trim_x(target_x):
    x_range = list()
    x = 0
    while not x * (x + 1) / 2 >= target_x[0]:
        x += 1
    while not x * (x + 1) / 2 > target_x[1]:
        x_range.append(x)
        x += 1
    return x_range


def part1(file, max_y):
    target_area = getData(file)
    probe = [0, 0]
    highest_init_y = 0
    for x in trim_x(target_area['x']):
        for j in range(-max_y, max_y):
            init_vel = [x, j]
            if throw(probe, init_vel, target_area):
                if j > highest_init_y:
                    highest_init_y = init_vel[1]

    return int(highest_init_y * (highest_init_y + 1) / 2)


def part2(file, max_x, max_y):
    init_vel_count = 0
    target_area = getData(file)
    probe = [0, 0]
    for i in range(max_x):
        for j in range(-max_y, max_y):
            init_vel = [i, j]
            if throw(probe, init_vel, target_area):
                init_vel_count += 1

    return init_vel_count


print("Solution 1:", part1("input.txt", 100))
print("Solution 2:", part2("input.txt", 500, 500))
