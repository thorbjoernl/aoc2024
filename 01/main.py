import math
from collections import Counter


# Helpers
def read_lists(fp: str) -> tuple[list[int], list[int]]:
    with open(fp) as f:
        a, b = [], []
        for l in f.readlines():
            spl = l.split()

            a.append(int(spl[0].strip()))
            b.append(int(spl[1].strip()))
    return a, b


# Part 1
A, B = read_lists("input")
A, B = sorted(A), sorted(B)
_sum = 0
for a, b in zip(A, B):
    _sum += abs(a - b)

print(_sum)  # 1873376


# Part 2
counts = Counter(B)

_similarity = 0
for a in A:
    _similarity += counts[a] * a

print(_similarity)  # 18997088
