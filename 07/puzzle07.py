"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 7


def alignSubmarines(file):
    from collections import Counter

    data_list = list(map(int, open(file, "r").readline().split(",")))
    positions = Counter(data_list)

    min_fuel_sum = float('inf')

    for lead_position in positions.keys():
        current_fuel_sum = 0
        for position in positions.keys():
            current_fuel_sum += abs(position - lead_position) * positions[position]
        min_fuel_sum = min(min_fuel_sum, current_fuel_sum)

    return min_fuel_sum


def alignSubmarinesNonLinear(file):
    from collections import Counter

    data_list = list(map(int, open(file, "r").readline().split(",")))
    positions = Counter(data_list)

    min_fuel_sum = float('inf')

    for lead_position in positions.keys():
        current_fuel_sum = 0
        for position in positions.keys():
            current_fuel_sum += calculateConsumption(position, lead_position) * positions[position]
        min_fuel_sum = min(min_fuel_sum, current_fuel_sum)

    return min_fuel_sum


def calculateConsumption(position1, position2):
    distance = abs(position1 - position2)
    consumption = 0
    for i in range(distance):
        consumption += i + 1
    return consumption


print("Solution 1: " + str(alignSubmarines("input.txt")))
print("Solution 2: " + str(alignSubmarinesNonLinear("input.txt")))
