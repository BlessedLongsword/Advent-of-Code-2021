"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 11

def count_flashes(file, steps):
    octopuses = [list(map(int, line.strip())) for line in open(file, 'r')]
    flashes = 0

    # print('Before any steps:')
    # printOctopuses(octopuses)

    for _ in range(steps):
        octopuses = [list(map(lambda x: (x + 1) % 10, octopus_line)) for octopus_line in octopuses]
        nines = list()
        # print('After step ' + str(_+1) + ':')
        # printOctopuses(octopuses)
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                if octopuses[i][j] == 9:
                    nines.append((i, j))
                elif octopuses[i][j] == 0:
                    flashes += 1
        for i, j in nines:
            flash(octopuses, i, j)

    return flashes


def flash(octopuses, i, j):
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if 0 <= i+di < len(octopuses) and 0 <= j+dj < len(octopuses):
            i_new, j_new = i+di, j+dj
            if octopuses[i_new][j_new] < 9 and (i_new, j_new):
                octopuses[i_new][j_new] += 1
                if octopuses[i_new][j_new] == 9:
                    flash(octopuses, i_new, j_new)


def printOctopuses(octopuses):
    printer = [list(map(str, octopus_line)) for octopus_line in octopuses]
    for line in printer:
        print(''.join(line))
    print()


def synchronized_flash(file):
    octopuses = [list(map(int, line.strip())) for line in open(file, 'r')]
    step = 0
    all_flashed = False

    # print('Before any steps:')
    # printOctopuses(octopuses)

    while not all_flashed:
        step += 1
        octopuses = [list(map(lambda x: (x + 1) % 10, octopus_line)) for octopus_line in octopuses]
        nines = list()
        # print('After step ' + str(step) + ':')
        # printOctopuses(octopuses)
        if sum([sum(octopus_line) for octopus_line in octopuses]) == 0:
            all_flashed = True
        else:
            for i in range(len(octopuses)):
                for j in range(len(octopuses[i])):
                    if octopuses[i][j] == 9:
                        nines.append((i, j))
            for i, j in nines:
                flash(octopuses, i, j)

    return step


print("Solution 1: " + str(count_flashes("input.txt", 100)))
print("Solution 2: " + str(synchronized_flash("input.txt")))
