"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 4

def getData(file):
    f = open(file, "r")
    board_lines = [line.strip() for line in f if not line.isspace()]

    numbers = board_lines.pop(0)

    counter = 0
    boards = {i: list() for i in range(len(board_lines) // 5)}

    for i, line in enumerate(board_lines):
        if i % 5 == 0 and i != 0:
            counter += 1
        boards[counter].append(list(map(int, line.split())))

    return list(map(int, numbers.split(","))), boards


def checkBoard(board):
    return checkLines(board) or checkColumns(board)


def checkLines(board):
    for line in board:
        if sum(line) == -5:
            return True
    return False


def checkColumns(board):
    for i in range(5):
        if sum([board[j][i] for j in range(5)]) == -5:
            return True
    return False


def getScore(board, number):
    score = 0

    for line in board:
        score += sum([num for num in line if num > -1])

    return score * number


def bingo(file):
    numbers, boards = getData(file)

    for i, number in enumerate(numbers):
        for board in boards.values():
            for line in board:
                if number in line:
                    line[line.index(number)] = -1
            if i > 4:
                if checkBoard(board):
                    return getScore(board, number)


def bingo_last(file):
    numbers, boards = getData(file)
    winning_boards = list()

    for i, number in enumerate(numbers):
        for j, board in boards.items():
            if j not in [item[0] for item in winning_boards]:
                for line in board:
                    if number in line:
                        line[line.index(number)] = -1
                if i > 4:
                    if checkBoard(board):
                        winning_boards.append((j, number))

    return getScore(boards[winning_boards[-1][0]], winning_boards[-1][1])


print("Solution 1: " + str(bingo("input.txt")))
print("Solution 2: " + str(bingo_last("input.txt")))
