f = open("inputs/day12.txt").read().split("\n")

# Note: Probably should have pattern matched for this one

dir_map = {0: "E", 90: "S", 180: "W", 270: "N"}
dir = 0
N = 0
E = 0
# Part 1
for line in f:
    d = line[0]
    value = int(line[1:])
    if d == "R":
        dir = (dir + value) % 360
    if d == "L":
        dir = (dir - value) % 360
    if d == "F":
        d = dir_map[dir]
    if d == "N":
        N += value
    if d == "S":
        N -= value
    if d == "E":
        E += value
    if d == "W":
        E -= value

print(abs(N) + abs(E))


# Part 2

sx, sy = 0, 0
wx, wy = 10, 1

for line in f:
    d = line[0]
    value = int(line[1:])
    if d == "F":
        sx, sy = sx + (wx * value), sy + (wy * value)
    if d == "R":
        for i in range(value // 90):
            wx, wy = wy, -wx
    if d == "L":
        for i in range(value // 90):
            wx, wy = -wy, wx
    if d == "E":
        wx, wy = wx + value, wy
    if d == "W":
        wx, wy = wx - value, wy
    if d == "N":
        wx, wy = wx, wy + value
    if d == "S":
        wx, wy = wx, wy - value

print(abs(sx) + abs(sy))
