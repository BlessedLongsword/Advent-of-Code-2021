"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 16

def getData(file):
    num_list = list(open(file).readline())
    num_list = [int(elem, 16) for elem in num_list]
    num_list = list(map(bin, num_list))
    for i, num in enumerate(num_list):
        num_list[i] = '0'*(4 - len(num[2:])) + num[2:]
    return ''.join(num_list)


def prod(nums):
    product = 1
    for num in nums:
        product *= num
    return product


def grt(nums):
    return int(nums[0] > nums[1])


def lst(nums):
    return int(nums[0] < nums[1])


def eq(nums):
    return int(nums[0] == nums[1])


def analyze_generic_packet(packet, idx):
    type_function = {0: sum, 1: prod, 2: min, 3: max, 5: grt, 6: lst, 7: eq}
    version_sum = 0
    version_sum += int(packet[idx:idx+3], 2)
    type_id = int(packet[idx+3:idx+6], 2)
    if type_id == 4:
        packet_value, idx = analyze_literal_packet(packet, idx+6)
    else:
        if packet[idx+6] == '1':
            sub_version, packet_values, idx = analyze_operator_packet_sub(packet, idx+7)
            version_sum += sub_version
            packet_value = type_function[type_id](packet_values)

        else:
            sub_version, packet_values, idx = analyze_operator_packet_len(packet, idx+7)
            version_sum += sub_version
            packet_value = type_function[type_id](packet_values)

    return version_sum, packet_value, idx


def analyze_literal_packet(packet, idx):
    packet_value = list()
    while packet[idx] == '1':
        packet_value.append(packet[idx + 1:idx + 5])
        idx = idx + 5
    packet_value.append(packet[idx + 1:idx + 5])
    return int(''.join(packet_value), 2), idx + 5


def analyze_operator_packet_sub(packet, idx):
    version_sum = 0
    packet_values = list()
    num_sub_packets = int(packet[idx:idx+11], 2)
    idx = idx + 11
    for i in range(num_sub_packets):
        sub_version, packet_value, idx = analyze_generic_packet(packet, idx)
        version_sum += sub_version
        packet_values.append(packet_value)
    return version_sum, packet_values, idx


def analyze_operator_packet_len(packet, idx):
    version_sum = 0
    packet_values = list()
    len_sub_packets = int(packet[idx:idx+15], 2)
    idx = idx + 15
    start = idx
    while idx - start < len_sub_packets:
        sub_version, packet_value, idx = analyze_generic_packet(packet, idx)
        version_sum += sub_version
        packet_values.append(packet_value)
    return version_sum, packet_values, idx


def part1(file):
    packet = getData(file)
    return analyze_generic_packet(packet, 0)[0]


def part2(file):
    packet = getData(file)
    return analyze_generic_packet(packet, 0)[1]


print("Solution 1:", part1("input.txt"))
print("Solution 2:", part2("input.txt"))
