import re
from collections import defaultdict


def read_input(fp: str):
    with open(fp) as f:
        return [x for x in f.read().split("\n") if x != ""]


data = read_input("input")

# Get every row as string (list comprehension so it is copied)
possible_strings = [r for r in data]

# Get every column as string
for i in range(len(data[0])):
    possible_strings.append("".join([x[i] for x in data]))

# Generate diagonal strings (both / and \)
diag1 = defaultdict(lambda: list())
diag2 = defaultdict(lambda: list())

for x in range(len(data[0])):
    for y in range(len(data)):
        # Neat trick for finding diagonals:
        # https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        diag1[x + y].append(data[y][x])
        diag2[x - y].append(data[y][x])

for seq in list(diag1.values()) + list(diag2.values()):
    string = "".join(seq)
    possible_strings.append(string)

_sum = 0
for string in possible_strings:
    # Capturing group inside lookahead to ensure overlapping matches are caught.
    _sum += len(re.findall(r"(?=(XMAS|SAMX))", string))
print(_sum)  # 2646


# Part 2
def inv_letter(val):
    if val == "M":
        return "S"
    if val == "S":
        return "M"
    raise Exception


_sum = 0
for x in range(len(data[0]) - 2):
    for y in range(len(data) - 2):
        if data[y][x] not in ["M", "S"]:
            continue

        if data[y + 1][x + 1] != "A":
            continue

        if data[y + 2][x + 2] != inv_letter(data[y][x]):
            continue

        if data[y + 2][x] not in ["M", "S"]:
            continue

        if data[y][x + 2] != inv_letter(data[y + 2][x]):
            continue

        _sum += 1

print(_sum)
