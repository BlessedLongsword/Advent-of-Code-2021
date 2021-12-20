"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""

# Puzzle 20


def getData(file):
    iea, input_image = open(file).read().split('\n\n')
    return iea, input_image.split('\n')


def printImage(image):
    print()
    for line in image:
        print(line)
    print()


def process_pixel(input_image, i, j, step, iea):
    bin_list = []
    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < len(input_image) and 0 <= new_j < len(input_image[i]):
            bin_list.append('1' if input_image[new_i][new_j] == '#' else '0')
        else:
            if step == 0 or iea[0] == '.':
                char = '.'
            else:
                if step % 2 == 0:
                    char = iea[-1]
                else:
                    char = iea[0]
            bin_list.append('1' if char == '#' else '0')
    return int(''.join(bin_list), 2)


def extendImage(image, step, iea):
    if step == 0 or iea[0] == '.':
        char = '.'
    else:
        if step % 2 == 0:
            char = iea[-1]
        else:
            char = iea[0]
    image.insert(0, char * len(image[0]))
    image.append(char * len(image[0]))
    for i in range(len(image)):
        image[i] = char + image[i] + char


def modify_image(iea, image, idx_pixels):
    for idx, i, j in idx_pixels:
        image[i] = list(image[i])
        image[i][j] = '#' if iea[idx] == '#' else '.'
        image[i] = ''.join(image[i])


def process_iea(iea, image, step):
    idx_pixels = []
    extendImage(image, step, iea)
    # printImage(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            idx_pixels.append((process_pixel(image, i, j, step, iea), i, j))
    modify_image(iea, image, idx_pixels)


def count_light(image):
    light = 0
    for line in image:
        for char in line:
            light += 1 if char == '#' else 0
    return light


def enhance_image(file, steps):
    iea, image = getData(file)
    # printImage(image)
    for i in range(steps):
        process_iea(iea, image, i)
        # print(i, count_light(image))
    # printImage(image)
    return count_light(image)


print("Solution 1:", enhance_image("input.txt", 2))
print("Solution 2:", enhance_image("input.txt", 50))
