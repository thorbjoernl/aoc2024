from collections import defaultdict, deque


def read_and_parse_input(fp: str):
    with open(fp) as f:
        lines = f.read().split("\n")

    mapping = defaultdict(lambda: list())
    for i, l in enumerate(lines):
        if l == "":
            break

        p1, p2 = l.split("|")

        mapping[p2].append(p1)

    sequences = []
    for i, l in enumerate(lines[(i + 1) :]):
        if l == "":
            break
        sequences.append(l.split(","))

    return mapping, sequences


mapping, sequences = read_and_parse_input("input")
# Mapping is a dict which for each entry contains the pages that
# must come BEFORE it.
# Sequences is a list of the split sequences.


# Part 1
def check_sequence(seq: list[str], mapping: dict):
    # Checks if a sequence is correct given a mapping.
    previous_pages = set()
    for page in seq:
        for x in mapping[page]:
            if x not in seq:
                continue

            if x not in previous_pages:
                return False

        previous_pages.add(page)

    return True


_sum = 0
for seq in sequences:
    if check_sequence(seq, mapping):
        _sum += int(seq[len(seq) // 2])

print(_sum)  # 5713


# Part 2
_sum = 0
for seq in sequences:
    if check_sequence(seq, mapping):
        continue

    new_seq = []
    deq = deque(seq)
    while len(deq) > 0:
        page = deq.pop()
        _append = True
        for x in mapping[page]:
            if x not in seq:
                continue

            if x not in new_seq:
                _append = False
                break

        if _append:
            new_seq.append(page)
            continue

        deq.appendleft(page)

    assert set(new_seq) == set(seq)
    assert check_sequence(new_seq, mapping)
    _sum += int(new_seq[len(new_seq) // 2])

print(_sum)  # 5180
