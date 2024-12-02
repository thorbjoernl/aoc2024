def read_and_parse_input(fp: str):
    with open(fp) as f:
        return [[int(x) for x in l.strip().split()] for l in f.readlines()]

def is_sequence_safe(r: list[int]):
    safe = True
    i = 1
    if r[1]-r[0] > 0:
        increasing = True
    elif r[1]-r[0] < 0:
        increasing = False
    else:
        return False

    i=0
    while i < len(r)-1:
        i+=1

        diff = r[i]-r[i-1]

        if increasing:
            if not diff in [1, 2, 3]:
                safe=False
                break
        else:
            if not diff in [-1, -2, -3]:
                safe= False
                break
    
    return safe

reports = read_and_parse_input("input")
print(reports)


safe_count = 0
for r in reports:
    safe_count += is_sequence_safe(r)

print(safe_count) # 486

# Part 2
safe_count = 0
for r in reports:
    if is_sequence_safe(r):
        safe_count += 1
        continue
    
    i = 0
    while i < len(r):
        print(r[:i] + r[(i+1):])
        if is_sequence_safe(r[:i] + r[(i+1):]):
            safe_count += 1
            break
        i += 1
    
    print()
    
print(safe_count) # 520