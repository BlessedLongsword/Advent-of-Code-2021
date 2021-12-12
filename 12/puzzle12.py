"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 12

def count_paths(file, extra):
    connections = [line.strip().split('-') for line in open(file, 'r')]
    connections_by_cave = dict()
    for connection in connections:
        if connection[0] not in connections_by_cave:
            connections_by_cave[connection[0]] = [connection[1]]
        else:
            connections_by_cave[connection[0]].append(connection[1])
        if connection[1] not in connections_by_cave:
            connections_by_cave[connection[1]] = [connection[0]]
        else:
            connections_by_cave[connection[1]].append(connection[0])
    if extra:
        paths = find_paths_extra(connections_by_cave)
    else:
        paths = find_paths(connections_by_cave)
    return len(paths)


def find_paths(connections):
    paths = set()
    exploration = [('start', list(), set())]
    while exploration:
        current_cave_data = exploration.pop()
        cave, current_path, small_caves = current_cave_data[0], current_cave_data[1].copy(), current_cave_data[2].copy()
        current_path.append(cave)
        if cave == 'end':
            paths.add(tuple(current_path))
        else:
            if cave.islower():
                small_caves.add(cave)
            for connected_cave in connections[cave]:
                if connected_cave not in small_caves:
                    exploration.append((connected_cave, current_path, small_caves))

    return paths


def find_paths_extra(connections):
    paths = set()
    exploration = [('start', list(), set(), False)]
    while exploration:
        current_cave_data = exploration.pop()
        cave, current_path = current_cave_data[0], current_cave_data[1].copy()
        small_caves, small_cave_twice = current_cave_data[2].copy(), current_cave_data[3]
        small_caves_aux = small_caves.copy()
        small_caves_aux.add('start')
        current_path.append(cave)
        if cave == 'end':
            paths.add(tuple(current_path))
        else:
            if cave.islower():
                small_caves.add(cave)
            for connected_cave in connections[cave]:
                if connected_cave not in small_caves:
                    exploration.append((connected_cave, current_path, small_caves, small_cave_twice))
                    if cave.islower() and not small_cave_twice and not cave == 'start':
                        exploration.append((connected_cave, current_path, small_caves_aux, True))
    return paths


print("Solution 1: " + str(count_paths("input.txt", False)))
print("Solution 2: " + str(count_paths("input.txt", True)))
