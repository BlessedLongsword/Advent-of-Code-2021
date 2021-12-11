"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 9

def riskLevels(file):
    heightmap = [list(map(int, list(line.strip()))) for line in open(file, 'r')]
    risk_level = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            higher_adjacency = [True for k in range(4)]
            if j > 0:
                higher_adjacency[0] = heightmap[i][j] < heightmap[i][j-1]
            if i > 0:
                higher_adjacency[1] = heightmap[i][j] < heightmap[i-1][j]
            if j < len(heightmap[i]) - 1:
                higher_adjacency[2] = heightmap[i][j] < heightmap[i][j+1]
            if i < len(heightmap) - 1:
                higher_adjacency[3] = heightmap[i][j] < heightmap[i+1][j]
            if sum(higher_adjacency) == 4:
                risk_level += 1 + heightmap[i][j]

    return risk_level


def adjacency(heightmap, i, j):
    left, top, right, bottom = 0, 0, 0, 0
    heightmap[i][j] = -1
    if j > 0:
        if heightmap[i][j - 1] != -1 and heightmap[i][j - 1] != 9:
            left = 1 + adjacency(heightmap, i, j - 1)
    if i > 0:
        if heightmap[i - 1][j] != -1 and heightmap[i - 1][j] != 9:
            top = 1 + adjacency(heightmap, i - 1, j)
    if j < len(heightmap[i]) - 1:
        if heightmap[i][j + 1] != -1 and heightmap[i][j + 1] != 9:
            right = 1 + adjacency(heightmap, i, j + 1)
    if i < len(heightmap) - 1:
        if heightmap[i + 1][j] != -1 and heightmap[i + 1][j] != 9:
            bottom = 1 + adjacency(heightmap, i + 1, j)
    return left + top + right + bottom


def basins_problem(file, num_basins):
    heightmap = [list(map(int, list(line.strip()))) for line in open(file, 'r')]
    basin_size_prod = 1
    basins = list()
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if heightmap[i][j] != -1 and heightmap[i][j] != 9:
                basins.append(1 + adjacency(heightmap, i, j))

    for k in range(num_basins):
        biggest_basin = max(basins)
        basin_size_prod *= biggest_basin
        basins.remove(biggest_basin)

    return basin_size_prod


print("Solution 1: " + str(riskLevels("input.txt")))
print("Solution 2: " + str(basins_problem("input.txt", 3)))
