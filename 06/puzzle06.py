"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 6

def lanternfish_after_n_days(file, n, reproduction_cycle, newborn_extra):
    lanternfish = list(map(int, open(file, "r").readline().split(",")))

    timer_counts = dict()

    for timer in lanternfish:
        if timer not in timer_counts:
            timer_counts[timer] = [0, 0]
        timer_counts[timer][0] += 1

    for i in range(1, reproduction_cycle + 1):
        if i not in timer_counts:
            timer_counts[i] = [0, 0]

    for i in range(n):
        idx = reproduction_cycle if i % reproduction_cycle == 0 else i % reproduction_cycle
        newborn_idx = reproduction_cycle if (idx + newborn_extra) % reproduction_cycle == 0 \
            else (idx + newborn_extra) % reproduction_cycle
        timer_counts[newborn_idx][1] += timer_counts[idx][0]
        timer_counts[idx][0] += timer_counts[idx][1]
        timer_counts[idx][1] = 0

    return sum([timer_count[0] + timer_count[1] for timer_count in timer_counts.values()])


print("Solution 1: " + str(lanternfish_after_n_days("input.txt", 80, 7, 2)))
print("Solution 2: " + str(lanternfish_after_n_days("input.txt", 256, 7, 2)))
