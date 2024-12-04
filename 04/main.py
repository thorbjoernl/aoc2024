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
