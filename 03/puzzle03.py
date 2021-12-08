"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 3

def calculate_power_consumption(file):
    f = open(file, "r")
    rates = dict()

    for line in f:
        for i in range(len(line) - 1):
            if i not in rates:
                rates[i] = [0, 0]
            rates[i][0] += (int(line[i]) == 1)
            rates[i][1] += (int(line[i]) == 0)

    bin_gamma_rate = [int(rates[x][0] > rates[x][1]) for x in rates]
    bin_epsilon_rate = [int(not rate) for rate in bin_gamma_rate]

    gamma_rate = 0
    epsilon_rate = 0

    for i in range(len(bin_gamma_rate)):
        gamma_rate += (bin_gamma_rate[i]) * (2 ** (len(bin_gamma_rate) - i - 1))
        epsilon_rate += (bin_epsilon_rate[i]) * (2 ** (len(bin_gamma_rate) - i - 1))

    f.close()

    return gamma_rate * epsilon_rate


def get_value_from_criteria(values, step, criteria):
    if len(values) <= 0:
        return "Error"

    if len(values) == 1:
        return values[0]

    else:
        new_values0 = list()
        new_values1 = list()

        for value in values:
            if int(value[step]) == 0:
                new_values0.append(value)
            else:
                new_values1.append(value)

        if criteria:
            if len(new_values1) >= len(new_values0):
                return get_value_from_criteria(new_values1, step + 1, criteria)
            else:
                return get_value_from_criteria(new_values0, step + 1, criteria)
        else:
            if len(new_values0) <= len(new_values1):
                return get_value_from_criteria(new_values0, step + 1, criteria)
            else:
                return get_value_from_criteria(new_values1, step + 1, criteria)


def calculate_life_support_rating(file):
    f = open(file, "r")
    values = [line.strip() for line in f]
    bin_oxygen_rate = get_value_from_criteria(values, 0, 1)
    bin_co2_rate = get_value_from_criteria(values, 0, 0)

    oxygen_rate = 0
    co2_rate = 0

    for i in range(len(bin_oxygen_rate)):
        oxygen_rate += (int(bin_oxygen_rate[i])) * (2 ** (len(bin_oxygen_rate) - i - 1))
        co2_rate += (int(bin_co2_rate[i])) * (2 ** (len(bin_co2_rate) - i - 1))

    f.close()

    return oxygen_rate * co2_rate


print("Solution 1: " + str(calculate_power_consumption("input.txt")))
print("Solution 2: " + str(calculate_life_support_rating("input.txt")))
