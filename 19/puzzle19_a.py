"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021

Version inspired (or totally copied) by Andreu's Solution
"""

# Puzzle 19

import itertools as it
import numpy as np
from collections import Counter


def getData(file):
    data = open(file).read().split("\n\n")
    data = [paragraph.split('\n') for paragraph in data]
    data = {i: [list(map(int, line.split(','))) for line in data[i][1:]] for i in range(len(data))}
    return data


def rotations3d():
    x_rot = np.array([[1, 0, 0],
                      [0, 0, 1],
                      [0, -1, 0]])

    y_rot = np.array([[0, 0, 1],
                      [0, 1, 0],
                      [-1, 0, 0]])

    z_rot = np.array([[0, 1, 0],
                      [-1, 0, 0],
                      [0, 0, 1]])

    hashed, new = {}, {arr.tobytes(): arr for arr in [x_rot, y_rot, z_rot]}
    while new:
        hashed.update(new)
        new = {}
        for arr1, arr2 in it.product(hashed.values(), repeat=2):
            prod = np.dot(arr1, arr2)
            assert np.linalg.det(prod) == 1
            hash_prod = prod.tobytes()
            if hash_prod not in hashed:
                new[hash_prod] = prod

    return list(hashed.values())


def compare(list1, list2, rotations):
    for rot in rotations:
        l2rot = [np.dot(rot, triple) for triple in list2]
        matches = Counter()
        for i in range(len(list1)):
            for j in range(len(list2)):

                x1, y1, z1 = list1[i]
                x2, y2, z2 = l2rot[j]
                matches[(x1 - x2, y1 - y2, z1 - z2)] += 1
                mc = matches.most_common()[0]
                if mc[1] >= 12:
                    return True, mc[0], rot
    return False, None, None


def manhattan_distance(a, b):
    return np.abs(a - b).sum()


def part1(file):
    scanner_reads = getData(file)
    rotations = rotations3d()
    relations = []
    for i in range(len(scanner_reads)):
        for j in range(i+1, len(scanner_reads)):
            success, val, rot = compare(scanner_reads[i], scanner_reads[j], rotations)
            if success:
                relations.append([i, j, val, rot])
                inv = np.linalg.inv(rot).astype(int)
                relations.append([j, i, -np.dot(inv, val), inv])

    rel_to_zero = {0: [np.array([0, 0, 0]), np.identity(3, dtype=int)]}
    while len(rel_to_zero) < len(scanner_reads):
        for i, j, val, rot in relations:
            if i in rel_to_zero and j not in rel_to_zero:
                val1, rot1 = rel_to_zero[i]
                rot2 = np.dot(rot1, rot)
                val2 = val1 + np.dot(rot1, val)
                rel_to_zero[j] = [val2, rot2]

    beacons = set()
    for scanner, (val, rot) in rel_to_zero.items():
        for row in scanner_reads[scanner]:
            beacons.add(tuple(val + np.dot(rot, row)))
    return len(beacons), part2(rel_to_zero)


def part2(rels):
    max_dist = 0
    for i in range(len(rels)):
        for j in range(i + 1, len(rels)):
            max_dist = max(max_dist, manhattan_distance(rels[i][0], rels[j][0]))
    return max_dist


num_beacons, largest_man = part1("input.txt")
print("The number of beacons is", num_beacons, "and the largest Manhattan distance is", largest_man)

