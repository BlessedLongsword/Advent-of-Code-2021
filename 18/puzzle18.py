"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021

IMPORTANT NOTE:

LOAD A BIG SHOTGUN AND SHOOT ME IN THE HEAD PLEASE
PD: I love u Andreu <3

 ,________________________________
|__________,----------._ [____]  ""-,__  __...-----==="
        (_(||||||||||||)___________/   ""             |
           `----------'         [ ))"-,                |
                                ""    `,  _,--...___  |
                                        `/          """


# Puzzle 18

def getData(file):
    data = [eval(line.strip()) for line in open(file).readlines()]
    return data


def sum_snailfish(a, b):
    if a is None:
        return b
    elif b is None:
        return a
    elif a is None and b is None:
        return None
    else:
        return reduce([a, b])


def explode(num, depth):
    exploded = False
    added = False
    right = False
    l, r = None, None
    for i, sub_num in enumerate(num):
        if isinstance(sub_num, list) and not exploded:
            if depth >= 4:
                exploded = True
                l, r = sub_num
                num[i] = 0
                if i == 0:
                    if isinstance(num[1], int):
                        num[1] += r
                    else:
                        num[1][0] += r
                else:
                    if isinstance(num[0], int):
                        num[0] += l
                    else:
                        num[0][1] += l
                    right = True
                break
            else:
                exploded, added, right, l, r = explode(sub_num, depth + 1)
                if not added and exploded:
                    num[i].append('a')
                    if right:
                        if num[1] != num[i]:
                            added = True
                            if isinstance(num[1], int):
                                num[1] += r
                            else:
                                increment_lr(num[1], 0, r)
                    else:
                        if num[0] != num[i]:
                            added = True
                            if isinstance(num[0], int):
                                num[0] += l
                            else:
                                increment_lr(num[0], -1, l)
                    num[i].pop()

    return exploded, added, right, l, r


def increment_lr(num, direct, val):
    if isinstance(num[direct], int):
        num[direct] += val
    else:
        increment_lr(num[direct], direct, val)


def split(num):
    has_split = False
    if isinstance(num, list):
        for i, sub_num in enumerate(num):
            if not has_split:
                has_split, sp, val = split(sub_num)
                if sp:
                    num[i] = [val // 2, val // 2 + 1 if val % 2 == 1 else val // 2]
                    break
    else:
        if num > 9:
            return True, True, num
    return has_split, False, None


def reduce(num):
    reduced = False
    while not reduced:
        exploded, *_ = explode(num, 1)
        has_split = False
        if not exploded:
            has_split, *_ = split(num)
        reduced = not exploded and not has_split
    return num


def evaluate(num):
    if isinstance(num, list):
        value = 0
        value += 3 * evaluate(num[0]) + 2 * evaluate(num[1])
        return value
    else:
        return num


def part1(file):
    num_list = getData(file)
    current_num = None
    counter = 0
    for num in num_list:
        current_num = sum_snailfish(current_num, num)
    return evaluate(current_num)


def part2(file):
    from copy import deepcopy
    from itertools import permutations
    num_list = getData(file)
    return max(evaluate(sum_snailfish(deepcopy(a), deepcopy(b))) for a, b in permutations(num_list, 2))


print("Solution 1:", part1("input.txt"))
print("Solution 2:", part2("input.txt"))