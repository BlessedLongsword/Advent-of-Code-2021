"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 14

def getData(file):
    template, insertions = open(file).read().split('\n\n')
    rules = dict()
    for rule in insertions.split('\n'):
        key, value = rule.split(' -> ')
        rules[key] = value
    return template, rules


def get_substrings(string, size):
    if len(string) >= size:
        return [string[i:i+size] for i in range(len(string) - size + 1)]


def polymerization(template, rules, steps):
    polymer = template
    for _ in range(steps):
        polymer_pairs = get_substrings(polymer, 2)
        new_template = polymer_pairs.copy()
        for i, pair in enumerate(polymer_pairs):
            last_element = pair[1] if i == len(polymer_pairs) - 1 else ''
            new_template[i] = pair[0] + rules[pair] + last_element
        polymer = ''.join(new_template)
    return polymer


def common_subtraction(polymer):
    from collections import Counter
    elements = Counter(polymer)
    return elements.most_common()[0][1] - elements.most_common()[-1][1]


def efficient_polymerization(template, rules, steps):
    from collections import Counter
    polymer = Counter(get_substrings(template, 2))
    letter_frequency = Counter(template)
    for _ in range(steps):
        current_polymer = polymer.copy()
        for pair in current_polymer.keys():
            if polymer[pair] > 0:
                polymer[pair[0] + rules[pair]] += current_polymer[pair]
                polymer[rules[pair] + pair[1]] += current_polymer[pair]
                polymer[pair] -= current_polymer[pair]
                letter_frequency[rules[pair]] += current_polymer[pair]
    return letter_frequency.most_common()[0][1] - letter_frequency.most_common()[-1][1]


def part1(file):
    template, rules = getData(file)
    return efficient_polymerization(template, rules, 10)


def part2(file):
    template, rules = getData(file)
    return efficient_polymerization(template, rules, 40)


print("Solution 1: " + str(part1("input.txt")))
print("Solution 2: " + str(part2("input.txt")))
