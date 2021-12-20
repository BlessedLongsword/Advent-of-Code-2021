"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021


My own version that still does not work...
"""

# Puzzle 19

from copy import deepcopy
from itertools import permutations
from collections import Counter


def getData(file):
    data = open(file).read().split("\n\n")
    data = [paragraph.split('\n') for paragraph in data]
    data = {i: [list(map(int, line.split(','))) for line in data[i][1:]] for i in range(len(data))}
    return data


def get_all_permutations(_list_, sign_changes):
    all_sorted_perms = list()
    for sign_change in sign_changes:
        all_perm_group = get_permutations(change_signs(_list_, sign_change))
        for perm_group in all_perm_group:
            all_sorted_perms.append(perm_group)
    return all_sorted_perms


def get_permutations(_list_):
    perms = list()
    for triple in _list_:
        perms.append(list(permutations(triple)))
    sorted_perms = [[[0, 0, 0] for __ in range(len(perms))] for _ in range(len(perms[0]))]
    for i in range(3):
        for j in range(len(perms[0])):
            for k in range(len(perms)):
                sorted_perms[j][k][i] = perms[k][j][i]
    return sorted_perms


def change_signs(_list_, coords):
    changed_list = [list(triple) for triple in _list_]
    for triple in changed_list:
        for i in range(3):
            triple[i] = -triple[i] if coords[i] else triple[i]
    return changed_list


def compare(list1, list2):
    for i in range(len(list2)):
        matches = Counter()
        for j in range(len(list1[i])):
            for k in range(len(list2[i])):
                x1, y1, z1 = list1[0][j]
                x2, y2, z2 = list2[i][k]
                matches[(x1 - x2, y1 - y2, z1 - z2)] += 1
                mc = matches.most_common()[0]
                if mc[1] >= 12:
                    return True, mc[0], i % 6, i // 6
    return False, None, None, None


def sum_triples(triple1, triple2):
    return tuple(triple1[i] + triple2[i] for i in range(3))


def all_related(related, num_rel):
    visited = set()
    for x, y in related:
        visited.update({x, y})
    return len(visited) == num_rel and len(related) >= num_rel


def getPer(p1, p2):
    if p1 == 0:
        return p2
    elif p1 == 1:
        if p2 == 1:
            return 0
        elif p2 == 2:
            return 4
        elif p2 == 3:
            return 5
        elif p2 == 4:
            return 2
        elif p2 == 5:
            return 3
        else:
            return getPer(p2, p1)
    elif p1 == 2:
        if p2 == 2:
            return 3
        elif p2 == 3:
            return 1
        elif p2 == 4:
            return 5
        elif p2 == 5:
            return 4
        else:
            return getPer(p2, p1)
    elif p1 == 3:
        if p2 == 3:
            return 4
        elif p2 == 4:
            return 0
        elif p2 == 5:
            return 1
        else:
            return getPer(p2, p1)
    elif p1 == 4:
        if p2 == 4:
            return 3
        elif p2 == 5:
            return 2
        else:
            return getPer(p2, p1)
    elif p1 == 5:
        if p2 == 5:
            return 0
        else:
            return getPer(p2, p1)


def getInvPer(p):
    if p == 3:
        return 4
    elif p == 4:
        return 3
    else:
        return p


def getPermOr(p, o, sign_changes):
    return sign_changes.index(list(list(permutations(sign_changes[o]))[p]))


def getOr(o1, o2):
    if o1 == o2:
        return 0
    if o1 == 0:
        return o2
    elif o1 == 1:
        if 0 <= o2 <= 5:
            return getPer(o1, o2)
        elif o2 == 6:
            return 7
        else:
            return 6
    elif o1 == 2:
        if o2 == 3:
            return 6
        elif o2 == 4:
            return 1
        elif o2 == 5:
            return 7
        elif o2 == 6:
            return 3
        elif o2 == 7:
            return 5
        else:
            return getOr(o2, o1)
    elif o1 == 3:
        if o2 == 4:
            return 7
        elif o2 == 5:
            return 1
        elif o2 == 6:
            return 2
        elif o2 == 7:
            return 4
        else:
            return getOr(o2, o1)
    elif o1 == 4:
        if o2 == 5:
            return 6
        elif o2 == 6:
            return 5
        elif o2 == 7:
            return 3
        else:
            return getOr(o2, o1)
    elif o1 == 5:
        if o2 == 6:
            return 4
        elif o2 == 7:
            return 2
        else:
            return getOr(o2, o1)
    elif o1 == 6:
        if o2 == 7:
            return 1
        else:
            return getOr(o2, o1)
    elif o1 == 7:
        return getOr(o2, o1)


def manhattan_distance(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def part1(file):
    sign_changes = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    scanner_reads = getData(file)
    all_scanner_reads = {i: get_all_permutations(scanner_reads[i], sign_changes) for i in range(len(scanner_reads))}
    relations = dict()
    for i in range(len(all_scanner_reads)):
        for j in range(len(all_scanner_reads)):
            if i != j:
                success, value, p, o = compare(all_scanner_reads[i], all_scanner_reads[j])
                if success:
                    inv_o = getPermOr(p, o, sign_changes)
                    relations[(i, j)] = (value, p, inv_o)
    print(relations)

    relations_to_zero = {0: ((0, 0, 0), 0, 0)}
    while len(relations_to_zero) < len(scanner_reads):
        for relation in relations.keys():
            if relation[1] not in relations_to_zero:
                if relation[0] == 0:
                    relations_to_zero[relation[1]] = relations[relation]
                elif relation[0] in relations_to_zero:
                    val, p1, o1 = relations_to_zero[relation[0]]
                    val2, p2, o2 = relations[relation]
                    x1, y1, z1 = val
                    x2, y2, z2 = change_signs(permutations(val2), sign_changes[o1])[p1]
                    val_to_zero = (x1+x2, y1+y2, z1+z2)
                    p2_to_zero = getPer(p1, p2)
                    perm_o2 = getPermOr(p1, o2, sign_changes)
                    o2_to_zero = getOr(o1, perm_o2)
                    relations_to_zero[relation[1]] = (val_to_zero, p2_to_zero, o2_to_zero)

    print(relations_to_zero)

    beacons = set()
    for rel, (val, p, o) in relations_to_zero.items():
        for beacon in scanner_reads[rel]:
            x1, y1, z1 = val
            x2, y2, z2 = change_signs(permutations(beacon), sign_changes[o])[p]
            beacons.add((x1 + x2, y1 + y2, z1 + z2))

    return len(beacons), part2(relations_to_zero)


def part2(rels):
    max_dist = 0
    for i in range(1, len(rels)):
        for j in range(i + 1, len(rels)):
            max_dist = max(max_dist, manhattan_distance(rels[i][0], rels[j][0]))
    return max_dist


num_beacons, largest_man = part1("input.txt")
print("The number of beacons is", num_beacons, "and the largest Manhattan distance is", largest_man)
