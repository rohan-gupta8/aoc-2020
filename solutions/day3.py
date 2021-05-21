import math

f = open("inputs/day3.txt", "r")
inp = list(f.read().split("\n"))

c = [0] * 5
for i in range(1, len(inp)):
    c = [
        sum(x) for x in zip([(inp[i][(k * i) % len(inp[i])] == "#") for k in [1, 3, 5, 7]] + [0], c)
    ]
    if i % 2 == 0:
        if inp[i][(i // 2) % len(inp[i])] == "#":
            c[4] += 1

print(f"Part 1: {c[1]}")
print(f"Part 2: {math.prod(c)}")
