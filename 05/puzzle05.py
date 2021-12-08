"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 5

def getData(file):
    f = open(file, "r")
    coords = [(line.strip()).split("->") for line in f]
    for i, line in enumerate(coords):
        for j, pair in enumerate(line):
            coords[i][j] = list(map(int, (pair.strip()).split(",")))
    return coords


def getMax(axis, coords):
    return max([line[i][axis] for line in coords for i in range(2)]) + 1


def overlappingLines(file):
    coords = getData(file)
    diagram = [[0 for i in range(getMax(0, coords))] for j in range(getMax(1, coords))]
    overlaps = 0

    for line in coords:
        x1, y1, x2, y2 = int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                diagram[i][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                diagram[y1][j] += 1

    for x in range(len(diagram)):
        for y in range(len(diagram[x])):
            if diagram[x][y] >= 2:
                overlaps += 1

    return overlaps


def overlappingLines_wdiagonal(file):
    coords = getData(file)
    diagram = [[0 for i in range(getMax(0, coords))] for j in range(getMax(1, coords))]
    overlaps = 0

    for line in coords:
        x1, y1, x2, y2 = int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                diagram[i][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                diagram[y1][j] += 1
        else:
            counter = 0
            x1_lower, y1_lower = 1 if x1 < x2 else -1, 1 if y1 < y2 else -1
            while x1 + counter*x1_lower != x2 + x1_lower:
                diagram[y1 + counter*y1_lower][x1 + counter*x1_lower] += 1
                counter += 1

    for x in range(len(diagram)):
        for y in range(len(diagram[x])):
            if diagram[x][y] >= 2:
                overlaps += 1

    return overlaps


print("Solution 1: " + str(overlappingLines("input.txt")))
print("Solution 2: " + str(overlappingLines_wdiagonal("input.txt")))
