"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 2

def process_directions(file):
    f = open(file, "r")
    vertical = 0
    horizontal = 0

    for line in f:
        action = line.split()
        if action[0] == "down":
            vertical += int(action[1])
        elif action[0] == "up":
            vertical -= int(action[1])
        else:
            horizontal += int(action[1])

    f.close()

    return vertical * horizontal


def process_directions_aim(file):
    f = open(file, "r")
    vertical = 0
    horizontal = 0
    aim = 0

    for line in f:
        action = line.split()
        if action[0] == "down":
            aim += int(action[1])
        elif action[0] == "up":
            aim -= int(action[1])
        else:
            horizontal += int(action[1])
            vertical += int(action[1]) * aim

    f.close()

    return vertical * horizontal


print("Solution 1: " + str(process_directions("input.txt")))
print("Solution 2: " + str(process_directions_aim("input.txt")))
