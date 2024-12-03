import re


with open("input") as f:
    data = f.read()

# Part 1
match = re.findall(r"mul\((\d{1,3},\d{1,3})\)", data)

print(match)
_sum = 0
for i in match:
    splt = i.split(",")
    _sum += int(splt[0]) * int(splt[1])

print(_sum)  # 188192787

# Part 2
match = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", data)

do = True
_sum = 0
for i in match:
    if i == "do()":
        do = True
        continue
    if i == "don't()":
        do = False
        continue
    if do:
        s = i.replace("mul(", "").replace(")", "")
        a, b = [int(x) for x in s.split(",")]
        _sum += a * b

print(_sum)  # 113965544
