"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 01/12/2021
"""


# Puzzle 1

def increasings(file):
    incrementation = 0
    prev = None
    f = open(file, "r")

    for value in f:
        if prev is not None:
            incrementation += int(value) > prev
        prev = int(value)

    f.close()

    return incrementation


def increasings_windows(file):
    incrementation = 0
    prev1 = None
    prev2 = None
    prev_sum = None
    f = open(file, "r")

    for value in f:
        if prev1 is not None and prev2 is not None:
            window_sum = prev1 + prev2 + int(value)
            if prev_sum is not None:
                incrementation += window_sum > prev_sum
            prev_sum = window_sum
        prev2 = prev1
        prev1 = int(value)

    f.close()

    return incrementation


print("Solution 1: " + str(increasings("input.txt")))
print("Solution 2: " + str(increasings_windows("input.txt")))
