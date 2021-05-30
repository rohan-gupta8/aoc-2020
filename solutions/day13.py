from sympy.ntheory.modular import crt
m, buses = open("inputs/day13.txt").read().split("\n")

# Part 1
buses = list(map(lambda x: (x[0], int(x[1])), list(filter(lambda x: x[1] != "x", list(enumerate(buses.split(",")))))))
m = int(m)
ans, mintime = 10 ** 8, 10 ** 8
for _, bus in buses:
    if bus - m % bus < mintime:
        ans = bus
        mintime = bus - m % bus
print(ans * mintime)

# Part 2

a = list(map(lambda x: x[1] - x[0], buses))
n = list(map(lambda x: x[1], buses))

print(crt(n, a)[0])
