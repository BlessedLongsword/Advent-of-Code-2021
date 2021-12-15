"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 15

def getData(file):
    data = [[int(line[i]) for i in range(len(line.strip()))] for line in open(file).readlines()]
    return data


def l1_heuristic(matrix, i, j):
    return len(matrix) + len(matrix[i]) - i - j - 2


def reconstruct_path(came_from, start, goal):
    path = list()
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = came_from[current_node]
    path.append(start)
    path.reverse()
    return path


def aStarSearch(matrix, heuristic, start, goal):
    import heapq
    x, y = start
    frontier = []
    heapq.heappush(frontier, (heuristic(matrix, x, y), start))
    came_from = dict()
    g_scores = dict()
    came_from[start] = None
    g_scores[start] = 0

    while frontier:
        f_score, pos = heapq.heappop(frontier)
        i, j = pos
        if pos == goal:
            return g_scores[pos], reconstruct_path(came_from, start, pos)
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_i, new_j = i + di, j + dj
            new_pos = (new_i, new_j)
            if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[i]):
                new_score = g_scores[pos] + matrix[new_i][new_j]
                if new_pos not in g_scores or new_score < g_scores[new_pos]:
                    g_scores[new_pos] = new_score
                    heapq.heappush(frontier, (new_score + heuristic(matrix, new_i, new_j), new_pos))
                    came_from[new_pos] = pos

    return 'XD'


def expand_map(risk_map):
    full_risk_map = [[0 for _ in range(len(risk_map[0])*5)] for _ in range(len(risk_map)*5)]
    for i in range(len(risk_map)):
        for j in range(len(risk_map[0])):
            full_risk_map[i][j] = risk_map[i][j]

    for i in range(len(risk_map), len(full_risk_map)):
        for j in range(len(risk_map[0])):
            full_risk_map[i][j] = (full_risk_map[i - len(risk_map)][j] + 1) % 10
            if full_risk_map[i][j] == 0:
                full_risk_map[i][j] = 1

    for i in range(len(full_risk_map)):
        for j in range(len(risk_map[0]), len(full_risk_map[0])):
            full_risk_map[i][j] = (full_risk_map[i][j - len(risk_map[0])] + 1) % 10
            if full_risk_map[i][j] == 0:
                full_risk_map[i][j] = 1

    return full_risk_map


def print_risk_map(risk_map):
    print()
    for i in range(len(risk_map)):
        print(''.join(list(map(str, risk_map[i]))))
    print()


def part1(file):
    risk_map = getData(file)
    start, goal = (0, 0), (len(risk_map) - 1, len(risk_map[0]) - 1)
    return aStarSearch(risk_map, l1_heuristic, start, goal)


def part2(file):
    full_risk_map = expand_map(getData(file))
    start, goal = (0, 0), (len(full_risk_map) - 1, len(full_risk_map[0]) - 1)
    return aStarSearch(full_risk_map, l1_heuristic, start, goal)


print("Solution 1: " + str(part1("input.txt")[0]))
print("Solution 2: " + str(part2("input.txt")[0]))
