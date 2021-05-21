f = open("solutions/inputs/day5.txt", "r").read().split("\n")

mapping = {"R": "1", "L": "0", "F": "0", "B": "1"}
inp = [int("".join([mapping[c] for c in line]), 2) for line in f]

s = list(set(list(range(min(inp), max(inp) + 1))) - set(inp))

print(f"Part 1: {max(inp)}")
print(f"Part 2: {s[0]}")
