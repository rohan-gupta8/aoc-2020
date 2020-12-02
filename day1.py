import itertools
import math

f = open("inputs/day1.txt", "r")

inp = set(map(int, f.read().split("\n")))
sums = [(sum(i), i) for i in itertools.combinations(inp, 2)]

# part 1
for i in inp:
    if 2020 - i in inp:
        print(f"Part 1: {2020*i - i**2}")
        break

# part 2
for i in sums:
    if (2020 - i[0]) in inp and 2020 - i[0] not in i[1]:
        print(f"Part 2: {math.prod(i[1])*(2020 - i[0])}")
        break

