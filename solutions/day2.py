f = open("inputs/day2.txt", "r")

inp = list(f.read().split("\n"))

c = 0
# part 1
for i in inp:
    spl = i.split(" ")
    minf, maxf = int(spl[0].split("-")[0]), int(spl[0].split("-")[1])
    char = spl[1][0]

    if minf <= spl[2].count(char) <= maxf:
        c += 1

print(f"Part 1: {c}")

# part 2
c = 0
for i in inp:
    spl = i.split(" ")
    first, last = int(spl[0].split("-")[0]), int(spl[0].split("-")[1])
    char = spl[1][0]

    if (spl[2][first - 1] == char) ^ (spl[2][last - 1] == char):
        c += 1

print(f"Part 2: {c}")
