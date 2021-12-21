"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""

# Puzzle 21


import itertools as it
from collections import Counter


def getData(file):
    data = [int(line.split()[-1]) for line in open(file).readlines()]
    return data


def getUniverse_per_sum(faces, throws):
    universe_per_sum = Counter()
    for _set_ in [set(it.permutations(comb)) for comb in it.combinations_with_replacement(range(1, faces+1), throws)]:
        val = sum(list(_set_)[0])
        universe_per_sum[val] += len(_set_)
    return universe_per_sum


def part1(file):
    pp = getData(file)
    ps = [0, 0]
    die = 0
    turn = 0
    while ps[0] < 1000 and ps[1] < 1000:
        for _ in range(3):
            die += 1
            pp[turn] += die
        pp[turn] = pp[turn] % 10
        ps[turn] += pp[turn] if pp[turn] > 0 else 10
        turn = (turn + 1) % 2

    return min(ps) * die


def part2(file, faces, throws):
    universe_per_sum = getUniverse_per_sum(faces, throws)
    universes = Counter()
    universes[tuple(getData(file)), (0, 0), 0] = 1
    explored = True
    while explored:
        explored = False
        items = [item for item in universes.items()]
        for universe, count in items:
            pp, ps, turn = universe
            if ps[0] < 21 and ps[1] < 21:
                universes.pop(universe)
                explored = True
                for k, v in universe_per_sum.items():
                    npp, nps = list(pp), list(ps)
                    npp[turn] = (pp[turn] + k) % 10
                    nps[turn] = nps[turn] + npp[turn] if npp[turn] > 0 else nps[turn] + 10
                    universes[tuple(npp), tuple(nps), (turn + 1) % 2] += count * v
    pw = [0, 0]
    for universe in universes:
        pp, ps, turn = universe
        if ps[0] >= 21:
            pw[0] += universes[universe]
        elif ps[1] >= 21:
            pw[1] += universes[universe]
    return max(pw)


print("Solution 1:", part1("input.txt"))
print("Solution 2:", part2("input.txt", 3, 3))
