def read_and_parse_input(fp: str):
    with open(fp) as f:
        return [[int(x) for x in l.strip().split()] for l in f.readlines()]


def is_sequence_safe(r: list[int]):
    delta = [a - b for a, b in zip(r, r[1:])]
    is_monotonous = all([d > 0 for d in delta]) or all([d < 0 for d in delta])
    is_in_range = all([abs(x) in [1, 2, 3] for x in delta])

    return is_in_range and is_monotonous


reports = read_and_parse_input("input")


safe_count = 0
for r in reports:
    safe_count += is_sequence_safe(r)

print(safe_count)  # 486

# Part 2
safe_count = 0
for r in reports:
    if is_sequence_safe(r):
        safe_count += 1
        continue

    i = 0
    while i < len(r):
        if is_sequence_safe(r[:i] + r[(i + 1) :]):
            safe_count += 1
            break
        i += 1


print(safe_count)  # 520
