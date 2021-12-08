"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 8


def getData(file):
    f = open(file, 'r')
    data = [line.strip().split("|") for line in f]
    return [[line[0].split(), line[1].split()] for line in data]


def easyDigits(file):
    input_lines = getData(file)
    digits_lengths = {2, 4, 3, 7}
    digit_sum = 0

    for line in input_lines:
        for entry in line[1]:
            digit_sum += len(entry) in digits_lengths
    return digit_sum


def getEasyDigits(line):
    digit_lengths = {2: 1, 4: 4, 3: 7, 7: 8}
    digit_segments = dict()

    for part in line:
        for entry in part:
            if len(entry) in digit_lengths.keys():
                digit_segments[digit_lengths[len(entry)]] = set(entry)

    return digit_segments


def getPos0(digit_segments):
    return digit_segments[7].difference(digit_segments[1])


def getPos1(digit_segments, segment_positions):
    total = set()
    for entry in segment_positions.values():
        total.update(entry)
    return digit_segments[8].difference(total)


def getPos2(digit_segments, line):
    for entry in line:
        if len(entry) == 6:
            if digit_segments[8].difference(set(entry)).issubset(digit_segments[1]):
                return digit_segments[8].difference(set(entry))


def getPos3(digit_segments, line):
    for entry in line:
        if len(entry) == 6:
            if set(entry) != digit_segments[6] and set(entry) != digit_segments[9]:
                return digit_segments[8].difference(set(entry))


def getPos4(digit_segments, line):
    pos4and6 = digit_segments[8].difference(digit_segments[7].union(digit_segments[4]))
    for entry in line:
        if len(entry) == 6 and len(pos4and6.difference(set(entry))) == 1:
            return pos4and6.difference(set(entry))


def getPos5(digit_segments, segment_positions):
    return digit_segments[1].difference(segment_positions[2])


def getPos6(digit_segments, segment_positions):
    return digit_segments[9].difference(digit_segments[4].union(segment_positions[0]))


def completeSegments(line):
    digit_segments = getEasyDigits(line)
    segment_positions = dict()
    segment_positions[0] = getPos0(digit_segments)
    segment_positions[4] = getPos4(digit_segments, line[0])
    digit_segments[9] = digit_segments[8].difference(segment_positions[4])
    segment_positions[6] = getPos6(digit_segments, segment_positions)
    segment_positions[2] = getPos2(digit_segments, line[0])
    digit_segments[6] = digit_segments[8].difference(segment_positions[2])
    digit_segments[5] = digit_segments[9].difference(segment_positions[2])
    segment_positions[5] = getPos5(digit_segments, segment_positions)
    segment_positions[3] = getPos3(digit_segments, line[0])
    digit_segments[0] = digit_segments[8].difference(segment_positions[3])
    segment_positions[1] = getPos1(digit_segments, segment_positions)
    digit_segments[2] = digit_segments[8].difference(segment_positions[1].union(segment_positions[5]))
    digit_segments[3] = digit_segments[8].difference(segment_positions[1].union(segment_positions[4]))
    print(segment_positions)
    print(digit_segments)
    return digit_segments


def decode_outputs(file):
    input_lines = getData(file)
    output_sum = 0

    for line in input_lines:
        digit_segments = completeSegments(line)
        digit_lengths = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
        sum_value = list()
        for output in line[1]:
            output_length = len(output)
            if len(digit_lengths[output_length]) == 1:
                sum_value.append(digit_lengths[output_length][0])
            else:
                for val in digit_lengths[output_length]:
                    if digit_segments[val] == set(output):
                        sum_value.append(val)
                        break
        output_sum += sum([sum_value[len(sum_value) - i - 1]*(10**i) for i in range(len(sum_value))])

    return output_sum


print("Solution 1: " + str(easyDigits("input.txt")))
print("Solution 2: " + str(decode_outputs("input.txt")))
