"""
Antonio Tigri (Blessed Longsword)
Advent of Code 2021 - 02/12/2021
"""


# Puzzle 10

def syntax_error(file):
    lines = [line.strip() for line in open(file, 'r')]
    chunk_relations = {'(': ')', '[': ']', '{': '}', '<': '>'}
    chunk_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        chunks = list()
        for char in line:
            if char in chunk_relations.keys():
                chunks.append(char)
            else:
                chunk_opener = chunks.pop()
                if chunk_relations[chunk_opener] != char:
                    score += chunk_scores[char]
                    break

    return score


def middle_score(file):
    lines = [line.strip() for line in open(file, 'r')]
    chunk_relations = {'(': ')', '[': ']', '{': '}', '<': '>'}
    chunk_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = list()
    for line in lines:
        chunks = list()
        completable = True
        score = 0
        for char in line:
            if char in chunk_relations.keys():
                chunks.append(char)
            else:
                chunk_opener = chunks.pop()
                if chunk_relations[chunk_opener] != char:
                    completable = False
                    break
        if completable:
            rang = len(chunks)
            for i in range(rang):
                score *= 5
                score += chunk_scores[chunk_relations[chunks.pop()]]
            scores.append(score)

    scores.sort()

    return scores[len(scores)//2]


print("Solution 1: " + str(syntax_error("input.txt")))
print("Solution 2: " + str(middle_score("input.txt")))

